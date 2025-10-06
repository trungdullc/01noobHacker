# Groot Level 05 → 06 Get-CimInstance Win32_StartupCommand

## Previous Flag
```
wk11_enterprise
```

## Goal
The password for groot7 is the name of the program that is set to start when this user logs in PLUS the name of the file on the desktop.<br>

NOTE:<br>
– Omit the executable extension.<br>
– If the program is “mspaint” and the file on the desktop is named “_log”, the password would be “mspaint_log”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-CimInstance Win32_StartupCommand
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot6@groot.underthewire.tech -p 22 ⌨️
groot6@groot.underthewire.tech's password: ⌨️ wk11_enterprise

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot6\desktop> dir ⌨️

    Directory: C:\users\Groot6\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/21/2020   1:24 PM              0 _rules 👀

PS C:\users\Groot6\desktop> Get-CimInstance Win32_StartupCommand ⌨️

Command          User                Caption
-------          ----                -------
                 underthewire\Groot6 New Value #1
                 underthewire\Groot6 New Value #2
                 underthewire\Groot6 New Value #3
                 underthewire\Groot6 New Value #4
C:\star-lord.exe underthewire\Groot6 star-lord 👀

PS C:\users\Groot6\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot7@groot.underthewire.tech -p 22 ⌨️
groot7@groot.underthewire.tech's password: ⌨️ star-lord_rules

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot7\desktop> whoami ⌨️
underthewire\groot7
```

## Flag
star-lord_rules

## Continue
[Continue](./Groot0607.md)