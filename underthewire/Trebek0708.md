# Trebek Level 07 → 08 -join[System.IO.File]::ReadAllBytes((ls .\Clone_Trooper_data.pdf).FullName)[0..7]

## Previous Flag
```
han_solo99
```

## Goal
The password for trebek9 the first 8 bytes of the file located on the desktop. Combine the answer together with NO spaces.

## What I learned
```
Use .NET reflection to read the file bytes and select the first 8 bytes, starting at index 0, then -join to merge into a string
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek8@groot.underthewire.tech -p 22 ⌨️
trebek8@groot.underthewire.tech's password: ⌨️ han_solo99

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek8\desktop> dir ⌨️

    Directory: C:\users\trebek8\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:55 AM         221184 Clone_Trooper_data.pdf

PS C:\users\trebek8\desktop> [System.IO.File]::ReadAllBytes((ls .\Clone_Trooper_data.pdf).FullName)[0..7]
77
90
144
0
3
0
0
0

PS C:\users\trebek8\desktop> -join[System.IO.File]::ReadAllBytes((ls .\Clone_Trooper_data.pdf).FullName)[0..7] ⌨️
779014403000 🔐

PS C:\users\trebek8\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek9@groot.underthewire.tech -p 22 ⌨️
trebek9@groot.underthewire.tech's password: ⌨️ 779014403000 

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek9\desktop> whoami ⌨️
underthewire\trebek9
```

## Flag
779014403000

## Continue
[Continue](./Trebek0809.md)