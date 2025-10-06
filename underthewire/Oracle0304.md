# Oracle Level 03 → 04 Get-GPO -All | Sort-Object CreationTime -Descending | Select-Object -First 1

## Previous Flag
```
05/09/2017
```

## Goal
The password for oracle5 is the name of the GPO that was last created PLUS the name of the file on the user’s desktop.<br>

NOTE:<br>
– If the GPO name is “blob” and the file on the desktop is named “1234”, the password would be “blob1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
GPO (Group Policy Object) is a feature of Windows Group Policy that lets administrators define rules and settings for users and computers in an Active Directory (AD) environment

Get-GPO -All | Sort-Object CreationTime -Descending | Select-Object -First 1
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle4@groot.underthewire.tech -p 22 ⌨️
oracle4@groot.underthewire.tech's password: ⌨️ 05/09/2017

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle4\desktop> dir ⌨️

    Directory: C:\users\Oracle4\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:49 AM              0 83 👀

PS C:\users\Oracle4\desktop> Get-Help Get-GPO ⌨️
PS C:\users\Oracle4\desktop> Get-GPO -All ⌨️

DisplayName      : Default Domain Policy
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 31b2f340-016d-11d2-945f-00c04fb984f9
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 2:51:10 AM
ModificationTime : 8/30/2018 10:45:42 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 4, SysVol Version: 4
WmiFilter        :

DisplayName      : Charlie
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 44080cf1-1053-467d-b000-2ea3f27dbbfa
GpoStatus        : AllSettingsEnabled
Description      : I_am_Groot
CreationTime     : 11/20/2018 12:18:09 AM
ModificationTime : 11/20/2018 12:18:08 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Alpha
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 49401c32-4145-463f-b5e7-816926d4f78d
GpoStatus        : AllSettingsEnabled
Description      : Are you there?
CreationTime     : 1/13/2019 9:40:20 PM
ModificationTime : 1/13/2019 9:40:20 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Echo
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 5d91f4cf-3487-40ec-99ed-d219371c0a7c
GpoStatus        : AllSettingsEnabled
Description      : Phone Home
CreationTime     : 8/30/2018 10:49:44 AM
ModificationTime : 8/30/2018 10:49:44 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

DisplayName      : Default Domain Controllers Policy
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 6ac1786c-016f-11d2-945f-00c04fb984f9
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 2:51:10 AM
ModificationTime : 12/9/2018 8:25:40 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 9, SysVol Version: 9
WmiFilter        :

DisplayName      : Default
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : ecb4a7c0-b4e1-41b1-9e89-161cfa679999
GpoStatus        : AllSettingsEnabled
Description      :
CreationTime     : 8/30/2018 3:07:39 AM
ModificationTime : 8/30/2018 3:07:40 AM
UserVersion      : AD Version: 1, SysVol Version: 1
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :

DisplayName      : Delta
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : fc6f3bf4-9239-4308-9956-a9d0d9569505
GpoStatus        : AllSettingsEnabled
Description      : I_am
CreationTime     : 8/30/2018 10:49:44 AM
ModificationTime : 8/30/2018 10:49:44 AM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 0, SysVol Version: 0
WmiFilter        :

PS C:\users\Oracle4\desktop> Get-GPO -All | Sort-Object CreationTime -Descending | Select-Object -First 1 ⌨️

DisplayName      : Alpha 👀
DomainName       : underthewire.tech
Owner            : underthewire\Domain Admins
Id               : 49401c32-4145-463f-b5e7-816926d4f78d
GpoStatus        : AllSettingsEnabled
Description      : Are you there?
CreationTime     : 1/13/2019 9:40:20 PM
ModificationTime : 1/13/2019 9:40:20 PM
UserVersion      : AD Version: 0, SysVol Version: 0    
ComputerVersion  : AD Version: 0, SysVol Version: 0    
WmiFilter        :

PS C:\users\Oracle4\desktop> (Get-GPO -All | Sort-Object CreationTime -Descending | Select-Object -First 1).DisplayName.ToLower() + (ls -File).Name.ToLower() ⌨️
alpha83 🔐

PS C:\users\Oracle4\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle5@groot.underthewire.tech -p 22 ⌨️
oracle5@groot.underthewire.tech's password: ⌨️ alpha83

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle5\desktop> whoami ⌨️
underthewire\oracle5
```

## Flag
alpha83

## Continue
[Continue](./Oracle0405.md)