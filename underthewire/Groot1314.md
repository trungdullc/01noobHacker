# Groot Level 13 → 14 Get-SmbShare -Name "*task*"

## Previous Flag
```
utw_team_ned
```

## Goal
The password for groot15 is the description of the share whose name contains “task” in it PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the description is “frozen_pizza” and the file on the desktop is named “_sucks”, the password would be “frozen_pizza_sucks”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-SmbShare -Name "*task*"
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot14@groot.underthewire.tech -p 22 ⌨️
groot14@groot.underthewire.tech's password: ⌨️ utw_team_ned

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot14\desktop> dir ⌨️

    Directory: C:\users\Groot14\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 _8 👀

PS C:\users\Groot14\desktop> Get-Help Get-SmbShare ⌨️
PS C:\users\Groot14\desktop> Get-SmbShare -Name "*task*" ⌨️

Name   ScopeName Path Description
----   --------- ---- -----------
Tasker *              scheduled_things 👀

PS C:\users\Groot14\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot15@groot.underthewire.tech -p 22 ⌨️
groot15@groot.underthewire.tech's password: ⌨️ scheduled_things_8

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot15\desktop> whoami ⌨️
underthewire\groot15
```

## Flag
scheduled_things_8

## Continue
[Continue](./Groot1415.md)