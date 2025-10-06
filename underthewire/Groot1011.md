# Groot Level 10 → 11 Get-Content TPS_Reports04.pdf -Raw -Stream secret

## Previous Flag
```
taserface
```

## Goal
The password for groot12 is within an alternate data stream (ADS) somewhere on the desktop.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```
# command to look up all the streams inside the current directory
Get-ChildItem -File | Get-Item -Stream * | Select-Object FileName, Stream

Get-Content TPS_Reports04.pdf -Raw -Stream secret

What Streams Are
    NTFS (Windows’ default file system) allows more than one “stream” of data per file
    Every file has a default data stream (:$DATA) — that’s the actual file contents you see normally
    You can create additional named streams to store extra data hidden inside the file, without affecting its size in Explorer

Why ADS Exists
    Often used by metadata, digital rights info, or hiding data (sometimes maliciously)
    Example: Internet Explorer used to mark downloaded files with a hidden Zone.Identifier stream
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot11@groot.underthewire.tech -p 22 ⌨️
groot11@groot.underthewire.tech's password: ⌨️ taserface

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot11\desktop> ls ⌨️

    Directory: C:\users\Groot11\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM             30 TPS_Reports01.txt
-a----        8/30/2018   5:52 AM             30 TPS_Reports02.doc
-a----        8/30/2018   5:52 AM              0 TPS_Reports03.txt
-a----        8/30/2018  10:51 AM             30 TPS_Reports04.pdf
-a----        8/30/2018   5:52 AM             30 TPS_Reports05.xlsx
-a----        8/30/2018   5:52 AM             30 TPS_Reports06.pptx

PS C:\users\Groot11\desktop> Get-ChildItem -File | Get-Item -Stream * | Select-Object FileName, Stream ⌨️

FileName                                    Stream
--------                                    ------
C:\users\Groot11\desktop\TPS_Reports01.txt  :$DATA
C:\users\Groot11\desktop\TPS_Reports02.doc  :$DATA
C:\users\Groot11\desktop\TPS_Reports03.txt  :$DATA
C:\users\Groot11\desktop\TPS_Reports04.pdf  :$DATA
C:\users\Groot11\desktop\TPS_Reports04.pdf  secret 👀
C:\users\Groot11\desktop\TPS_Reports05.xlsx :$DATA
C:\users\Groot11\desktop\TPS_Reports06.pptx :$DATA

PS C:\users\Groot11\desktop> Get-Content TPS_Reports04.pdf -Raw -Stream secret ⌨️
spaceships 🔐

PS C:\users\Groot11\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot12@groot.underthewire.tech -p 22 ⌨️
groot12@groot.underthewire.tech's password: ⌨️ spaceships

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot12\desktop> whoami ⌨️
underthewire\groot12
```

## Flag
spaceships

## Continue
[Continue](./Groot1112.md)