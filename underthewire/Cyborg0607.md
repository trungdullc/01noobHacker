# Cyborg Level 06 → 07 Get-CimInstance Win32_StartupCommand

## Previous Flag
```
cybergeddon
```

## Goal
The password for cyborg8 is the executable name of a program that will start automatically when cyborg7 logs in.<br>

NOTE: – The password will be lowercase no matter how it appears on the screen.

## What I learned
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Get-Help Get-CimInstance

getCIMinstance     used to retrieve info about computer system or its users, so search for startup commands

Get-CimInstance Win32_StartupCommand
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg7@cyborg.underthewire.tech -p 22 ⌨️
cyborg7@cyborg.underthewire.tech's password: ⌨️ cybergeddon

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!  

PS C:\users\cyborg7\Desktop> Get-Help Get-CimInstance ⌨️
PS C:\users\cyborg7\Desktop> Get-CimInstance Win32_StartupCommand ⌨️

Command                            User                 Caption
-------                            ----                 -------
C:\program files\SkyNet\skynet.exe underthewire\cyborg7 SKYNET 🔐

PS C:\users\cyborg7\Desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg8@cyborg.underthewire.tech -p 22 ⌨️
cyborg8@cyborg.underthewire.tech's password: skynet ⌨️

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg8\desktop> whoami ⌨️
underthewire\cyborg8
```

## Flag
skynet

## Continue
[Continue](./Cyborg0708.md)