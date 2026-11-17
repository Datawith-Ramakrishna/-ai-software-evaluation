$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)
& .\.venv\Scripts\python.exe evaluation\collect.py
if ($LASTEXITCODE -ne 0) { throw 'Collection failed' }
& .\.venv\Scripts\python.exe evaluationnalyze.py
if ($LASTEXITCODE -ne 0) { throw 'Analysis failed' }
Write-Host 'Open evaluation\comparison.png and evaluation\summary.txt'
