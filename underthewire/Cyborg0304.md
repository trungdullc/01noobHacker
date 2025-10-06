# Cyborg Level 03 → 04 Get-Module -ListAvailable | Where-Object { $_.Version -eq "8.9.8.9" }

## Previous Flag
```
88_objects
```

## Goal
The password for cyborg5 is the PowerShell module name with a version number of 8.9.8.9 PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the module name is “bob” and the file on the desktop is called “_settings”, then the password is “bob_settings”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
# Note: Select-String expects strings (text), not objects
# Get-Module -ListAvailable | Select-String "8.9.8.9"

Get-Module -ListAvailable | Where-Object { $_.Version -like "*8.9.8.9*" }
Get-Module -ListAvailable | Where-Object { $_.Version -eq "8.9.8.9" }
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg4@cyborg.underthewire.tech -p 22 ⌨️
cyborg4@cyborg.underthewire.tech's password: ⌨️ 88_objects

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg4\desktop> dir ⌨️

    Directory: C:\users\cyborg4\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _eggs 👀

PS C:\users\cyborg4\desktop> Get-Module -ListAvailable | Select-String "8.9.8.9" ⌨️                                                
PS C:\users\cyborg4\desktop>  Get-Module -ListAvailable | Where-Object { $_.Version -like "*8.9.8.9*" } ⌨️

    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   8.9.8.9    bacon 👀                             Get-bacon

PS C:\users\cyborg4\desktop> Get-Module -ListAvailable | Where-Object { $_.Version -eq "8.9.8.9" } ⌨️

    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   8.9.8.9    bacon 👀                              Get-bacon

PS C:\users\cyborg4\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg5@cyborg.underthewire.tech -p 22 ⌨️
cyborg5@cyborg.underthewire.tech's password: ⌨️ bacon_eggs

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg5\desktop> whoami ⌨️
underthewire\cyborg5
```

## Flag
bacon_eggs

## Continue
[Continue](./Cyborg0405.md)