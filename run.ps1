#!/usr/bin/env pwsh
# run.ps1

Write-Host "Compiling..."
gcc ./src/main.c -o sqrt_comp.exe

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Compilation failed."
    exit 1
}

Write-Host "Running..."
./sqrt_comp.exe > errors.csv

Write-Host "Plotting..."
python ./plot.py

Write-Host "✅ Done."
