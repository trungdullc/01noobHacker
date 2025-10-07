# Century Level 05 → 06 find . -maxdepth 1 -type d | wc -l

## Previous Flag
```
underthewire3347
```

## Goal
The password for Century7 is the number of folders on the desktop.

## What I learned
```
(Get-ChildItem -Directory).Count            find . -maxdepth 1 -type d | wc -l      (non-recursive)
                                            ls -l | grep '^d' | wc -l   (not 100% safe)
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century6@century.underthewire.tech -p 22 ⌨️
century6@century.underthewire.tech's password: ⌨️ underthewire3347

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century6\desktop> dir ⌨️

    Directory: C:\users\century6\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        8/30/2018   3:29 AM                countme1012
d-----        8/30/2018   3:29 AM                countme1024
d-----        8/30/2018   3:29 AM                countme1025
d-----        8/30/2018   3:29 AM                countme1031
d-----        8/30/2018   3:29 AM                countme1056
d-----        8/30/2018   3:29 AM                countme1058
d-----        8/30/2018   3:29 AM                countme1068
d-----        8/30/2018   3:29 AM                countme1074
d-----        8/30/2018   3:29 AM                countme1083
d-----        8/30/2018   3:29 AM                countme1090
d-----        8/30/2018   3:29 AM                countme1102
d-----        8/30/2018   3:29 AM                countme1112
d-----        8/30/2018   3:29 AM                countme1117
d-----        8/30/2018   3:29 AM                countme1118
d-----        8/30/2018   3:29 AM                countme1127
d-----        8/30/2018   3:29 AM                countme1135
d-----        8/30/2018   3:29 AM                countme1137
d-----        8/30/2018   3:29 AM                countme1157
d-----        8/30/2018   3:29 AM                countme1186
d-----        8/30/2018   3:29 AM                countme1190
d-----        8/30/2018   3:29 AM                countme1198
d-----        8/30/2018   3:29 AM                countme1208
d-----        8/30/2018   3:29 AM                countme1223
d-----        8/30/2018   3:29 AM                countme1246
d-----        8/30/2018   3:29 AM                countme1253
d-----        8/30/2018   3:29 AM                countme1262
d-----        8/30/2018   3:29 AM                countme1272
d-----        8/30/2018   3:29 AM                countme1273
d-----        8/30/2018   3:29 AM                countme1295
d-----        8/30/2018   3:29 AM                countme1302
d-----        8/30/2018   3:29 AM                countme1310
d-----        8/30/2018   3:29 AM                countme1328
d-----        8/30/2018   3:29 AM                countme1334
d-----        8/30/2018   3:29 AM                countme1342
d-----        8/30/2018   3:29 AM                countme1359
d-----        8/30/2018   3:29 AM                countme1373
d-----        8/30/2018   3:29 AM                countme1381
d-----        8/30/2018   3:29 AM                countme1390
d-----        8/30/2018   3:29 AM                countme1394
d-----        8/30/2018   3:29 AM                countme1402
d-----        8/30/2018   3:29 AM                countme1405
d-----        8/30/2018   3:29 AM                countme1406
d-----        8/30/2018   3:29 AM                countme1414
d-----        8/30/2018   3:29 AM                countme1425
d-----        8/30/2018   3:29 AM                countme1455
d-----        8/30/2018   3:29 AM                countme1480
d-----        8/30/2018   3:29 AM                countme1481
d-----        8/30/2018   3:29 AM                countme149
d-----        8/30/2018   3:29 AM                countme1491
d-----        8/30/2018   3:29 AM                countme1512
d-----        8/30/2018   3:29 AM                countme1522
d-----        8/30/2018   3:29 AM                countme1527
d-----        8/30/2018   3:29 AM                countme1531
d-----        8/30/2018   3:29 AM                countme1538
d-----        8/30/2018   3:29 AM                countme1539
d-----        8/30/2018   3:29 AM                countme1552
d-----        8/30/2018   3:29 AM                countme1560
d-----        8/30/2018   3:29 AM                countme1563
d-----        8/30/2018   3:29 AM                countme1572
d-----        8/30/2018   3:29 AM                countme1587
d-----        8/30/2018   3:29 AM                countme1593
d-----        8/30/2018   3:29 AM                countme1594
d-----        8/30/2018   3:29 AM                countme1596
d-----        8/30/2018   3:29 AM                countme1600
d-----        8/30/2018   3:29 AM                countme1618
d-----        8/30/2018   3:29 AM                countme1630
d-----        8/30/2018   3:29 AM                countme1633
d-----        8/30/2018   3:29 AM                countme1638
d-----        8/30/2018   3:29 AM                countme1647
d-----        8/30/2018   3:29 AM                countme166
d-----        8/30/2018   3:29 AM                countme1674
d-----        8/30/2018   3:29 AM                countme1684
d-----        8/30/2018   3:29 AM                countme1687
d-----        8/30/2018   3:29 AM                countme1693
d-----        8/30/2018   3:29 AM                countme1711
d-----        8/30/2018   3:29 AM                countme1714
d-----        8/30/2018   3:29 AM                countme173
d-----        8/30/2018   3:29 AM                countme1749
d-----        8/30/2018   3:29 AM                countme176
d-----        8/30/2018   3:29 AM                countme177
d-----        8/30/2018   3:29 AM                countme1772
d-----        8/30/2018   3:29 AM                countme1774
d-----        8/30/2018   3:29 AM                countme1776
d-----        8/30/2018   3:29 AM                countme178
d-----        8/30/2018   3:29 AM                countme1789
d-----        8/30/2018   3:29 AM                countme1802
d-----        8/30/2018   3:29 AM                countme1816
d-----        8/30/2018   3:29 AM                countme1824
d-----        8/30/2018   3:29 AM                countme1833
d-----        8/30/2018   3:29 AM                countme1835
d-----        8/30/2018   3:29 AM                countme1848
d-----        8/30/2018   3:29 AM                countme1852
d-----        8/30/2018   3:29 AM                countme1860
d-----        8/30/2018   3:29 AM                countme1861
d-----        8/30/2018   3:29 AM                countme188
d-----        8/30/2018   3:29 AM                countme1897
d-----        8/30/2018   3:29 AM                countme1903
d-----        8/30/2018   3:29 AM                countme1904
d-----        8/30/2018   3:29 AM                countme1913
d-----        8/30/2018   3:29 AM                countme1935
d-----        8/30/2018   3:29 AM                countme1966
d-----        8/30/2018   3:29 AM                countme1979
d-----        8/30/2018   3:29 AM                countme1988
d-----        8/30/2018   3:29 AM                countme1995
d-----        8/30/2018   3:29 AM                countme20
d-----        8/30/2018   3:29 AM                countme200
d-----        8/30/2018   3:29 AM                countme204
d-----        8/30/2018   3:29 AM                countme205
d-----        8/30/2018   3:29 AM                countme215
d-----        8/30/2018   3:29 AM                countme239
d-----        8/30/2018   3:29 AM                countme24
d-----        8/30/2018   3:29 AM                countme240
d-----        8/30/2018   3:29 AM                countme254
d-----        8/30/2018   3:29 AM                countme270
d-----        8/30/2018   3:29 AM                countme28
d-----        8/30/2018   3:29 AM                countme295
d-----        8/30/2018   3:29 AM                countme297
d-----        8/30/2018   3:29 AM                countme32
d-----        8/30/2018   3:29 AM                countme320
d-----        8/30/2018   3:29 AM                countme323
d-----        8/30/2018   3:29 AM                countme334
d-----        8/30/2018   3:29 AM                countme340
d-----        8/30/2018   3:29 AM                countme348
d-----        8/30/2018   3:29 AM                countme352
d-----        8/30/2018   3:29 AM                countme362
d-----        8/30/2018   3:29 AM                countme366
d-----        8/30/2018   3:29 AM                countme385
d-----        8/30/2018   3:29 AM                countme387
d-----        8/30/2018   3:29 AM                countme391
d-----        8/30/2018   3:29 AM                countme398
d-----        8/30/2018   3:29 AM                countme401
d-----        8/30/2018   3:29 AM                countme402
d-----        8/30/2018   3:29 AM                countme416
d-----        8/30/2018   3:29 AM                countme422
d-----        8/30/2018   3:29 AM                countme432
d-----        8/30/2018   3:29 AM                countme44
d-----        8/30/2018   3:29 AM                countme440
d-----        8/30/2018   3:29 AM                countme460
d-----        8/30/2018   3:29 AM                countme493
d-----        8/30/2018   3:29 AM                countme502
d-----        8/30/2018   3:29 AM                countme526
d-----        8/30/2018   3:29 AM                countme527
d-----        8/30/2018   3:29 AM                countme536
d-----        8/30/2018   3:29 AM                countme556
d-----        8/30/2018   3:29 AM                countme559
d-----        8/30/2018   3:29 AM                countme564
d-----        8/30/2018   3:29 AM                countme567
d-----        8/30/2018   3:29 AM                countme568
d-----        8/30/2018   3:29 AM                countme573
d-----        8/30/2018   3:29 AM                countme598
d-----        8/30/2018   3:29 AM                countme613
d-----        8/30/2018   3:29 AM                countme618
d-----        8/30/2018   3:29 AM                countme619
d-----        8/30/2018   3:29 AM                countme624
d-----        8/30/2018   3:29 AM                countme625
d-----        8/30/2018   3:29 AM                countme627
d-----        8/30/2018   3:29 AM                countme635
d-----        8/30/2018   3:29 AM                countme636
d-----        8/30/2018   3:29 AM                countme651
d-----        8/30/2018   3:29 AM                countme656
d-----        8/30/2018   3:29 AM                countme66
d-----        8/30/2018   3:29 AM                countme667
d-----        8/30/2018   3:29 AM                countme674
d-----        8/30/2018   3:29 AM                countme678
d-----        8/30/2018   3:29 AM                countme679
d-----        8/30/2018   3:29 AM                countme700
d-----        8/30/2018   3:29 AM                countme716
d-----        8/30/2018   3:29 AM                countme734
d-----        8/30/2018   3:29 AM                countme747
d-----        8/30/2018   3:29 AM                countme750
d-----        8/30/2018   3:29 AM                countme752
d-----        8/30/2018   3:29 AM                countme762
d-----        8/30/2018   3:29 AM                countme763
d-----        8/30/2018   3:29 AM                countme765
d-----        8/30/2018   3:29 AM                countme774
d-----        8/30/2018   3:29 AM                countme780
d-----        8/30/2018   3:29 AM                countme810
d-----        8/30/2018   3:29 AM                countme819
d-----        8/30/2018   3:29 AM                countme829
d-----        8/30/2018   3:29 AM                countme833
d-----        8/30/2018   3:29 AM                countme839
d-----        8/30/2018   3:29 AM                countme84
d-----        8/30/2018   3:29 AM                countme854
d-----        8/30/2018   3:29 AM                countme861
d-----        8/30/2018   3:29 AM                countme862
d-----        8/30/2018   3:29 AM                countme867
d-----        8/30/2018   3:29 AM                countme876
d-----        8/30/2018   3:29 AM                countme884
d-----        8/30/2018   3:29 AM                countme902
d-----        8/30/2018   3:29 AM                countme908
d-----        8/30/2018   3:29 AM                countme909
d-----        8/30/2018   3:29 AM                countme912
d-----        8/30/2018   3:29 AM                countme945
d-----        8/30/2018   3:29 AM                countme949
d-----        8/30/2018   3:29 AM                countme972
d-----        8/30/2018   3:29 AM                countme978
d-----        8/30/2018   3:29 AM                countme981

PS C:\users\century6\desktop> (ls -Directory).Count ⌨️
197 🔐
PS C:\users\century6\desktop> (dir -Directory).Count ⌨️
197 🔐
PS C:\users\century6\desktop> (Get-ChildItem -Directory).Count ⌨️
197 🔐
PS C:\users\century6\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century7@century.underthewire.tech -p 22 ⌨️
century7@century.underthewire.tech's password: ⌨️ 197 

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century7\desktop> whoami ⌨️
underthewire\century7
```

## Flag
197

## Continue
[Continue](./Century0607.md)