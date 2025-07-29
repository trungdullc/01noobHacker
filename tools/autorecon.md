# autorecon
```
Source: https://github.com/Tib3rius/AutoRecon
Description:
AutoRecon automatically:
    Detects open ports (via nmap)
    Identifies running services
    Runs service-specific enumeration tools (smbmap, enum4linux, ftp-anon, nikto)
    Saves organized output to folders

sudo apt install autorecon                              git clone https://github.com/Tib3rius/AutoRecon.git
                                                        cd AutoRecon
                                                        pip3 install -r requirements.txt
                                                        python3 setup.py install

# Basic scan w/ default settings
autorecon -vv 192.168.0.1

# Basic scan w/ multiple targets
autorecon 10.10.10.125 10.10.10.129

# Custom wordlist for brute force
autorecon --wordlist /usr/share/wordlists/rockyou.txt 10.10.10.125
```

## Comparison to other programs
```
Tool	                Focus
AutoRecon	            Recon/Enumeration automation
Nmap	                Port and service scanning
LinPEAS, WinPEAS	    Post-exploitation privilege escalation
enum4linux	            Manual SMB/Windows enumeration
recon-ng	            Web and OSINT recon
```

## Back to README.md
[BACK](/README.md)