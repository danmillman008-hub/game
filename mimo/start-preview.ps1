# اجرای پیش‌نمایش میمو روی ویندوز
#
#   .\start-preview.ps1                 → http://localhost:4000
#   .\start-preview.ps1 -NoEngines      → فقط پوسته و موتور یادگیری
#
# پیش‌نیاز: Python 3.11+، Node.js 22+ و npm. اسکریپت خودش موتورها را (یک‌بار) نصب می‌کند.

param(
  [int]$Port = 4000,
  [int]$EpmPort = 8765,
  [int]$LhPort = 3000,
  [switch]$NoEngines
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$runtime = Join-Path $here '.runtime'
$logs = Join-Path $runtime 'logs'
New-Item -ItemType Directory -Force -Path $logs, (Join-Path $runtime 'epm-data'), (Join-Path $runtime 'lh-data') | Out-Null

function Say($message) { Write-Host "[میمو] $message" -ForegroundColor Cyan }
function Warn($message) { Write-Host "[میمو] $message" -ForegroundColor Yellow }

foreach ($tool in 'python', 'node', 'npm', 'git') {
  if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) { throw "ابزار لازم نصب نیست: $tool" }
}

$epmDist = Join-Path $here 'engines\src\epm\frontend\dist-preview\index.html'
$lhModules = Join-Path $here 'engines\src\learnharness\node_modules'
if (-not $NoEngines -and ((-not (Test-Path $epmDist)) -or (-not (Test-Path $lhModules)))) {
  Say 'موتورها آماده نیستند؛ نصب اولیه آغاز می‌شود (چند دقیقه).'
  & bash (Join-Path $here 'tools\bootstrap_engines.sh')
}

$processes = @()
$env:PREVIEW_PORT = "$Port"
$env:EPM_URL = "http://127.0.0.1:$EpmPort"
$env:LH_URL = "http://127.0.0.1:$LhPort"

function Wait-Http($url, $seconds, $label) {
  for ($i = 0; $i -lt $seconds; $i += 2) {
    try {
      $response = Invoke-WebRequest -Uri $url -TimeoutSec 2 -UseBasicParsing
      if ($response.StatusCode -lt 500) { Say "$label آماده است"; return $true }
    } catch { Start-Sleep -Seconds 2 }
  }
  Warn "$label پاسخ نداد؛ بخش مربوطه غیرفعال می‌ماند."
  return $false
}

try {
  if (-not $NoEngines) {
    $venvPython = Join-Path $runtime 'epm-venv\Scripts\python.exe'
    if (Test-Path $venvPython) {
      Say "اجرای EPM روی 127.0.0.1:$EpmPort"
      $epmArgs = @{
        FilePath = $venvPython
        ArgumentList = 'backend/standalone_main.py'
        WorkingDirectory = (Join-Path $here 'engines\src\epm')
        RedirectStandardOutput = (Join-Path $logs 'epm.log')
        RedirectStandardError = (Join-Path $logs 'epm.err.log')
        PassThru = $true
      }
      $env:EPM_DATA_DIR = Join-Path $runtime 'epm-data'
      $env:EPM_FRONTEND_DIST = Join-Path $here 'engines\src\epm\frontend\dist-preview'
      $env:EPM_AUTH = '0'
      $env:EPM_PORT = "$EpmPort"
      $env:EPM_HOST = '127.0.0.1'
      $processes += Start-Process @epmArgs
      Wait-Http "http://127.0.0.1:$EpmPort/api/health" 60 'EPM' | Out-Null
    }

    if (Test-Path $lhModules) {
      Say "اجرای LearnHarness روی 127.0.0.1:$LhPort"
      $env:LH_DATA_DIR = Join-Path $runtime 'lh-data'
      $env:LH_AUTH_FILE = Join-Path $runtime 'lh-auth.json'
      $lh = Start-Process -FilePath 'npm.cmd' -ArgumentList 'run', 'dev', '--', '--port', "$LhPort" `
        -WorkingDirectory (Join-Path $here 'engines\src\learnharness') `
        -RedirectStandardOutput (Join-Path $logs 'learnharness.log') `
        -RedirectStandardError (Join-Path $logs 'learnharness.err.log') -PassThru
      $processes += $lh
      Wait-Http "http://127.0.0.1:$LhPort/max" 180 'LearnHarness (Max)' | Out-Null
    }
  }

  Say "پوستهٔ میمو: http://localhost:$Port"
  Say "پورت‌ها: پوسته $Port · EPM $EpmPort · LearnHarness $LhPort"
  Say 'برای توقف: Ctrl+C'
  & python (Join-Path $here 'host\preview_host.py') --port $Port
}
finally {
  Warn 'در حال توقف سرویس‌ها…'
  foreach ($process in $processes) {
    if ($process -and -not $process.HasExited) { Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue }
  }
}
