# Century Level 04 → 05 domainname

## Previous Flag
```
15768
```

## Goal
The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the short name of the domain is “blob” and the file on the desktop is named “1234”, the password would be “blob1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-WmiObject Win32_ComputerSystem                  dnsdomainname       hostname -f
                                                    hostname
                                                    lscpu               # CPU info
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century5@century.underthewire.tech -p 22 ⌨️
century5@century.underthewire.tech's password: ⌨️ 15768 

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century5\desktop> Get-WmiObject Win32_ComputerSystem ⌨️

Domain              : underthewire.tech 👀
Manufacturer        : BOCHS_
Model               : BXPC____
Name                : UTW
PrimaryOwnerName    : UTW_Team
TotalPhysicalMemory : 16776658944  

PS C:\users\century5\desktop> dir ⌨️

    Directory: C:\users\century5\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM             54 3347 👀

PS C:\users\century5\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century6@century.underthewire.tech -p 22 ⌨️
century6@century.underthewire.tech's password: ⌨️ underthewire3347

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century6\desktop> whoami ⌨️
underthewire\century6
```

## Flag
underthewire3347

## Continue
[Continue](./Century0506.md)