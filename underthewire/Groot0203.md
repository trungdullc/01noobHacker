# Groot Level 02 → 03 grep -wo 'beetle' words.txt | wc -l

## Previous Flag
```
hiding
```

## Goal
The password for groot4 is the number of times the word “beetle” is listed in the file on the desktop.

## What I learned
```
# case-sensitive whole-word count
grep -wo 'beetle' words.txt | wc -l

# case-insensitive
grep -owi 'beetle' words.txt | wc -l

(Select-String -Path "words.txt" -Pattern '\bbeetle\b' -AllMatches | ForEach-Object { $_.Matches.Count } | Measure-Object -Sum).Sum
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot3@groot.underthewire.tech -p 22 ⌨️
groot3@groot.underthewire.tech's password: hiding ⌨️

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot3\desktop> dir ⌨️

    Directory: C:\users\Groot3\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM        2357296 words.txt 👀

PS C:\users\Groot3\desktop> (Select-String -Path "words.txt" -Pattern '\bbeetle\b' -AllMatches | ForEach-Object { $_.Matches.Count } | Measure-Object -Sum).Sum ⌨️
5 🔐

PS C:\users\Groot3\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot4@groot.underthewire.tech -p 22 ⌨️
groot4@groot.underthewire.tech's password: ⌨️ 5

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot4\desktop> whoami ⌨️
underthewire\groot4
```

## Flag
5

## Continue
[Continue](./Groot0304.md)