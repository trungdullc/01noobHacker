# Trebek Level 01 → 02 Get-CimInstance Win32_Service -Filter 'Name like "C-3PO"' | Select-Object *

## Previous Flag
```
mess_cleaner
```

## Goal
The password for trebek3 is the name of the executable associated with the C-3PO service PLUS the name of the file on the user’s desktop.<br>

NOTE:<br>
– Don’t include the file extension (i.e.- .exe). If the executable name is “binary.exe” and the file on the desktop is named “1234”, the password would be “binary1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-Service cmdlet does not return the binary path, so we need to query a lower level interface such as CIM or WMI

Get-CimInstance Win32_Service -Filter 'Name like "C-3PO"' | Select-Object *
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek2@groot.underthewire.tech -p 22 ⌨️
trebek2@groot.underthewire.tech's password: ⌨️ mess_cleaner

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek2\desktop> Get-Help Get-CimInstance ⌨️
PS C:\users\trebek2\desktop> Get-CimInstance Win32_Service -Filter 'Name like "C-3PO"' | Select-Object * ⌨️

Name                    : C-3PO
Status                  : OK
ExitCode                : 0
DesktopInteract         : False
ErrorControl            : Normal
PathName                : g:\star_wars\droid.exe 👀
ServiceType             : Own Process
StartMode               : Auto
Caption                 : C-3PO
Description             :
InstallDate             :
CreationClassName       : Win32_Service
Started                 : False
SystemCreationClassName : Win32_ComputerSystem  
SystemName              : UTW
AcceptPause             : False
AcceptStop              : False
DisplayName             : C-3PO
ServiceSpecificExitCode : 0
StartName               : LocalSystem
State                   : Stopped
TagId                   : 0
CheckPoint              : 0
DelayedAutoStart        : False
ProcessId               : 0
WaitHint                : 0
PSComputerName          :
CimClass                : root/cimv2:Win32_Service
CimInstanceProperties   : {Caption, Description, InstallDate, Name...}
CimSystemProperties     : Microsoft.Management.Infrastructure.CimSystemProperties

PS C:\users\trebek2\desktop> (Get-CimInstance Win32_Service -Filter 'Name like "C-3PO"').PathName.Split("\\")[-1].Split("\.")[0].ToLower() + (ls -File).Name.ToLower() ⌨️
droid823

PS C:\users\trebek2\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek3@groot.underthewire.tech -p 22 ⌨️
trebek3@groot.underthewire.tech's password: ⌨️ droid823

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek3\desktop> whoami ⌨️
underthewire\trebek3
```

## Flag
droid823

## Continue
[Continue](./Trebek0203.md)