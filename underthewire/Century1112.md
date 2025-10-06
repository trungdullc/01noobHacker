# Century Level 11 → 12 Active Directory, Domain Controller

## Previous Flag
```
secret_sauce
```

## Goal
The password for Century13 is the description of the computer designated as a Domain Controller within this domain PLUS the name of the file on the desktop.<br>

NOTE:<br>
– The password will be lowercase no matter how it appears on the screen<br>
– If the description “today_is” and the file on the desktop is named “_cool”, the password would be “today_is_cool”

## What I learned
```
Get-ADDomainController                                          Linux doesn’t have Active Directory built-in
Get-ADComputer -Identity "UTW" -Properties * 
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century12@century.underthewire.tech -p 22 ⌨️
century12@century.underthewire.tech's password: ⌨️ secret_sauce

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century12\desktop> dir

    Directory: C:\users\century12\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:34 AM             30 _things 👀

PS C:\users\century12\desktop> Get-ADDomainController ⌨️

ComputerObjectDN           : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DefaultPartition           : DC=underthewire,DC=tech
Domain                     : underthewire.tech
Enabled                    : True
Forest                     : underthewire.tech
HostName                   : utw.underthewire.tech
InvocationId               : 09ee1897-2210-4ac9-989d-e19b4241e9c6
IPv4Address                : 192.99.167.156
IPv6Address                :
IsGlobalCatalog            : True
IsReadOnly                 : False
LdapPort                   : 389
Name                       : UTW 👀
NTDSSettingsObjectDN       : CN=NTDS Settings,CN=UTW,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=underthewire,DC=tech
OperatingSystem            : Windows Server 2016 Standard
OperatingSystemHotfix      :
OperatingSystemServicePack :
OperatingSystemVersion     : 10.0 (14393)
OperationMasterRoles       : {SchemaMaster, DomainNamingMaster, PDCEmulator, RIDMaster...}
                             CN=Schema,CN=Configuration,DC=underthewire,DC=tech, CN=Configuration,DC=underthewire,DC=tech...}
ServerObjectDN             : CN=UTW,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=underthewire,DC=tech
ServerObjectGuid           : df17c8a3-dd76-438b-8ddf-b7ad3e624618
Site                       : Default-First-Site-Name
SslPort                    : 636

PS C:\users\century12\desktop> Get-ADComputer -Identity "UTW" -Properties * ⌨️

AccountExpirationDate                :
accountExpires                       : 9223372036854775807
AccountLockoutTime                   :
AccountNotDelegated                  : False
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 0
badPasswordTime                      : 0
badPwdCount                          : 0
CannotChangePassword                 : False
CanonicalName                        : underthewire.tech/Domain Controllers/UTW
Certificates                         : {}
CN                                   : UTW
codePage                             : 0
CompoundIdentitySupported            : {False}
countryCode                          : 0
Created                              : 8/30/2018 2:53:47 AM
createTimeStamp                      : 8/30/2018 2:53:47 AM
Deleted                              :
Description                          : i_authenticate 👀
DisplayName                          :
DistinguishedName                    : CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech
DNSHostName                          : utw.underthewire.tech
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {5/19/2020 6:51:38 PM, 5/19/2020 6:51:21 PM, 8/30/2018 3:21:15 AM, 8/30/2018 2:53:49 AM...}
Enabled                              : True
HomedirRequired                      : False
HomePage                             :
instanceType                         : 4
IPv4Address                          : 192.99.167.156
IPv6Address                          :
isCriticalSystemObject               : True
isDeleted                            :
KerberosEncryptionType               : {RC4, AES128, AES256}
LastBadPasswordAttempt               :
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 134038921337602395
LastLogonDate                        : 9/26/2025 7:22:13 AM
lastLogonTimestamp                   : 134033449337582926
localPolicyFlags                     : 0
Location                             :
LockedOut                            : False
logonCount                           : 16376
ManagedBy                            :
MemberOf                             : {}
MNSLogonAccount                      : False
Modified                             : 9/26/2025 7:22:13 AM
modifyTimeStamp                      : 9/26/2025 7:22:13 AM
msDFSR-ComputerReferenceBL           : {CN=UTW,CN=Topology,CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=underthewire,DC=tech}
msDS-SupportedEncryptionTypes        : 28
msDS-User-Account-Control-Computed   : 0
Name                                 : UTW
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Computer,CN=Schema,CN=Configuration,DC=underthewire,DC=tech
ObjectClass                          : computer
ObjectGUID                           : 5ca56844-bb73-4234-ac85-eed2d0d01a2e
objectSid                            : S-1-5-21-758131494-606461608-3556270690-1000
OperatingSystem                      : Windows Server 2016 Standard
OperatingSystemHotfix                :
OperatingSystemServicePack           :
OperatingSystemVersion               : 10.0 (14393)
PasswordExpired                      : False
PasswordLastSet                      : 9/6/2025 3:11:20 PM
PasswordNeverExpires                 : False
PasswordNotRequired                  : False
PrimaryGroup                         : CN=Domain Controllers,CN=Users,DC=underthewire,DC=tech
primaryGroupID                       : 516
PrincipalsAllowedToDelegateToAccount : {}
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 134016450802670424
rIDSetReferences                     : {CN=RID Set,CN=UTW,OU=Domain Controllers,DC=underthewire,DC=tech}
SamAccountName                       : UTW$
sAMAccountType                       : 805306369
sDRightsEffective                    : 0
serverReferenceBL                    : {CN=UTW,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=underthewire,DC=tech}
ServiceAccount                       : {}
servicePrincipalName                 : {Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/utw.underthewire.tech,
                                       ldap/utw.underthewire.tech/ForestDnsZones.underthewire.tech,
                                       ldap/utw.underthewire.tech/DomainDnsZones.underthewire.tech, TERMSRV/UTW...}
ServicePrincipalNames                : {Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/utw.underthewire.tech,
                                       ldap/utw.underthewire.tech/ForestDnsZones.underthewire.tech,
                                       ldap/utw.underthewire.tech/DomainDnsZones.underthewire.tech, TERMSRV/UTW...}
SID                                  : S-1-5-21-758131494-606461608-3556270690-1000
SIDHistory                           : {}
TrustedForDelegation                 : True
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 532480
userCertificate                      : {}
UserPrincipalName                    :
uSNChanged                           : 3859624
uSNCreated                           : 12293
whenChanged                          : 9/26/2025 7:22:13 AM
whenCreated                          : 8/30/2018 2:53:47 AM

PS C:\users\century12\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century13@century.underthewire.tech -p 22 ⌨️
century13@century.underthewire.tech's password: ⌨️ i_authenticate_things

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century13\desktop> whoami ⌨️
underthewire\century13
```

## Flag
i_authenticate_things

## Continue
[Continue](./Century1213.md)