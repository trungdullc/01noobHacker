# smbmap
```
Description: smbclient that also tells permissions and access

# Attempt to list SMB shares as the user "anonymous"
smbmap -H 10.10.10.125 -u anonymous

# Try to list shares without specifying a username (uses defaults)
smbmap -H 10.10.10.125

# Attempt to list SMB shares using "anonymous" user and specify domain "HTB.LOCAL"
smbmap -H 10.10.10.125 -u anonymous -d HTB.LOCAL

# If no domain controller is available, try "localhost" as the domain
smbmap -H 10.10.10.125 -u anonymous -d localhost

# Run enum4linux for comprehensive SMB/NetBIOS enumeration (users, shares, OS info, etc.)
enum4linux 10.10.10.125

# List all SMB shares on the target using SMBv2 protocol, no password (-N)
smbclient -m SMB2 -N -L //10.10.10.125/

# Connect to a specific SMB share (e.g., "Reports") using SMBv2 and no password
smbclient -m SMB2 -N //10.10.10.125/Reports

# If log in correctly use ls, get (DL files), put (Upload files)
smb: \> prompt
```

## Back to README.md
[BACK](/README.md)