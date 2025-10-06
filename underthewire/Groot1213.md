# Groot Level 12 → 13 Get-Item "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Get-ItemProperty -Name "RegisteredOwner"

## Previous Flag
```
airwolf
```

## Goal
The password for groot14 is the name of the Registered Owner of this system as depicted in the Registry PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the Registered Owner is “Elroy” and the file on the desktop is named “_bob”, the password would be “elroy_bob”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-Item "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Get-ItemProperty -Name "RegisteredOwner"
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot13@groot.underthewire.tech -p 22 ⌨️
groot13@groot.underthewire.tech's password: ⌨️ airwolf

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot13\desktop> dir 

    Directory: C:\users\Groot13\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 _ned 👀

PS C:\users\Groot13\desktop> Get-Item "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Get-ItemProperty -Name "RegisteredOwner" ⌨️

RegisteredOwner : UTW_Team 👀
PSPath          : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
PSParentPath    : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT
PSChildName     : CurrentVersion
PSProvider      : Microsoft.PowerShell.Core\Registry

PS C:\users\Groot13\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot14@groot.underthewire.tech -p 22 ⌨️
groot14@groot.underthewire.tech's password: ⌨️ utw_team_ned

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot14\desktop> whoami ⌨️
underthewire\groot14
```

## Flag
utw_team_ned

## Continue
[Continue](./Groot1314.md)