# Groot Level 03 → 04 -Recurse -ErrorAction SilentlyContinue

## Previous Flag
```
5
```

## Goal
The password for groot5 is the name of the Drax subkey within the HKEY_CURRENT_USER (HKCU) registry hive.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```

```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot4@groot.underthewire.tech -p 22 ⌨️
groot4@groot.underthewire.tech's password: ⌨️ 5

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot4\desktop> dir ⌨️

    Directory: C:\users\Groot4\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        1/13/2025   2:20 PM        2125818 out.txt
-a----        8/24/2024   5:05 PM         190334 registry.txt                                                                                             
-a----        9/18/2025   1:28 PM              0 script.ps1

PS C:\users\Groot4\desktop> Get-ChildItem HKCU:\ -Recurse -ErrorAction SilentlyContinue | Where-Object {$_.Name -like '*Drax*'} ⌨️

    Hive: HKEY_CURRENT_USER\Software\Microsoft\Assistance

Name                           Property
----                           --------
Drax                           destroyer : test

    Hive: HKEY_CURRENT_USER\Software\Microsoft\Assistance\Drax

Name                           Property
----                           --------
destroyer 🔐

PS C:\users\Groot4\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot5@groot.underthewire.tech -p 22 ⌨️
groot5@groot.underthewire.tech's password: destroyer

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot5\desktop> whoami ⌨️
underthewire\groot5
```

## Flag
destroyer

## Continue
[Continue](./Groot0405.md)