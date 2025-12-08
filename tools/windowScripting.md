# Windows Batch scripting
```python
Description: cmd.exe script different than Linux

# Note: Python script into a Windows executable
pip install pyinstaller
pyinstaller --onefile pythonScript.py
    Generates dist/pythonScript.exe
```

| Action / Command | Windows Batch (cmd.exe) | Bash / sh (Linux, macOS) | PowerShell |
|-----------------|------------------------|--------------------------|------------|
| **Print text** | `echo Hello` | `echo "Hello"` | `Write-Output "Hello"` (alias `echo`) |
| **List files** | `dir` | `ls` / `ls -l` | `Get-ChildItem` (alias `ls`) |
| **Change directory** | `cd folder` | `cd folder` | `Set-Location folder` (alias `cd`) |
| **Copy file** | `copy src dest` | `cp src dest` | `Copy-Item src dest` |
| **Move file** | `move src dest` | `mv src dest` | `Move-Item src dest` |
| **Delete file / dir** | `del file.txt` / `rmdir /S /Q folder` | `rm file.txt` / `rm -r folder` | `Remove-Item file.txt` / `Remove-Item folder -Recurse` |
| **Create directory** | `mkdir folder` | `mkdir folder` | `New-Item -ItemType Directory folder` (alias `mkdir`) |
| **Show current path** | `cd` | `pwd` | `Get-Location` |
| **Set variable** | `set NAME=value` | `NAME=value` (export: `export NAME=value`) | `$env:NAME = 'value'` or `$NAME = 'value'` |
| **Use variable** | `%NAME%` | `$NAME` | `$NAME` (environment: `$env:NAME`) |
| **Prompt for input** | `set /p var=Enter:` | `read var` | `$var = Read-Host "Enter:"` |
| **If statement** | `if %x%==1 ( ... ) else ( ... )` | `if [ "$x" -eq 1 ]; then ...; fi` | `if ($x -eq 1) { ... } else { ... }` |
| **For / Loop** | `for %%i in (*.txt) do echo %%i` | `for f in *.txt; do echo "$f"; done` | `foreach ($f in Get-ChildItem *.txt) { $f }` |
| **Comments** | `REM comment` or `:: comment` | `# comment` | `# comment` |
| **Search text in file (`grep`)** | `find "text" file.txt` / `findstr /S /I "text" *.*` (recursive) | `grep "text" file.txt` / `grep -R "text" .` | `Select-String "text" file.txt` / `Select-String -Path . -Pattern "text" -Recurse` |
| **wget (download)** | Not installed by default; can use `wget.exe` if added | `wget https://example.com/file` | `wget https://example.com/file` (alias to `Invoke-WebRequest`, not GNU) |
| **curl (download)** | `curl https://example.com` (Windows 10+ ships curl.exe) | `curl https://example.com` | `curl https://example.com` (alias to `Invoke-WebRequest`) |
| **PowerShell-style download** | — (use curl.exe or wget.exe) | `curl -o file https://...` | `Invoke-WebRequest https://... -OutFile file` |
| **Pipe output** | `command | other` (text) | `command | other` (text) | `command | other` (passes objects, not plain text) |
| **Run executable** | `program.exe` | `./program` or `program` | `.\program.exe` |


## Back to README.md
[BACK](../README.md)