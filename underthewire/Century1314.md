# Century Level 13 → 14 grep -wo "polo" countpolos | wc -l

## Previous Flag
```
755
```

## Goal
The password for Century15 is the number of times the word “polo” appears within the file on the desktop.<br>

NOTE: You should count the instances of the whole word only..

## What I learned
```
(Get-Content countpolos -Raw) -split '\b' | Where-Object {$_ -eq 'polo'} | Measure-Object | Select -Expand Count

                                                        grep -wo "polo" countpolos | wc -l
                                                            -w → match whole word only
                                                            -o → print only the match, one per line
                                                            wc -l → count the lines (number of matches)
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century14@century.underthewire.tech -p 22 ⌨️
century14@century.underthewire.tech's password: ⌨️ 755

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century14\desktop> dir ⌨️

    Directory: C:\users\century14\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  11:24 PM         202900 countpolos 👀

PS C:\users\century14\desktop> Select-String -Path "countpolos" -Pattern "\bpolo\b" -AllMatches | ForEach-Object { $_.Matches.Count } | Measure-Object -Sum | Select-Object -ExpandProperty Sum ⌨️
153 🔐
PS C:\users\century14\desktop> (Get-Content countpolos -Raw) -split '\b' | Where-Object {$_ -eq 'polo'} | Measure-Object | Select -Expand Count ⌨️
153 🔐
PS C:\users\century14\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century15@century.underthewire.tech -p 22 ⌨️
century15@century.underthewire.tech's password: 153 ⌨️

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century15\desktop> whoami ⌨️
underthewire\century15
```

## Flag
153

## Continue
[Continue](./Century1415.md)