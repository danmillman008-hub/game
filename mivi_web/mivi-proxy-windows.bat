<# :
@echo off
title Mivi Local CORS Proxy
echo ============================================================
echo   Mivi Local Proxy - starting on http://localhost:8770
echo   Keep this window OPEN while generating videos.
echo   Close it or press Ctrl+C to stop.
echo ============================================================
powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-Expression ((Get-Content -LiteralPath '%~f0' -Raw))"
echo.
echo Proxy stopped. Press any key to close...
pause >nul
exit /b
: #>

# ===== PowerShell part (Windows 10 has everything built in, no install) =====
try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
} catch {}

$Prefix  = 'http://localhost:8770/'
$Allowed = @('ufotosoft.com', 'videomate.cc', 'wiseoel.com')
$SkipHeaders = @(
    'Connection','Content-Length','Content-Type','Date','Expect','Host',
    'Keep-Alive','Range','Referer','Transfer-Encoding','User-Agent',
    'Proxy-Connection','Accept'
)

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add($Prefix)
try {
    $listener.Start()
} catch {
    Write-Host "ERROR starting listener: $_" -ForegroundColor Red
    exit 1
}
Write-Host "Mivi CORS proxy running: $Prefix" -ForegroundColor Green
Write-Host "Allowed hosts: $($Allowed -join ', ')"

function Send-Text($ctx, $code, $text) {
    $b = [Text.Encoding]::UTF8.GetBytes($text)
    $ctx.Response.StatusCode = $code
    $ctx.Response.ContentType = 'text/plain; charset=utf-8'
    $ctx.Response.OutputStream.Write($b, 0, $b.Length)
    $ctx.Response.Close()
}

while ($listener.IsListening) {
    $ctx = $null
    try {
        $ctx = $listener.GetContext()
        $req = $ctx.Request
        $res = $ctx.Response
        $res.Headers.Add('Access-Control-Allow-Origin', '*')
        $res.Headers.Add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        $res.Headers.Add('Access-Control-Allow-Headers', '*')

        if ($req.HttpMethod -eq 'OPTIONS') {
            $res.StatusCode = 204
            $res.Close()
            continue
        }

        $u = $req.QueryString['u']
        if (-not $u) { Send-Text $ctx 400 'missing u='; continue }

        $uri = $null
        if (-not [Uri]::TryCreate($u, [UriKind]::Absolute, [ref]$uri)) {
            Send-Text $ctx 400 'bad url'; continue
        }
        $hostOnly = $uri.Host
        $ok = $false
        foreach ($a in $Allowed) {
            if ($hostOnly -eq $a -or $hostOnly.EndsWith('.' + $a)) { $ok = $true }
        }
        if (-not $ok) { Send-Text $ctx 403 "host not allowed: $hostOnly"; continue }

        # read raw request body (multipart for uploads, json for tasks)
        $ms = New-Object IO.MemoryStream
        $req.InputStream.CopyTo($ms)
        $body = $ms.ToArray()

        $hwr = [System.Net.HttpWebRequest]::Create($u)
        $hwr.Method = $req.HttpMethod
        $hwr.AllowAutoRedirect = $true
        $hwr.AutomaticDecompression = [Net.DecompressionMethods]::GZip -bor [Net.DecompressionMethods]::Deflate
        $hwr.Timeout = 300000
        $hwr.ReadWriteTimeout = 300000

        foreach ($k in $req.Headers.AllKeys) {
            if ($SkipHeaders -contains $k) { continue }
            try {
                $hwr.Headers.Add($k, $req.Headers[$k])
            } catch {}
        }
        if ($req.UserAgent) { try { $hwr.UserAgent = $req.UserAgent } catch {} }
        if ($req.Accept)     { try { $hwr.Accept = $req.Accept } catch {} }
        if ($req.Referer)    { try { $hwr.Referer = $req.Referer } catch {} }

        if ($body.Length -gt 0) {
            $hwr.ContentType = $req.ContentType
            $hwr.ContentLength = $body.Length
            $rs = $hwr.GetRequestStream()
            $rs.Write($body, 0, $body.Length)
            $rs.Close()
        }

        try {
            $up = $hwr.GetResponse()
            $res.StatusCode = [int]$up.StatusCode
            if ($up.ContentType) { $res.ContentType = $up.ContentType }
            $up.GetResponseStream().CopyTo($res.OutputStream)
            $up.Close()
            $res.Close()
            Write-Host ("{0} {1} -> {2}" -f $req.HttpMethod, $uri.AbsolutePath, [int]$up.StatusCode)
        } catch [System.Net.WebException] {
            $r = $_.Exception.Response
            if ($r) {
                $res.StatusCode = [int]$r.StatusCode
                if ($r.ContentType) { $res.ContentType = $r.ContentType }
                $r.GetResponseStream().CopyTo($res.OutputStream)
                $r.Close()
                $res.Close()
                Write-Host ("{0} {1} -> upstream {2}" -f $req.HttpMethod, $uri.AbsolutePath, [int]$r.StatusCode) -ForegroundColor Yellow
            } else {
                Send-Text $ctx 502 ("upstream error: " + $_.Exception.Message)
            }
        }
    } catch {
        if ($ctx) {
            try { Send-Text $ctx 502 ("proxy error: " + $_.Exception.Message) } catch {}
        }
        Start-Sleep -Milliseconds 100
    }
}
