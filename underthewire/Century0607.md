# Century Level 06 → 07 find . -type f -iname "readme*" & cat

## Previous Flag
```
197
```

## Goal
The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```
# Find in current directory
Get-ChildItem -File -Filter "readme*"                                               find . -maxdepth 1 -type f -iname "readme*"
# Find recursively (search all subfolders)
Get-ChildItem -Recurse -File -Filter "readme*"                                      find . -type f -iname "readme*"
# Case-insensitive match with Where-Object
Get-ChildItem -File -Recurse | Where-Object { $_.Name -match '^readme' }            find . -type f -regex '.*/[Rr][Ee][Aa][Dd][Mm][Ee].*'
# Return full path
Get-ChildItem -Recurse -File -Filter "readme*" | Select-Object -Expand FullName     find . -type f -iname "readme*" -print
                                                                                    locate -i readme

Get-Content Readme.txt                                                              cat Readme.txt
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century7@century.underthewire.tech -p 22 ⌨️
century7@century.underthewire.tech's password: ⌨️ 197 

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century7\desktop> cd .. ⌨️
PS C:\users\century7> dir ⌨️

    Directory: C:\users\century7

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        7/16/2016   1:23 PM                Desktop
d-r---        8/30/2018   3:10 AM                Documents
d-----        1/22/2025  10:36 PM                Downloads
d-r---        7/16/2016   1:23 PM                Favorites
d-r---        7/16/2016   1:23 PM                Links
d-r---        7/16/2016   1:23 PM                Music
d-r---        7/16/2016   1:23 PM                Pictures
d-----        7/16/2016   1:23 PM                Saved Games
d-r---        7/16/2016   1:23 PM                Videos

PS C:\users\century7> Get-ChildItem -File -Filter "readme*" ⌨️
PS C:\users\century7> Get-ChildItem -Recurse -File -Filter "readme*" ⌨️

    Directory: C:\users\century7\Downloads 👀

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM              7 Readme.txt

PS C:\users\century7> Get-ChildItem -File -Recurse | Where-Object { $_.Name -match '^readme' } ⌨️

    Directory: C:\users\century7\Downloads

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM              7 Readme.txt

PS C:\users\century7> Get-ChildItem -Recurse -File -Filter "readme*" | Select-Object -Expand FullName ⌨️
C:\users\century7\Downloads\Readme.txt 👀

PS C:\users\century7> Get-Content .\Downloads\Readme.txt ⌨️
7points 🔐
PS C:\users\century7> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century8@century.underthewire.tech -p 22 ⌨️
century8@century.underthewire.tech's password: ⌨️ 7points 

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century8\desktop> whoami ⌨️
underthewire\century8
```

## Flag
7points

## Continue
[Continue](./Century0708.md)