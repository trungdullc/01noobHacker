# Trebek Level 12 → 13 (Get-ADUser -Filter * -Properties City).Where({$_.City})

## Previous Flag
```
poe.dameron53
```

## Goal
The password for trebek14 is the last name of the user who has an encoded PowerShell command in their City property PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the last name is “doe” and the file on the desktop is named “1234”, the password would be “doe1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
(Get-ADUser -Filter * -Properties City).Where({$_.City})
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek13@groot.underthewire.tech -p 22 ⌨️
trebek13@groot.underthewire.tech's password: ⌨️ poe.dameron53

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek13\desktop> dir 

    Directory: C:\users\trebek13\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:49 AM              0 3003 👀

PS C:\users\trebek13\desktop> Get-ADUser -Filter * -Properties City | Select-Object -First 3 ⌨️

City              :
DistinguishedName : CN=Administrator,CN=Users,DC=underthewire,DC=tech
Enabled           : True
GivenName         :
Name              : Administrator
ObjectClass       : user
ObjectGUID        : 427058c2-1d57-4e49-a23d-204865b502ae
SamAccountName    : Administrator
SID               : S-1-5-21-758131494-606461608-3556270690-500
Surname           :
UserPrincipalName :

City              :
DistinguishedName : CN=Guest,CN=Users,DC=underthewire,DC=tech
Enabled           : False
GivenName         :
Name              : Guest
ObjectClass       : user
ObjectGUID        : 5eec2c1d-caa5-48a5-bc68-f720f756447c
SamAccountName    : Guest
SID               : S-1-5-21-758131494-606461608-3556270690-501
Surname           :
UserPrincipalName :

City              : 
DistinguishedName : CN=DefaultAccount,CN=Users,DC=underthewire,DC=tech
Enabled           : False
GivenName         :
Name              : DefaultAccount
ObjectClass       : user
ObjectGUID        : 1d22dd43-5bc4-4a17-9bce-596a3a044b80
SamAccountName    : DefaultAccount
SID               : S-1-5-21-758131494-606461608-3556270690-503
Surname           :
UserPrincipalName :

PS C:\users\trebek13\desktop> (Get-ADUser -Filter * -Properties City).Where({$_.City}) ⌨️

City              : agBvAGkAbgBfAHQAaABlAF8AcgBlAGIAZQBsAHMA
DistinguishedName : CN=Prindel,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Prindel
Name              : Prindel
ObjectClass       : user
ObjectGUID        : 8edb88c2-c69b-4d78-957e-6c1d1b08f2a5
SamAccountName    : Prindel
SID               : S-1-5-21-758131494-606461608-3556270690-2178
Surname           : Prindel 👀
UserPrincipalName : Prindel

PS C:\users\trebek13\desktop> (Get-ADUser -Filter * -Properties City).Where({$_.City}).Surname.ToLower() + (ls -File).Name.ToLower() ⌨️
prindel3003 🔐

PS C:\users\trebek13\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek14@groot.underthewire.tech -p 22 ⌨️
trebek14@groot.underthewire.tech's password: ⌨️ prindel3003

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek14\desktop> whoami ⌨️
underthewire\trebek14
```

## Flag
prindel3003

## Continue
[Continue](./Trebek1314.md)