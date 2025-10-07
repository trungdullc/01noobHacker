# Trebek Level 08 → 09 Get-SmbShare

## Previous Flag
```
779014403000
```

## Goal
The password for trebek10 is the name of the potentially rogue share on the system PLUS the name of the file on the desktop.<br>

Note:<br>
– If the share name is “share$” and the file on the desktop is named “_today”, the password would be “share$_today”.<br>
– Exclude any default shares typically found on a Domain Controller.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-SmbShare
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek9@groot.underthewire.tech -p 22 ⌨️
trebek9@groot.underthewire.tech's password: ⌨️ 779014403000

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek9\desktop> dir ⌨️

    Directory: C:\users\trebek9\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:48 AM              0 _hiding 👀

PS C:\users\trebek9\desktop> Get-Command "Get-*Share*" ⌨️

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        Get-FileShare                                      2.0.0.0    Storage
Function        Get-FileShareAccessControlEntry                    2.0.0.0    Storage
Function        Get-NfsShare                                       1.0        NFS
Function        Get-NfsSharePermission                             1.0        NFS
Function        Get-SmbShare                                       2.0.0.0    SmbShare 👀
Function        Get-SmbShareAccess                                 2.0.0.0    SmbShare
Cmdlet          Get-IISSharedConfig                                1.0.0.0    IISAdministration

PS C:\users\trebek9\desktop> Get-SmbShare ⌨️

Name           ScopeName Path Description
----           --------- ---- -----------
ADMIN$         *              Remote Admin
C$             *              Default share
IPC$           *              Remote IPC
NETLOGON       *              Logon server share
shoretroopers$ *              Nothing to see here 👀
SYSVOL         *              Logon server share
Tasker         *              scheduled_things

PS C:\users\trebek9\desktop> (Get-SmbShare -Name 'shoretroopers$').Name.ToLower() + (ls -File).Name.ToLower() ⌨️
shoretroopers$_hiding 🔐

PS C:\users\trebek9\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek10@groot.underthewire.tech -p 22 ⌨️
trebek10@groot.underthewire.tech's password: ⌨️ shoretroopers$_hiding

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek10\desktop> whoami ⌨️
underthewire\trebek10
```

## Flag
shoretroopers$_hiding

## Continue
[Continue](./Trebek0910.md)