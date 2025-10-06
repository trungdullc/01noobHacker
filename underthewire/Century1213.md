# Century Level 12 → 13 scp, wc -w

## Previous Flag
```
i_authenticate_things
```

## Goal
The password for Century14 is the number of words within the file on the desktop.

## What I learned
```
(gc countmywords -Raw) -split '\s+' | ? {$_} | measure | % Count            cat countmywords | wc -w
(Get-Content "countmywords" -Raw -Encoding UTF8) -split '\s+' | Where-Object {$_ -ne ""} | Measure-Object | Select-Object -ExpandProperty Count

# DL file than use word count program or put into word
scp century13@century.underthewire.tech:C:\users\century13\desktop\countmywords C:\Users\trung.DESKTOP-G7C81CH\Downloads
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century13@century.underthewire.tech -p 22 ⌨️
century13@century.underthewire.tech's password: ⌨️ i_authenticate_things

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century13\desktop> dir ⌨️

    Directory: C:\users\century13\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:38 AM           7894 countmywords 👀

PS C:\users\century13\desktop> (gc countmywords -Raw) -split '\s+' | ? {$_} | measure | % Count ⌨️
755 🔐
PS C:\users\century13\desktop> (Get-Content "countmywords" -Raw -Encoding UTF8) -split '\s+' | Where-Object {$_ -ne ""} | Measure-Object | Select-Object -ExpandProperty Count ⌨️
755 🔐
PS C:\users\century13\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> scp century13@century.underthewire.tech:C:\users\century13\desktop\countmywords C:\Users\trung.DESKTOP-G7C81CH\Downloads ⌨️
century13@century.underthewire.tech's password: ⌨️ i_authenticate_things
countmywords                                           100% 7894    74.8KB/s   00:00

# Google: word counter online
https://wordcounter.net/
755 words 7,894 characters  🔐

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century14@century.underthewire.tech -p 22
century14@century.underthewire.tech's password: ⌨️ 755

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century14\desktop> whoami ⌨️
underthewire\century14
```

## Flag
755

## Continue
[Continue](./Century1314.md)