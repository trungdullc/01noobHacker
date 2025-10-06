# Groot Level 08 → 09 Get-ADOrganizationalUnit -Filter * -Properties ProtectedFromAccidentalDeletion | Where-Object {-not $_.ProtectedFromAccidentalDeletion}

## Previous Flag
```
call_me_starlord
```

## Goal
The password for groot10 is the name of the OU that doesn’t have accidental deletion protection enabled PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the name of the OU is called “blue” and the file on the desktop is named “_bob”, the password would be “blue_bob”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-Help Get-ADOrganizationalUnit
Get-ADOrganizationalUnit -Filter * -Properties * | Get-Member -Name '*delet*' 
Get-ADOrganizationalUnit -Filter * -Properties ProtectedFromAccidentalDeletion | Where-Object {-not $_.ProtectedFromAccidentalDeletion}
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot9@groot.underthewire.tech -p 22 ⌨️
groot9@groot.underthewire.tech's password: ⌨️ call_me_starlord

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot9\desktop> dir ⌨️

    Directory: C:\users\Groot9\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 _tester 👀

PS C:\users\Groot9\desktop> Get-ADOrganizationalUnit -Filter * -Properties * | Get-Member -Name '*delet*' ⌨️

   TypeName: Microsoft.ActiveDirectory.Management.ADOrganizationalUnit

Name                            MemberType Definition
----                            ---------- ----------
Deleted                         Property   System.Boolean Deleted {get;}
isDeleted                       Property   System.Boolean isDeleted {get;}
ProtectedFromAccidentalDeletion Property   System.Boolean ProtectedFromAccidentalDeletion {get;set;} 👀

PS C:\users\Groot9\desktop> Get-ADOrganizationalUnit -Filter * -Properties ProtectedFromAccidentalDeletion | Where-Object {-not $_.ProtectedFromAccidentalDeletion} ⌨️

City                            :
Country                         :
DistinguishedName               : OU=T-25,OU=X-Wing,DC=underthewire,DC=tech
LinkedGroupPolicyObjects        : {cn={49401C32-4145-463F-B5E7-816926D4F78D},cn=policies,cn=system,DC=underthewire,DC=tech}
ManagedBy                       :
Name                            : T-25 👀
ObjectClass                     : organizationalUnit
ObjectGUID                      : fc15c303-dd9a-4c44-a941-314cc6fdd394
PostalCode                      :
ProtectedFromAccidentalDeletion : False
State                           :
StreetAddress                   :

PS C:\users\Groot9\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot10@groot.underthewire.tech -p 22 ⌨️
groot10@groot.underthewire.tech's password: ⌨️ t-25_tester

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot10\desktop> whoami ⌨️
underthewire\groot10
```

## Flag
t-25_tester

## Continue
[Continue](./Groot0910.md)