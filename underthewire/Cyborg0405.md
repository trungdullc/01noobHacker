# Cyborg Level 04 → 05 variable

## Previous Flag
```
bacon_eggs
```

## Goal
The password for cyborg6 is the last name of the user who has logon hours set on their account PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the last name is “fields” and the file on the desktop is called “_address”, then the password is “fields_address”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Get-Help Where-Object

(Get-ADUser -Filter * -Properties logonHours,Surname | Where-Object { $_.logonHours -and $_.Surname } | Select-Object -First 1 -ExpandProperty Surname).ToLower() + (Get-Item .).Name
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg5@cyborg.underthewire.tech -p 22 ⌨️
cyborg5@cyborg.underthewire.tech's password: ⌨️ bacon_eggs

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg5\desktop> dir ⌨️

    Directory: C:\users\cyborg5\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _timer 👀

# Method 1:
PS C:\users\cyborg5\desktop> Get-ADUser -Filter * -Properties * | Where-Object { $_.Name -like "*hours*" } ⌨️
PS C:\users\cyborg5\desktop> Get-ADUser -Filter * -Properties * | Get-Member -Name '*hours*' ⌨️

   TypeName: Microsoft.ActiveDirectory.Management.ADUser 

Name       MemberType Definition
----       ---------- ----------
logonHours Property   System.Byte[] logonHours {get;set;} 👀

PS C:\users\cyborg5\desktop> Get-ADUser -Filter * -Properties * | Where-Object { $_.logonHours } ⌨️

AccountExpirationDate                :
accountExpires                       : 0
AccountLockoutTime                   :
AccountNotDelegated                  : False
adminCount                           : 1
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 140
badPasswordTime                      : 134035915323071364
badPwdCount                          : 140
CannotChangePassword                 : False
CanonicalName                        : underthewire.tech/Users/Administrator
Certificates                         : {}
City                                 :
CN                                   : Administrator
codePage                             : 0
Company                              :
CompoundIdentitySupported            : {}
Country                              :
countryCode                          : 0
Created                              : 8/30/2018 2:51:16 AM
createTimeStamp                      : 8/30/2018 2:51:16 AM
Deleted                              :
Department                           :
Description                          : Built-in account for administering the computer/domain
DisplayName                          :
DistinguishedName                    : CN=Administrator,CN=Users,DC=underthewire,DC=tech
Division                             :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {8/30/2018 3:09:00 AM, 8/30/2018 3:08:59 AM, 8/30/2018 2:53:49 AM, 1/1/1601 6:12:16 PM}
EmailAddress                         :
EmployeeID                           :
EmployeeNumber                       :
Enabled                              : True
Fax                                  : 
GivenName                            :
HomeDirectory                        :
HomedirRequired                      : False
HomeDrive                            :
HomePage                             :
HomePhone                            :
Initials                             :
instanceType                         : 4
isCriticalSystemObject               : True
isDeleted                            :
KerberosEncryptionType               : {}
LastBadPasswordAttempt               : 9/29/2025 3:52:12 AM
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 134031264228021418
LastLogonDate                        : 9/20/2025 11:00:13 PM
lastLogonTimestamp                   : 134028828133979336
LockedOut                            : False
logonCount                           : 570
logonHours                           : {255, 255, 255, 255...}
LogonWorkstations                    :
Manager                              :
MemberOf                             : {CN=Group Policy Creator Owners,CN=Users,DC=underthewire,DC=tech, CN=Domain Admins,CN=Users,DC=underthewire,DC=tech,  
                                       CN=Enterprise Admins,CN=Users,DC=underthewire,DC=tech, CN=Schema Admins,CN=Users,DC=underthewire,DC=tech...}
MNSLogonAccount                      : False
MobilePhone                          :
Modified                             : 9/20/2025 11:00:13 PM
modifyTimeStamp                      : 9/20/2025 11:00:13 PM
msDS-User-Account-Control-Computed   : 0
Name                                 : Administrator
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Person,CN=Schema,CN=Configuration,DC=underthewire,DC=tech
ObjectClass                          : user
ObjectGUID                           : 427058c2-1d57-4e49-a23d-204865b502ae
objectSid                            : S-1-5-21-758131494-606461608-3556270690-500
Office                               :
OfficePhone                          :
Organization                         :
OtherName                            :
PasswordExpired                      : False
PasswordLastSet                      : 8/30/2018 2:41:02 AM
PasswordNeverExpires                 : False
PasswordNotRequired                  : False
POBox                                :
PostalCode                           :
PrimaryGroup                         : CN=Domain Users,CN=Users,DC=underthewire,DC=tech
primaryGroupID                       : 513
PrincipalsAllowedToDelegateToAccount : {}
ProfilePath                          :
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 131800704624162195
SamAccountName                       : Administrator
sAMAccountType                       : 805306368
ScriptPath                           :
sDRightsEffective                    : 0
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-758131494-606461608-3556270690-500
SIDHistory                           : {}
SmartcardLogonRequired               : False
State                                :
StreetAddress                        :
Surname                              :
Title                                :
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 512
userCertificate                      : {}
UserPrincipalName                    :
uSNChanged                           : 3856971
uSNCreated                           : 8196
whenChanged                          : 9/20/2025 11:00:13 PM
whenCreated                          : 8/30/2018 2:51:16 AM

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
CanonicalName                        : underthewire.tech/X-Wing/T-85/Rowray, Benny
Certificates                         : {}
City                                 :
CN                                   : Rowray, Benny
codePage                             : 0
Company                              :
CompoundIdentitySupported            : {}
Country                              :
countryCode                          : 0
Created                              : 8/30/2018 3:25:36 AM
createTimeStamp                      : 8/30/2018 3:25:36 AM
Deleted                              :
Department                           :
Description                          :
DisplayName                          : Rowray, Benny
DistinguishedName                    : CN=Rowray\, Benny  \ ,OU=T-85,OU=X-Wing,DC=underthewire,DC=tech
Division                             :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {1/1/1601 12:00:00 AM}
EmailAddress                         : Benny.Rowray@underthewire.tech
EmployeeID                           :
EmployeeNumber                       :
Enabled                              : False
Fax                                  :
GivenName                            : Benny
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
logonHours                           : {0, 0, 0, 0...}
LogonWorkstations                    :
mail                                 : Benny.Rowray@underthewire.tech
Manager                              :
MemberOf                             : {}
MNSLogonAccount                      : False
MobilePhone                          :
Modified                             : 8/30/2018 10:45:34 AM
modifyTimeStamp                      : 8/30/2018 10:45:34 AM
msDS-User-Account-Control-Computed   : 8388608
Name                                 : Rowray, Benny
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Person,CN=Schema,CN=Configuration,DC=underthewire,DC=tech
ObjectClass                          : user
ObjectGUID                           : c9aad4f3-3e4f-46b5-84db-2bb7105796dd
objectSid                            : S-1-5-21-758131494-606461608-3556270690-1647
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
SamAccountName                       : Benny.Rowray
sAMAccountType                       : 805306368
ScriptPath                           :
sDRightsEffective                    : 0
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-758131494-606461608-3556270690-1647
SIDHistory                           : {}
SmartcardLogonRequired               : False
sn                                   : Rowray
State                                :
StreetAddress                        :
Surname                              : Rowray 👀
Title                                :
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 514
userCertificate                      : {}
UserPrincipalName                    : Benny.Rowray
uSNChanged                           : 19944
uSNCreated                           : 16493
whenChanged                          : 8/30/2018 10:45:34 AM
whenCreated                          : 8/30/2018 3:25:36 AM

PS C:\users\cyborg5\desktop> Get-ADUser -Filter * -Properties * | Where-Object { $_.logonHours } | Select Surname, logonHours ⌨️

Surname logonHours
------- ----------
        {255, 255, 255, 255...}
Rowray  {0, 0, 0, 0...} 👀

# Method 2
# Get all of the users in AD, all of their properties, and store them in a variable
PS C:\users\cyborg5\desktop> $allADUsers = Get-ADUser -Filter * -Properties * ⌨️❤️❤️❤️❤️❤️
# PS C:\users\cyborg5\desktop> echo $allAdUsers ⌨️

# Get-Member cmdlet to inspect the AD user object properties where any property contains the word "hours"
PS C:\users\cyborg5\desktop> $allADUsers | Get-Member -Name '*hours*' ⌨️

   TypeName: Microsoft.ActiveDirectory.Management.ADUser 

Name       MemberType Definition
----       ---------- ----------
logonHours Property   System.Byte[] logonHours {get;set;} 👀

# Where-Object {$_.logonHours} syntax means the property has to contain data for the object to be returned in the output
# Then select the last name and hours

PS C:\users\cyborg5\desktop> $allADUsers | Where-Object {$_.logonHours} | Select Surname, logonHours ⌨️

Surname logonHours
------- ----------
        {255, 255, 255, 255...}
Rowray  {0, 0, 0, 0...} 👀

PS C:\users\cyborg5\desktop> ($allADUsers | Where-Object {$_.logonHours -and $_.Surname}).Surname.ToLower() + (ls -File).Name ⌨️
rowray_timer 🔐
PS C:\users\cyborg5\desktop> ($allADUsers | Where-Object {$_.logonHours -and $_.Surname}).Surname.ToLower() + (dir -File).Name ⌨️
rowray_timer 🔐
PS C:\users\cyborg5\desktop> ($allADUsers | Where-Object {$_.logonHours -and $_.Surname}).Surname.ToLower() + (dir).Name ⌨️  
rowray_timer 🔐
PS C:\users\cyborg5\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg6@cyborg.underthewire.tech -p 22 ⌨️
cyborg6@cyborg.underthewire.tech's password: ⌨️ rowray_timer

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg6\desktop> whoami ⌨️
underthewire\cyborg6
```

## Flag
rowray_timer

## Continue
[Continue](./Cyborg0506.md)