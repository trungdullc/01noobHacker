# Century Level 00 → 01 Build Version

## Previous Flag
```
century1
```

## Goal
The password for Century2 is the build version of the instance of PowerShell installed on this system.

NOTE:<br>
– The format is as follows: **.*.*****.****<br>
– Include all periods<br>
– Be sure to look for build version and NOT PowerShell version

IMPORTANT:<br>
Once you feel you have completed the Century1 challenge, start a new connection to the server, and log in with the username of Century2 and this password will be the answer from Century1.<br>
If successful, close out the Century1 connection and begin to solve the Century2 challenge. This concept is repeated over and over until you reach the end of the game.

## What I learned
```
Get-Host                                                info about shell instead of the server
Get-CimInstance -ClassName Win32_OperatingSystem        information about the operating system
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century1@century.underthewire.tech -p 22 ⌨️
century1@century.underthewire.tech's password: ⌨️ century1

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century1\desktop> Get-Host ⌨️

Name             : ConsoleHost
Version          : 5.1.14393.8422 👀
InstanceId       : 327c947c-8a45-4288-8812-67202b936f84
UI               : System.Management.Automation.Internal.Host.InternalHostUserInterface
CurrentCulture   : en-US
CurrentUICulture : en-US
PrivateData      : Microsoft.PowerShell.ConsoleHost+ConsoleColorProxy
DebuggerEnabled  : True
IsRunspacePushed : False
Runspace         : System.Management.Automation.Runspaces.LocalRunspace

PS C:\users\century1\desktop> Get-CimInstance -ClassName Win32_OperatingSystem ⌨️

SystemDirectory     Organization BuildNumber RegisteredUser SerialNumber            Version   
---------------     ------------ ----------- -------------- ------------            -------   
C:\Windows\system32 OVH SAS      14393       UTW_Team       00377-60000-00000-AA934 10.0.14393 👀

# Note: Missing some numbers so combine both
10.0.14393.8422 🔐

PS C:\users\century1\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century2@century.underthewire.tech -p 22 ⌨️
century2@century.underthewire.tech's password: ⌨️ 10.0.14393.8422
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century2\desktop> whoami ⌨️
underthewire\century2
```

## Flag
10.0.14393.8422

## Continue
[Continue](./Century0102.md)