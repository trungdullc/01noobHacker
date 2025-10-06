# Groot Level 06 → 07 Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Services' | Where-Object {$_.Name -like '*applocker*'}

## Previous Flag
```
star-lord_rules
```

## Goal
The password for groot8 is the name of the dll, as depicted in the registry, associated with the “applockerfltr” service PLUS the name of the file on the desktop.<br>

NOTE:<br>
– The password will be lowercase no matter how it appears on the screen.<br>
– If the name of the dll is “abc.dll” and the file on the desktop is named “_1234”, the password would be “abc_1234”.

## What I learned
```
Note: Can't use stuff like the -Filter option and wildcards in the registry

Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Services' | Where-Object {$_.Name -like '*applocker*'}
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot7@groot.underthewire.tech -p 22 ⌨️
groot7@groot.underthewire.tech's password: ⌨️ star-lord_rules

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot7\desktop> dir ⌨️

    Directory: C:\users\Groot7\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        5/31/2021   5:13 PM              0 _home 👀

PS C:\users\Groot7\desktop> Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Services' | Where-Object {$_.Name -like '*applocker*'} ⌨️

    Hive: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services

Name                           Property
----                           --------
applockerfltr                  DisplayName     : @%systemroot%\system32\srpapi.dll,-102 👀
                               ErrorControl    : 1
                               ImagePath       : system32\drivers\applockerfltr.sys
                               Start           : 3
                               Type            : 1
                               Description     : @%systemroot%\system32\srpapi.dll,-103
                               DependOnService : {FltMgr, AppID, AppIDSvc}

PS C:\users\Groot7\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot8@groot.underthewire.tech -p 22 ⌨️
groot8@groot.underthewire.tech's password: ⌨️ srpapi_home

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot8\desktop> whoami ⌨️
underthewire\groot8
```

## Flag
srpapi_home

## Continue
[Continue](./Groot0708.md)