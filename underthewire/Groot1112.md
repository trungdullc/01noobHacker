# Groot Level 11 → 12 Get-Acl "Nine Realms"

## Previous Flag
```
spaceships
```

## Goal
The password for groot13 is the owner of the Nine Realms folder on the desktop.<br>

NOTE:<br>
– Exclude the Administrator, the Administrators group, and System.<br>
– The password will be lowercase with no punctuation no matter how it appears on the screen. For example, if the owner is “john.doe”, it would be “johndoe”.

## What I learned
```
acl- access control list                linux - chown
Get-Acl "Nine Realms"
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot12@groot.underthewire.tech -p 22 ⌨️
groot12@groot.underthewire.tech's password: ⌨️ spaceships

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot12\desktop> dir ⌨️

    Directory: C:\users\Groot12\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        8/30/2018  10:51 AM                Nine Realms 👀

PS C:\users\Groot12\desktop> Get-Help Get-Acl ⌨️
PS C:\users\Groot12\desktop> Get-Acl "Nine Realms" ⌨️

    Directory: C:\users\Groot12\desktop

Path        Owner                Access
----        -----                ------
Nine Realms underthewire\Airwolf 🔐 NT AUTHORITY\SYSTEM Allow  FullControl...

PS C:\users\Groot12\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot13@groot.underthewire.tech -p 22 ⌨️
groot13@groot.underthewire.tech's password: ⌨️ airwolf

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot13\desktop> whoami ⌨️
underthewire\groot13
```

## Flag
airwolf

## Continue
[Continue](./Groot1213.md)