# Groot Level 04 → 05 -Properties * | Format-List * 

## Previous Flag
```
destroyer
```

## Goal
The password for groot6 is the name of the workstation that the user with a username of “baby.groot” can log into as depicted in Active Directory PLUS the name of the file on the desktop<br>

NOTE:<br>
– If the workstation is “system1” and the file on the desktop is named “_log”, the password would be “system1_log”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-ADUser -Identity baby.groot -Properties * | Format-List * 
    -Properties * tells Get-ADUser to retrieve all properties, not just the default ones
    Format-List * prints them in a readable list instead of a table

Get-ADUser -Filter 'samAccountName -like "baby.groot"' -Properties userWorkstations
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot5@groot.underthewire.tech -p 22 ⌨️
groot5@groot.underthewire.tech's password: ⌨️ destroyer

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot5\desktop> dir ⌨️

    Directory: C:\users\Groot5\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/20/2020   3:38 PM              0 _enterprise 👀

PS C:\users\Groot5\desktop> Get-ADUser -Filter 'samAccountName -like "baby.groot"' ⌨️

DistinguishedName : CN=Groot \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Baby
Name              : Groot
ObjectClass       : user
ObjectGUID        : c938286d-f672-45b7-97ee-b371f0e39836
SamAccountName    : baby.groot
SID               : S-1-5-21-758131494-606461608-3556270690-2175
Surname           : Groot
UserPrincipalName : baby.groot

# Show All Properties of object in a formatted list
PS C:\users\Groot5\desktop> Get-ADUser -Identity baby.groot -Properties * | Format-List * ⌨️

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
CanonicalName                        : underthewire.tech/X-Wing/T-65/Groot
Certificates                         : {}
City                                 :
CN                                   : Groot
codePage                             : 0
Company                              :
CompoundIdentitySupported            : {}
Country                              : 
countryCode                          : 0
Created                              : 8/30/2018 3:28:43 AM
createTimeStamp                      : 8/30/2018 3:28:43 AM
Deleted                              :
Department                           :
Description                          :
DisplayName                          : Groot
DistinguishedName                    : CN=Groot \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Division                             :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {1/1/1601 12:00:00 AM}
EmailAddress                         : baby.groot@underthewire.tech
EmployeeID                           :
EmployeeNumber                       :
Enabled                              : False
Fax                                  :
GivenName                            : Baby
HomeDirectory                        :
HomedirRequired                      : False
HomeDrive                            :
HomePage                             :
HomePhone                            :
Initials                             :
instanceType                         : 4
isDeleted                            :
KerberosEncryptionType               : {}
LastBadPasswordAttempt               :
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 0
LastLogonDate                        :
LockedOut                            : False
logonCount                           : 0
LogonWorkstations                    : wk11
mail                                 : baby.groot@underthewire.tech
Manager                              :
MemberOf                             : {}
MNSLogonAccount                      : False
MobilePhone                          :
Modified                             : 8/30/2018 10:51:10 AM
modifyTimeStamp                      : 8/30/2018 10:51:10 AM
msDS-User-Account-Control-Computed   : 8388608
Name                                 : Groot
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Person,CN=Schema,CN=Configuration,DC=underthewire,DC=tech
ObjectClass                          : user
ObjectGUID                           : c938286d-f672-45b7-97ee-b371f0e39836
objectSid                            : S-1-5-21-758131494-606461608-3556270690-2175
Office                               :
OfficePhone                          :
Organization                         :
OtherName                            :
PasswordExpired                      : True
PasswordLastSet                      :
PasswordNeverExpires                 : False
PasswordNotRequired                  : False
POBox                                :
PostalCode                           :
PrimaryGroup                         : CN=Domain Users,CN=Users,DC=underthewire,DC=tech
primaryGroupID                       : 513
PrincipalsAllowedToDelegateToAccount : {}
ProfilePath                          :
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 0
SamAccountName                       : baby.groot
sAMAccountType                       : 805306368
ScriptPath                           :
sDRightsEffective                    : 0
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-758131494-606461608-3556270690-2175
SIDHistory                           : {}
SmartcardLogonRequired               : False
sn                                   : Groot
State                                :
StreetAddress                        :
Surname                              : Groot
Title                                :
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 514
userCertificate                      : {}
UserPrincipalName                    : baby.groot
userWorkstations                     : wk11 👀
uSNChanged                           : 20021
uSNCreated                           : 19663
whenChanged                          : 8/30/2018 10:51:10 AM
whenCreated                          : 8/30/2018 3:28:43 AM
PropertyNames                        : {AccountExpirationDate, accountExpires, AccountLockoutTime, AccountNotDelegated...}
AddedProperties                      : {}
RemovedProperties                    : {}
ModifiedProperties                   : {}
PropertyCount                        : 107

PS C:\users\Groot5\desktop> Get-ADUser -Filter 'samAccountName -like "baby.groot"' -Properties userWorkstations ⌨️

DistinguishedName : CN=Groot \ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Baby
Name              : Groot
ObjectClass       : user
ObjectGUID        : c938286d-f672-45b7-97ee-b371f0e39836
SamAccountName    : baby.groot
SID               : S-1-5-21-758131494-606461608-3556270690-2175
Surname           : Groot
UserPrincipalName : baby.groot
userWorkstations  : wk11 👀

PS C:\users\Groot5\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot6@groot.underthewire.tech -p 22 ⌨️
groot6@groot.underthewire.tech's password: ⌨️ wk11_enterprise

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot6\desktop> whoami ⌨️
underthewire\groot6
```

## Flag
wk11_enterprise

## Continue
[Continue](./Groot0506.md)