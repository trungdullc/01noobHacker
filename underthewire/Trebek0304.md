# Trebek Level 03 → 04 Get-ChildItem "C:\Windows\Prefetch" -Filter '*access*'

## Previous Flag
```
10.30.1.18address
```

## Goal
The password for trebek5 is the last execution date of Microsoft Access PLUS the name of the text file on the user’s desktop.<br>

Note:<br>
– Format for the date is 2 digit month, 2 digit day, 4 digit year. Ex: 9 feb 2009 would be 02/09/2009.<br>
– If the date is “02/09/2009” and the file on the desktop is named “_bob”, the password would be “02/09/2009_bob”.

## What I learned
```
Get-ChildItem "C:\Windows\Prefetch" -Filter '*access*'
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek4@groot.underthewire.tech -p 22 ⌨️
trebek4@groot.underthewire.tech's password: ⌨️ 10.30.1.18address

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek4\desktop> dir

    Directory: C:\users\trebek4\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:46 AM              0 _red 👀

# ChatGPT: timestamps relating to binaries that are no longer installed
# C:\Windows\Prefetch

PS C:\users\trebek4\desktop> Get-ChildItem "C:\Windows\Prefetch" -Filter '*access*' ⌨️

    Directory: C:\Windows\Prefetch

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         1/5/2017 👀 6:04 PM          65058 MSACCESS.EXE-EF45328A.pf

PS C:\users\trebek4\desktop> (Get-ChildItem "C:\Windows\Prefetch" -Filter '*access*').LastAccessTime.ToString('MM/dd/yyyy') + (ls -File).Name.ToLower() ⌨️
01/05/2017_red 🔐

PS C:\users\trebek4\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek5@groot.underthewire.tech -p 22 ⌨️
trebek5@groot.underthewire.tech's password: ⌨️ 01/05/2017_red

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek5\desktop> whoami ⌨️
underthewire\trebek5
```

## Flag
01/05/2017_red 

## Continue
[Continue](./Trebek0405.md)