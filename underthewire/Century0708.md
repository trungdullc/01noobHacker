# Century Level 07 → 08 sort unique.txt | uniq -u | wc -l

## Previous Flag
```
7points
```

## Goal
The password for Century9 is the number of unique entries within the file on the desktop.

## What I learned
```
Get-Content unique.txt | Select-Object -First 5             cat unique.txt | head -n 5
Get-Content unique.txt | Select-Object -Last 5              cat unique.txt | tail -n 5

(Get-Content unique.txt | Sort-Object | Group-Object | Where-Object { $_.Count -eq 1 } | ForEach-Object { $_.Name }).Count
                                                            cat unique.txt | sort | unique | wc -l
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century8@century.underthewire.tech -p 22 ⌨️
century8@century.underthewire.tech's password: ⌨️ 7points

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century8\desktop> dir ⌨️

    Directory: C:\users\century8\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:33 AM          15858 unique.txt 👀

PS C:\users\century8\desktop> Get-Content unique.txt | Select-Object -First 5 ⌨️
recreatively
proboscidean
commenceable
simptico
zoon

PS C:\users\century8\desktop> (Get-Content .\unique.txt | Sort-Object -Unique).Count ⌨️
696 🔐

PS C:\users\century8\desktop> (Get-Content unique.txt | Sort-Object | Group-Object | Where-Object { $_.Count -eq 1 } | ForEach-Object { $_.Name }).Count ⌨️
696 🔐
PS C:\users\century8\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century9@century.underthewire.tech -p 22 ⌨️
century9@century.underthewire.tech's password: ⌨️ 696

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century9\desktop> whoami ⌨️
underthewire\century9
```

## Flag
696

## Continue
[Continue](./Century0809.md)