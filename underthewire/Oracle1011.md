# Oracle Level 10 → 11 Get-SmbMapping

## Previous Flag
```
yondu
```

## Goal
The password for oracle12 is the drive letter associated with the mapped drive that this user has.<br>

NOTE: Submission should be one letter and lowercase. 

## What I learned
```
Get-SmbMapping
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle11@groot.underthewire.tech -p 22 ⌨️
oracle11@groot.underthewire.tech's password: ⌨️ yondu

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle11\desktop> Get-Command Get-*Mapping* ⌨️

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        Get-DtcClusterTMMapping                            1.0.0.0    MsDtc
Function        Get-NetNatStaticMapping                            1.0.0.0    NetNat
Function        Get-NfsMappingStore                                1.0        NFS
Function        Get-SmbMapping                                     2.0.0.0    SmbShare 👀

PS C:\users\Oracle11\desktop> Get-Help Get-SmbMapping ⌨️
PS C:\users\Oracle11\desktop> Get-SmbMapping ⌨️

Status      Local Path Remote Path
------      ---------- -----------
Unavailable M:         \\127.0.0.1\WsusContent

PS C:\users\Oracle11\desktop> (Get-SmbMapping).LocalPath.Split(':')[0].ToLower() ⌨️
m 🔐

PS C:\users\Oracle11\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle12@groot.underthewire.tech -p 22 ⌨️
oracle12@groot.underthewire.tech's password: ⌨️ m

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\oracle12\desktop> whoami ⌨️
underthewire\oracle12
```

## Flag
m

## Continue
[Continue](./Oracle1112.md)