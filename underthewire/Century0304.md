# Century Level 03 → 04 cd "Can You Open Me"

## Previous Flag
```
123
```

## Goal
The password for Century5 is the name of the file within a directory on the desktop that has spaces in its name.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```
tab is your friend
" " or ' ' for filename w/ spaces
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century4@century.underthewire.tech -p 22 ⌨️
century4@century.underthewire.tech's password: ⌨️ 123

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century4\desktop> dir ⌨️

    Directory: C:\users\century4\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d👀-----        4/27/2025   7:57 PM                Can You Open Me 👀

PS C:\users\century4\desktop> cd '.\Can You Open Me' ⌨️
PS C:\users\century4\desktop\Can You Open Me> dir ⌨️

    Directory: C:\users\century4\desktop\Can You Open Me

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        4/27/2025   7:57 PM             24 15768 🔐

PS C:\users\century4\desktop\Can You Open Me> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century5@century.underthewire.tech -p 22 ⌨️
century5@century.underthewire.tech's password: ⌨️ 15768 
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century5\desktop> whoami ⌨️
underthewire\century5
```

## Flag
15768

## Continue
[Continue](./Century0405.md)