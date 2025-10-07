# Century Level 04 → 05 domainname

## Previous Flag
```
15768
```

## Goal
The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the short name of the domain is “blob” and the file on the desktop is named “1234”, the password would be “blob1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-WmiObject Win32_ComputerSystem                  dnsdomainname       hostname -f
                                                    hostname
                                                    lscpu               # CPU info
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century5@century.underthewire.tech -p 22 ⌨️
century5@century.underthewire.tech's password: ⌨️ 15768

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century5\desktop> dir ⌨️

    Directory: C:\users\century5\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM             54 3347 👀

# Method 1: ChatGPT: name of the domain in which this system resides
PS C:\users\century5\desktop> (Get-WmiObject Win32_ComputerSystem).Domain ⌨️
underthewire.tech
PS C:\users\century5\desktop> (Get-WmiObject Win32_ComputerSystem).Domain + (ls -File).Name ⌨️
underthewire.tech3347 🔐

# Method 2: ChatGPT
PS C:\users\century5\desktop> (Get-CimInstance Win32_ComputerSystem).Domain + (ls).Name ⌨️
underthewire.tech3347 🔐

PS C:\users\century5\desktop> Get-ADDomain ⌨️                         

AllowedDNSSuffixes                 : {}
ChildDomains                       : {}
ComputersContainer                 : CN=Computers,DC=underthewire,DC=tech
DeletedObjectsContainer            : CN=Deleted Objects,DC=underthewire,DC=tech   
DistinguishedName                  : DC=underthewire,DC=tech
DNSRoot                            : underthewire.tech
DomainControllersContainer         : OU=Domain Controllers,DC=underthewire,DC=tech
DomainMode                         : Windows2016Domain
DomainSID                          : S-1-5-21-758131494-606461608-3556270690
ForeignSecurityPrincipalsContainer : CN=ForeignSecurityPrincipals,DC=underthewire,DC=tech
Forest                             : underthewire.tech
InfrastructureMaster               : utw.underthewire.tech
LastLogonReplicationInterval       :
LinkedGroupPolicyObjects           : {cn={ECB4A7C0-B4E1-41B1-9E89-161CFA679999},cn=policies,cn=system,DC=underthewire,DC=tech,
                                     CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=underthewire,DC=tech}
LostAndFoundContainer              : CN=LostAndFound,DC=underthewire,DC=tech
ManagedBy                          :
Name                               : underthewire 👀
NetBIOSName                        : underthewire
ObjectClass                        : domainDNS
ObjectGUID                         : bdccf3ad-b495-4d86-a94c-60f0d832e6f0
ParentDomain                       :
PDCEmulator                        : utw.underthewire.tech
PublicKeyRequiredPasswordRolling   : True
QuotasContainer                    : CN=NTDS Quotas,DC=underthewire,DC=tech
ReadOnlyReplicaDirectoryServers    : {}
ReplicaDirectoryServers            : {utw.underthewire.tech}
RIDMaster                          : utw.underthewire.tech
SubordinateReferences              : {DC=ForestDnsZones,DC=underthewire,DC=tech, DC=DomainDnsZones,DC=underthewire,DC=tech, 
                                     CN=Configuration,DC=underthewire,DC=tech}
SystemsContainer                   : CN=System,DC=underthewire,DC=tech
UsersContainer                     : CN=Users,DC=underthewire,DC=tech

PS C:\users\century5\desktop> Get-ADDomain | Get-Member ⌨️

   TypeName: Microsoft.ActiveDirectory.Management.ADDomain

Name                               MemberType            Definition
----                               ----------            ----------
Contains                           Method                bool Contains(string propertyName)
Equals                             Method                bool Equals(System.Object obj)
GetEnumerator                      Method                System.Collections.IDictionaryEnumerator GetEnumerator()
GetHashCode                        Method                int GetHashCode()
GetType                            Method                type GetType()
ToString                           Method                string ToString()
Item                               ParameterizedProperty Microsoft.ActiveDirectory.Management.ADPropertyValueCollection Item(string propertyName) {get;}   
AllowedDNSSuffixes                 Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection AllowedDNSSuffixes {get;set;}      
ChildDomains                       Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection ChildDomains {get;}
ComputersContainer                 Property              System.String ComputersContainer {get;}
DeletedObjectsContainer            Property              System.String DeletedObjectsContainer {get;}
DistinguishedName                  Property              System.String DistinguishedName {get;set;}
DNSRoot                            Property              System.String DNSRoot {get;}
DomainControllersContainer         Property              System.String DomainControllersContainer {get;}
DomainMode                         Property              System.Nullable`1[[Microsoft.ActiveDirectory.Management.ADDomainMode, Microsoft.ActiveDirector... 
DomainSID                          Property              System.Security.Principal.SecurityIdentifier DomainSID {get;set;}
ForeignSecurityPrincipalsContainer Property              System.String ForeignSecurityPrincipalsContainer {get;}
Forest                             Property              System.String Forest {get;}
InfrastructureMaster               Property              System.String InfrastructureMaster {get;}
LastLogonReplicationInterval       Property              System.Nullable`1[[System.TimeSpan, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken...
LinkedGroupPolicyObjects           Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection LinkedGroupPolicyObjects {get;}    
LostAndFoundContainer              Property              System.String LostAndFoundContainer {get;}
ManagedBy                          Property              System.String ManagedBy {get;set;}
Name                               Property              System.String Name {get;}
NetBIOSName                        Property              System.String NetBIOSName {get;}
ObjectClass                        Property              System.String ObjectClass {get;set;}
ObjectGUID                         Property              System.Nullable`1[[System.Guid, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77... 
ParentDomain                       Property              System.String ParentDomain {get;}
PDCEmulator                        Property              System.String PDCEmulator {get;}
PublicKeyRequiredPasswordRolling   Property              System.Boolean PublicKeyRequiredPasswordRolling {get;set;}
QuotasContainer                    Property              System.String QuotasContainer {get;}
ReadOnlyReplicaDirectoryServers    Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection ReadOnlyReplicaDirectoryServers... 
ReplicaDirectoryServers            Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection ReplicaDirectoryServers {get;}     
RIDMaster                          Property              System.String RIDMaster {get;}
SubordinateReferences              Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection SubordinateReferences {get;}       
SystemsContainer                   Property              System.String SystemsContainer {get;}
UsersContainer                     Property              System.String UsersContainer {get;}

# Note: Select-Object gets column vs Property ❤️
PS C:\users\century5\desktop> Get-ADDomain | Get-Member | Select-Object Name ⌨️

Name
----
Contains
Equals
GetEnumerator
GetHashCode
GetType
ToString
Item
AllowedDNSSuffixes
ChildDomains
ComputersContainer
DeletedObjectsContainer
DistinguishedName
DNSRoot
DomainControllersContainer
DomainMode
DomainSID
ForeignSecurityPrincipalsContainer
Forest
InfrastructureMaster
LastLogonReplicationInterval
LinkedGroupPolicyObjects
LostAndFoundContainer
ManagedBy
Name
NetBIOSName
ObjectClass
ObjectGUID
ParentDomain
PDCEmulator
PublicKeyRequiredPasswordRolling
QuotasContainer
ReadOnlyReplicaDirectoryServers
ReplicaDirectoryServers
RIDMaster
SubordinateReferences
SystemsContainer
UsersContainer

# Important: When using Property don't forget ().
PS C:\users\century5\desktop> (Get-ADDomain).Name + (ls -File).Name ⌨️
underthewire3347 🔐

PS C:\users\century5\desktop> [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain().Name.Split('.')[0] ⌨️
underthewire
PS C:\users\century5\desktop> [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain().Name.Split('.')[0] + (ls -File).Name ⌨️
underthewire3347 🔐

# Method 4:
PS C:\users\century5\desktop> Get-WmiObject Win32_ComputerSystem ⌨️
Domain              : underthewire.tech 👀
Manufacturer        : BOCHS_
Model               : BXPC____
Name                : UTW
PrimaryOwnerName    : UTW_Team
TotalPhysicalMemory : 16776658944  

PS C:\users\century5\desktop> (Get-WmiObject Win32_ComputerSystem) | Get-Member "Domain" ⌨️

   TypeName: System.Management.ManagementObject#root\cimv2\Win32_ComputerSystem

Name   MemberType Definition
----   ---------- ----------
Domain Property   string Domain {get;set;}

PS C:\users\century5\desktop> Get-WmiObject Win32_ComputerSystem | Select-Object Domain ⌨️

Domain
------
underthewire.tech

PS C:\users\century5\desktop> ((Get-WmiObject Win32_ComputerSystem).Domain -split '\.')[0] ⌨️❤️❤️❤️❤️❤️
underthewire
PS C:\users\century5\desktop> ((Get-WmiObject Win32_ComputerSystem).Domain -split '\.')[0] + (ls -File).Name ⌨️
underthewire3347 🔐

PS C:\users\century5\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century6@century.underthewire.tech -p 22 ⌨️
century6@century.underthewire.tech's password: ⌨️ underthewire3347

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century6\desktop> whoami ⌨️
underthewire\century6
```

## Flag
underthewire3347

## Continue
[Continue](./Century0506.md)