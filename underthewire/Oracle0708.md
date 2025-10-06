# Oracle Level 07 → 08 (cat .\logs.txt | Select-String 'guardian.galaxy.com').ToString()

## Previous Flag
```
multiverse111
```

## Goal
The password for oracle9 is the name of the file in the GET Request from www.guardian.galaxy.com within the log file on the desktop.<br>

NOTE:<br>
– Don’t include the extension.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
(cat .\logs.txt | Select-String 'guardian.galaxy.com').ToString()
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle8@groot.underthewire.tech -p 22 ⌨️
oracle8@groot.underthewire.tech's password: ⌨️ multiverse111

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle8\desktop> dir ⌨️

    Directory: C:\users\Oracle8\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM         405295 logs.txt

PS C:\users\Oracle8\desktop> Get-Content .\logs.txt | Select-Object -First 5 ⌨️
144.92.52.202 - - [28/Jul/1995:12:27:25 -0400] "GET /shuttle/missions/sts-69/mission-sts-69.html HTTP/1.0" 200 10136
egate.ska.com - - [28/Jul/1995:12:27:25 -0400] "GET /shuttle/missions/sts-70/images/KSC-95EC-1012.jpg HTTP/1.0" 200 83915    
144.92.52.202 - - [28/Jul/1995:12:27:26 -0400] "GET /shuttle/missions/sts-69/sts-69-patch-small.gif HTTP/1.0" 200 8083       
144.92.52.202 - - [28/Jul/1995:12:27:28 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1713
sanders.jsc.nasa.gov - - [28/Jul/1995:12:27:28 -0400] "GET /shuttle/missions/sts-69/sts-69-patch-small.gif HTTP/1.0" 200 8083

PS C:\users\Oracle8\desktop> (cat .\logs.txt | Select-String 'guardian.galaxy.com').ToString() ⌨️
guardian.galaxy.com - - [28/Jul/1995:13:03:55 -0400] "GET /images/star-lord.gif HTTP/1.0" 200 786 👀

PS C:\users\Oracle8\desktop> (cat .\logs.txt | Select-String 'guardian.galaxy.com').ToString().Split('/')[4].Split('\.')[0].ToLower() ⌨️
star-lord 🔐

PS C:\users\Oracle9\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle9@groot.underthewire.tech -p 22 ⌨️
oracle9@groot.underthewire.tech's password: ⌨️ star-lord

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle9\desktop> whoami ⌨️
underthewire\oracle9
```

## Flag
star-lord

## Continue
[Continue](./Oracle0809.md)