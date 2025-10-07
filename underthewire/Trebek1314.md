# Trebek Level 13 → 14 (Get-ADUser -Filter * -Properties City).Where({$_.City}).City

## Previous Flag
```
prindel3003
```

## Goal
The password for trebek15 is the output from decoding the PowerShell code found in the account properties of the user account from the previous level PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the output is “blue_and_red” and the file on the desktop is named “_are_great”, the password would be “blue_and_red_are_great”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
(Get-ADUser -Filter * -Properties City).Where({$_.City}).City
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek14@groot.underthewire.tech -p 22 ⌨️
trebek14@groot.underthewire.tech's password: ⌨️ prindel3003

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek14\desktop> dir ⌨️

    Directory: C:\users\trebek14\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:49 AM              0 _today 👀

PS C:\users\trebek14\desktop> Get-ADUser -Filter * -Properties City | Select-Object -First 3 ⌨️

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

PS C:\users\trebek14\desktop> (Get-ADUser -Filter * -Properties City).Where({$_.City}) ⌨️

City              : agBvAGkAbgBfAHQAaABlAF8AcgBlAGIAZQBsAHMA 👀
DistinguishedName : CN=Prindel,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Prindel
Name              : Prindel
ObjectClass       : user
ObjectGUID        : 8edb88c2-c69b-4d78-957e-6c1d1b08f2a5
SamAccountName    : Prindel
SID               : S-1-5-21-758131494-606461608-3556270690-2178
Surname           : Prindel
UserPrincipalName : Prindel

PS C:\users\trebek14\desktop> (Get-ADUser -Filter * -Properties City).Where({$_.City}).City ⌨️
agBvAGkAbgBfAHQAaABlAF8AcgBlAGIAZQBsAHMA
PS C:\users\trebek14\desktop> (Get-ADUser -Filter * -Properties City).Where({$_.City}).City.ForEach({[Convert]::FromBase64String($_)}) ⌨️
106
0
111
0
105
0
110
0
95
0
116
0
104
0
101
0
95
0
114
0
101
0
98
0
101
0
108
0
115
0

# Note: Remove Null Bytes
PS C:\users\trebek14\desktop> (Get-ADUser -Filter * -Properties City).Where({$_.City}).City.ForEach({[Convert]::FromBase64String($_).Where({$_ -ne 00})}) ⌨️
106
111
105
110
95
116
104
101
95
114
101
98
101
108
115
PS C:\users\trebek14\desktop> (Get-ADUser -Filter * -Properties City).Where({$_.City}).City.ForEach({[System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($_).Where({$_ -ne 00}))}).ToLower() + (ls -File).Name.ToLower() ⌨️
join_the_rebels_today 🔐

PS C:\users\trebek14\desktop> exit
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek15@groot.underthewire.tech -p 22 ⌨️
trebek15@groot.underthewire.tech's password: ⌨️ join_the_rebels_today

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek15\desktop> whoami ⌨️
underthewire\trebek15
```

## Flag
join_the_rebels_today

## Continue
[Continue](./Trebek1415.md)