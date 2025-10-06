# Century Level 01 → 02 wget but for PS

## Previous Flag
```
10.0.14393.8422
```

## Goal
The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

NOTE:
– If the name of the cmdlet is “get-web” and the file on the desktop is named “1234”, the password would be “get-web1234”.
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Invoke-Webrequest               wget
dir                             ls
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century2@century.underthewire.tech -p 22 ⌨️
century1@century.underthewire.tech's password: ⌨️ 10.0.14393.8422
PS C:\users\century2\desktop> dir ⌨️

    Directory: C:\users\century2\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM            693 443 👀

PS C:\users\century2\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century3@century.underthewire.tech -p 22 ⌨️
century3@century.underthewire.tech's password: ⌨️ invoke-webrequest443 
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century3\desktop> whoami ⌨️
underthewire\century3
```

## Flag
invoke-webrequest443 

## Continue
[Continue](./Century0203.md)