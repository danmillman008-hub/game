@echo off
setlocal EnableExtensions
title Mivi Local CORS Proxy
cd /d "%~dp0"

echo ============================================================
echo    Mivi Local CORS Proxy  -  http://localhost:8770
echo    Keep this window OPEN while generating videos.
echo    Close it or press Ctrl+C to stop.
echo ============================================================
echo.

rem --- Self-check: the file must keep its .bat extension ---
if /I "%~x0" NEQ ".bat" (
  echo [ERROR] This file must be named  mivi-proxy-windows.bat
  echo         Windows probably saved it as a .txt file.
  echo         Turn on "File name extensions" in Explorer and rename it.
  echo.
  pause
  exit /b 1
)

rem --- Locate PowerShell ---
set "PS=powershell.exe"
where %PS% >nul 2>nul
if errorlevel 1 (
  if exist "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" (
    set "PS=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
  ) else (
    echo [ERROR] PowerShell was not found on this PC.
    echo         Use the Python proxy instead:  python proxy.py
    echo.
    pause
    exit /b 1
  )
)

rem --- Run the PowerShell payload that sits below the marker line ---
rem --- The marker token is split here so this line cannot match itself ---
%PS% -NoLogo -NoProfile -ExecutionPolicy Bypass -Command "$l=[IO.File]::ReadAllLines('%~f0');$i=0;while($l[$i] -notlike ('*PS_PAYLOAD'+'_START*')){$i++};try{iex(($l|Select-Object -Skip ($i+1))-join[Environment]::NewLine)}catch{Write-Host '';Write-Host ('[ERROR] '+$_.Exception.Message) -ForegroundColor Red;Write-Host 'If Windows blocked the file: right-click it, choose Properties, Unblock, OK.' -ForegroundColor Yellow}"

echo.
echo Proxy stopped. Press any key to close...
pause >nul
exit /b 0
rem ### PS_PAYLOAD_START ###
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}

$Prefixes = @('http://localhost:8770/', 'http://127.0.0.1:8770/')
$Allowed  = @('ufotosoft.com', 'videomate.cc', 'wiseoel.com')
$SkipHeaders = @(
  'Connection','Content-Length','Date','Expect','Host',
  'Keep-Alive','Range','Referer','Transfer-Encoding',
  'Proxy-Connection'
)

$listener = New-Object System.Net.HttpListener
foreach ($p in $Prefixes) { $listener.Prefixes.Add($p) }
try {
  $listener.Start()
} catch {
  Write-Host ""
  Write-Host ("[ERROR] Could not start on port 8770: " + $_.Exception.Message) -ForegroundColor Red
  Write-Host "Another program (or an older proxy window) is probably using the port." -ForegroundColor Yellow
  Write-Host "Close the old proxy window and try again." -ForegroundColor Yellow
  exit 1
}

Write-Host ""
Write-Host "Mivi CORS proxy running:" -ForegroundColor Green
foreach ($p in $Prefixes) { Write-Host ("  " + $p) -ForegroundColor Green }
Write-Host ("Allowed hosts: " + ($Allowed -join ', '))
Write-Host "Waiting for requests from the Mivi web app... (Ctrl+C to stop)"
Write-Host ""

function Send-Text($ctx, $code, $text) {
  try {
    $b = [Text.Encoding]::UTF8.GetBytes($text)
    $ctx.Response.StatusCode = $code
    $ctx.Response.ContentType = 'text/plain; charset=utf-8'
    $ctx.Response.OutputStream.Write($b, 0, $b.Length)
    $ctx.Response.Close()
  } catch {}
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
    if (-not $ok) { Send-Text $ctx 403 ("host not allowed: " + $hostOnly); continue }

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
      try { $hwr.Headers.Add($k, $req.Headers[$k]) } catch {}
    }
    if ($req.UserAgent) { try { $hwr.UserAgent = $req.UserAgent } catch {} }
    if ($req.Accept)     { try { $hwr.Accept = $req.Accept } catch {} }
    if ($req.Referer)    { try { $hwr.Referer = $req.Referer } catch {} }
    if ($req.ContentType) { try { $hwr.ContentType = $req.ContentType } catch {} }

    if ($body.Length -gt 0) {
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
