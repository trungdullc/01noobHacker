# Century Level 10 → 11 ls -laR | grep -v "desktop.ini" 2>/dev/null

## Previous Flag
```
windowsupdates110
```

## Goal
The password for Century12 is the name of the hidden file within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile.<br>

NOTE:<br>
– Exclude “desktop.ini”<br>
– The password will be lowercase no matter how it appears on the screen

## What I learned
```
                                                                    # grep -v (exclude pattern)
Get-ChildItem -Recurse -Hidden -Exclude "desktop.ini" 2>$null       ls -laR | grep -v "desktop.ini" 2>/dev/null
                                                                    # find files with -not -name or ! -name
                                                                    find . -type f ! -name "*.log"
                                                                    # Exclude a directory
                                                                    find . -type f -not -path "./node_modules/*"
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century11@century.underthewire.tech -p 22 ⌨️
century11@century.underthewire.tech's password: ⌨️ windowsupdates110

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century11\desktop> dir ⌨️
PS C:\users\century11\desktop> cd .. ⌨️
PS C:\users\century11> dir ⌨️

    Directory: C:\users\century11

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        9/16/2024   3:40 PM                AppData
d-r---        7/16/2016   1:23 PM                Desktop
d-----         3/8/2025   6:59 AM                Documents
d-r---        8/30/2018   3:34 AM                Downloads
d-r---        7/16/2016   1:23 PM                Favorites
d-r---        7/16/2016   1:23 PM                Links
d-r---        7/16/2016   1:23 PM                Music
d-r---        7/16/2016   1:23 PM                Pictures
d-----        7/16/2016   1:23 PM                Saved Games
d-r---        7/16/2016   1:23 PM                Videos

PS C:\users\century11> Get-ChildItem -Recurse -Hidden 2>$null ⌨️

    Directory: C:\users\century11

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Application Data
d--hsl        8/30/2018   3:11 AM                Cookies
d--hsl        8/30/2018   3:11 AM                Local Settings
d--hsl        8/30/2018   3:11 AM                My Documents
d--hsl        8/30/2018   3:11 AM                NetHood
d--hsl        8/30/2018   3:11 AM                PrintHood
d--hsl        8/30/2018   3:11 AM                Recent
d--hsl        8/30/2018   3:11 AM                SendTo
d--hsl        8/30/2018   3:11 AM                Start Menu
d--hsl        8/30/2018   3:11 AM                Templates
-a-h--         8/4/2025   7:20 PM         262144 NTUSER.DAT
-a-hs-        8/30/2018   3:11 AM          98304 ntuser.dat.LOG1
-a-hs-        8/30/2018   3:11 AM         126976 ntuser.dat.LOG2
-a-hs-        7/12/2020  10:55 PM          65536 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TM.blf
-a-hs-        6/14/2020   4:36 AM         524288 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000001.regtrans-ms
-a-hs-        7/12/2020  10:55 PM         524288 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000002.regtrans-ms
---hs-        8/30/2018   3:11 AM             20 ntuser.ini

    Directory: C:\users\century11\AppData\Local

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Application Data
d--hsl        8/30/2018   3:11 AM                History
d--hsl        8/30/2018   3:11 AM                Temporary Internet Files

    Directory: C:\users\century11\AppData\Local\Microsoft\Windows

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Temporary Internet Files
-a-h--        8/30/2018   3:11 AM           8192 UsrClass.dat
-a-hs-        8/30/2018   3:11 AM           8192 UsrClass.dat.LOG1
-a-hs-        8/30/2018   3:11 AM           8192 UsrClass.dat.LOG2
-a-hs-        8/30/2018   3:11 AM          65536 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TM.blf
-a-hs-        8/30/2018   3:11 AM         524288 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000001.regtrans-ms
-a-hs-        8/30/2018   3:11 AM         524288 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000002.regtrans-ms

    Directory: C:\users\century11\AppData\Local\Microsoft\Windows\WinX\Group1

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a-hs-        7/16/2016   1:21 PM             75 desktop.ini

    Directory: C:\users\century11\AppData\Local\Microsoft\Windows\WinX\Group2

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a-hs-        7/16/2016   1:21 PM            325 desktop.ini

    Directory: C:\users\century11\AppData\Local\Microsoft\Windows\WinX\Group3

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a-hs-        7/16/2016   1:21 PM            948 desktop.ini

    Directory: C:\users\century11\Documents

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                My Music
d--hsl        8/30/2018   3:11 AM                My Pictures
d--hsl        8/30/2018   3:11 AM                My Videos

    Directory: C:\users\century11\Downloads

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
--rh--        8/30/2018   3:34 AM             30 secret_sauce 👀

PS C:\users\century11> Get-ChildItem -Recurse -Hidden -Exclude "desktop.ini" 2>$null ⌨️

    Directory: C:\users\century11\AppData\Local

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Application Data
d--hsl        8/30/2018   3:11 AM                History

    Directory: C:\users\century11\AppData\Local\Microsoft\Windows

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Temporary Internet Files
-a-h--        8/30/2018   3:11 AM           8192 UsrClass.dat
-a-hs-        8/30/2018   3:11 AM           8192 UsrClass.dat.LOG1
-a-hs-        8/30/2018   3:11 AM           8192 UsrClass.dat.LOG2
-a-hs-        8/30/2018   3:11 AM          65536 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TM.blf
-a-hs-        8/30/2018   3:11 AM         524288 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000001.regtrans-ms
-a-hs-        8/30/2018   3:11 AM         524288 UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000002.regtrans-ms

    Directory: C:\users\century11\AppData\Local

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Temporary Internet Files

    Directory: C:\users\century11

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Application Data
d--hsl        8/30/2018   3:11 AM                Cookies

    Directory: C:\users\century11\Documents

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                My Music
d--hsl        8/30/2018   3:11 AM                My Pictures
d--hsl        8/30/2018   3:11 AM                My Videos

    Directory: C:\users\century11\Downloads

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
--rh--        8/30/2018   3:34 AM             30 secret_sauce 👀

    Directory: C:\users\century11

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d--hsl        8/30/2018   3:11 AM                Local Settings
d--hsl        8/30/2018   3:11 AM                My Documents
d--hsl        8/30/2018   3:11 AM                NetHood
d--hsl        8/30/2018   3:11 AM                PrintHood
d--hsl        8/30/2018   3:11 AM                Recent
d--hsl        8/30/2018   3:11 AM                SendTo
d--hsl        8/30/2018   3:11 AM                Start Menu
d--hsl        8/30/2018   3:11 AM                Templates
-a-h--         8/4/2025   7:20 PM         262144 NTUSER.DAT
-a-hs-        8/30/2018   3:11 AM          98304 ntuser.dat.LOG1
-a-hs-        8/30/2018   3:11 AM         126976 ntuser.dat.LOG2
-a-hs-        7/12/2020  10:55 PM          65536 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TM.blf
-a-hs-        6/14/2020   4:36 AM         524288 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000001.regtrans-ms
-a-hs-        7/12/2020  10:55 PM         524288 NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000002.regtrans-ms
---hs-        8/30/2018   3:11 AM             20 ntuser.ini

PS C:\users\century11> Get-ChildItem -Hidden -Recurse -File -ErrorAction SilentlyContinue | Select-Object -Unique Name

Name
----
NTUSER.DAT
ntuser.dat.LOG1
ntuser.dat.LOG2
NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TM.blf
NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000001.regtrans-ms
NTUSER.DAT{0f893ee4-78e5-11e6-90dd-eefb07825ed9}.TMContainer00000000000000000002.regtrans-ms
ntuser.ini
UsrClass.dat
UsrClass.dat.LOG1
UsrClass.dat.LOG2
UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TM.blf
UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000001.regtrans-ms
UsrClass.dat{d82669b3-abff-11e8-90ee-e14c26db97e8}.TMContainer00000000000000000002.regtrans-ms
desktop.ini
secret_sauce

PS C:\users\century11> Get-ChildItem -Hidden -Recurse -File -ErrorAction SilentlyContinue | Select-Object -Unique Name | Where-Object {$_.Name -like "*secret*"} ⌨️

Name        
----        
secret_sauce

PS C:\users\century11> Get-Content .\Downloads\secret_sauce ⌨️
Congratulations. You found it!
PS C:\users\century11> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century12@century.underthewire.tech -p 22 ⌨️
century12@century.underthewire.tech's password: ⌨️ secret_sauce

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century12\desktop> whoami ⌨️
underthewire\century12
```

## Flag
secret_sauce

## Continue
[Continue](./Century1112.md)