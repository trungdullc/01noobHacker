# Century Level 02 → 03 wc -l for PS

## Previous Flag
```
invoke-webrequest443 
```

## Goal
The password for Century4 is the number of files on the desktop.

## What I learned
```
(Get-ChildItem -File).Count             ls -l | wc

Get-ChildItem (alias: dir, ls)                          ls -l
    a = Archive                                         1st char: type (d = directory, - = file, l = symlink, etc.)
    r = Read-only                                       Next 3: owner permissions (rwx)
    h = Hidden                                          Next 3: group permissions (rwx)
    s = System                                          Last 3: others’ permissions (rwx)
    d = Directory
    l = Reparse point / symbolic link

Get-Acl .\99 | Format-List
(Get-Acl .\99).Access | Format-Table IdentityReference, FileSystemRights, AccessControlType

wc file.txt
120  450  3250 file.txt

    120 → number of lines (-l)
    450 → number of words (-w)
    3250 → number of bytes (-c)
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century3@century.underthewire.tech -p 22 ⌨️
century3@century.underthewire.tech's password: ⌨️ invoke-webrequest443 
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century3\desktop> dir ⌨️

    Directory: C:\users\century3\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM             33 countme1012
-a----        8/30/2018   3:29 AM             33 countme1064
-a----        8/30/2018   3:29 AM             33 countme1079
-a----        8/30/2018   3:29 AM             33 countme1099
-a----        8/30/2018   3:29 AM             33 countme1118
-a----        8/30/2018   3:29 AM             33 countme1128
-a----        8/30/2018   3:29 AM             33 countme1134
-a----        8/30/2018   3:29 AM             33 countme1153
-a----        8/30/2018   3:29 AM             33 countme1171
-a----        8/30/2018   3:29 AM             33 countme1202
-a----        8/30/2018   3:29 AM             33 countme1209
-a----        8/30/2018   3:29 AM             33 countme123
-a----        8/30/2018   3:29 AM             33 countme1244
-a----        8/30/2018   3:29 AM             33 countme1245
-a----        8/30/2018   3:29 AM             33 countme125
-a----        8/30/2018   3:29 AM             33 countme1261
-a----        8/30/2018   3:29 AM             33 countme1289
-a----        8/30/2018   3:29 AM             33 countme1302
-a----        8/30/2018   3:29 AM             33 countme131
-a----        8/30/2018   3:29 AM             33 countme1320
-a----        8/30/2018   3:29 AM             33 countme1348
-a----        8/30/2018   3:29 AM             33 countme1353
-a----        8/30/2018   3:29 AM             33 countme1365
-a----        8/30/2018   3:29 AM             33 countme1384
-a----        8/30/2018   3:29 AM             33 countme1389
-a----        8/30/2018   3:29 AM             33 countme140
-a----        8/30/2018   3:29 AM             33 countme1403
-a----        8/30/2018   3:29 AM             33 countme1422
-a----        8/30/2018   3:29 AM             33 countme1427
-a----        8/30/2018   3:29 AM             33 countme1444
-a----        8/30/2018   3:29 AM             33 countme145
-a----        8/30/2018   3:29 AM             33 countme1457
-a----        8/30/2018   3:29 AM             33 countme1471
-a----        8/30/2018   3:29 AM             33 countme1481
-a----        8/30/2018   3:29 AM             33 countme1530
-a----        8/30/2018   3:29 AM             33 countme1540
-a----        8/30/2018   3:29 AM             33 countme1552
-a----        8/30/2018   3:29 AM             33 countme1555
-a----        8/30/2018   3:29 AM             33 countme1559
-a----        8/30/2018   3:29 AM             33 countme1572
-a----        8/30/2018   3:29 AM             33 countme1612
-a----        8/30/2018   3:29 AM             33 countme1618
-a----        8/30/2018   3:29 AM             33 countme1623
-a----        8/30/2018   3:29 AM             33 countme1634
-a----        8/30/2018   3:29 AM             33 countme1674
-a----        8/30/2018   3:29 AM             33 countme1683
-a----        8/30/2018   3:29 AM             33 countme1701
-a----        8/30/2018   3:29 AM             33 countme1714
-a----        8/30/2018   3:29 AM             33 countme1720
-a----        8/30/2018   3:29 AM             33 countme1746
-a----        8/30/2018   3:29 AM             33 countme1747
-a----        8/30/2018   3:29 AM             33 countme1749
-a----        8/30/2018   3:29 AM             33 countme1776
-a----        8/30/2018   3:29 AM             33 countme1814
-a----        8/30/2018   3:29 AM             33 countme1822
-a----        8/30/2018   3:29 AM             33 countme1829
-a----        8/30/2018   3:29 AM             33 countme1837
-a----        8/30/2018   3:29 AM             33 countme1847
-a----        8/30/2018   3:29 AM             33 countme189
-a----        8/30/2018   3:29 AM             33 countme1920
-a----        8/30/2018   3:29 AM             33 countme1924
-a----        8/30/2018   3:29 AM             33 countme1945
-a----        8/30/2018   3:29 AM             33 countme1977
-a----        8/30/2018   3:29 AM             33 countme1984
-a----        8/30/2018   3:29 AM             33 countme220
-a----        8/30/2018   3:29 AM             33 countme248
-a----        8/30/2018   3:29 AM             33 countme26
-a----        8/30/2018   3:29 AM             33 countme262
-a----        8/30/2018   3:29 AM             33 countme268
-a----        8/30/2018   3:29 AM             33 countme290
-a----        8/30/2018   3:29 AM             33 countme3
-a----        8/30/2018   3:29 AM             33 countme304
-a----        8/30/2018   3:29 AM             33 countme320
-a----        8/30/2018   3:29 AM             33 countme34
-a----        8/30/2018   3:29 AM             33 countme342
-a----        8/30/2018   3:29 AM             33 countme346
-a----        8/30/2018   3:29 AM             33 countme35
-a----        8/30/2018   3:29 AM             33 countme367
-a----        8/30/2018   3:29 AM             33 countme378
-a----        8/30/2018   3:29 AM             33 countme380
-a----        8/30/2018   3:29 AM             33 countme389
-a----        8/30/2018   3:29 AM             33 countme436
-a----        8/30/2018   3:29 AM             33 countme443
-a----        8/30/2018   3:29 AM             33 countme446
-a----        8/30/2018   3:29 AM             33 countme455
-a----        8/30/2018   3:29 AM             33 countme459
-a----        8/30/2018   3:29 AM             33 countme462
-a----        8/30/2018   3:29 AM             33 countme464
-a----        8/30/2018   3:29 AM             33 countme473
-a----        8/30/2018   3:29 AM             33 countme489
-a----        8/30/2018   3:29 AM             33 countme496
-a----        8/30/2018   3:29 AM             33 countme5
-a----        8/30/2018   3:29 AM             33 countme512
-a----        8/30/2018   3:29 AM             33 countme541
-a----        8/30/2018   3:29 AM             33 countme554
-a----        8/30/2018   3:29 AM             33 countme597
-a----        8/30/2018   3:29 AM             33 countme602
-a----        8/30/2018   3:29 AM             33 countme629
-a----        8/30/2018   3:29 AM             33 countme64
-a----        8/30/2018   3:29 AM             33 countme688
-a----        8/30/2018   3:29 AM             33 countme691
-a----        8/30/2018   3:29 AM             33 countme698
-a----        8/30/2018   3:29 AM             33 countme700
-a----        8/30/2018   3:29 AM             33 countme704
-a----        8/30/2018   3:29 AM             33 countme707
-a----        8/30/2018   3:29 AM             33 countme719
-a----        8/30/2018   3:29 AM             33 countme75
-a----        8/30/2018   3:29 AM             33 countme750
-a----        8/30/2018   3:29 AM             33 countme758
-a----        8/30/2018   3:29 AM             33 countme759
-a----        8/30/2018   3:29 AM             33 countme768
-a----        8/30/2018   3:29 AM             33 countme775
-a----        8/30/2018   3:29 AM             33 countme779
-a----        8/30/2018   3:29 AM             33 countme798
-a----        8/30/2018   3:29 AM             33 countme802
-a----        8/30/2018   3:29 AM             33 countme87
-a----        8/30/2018   3:29 AM             33 countme875
-a----        8/30/2018   3:29 AM             33 countme877
-a----        8/30/2018   3:29 AM             33 countme891
-a----        8/30/2018   3:29 AM             33 countme923
-a----        8/30/2018   3:29 AM             33 countme929
-a----        8/30/2018   3:29 AM             33 countme972
-a----        8/30/2018   3:29 AM             33 countme996

PS C:\users\century3\desktop> (Get-ChildItem -File).Count ⌨️
123 🔐
PS C:\users\century3\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century4@century.underthewire.tech -p 22 ⌨️
century4@century.underthewire.tech's password: ⌨️ 123

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century4\desktop> whoami ⌨️
underthewire\century4
```

## Flag
123

## Continue
[Continue](./Century0304.md)