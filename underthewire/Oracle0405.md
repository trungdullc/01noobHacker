# Oracle Level 04 → 05 Get-GPO -All | Where-Object {$_.Description -eq 'I_AM_GROOT'}

## Previous Flag
```
alpha83
```

## Goal
The password for oracle6 is the name of the GPO that contains a description of “I_AM_GROOT” PLUS the name of the file on the user’s desktop.<br>

NOTE:<br>
– If you are using SSH, you MUST do a Help on the cmdlet needed to solve this. For example, if the cmdlet is “get-something” type “help get-something” first, this will make the cmdlet available for you to use. This is a bug in the SSH software used.<br>
– If the GPO description is “blob” and the file on the desktop is named “1234”, the password would be “blob1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-GPO -All | Where-Object {$_.Description -eq 'I_AM_GROOT'}
Get-GPO -All | Where-Object {$_.Description -like 'I_AM_GROOT'}
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle5@groot.underthewire.tech -p 22 ⌨️
oracle5@groot.underthewire.tech's password: ⌨️ alpha83

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle5\desktop> dir ⌨️

    Directory: C:\users\Oracle5\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:50 AM              0 1337 👀

PS C:\users\Oracle5\desktop> Get-GPO -All | Where-Object {$_.Description -eq 'I_AM_GROOT'} ⌨️

DisplayName      : Charlie 👀
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 44080cf1-1053-467d-b000-2ea3f27dbbfa
GpoStatus        : AllSettingsEnabled
Description      : I_am_Groot
CreationTime     : 11/20/2018 12:18:09 AM
ModificationTime : 11/20/2018 12:18:08 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

PS C:\users\Oracle5\desktop> Get-GPO -All | Where-Object {$_.Description -like 'I_AM_GROOT'}

DisplayName      : Charlie 👀
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 44080cf1-1053-467d-b000-2ea3f27dbbfa
GpoStatus        : AllSettingsEnabled
Description      : I_am_Groot
CreationTime     : 11/20/2018 12:18:09 AM
ModificationTime : 11/20/2018 12:18:08 AM
UserVersion      : AD Version: 0, SysVol Version: 0    
ComputerVersion  : AD Version: 0, SysVol Version: 0    
WmiFilter        :

PS C:\users\Oracle5\desktop> (Get-GPO -All | Where-Object {$_.Description -eq 'I_AM_GROOT'}).DisplayName.ToLower() + (dir -File).Name.ToLower() ⌨️
charlie1337 🔐

PS C:\users\Oracle5\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle6@groot.underthewire.tech -p 22 ⌨️
oracle6@groot.underthewire.tech's password: ⌨️ charlie1337

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle6\desktop> whoami ⌨️
underthewire\oracle6
```

## Flag
charlie1337

## Continue
[Continue](./Oracle0506.md)