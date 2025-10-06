# Groot Level 09 → 10 Compare-Object (Get-Content old.txt) (Get-Content new.txt)

## Previous Flag
```
t-25_tester
```

## Goal
The password for groot11 is the one word that makes the two files on the desktop different.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Linux:
    diff old.txt new.txt                # basic diff
    diff -y old.txt new.txt             # side-by-side comparison
    diff -w old.txt new.txt             # ignore whitespace differences
    diff -u old.txt new.txt             # unified format (good for patches)

    # use colordiff if installed to highlight differences
    colordiff old.txt new.txt

    # vimdiff for an interactive side-by-side view
    vimdiff old.txt new.txt

Windows:
    # basic comparison
    Compare-Object (Get-Content old.txt) (Get-Content new.txt)

    # more readable output
    Compare-Object (Get-Content old.txt) (Get-Content new.txt) -IncludeEqual

    # show only differences
    Compare-Object (Get-Content old.txt) (Get-Content new.txt) | ForEach-Object { "$($_.SideIndicator) $($_.InputObject)" }
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot10@groot.underthewire.tech -p 22 ⌨️
groot10@groot.underthewire.tech's password: ⌨️ t-25_tester

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot10\desktop> dir ⌨️

    Directory: C:\users\Groot10\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM          17324 new.txt
-a----        8/30/2018   5:52 AM          17313 old.txt

PS C:\users\Groot10\desktop> Get-Help Compare-Object ⌨️
PS C:\users\Groot10\desktop> Compare-Object (Get-Content old.txt) (Get-Content new.txt) ⌨️

InputObject SideIndicator
----------- -------------
taserface   => 🔐

PS C:\users\Groot10\desktop> Compare-Object (Get-Content old.txt) (Get-Content new.txt) | ForEach-Object { "$($_.SideIndicator) $($_.InputObject)" } ⌨️
=> taserface 🔐

PS C:\users\Groot10\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot11@groot.underthewire.tech -p 22 ⌨️
groot11@groot.underthewire.tech's password: ⌨️ taserface

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot11\desktop> whoami ⌨️
underthewire\groot11
```

## Flag
taserface

## Continue
[Continue](./Groot1011.md)