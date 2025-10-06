# Cyborg Level 02 → 03 cut -d: -f1 /etc/group | sort | uniq

## Previous Flag
```
172.31.45.167_ipv4
```

## Goal
The password for cyborg4 is the number of users in the Cyborg group within Active Directory PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the number of users is “20” and the file on the desktop is called “_users”, then the password is “20_users”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
# Return all groups in Active Directory                                 # cut extracts only the first field, group names
Get-ADGroup -Filter * | Select-Object Name                              cut -d: -f1 /etc/group
    -Filter * → returns all groups                                          
    Select-Object Name → shows only the Name property (cleaner output)

# Active Directory query using the Get-ADGroup cmdlet
# Returns/Retrieves AD group objects (security groups or distribution groups) from Active Directory
Get-ADGroup -Filter 'Name -like "Cyborg"'

# Retrieves all members of an AD group
Get-ADGroup -Filter 'Name -like "Cyborg"' | Get-ADGroupMember

(Get-ADGroup -Filter 'Name -like "Cyborg"' | Get-ADGroupMember).Count
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg3@cyborg.underthewire.tech -p 22 ⌨️
cyborg3@cyborg.underthewire.tech's password: ⌨️ 172.31.45.167_ipv4
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg3\desktop> dir ⌨️

    Directory: C:\users\cyborg3\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/26/2022   2:14 PM              0 _objects 👀

PS C:\users\cyborg4\desktop> Get-ADGroup -Filter * | Select-Object Name ⌨️

Name
----
Administrators
Users
Guests
Print Operators
Backup Operators
Replicator
Remote Desktop Users
Network Configuration Operators        
Performance Monitor Users
Performance Log Users
Distributed COM Users
IIS_IUSRS
Cryptographic Operators
Event Log Readers
Certificate Service DCOM Access
RDS Remote Access Servers
RDS Endpoint Servers
RDS Management Servers
Hyper-V Administrators
Access Control Assistance Operators
Remote Management Users
System Managed Accounts Group
Storage Replica Administrators
Domain Computers
Domain Controllers
Schema Admins
Enterprise Admins
Cert Publishers
Domain Admins
Domain Users
Domain Guests
Group Policy Creator Owners
RAS and IAS Servers
Server Operators
Account Operators
Pre-Windows 2000 Compatible Access
Incoming Forest Trust Builders
Windows Authorization Access Group
Terminal Server License Servers
Allowed RODC Password Replication Group
Denied RODC Password Replication Group
Read-only Domain Controllers
Enterprise Read-only Domain Controllers
Cloneable Domain Controllers
Protected Users
Key Admins
Enterprise Key Admins
DnsAdmins
DnsUpdateProxy
games
PSRemoting
cyborg 👀

PS C:\users\cyborg3\desktop> Get-ADGroup -Filter 'Name -like "Cyborg"' ⌨️

DistinguishedName : CN=cyborg,OU=Groups,DC=underthewire,DC=tech 
GroupCategory     : Distribution
GroupScope        : Global
Name              : cyborg 👀
ObjectClass       : group
ObjectGUID        : e9511d2f-b09b-40ef-a5b2-180e162ee4a7        
SamAccountName    : cyborg
SID               : S-1-5-21-758131494-606461608-3556270690-2180

PS C:\users\cyborg3\desktop> Get-ADGroup -Filter 'Name -like "Cyborg"' | Get-ADGroupMember ⌨️

distinguishedName : CN=Garafano\, Nida  \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
name              : Garafano, Nida
objectClass       : user
objectGUID        : 5a66b0ca-dab8-448b-9a53-c203f6c29217
SamAccountName    : Nida.Garafano
SID               : S-1-5-21-758131494-606461608-3556270690-2034

distinguishedName : CN=Garafola\, Nidia  \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
name              : Garafola, Nidia
objectClass       : user
objectGUID        : b1e8353c-66bf-446b-8272-387954c16930
SamAccountName    : Nidia.Garafola
SID               : S-1-5-21-758131494-606461608-3556270690-2035

distinguishedName : CN=Garahan\, Niesha  \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
name              : Garahan, Niesha
objectClass       : user
objectGUID        : 8f3a495f-d830-4f85-9bc5-cec8ad891cbc
SamAccountName    : Niesha.Garahan
SID               : S-1-5-21-758131494-606461608-3556270690-2036

distinguishedName : CN=Garala\, Nieves  \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
name              : Garala, Nieves
objectClass       : user
objectGUID        : db33b28f-bcc1-47e4-a61c-92397b479e95
SamAccountName    : Nieves.Garala
SID               : S-1-5-21-758131494-606461608-3556270690-2037

PS C:\users\cyborg3\desktop> (Get-ADGroup -Filter 'Name -like "Cyborg"' | Get-ADGroupMember).Count.ToString() + (gci -File).Name ⌨️
88_objects 👀
PS C:\users\cyborg3\desktop> (Get-ADGroup -Filter 'Name -like "Cyborg"' | Get-ADGroupMember).Count ⌨️                                       
88 👀
PS C:\users\cyborg3\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg4@cyborg.underthewire.tech -p 22 ⌨️
cyborg4@cyborg.underthewire.tech's password: ⌨️ 88_objects

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg4\desktop> whoami ⌨️
underthewire\cyborg4
```

## Flag
88_objects

## Continue
[Continue](./Cyborg0304.md)