# Cyborg Level 07 → 08 Get-Content -Path "1_qs5nwlcl7f_-SwNlQvOrAw.png" -Stream Zone.Identifier

## Previous Flag
```
skynet
```

## Goal
The password for cyborg9 is the Internet zone that the picture on the desktop was downloaded from.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Get-Help Get-Item

# Check if the zone is listed on the stream
Get-Item 1_qs5nwlcl7f_-SwNlQvOrAw.png -Stream *

Get-Content -Path "1_qs5nwlcl7f_-SwNlQvOrAw.png" -Stream Zone.Identifier

ChatGPT: How Zone.Identifier works
When you download a file from the Internet, Windows often attaches an alternate data stream (Zone.Identifier)
[ZoneTransfer]
ZoneId=3

    ZoneId=0 → Local Machine
    ZoneId=1 → Intranet
    ZoneId=2 → Trusted Sites
    ZoneId=3 → Internet
    ZoneId=4 → Restricted Sites
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg8@cyborg.underthewire.tech -p 22 ⌨️
cyborg8@cyborg.underthewire.tech's password: skynet ⌨️

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg8\desktop> dir ⌨️

    Directory: C:\users\cyborg8\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM          60113 1_qs5nwlcl7f_-SwNlQvOrAw.png 👀

PS C:\users\cyborg8\desktop> Get-Item 1_qs5nwlcl7f_-SwNlQvOrAw.png -Stream * ⌨️

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png::$DATA
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop
PSChildName   : 1_qs5nwlcl7f_-SwNlQvOrAw.png::$DATA
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png
Stream        : :$DATA
Length        : 60113

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop
PSChildName   : 1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png
Stream        : Zone.Identifier 👀
Length        : 26

PS C:\users\cyborg8\desktop> Get-Content -Path "1_qs5nwlcl7f_-SwNlQvOrAw.png" -Stream Zone.Identifier ⌨️
[ZoneTransfer]
ZoneId=4 👀
PS C:\users\cyborg8\desktop> (Get-Item 1_qs5nwlcl7f_-SwNlQvOrAw.png -Stream * | Get-Content -Stream 'Zone.Identifier').Split('=')[-1] ⌨️
4 🔐

PS C:\users\cyborg8\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg9@cyborg.underthewire.tech -p 22 ⌨️
cyborg9@cyborg.underthewire.tech's password: ⌨️ 4

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg9\desktop> whoami ⌨️
underthewire\cyborg9
```

## Flag
4

## Continue
[Continue](./Cyborg0809.md)