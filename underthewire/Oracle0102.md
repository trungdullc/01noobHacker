# Oracle Level 01 → 02 Get-ChildItem -File | Get-FileHash -Algorithm MD5 | Sort-Object Hash

## Previous Flag
```
utc
```

## Goal
The password for oracle3 is the last five digits of the MD5 hash, from the hashes of files on the desktop that appears twice.<br>

NOTE: The password will be lowercase no matter how it appears on the screen

## What I learned
```
Get-ChildItem -File | Get-FileHash -Algorithm MD5 | Sort-Object Hash
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle2@groot.underthewire.tech -p 22 ⌨️
oracle2@groot.underthewire.tech's password: ⌨️ utc

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle2\desktop> dir ⌨️

    Directory: C:\users\Oracle2\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM          68448 file.txt
-a----        8/30/2018   5:52 AM          68447 file1.txt
-a----        8/30/2018   5:52 AM          68452 file10.txt
-a----        8/30/2018   5:52 AM          68450 file11.txt
-a----        8/30/2018   5:52 AM          68450 file12.txt
-a----        8/30/2018   5:52 AM          68449 file13.txt
-a----        8/30/2018   5:52 AM          68450 file14.txt
-a----        8/30/2018   5:52 AM          68451 file15.txt
-a----        8/30/2018   5:52 AM          68448 file16.txt
-a----        8/30/2018   5:52 AM          68451 file17.txt
-a----        8/30/2018   5:52 AM          68451 file18.txt
-a----        8/30/2018   5:52 AM          68451 file19.txt
-a----        8/30/2018   5:52 AM          68449 file2.txt
-a----        8/30/2018   5:52 AM          68450 file20.txt
-a----        8/30/2018   5:52 AM          68451 file21.txt
-a----        8/30/2018   5:52 AM          68449 file3.txt
-a----        8/30/2018   5:52 AM          68449 file4.txt
-a----        8/30/2018   5:52 AM          68450 file5.txt
-a----        8/30/2018   5:52 AM          68450 file6.txt
-a----        8/30/2018   5:52 AM          68450 file7.txt
-a----        8/30/2018   5:52 AM          68450 file8.txt
-a----        8/30/2018   5:52 AM          68450 file9.txt

PS C:\users\Oracle2\desktop> Get-ChildItem -File | Get-FileHash -Algorithm MD5 | Sort-Object Hash ⌨️

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             0E848B375C2871DBFE0AD405B58BF4E2                                       C:\users\Oracle2\desktop\file19.txt
MD5             1463397F8FDB4B99CDE3DB0B1E37EA6E                                       C:\users\Oracle2\desktop\file11.txt
MD5             1C579B4F21EB236E0CC7ABBB0313AE4C                                       C:\users\Oracle2\desktop\file15.txt
MD5             1E0054A7A7C6D8C820C7307F94513E50                                       C:\users\Oracle2\desktop\file21.txt
MD5             226F590B023BF532FBEEB46154288644                                       C:\users\Oracle2\desktop\file10.txt
MD5             3444EAB3BB3F80522031104151DAADA5                                       C:\users\Oracle2\desktop\file7.txt
MD5             3705066150D7BF296F1E0F0EDC0DB9FA                                       C:\users\Oracle2\desktop\file6.txt
MD5             39A77E07A13922A8C971EB0BEEFFCEE3                                       C:\users\Oracle2\desktop\file8.txt
MD5             3E00A2BF4B49C7D18DBA79DD39C4B19C                                       C:\users\Oracle2\desktop\file18.txt
MD5             41E65125606DE228B94CC2C97B401C1A                                       C:\users\Oracle2\desktop\file20.txt
MD5             4A22F5027B6E3C09C9743DB955B6878A                                       C:\users\Oracle2\desktop\file2.txt
MD5             4CEB4AAE0231B53834280CC5314FB932                                       C:\users\Oracle2\desktop\file1.txt
MD5             5BE11FF0037EED156F77213658C2F5C4                                       C:\users\Oracle2\desktop\file16.txt 👀
MD5             5BE11FF0037EED156F77213658C2F5C4                                       C:\users\Oracle2\desktop\file.txt 👀
MD5             67CE823F3BCC2BCA22ADEB066160CF54                                       C:\users\Oracle2\desktop\file5.txt
MD5             BA5DACAC4B8791D0A10C606C7DCCD10C                                       C:\users\Oracle2\desktop\file14.txt
MD5             C6DDC40861E16E60E924C34ED00F787B                                       C:\users\Oracle2\desktop\file3.txt
MD5             CABBDEAF260BF1FE922A8605D4DDD2BE                                       C:\users\Oracle2\desktop\file9.txt
MD5             F0483A1F2E8A20412DBBFC12F99C1193                                       C:\users\Oracle2\desktop\file12.txt
MD5             FAB743AE9D2C15F5B84975A891133CCB                                       C:\users\Oracle2\desktop\file13.txt
MD5             FD74053193C5E5984E905FBDAD1D61BF                                       C:\users\Oracle2\desktop\file17.txt
MD5             FEB6246F13187BFBCA82EB9105B04B61                                       C:\users\Oracle2\desktop\file4.txt

PS C:\users\Oracle2\desktop> $Match = "5BE11FF0037EED156F77213658C2F5C4" ⌨️
PS C:\users\Oracle2\desktop> $Match.Substring(($Match.Length - 5), 5).ToLower() ⌨️
2f5c4 🔐

PS C:\users\Oracle2\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle3@groot.underthewire.tech -p 22 ⌨️
oracle3@groot.underthewire.tech's password: ⌨️ 2f5c4

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle3\desktop> whoami ⌨️
underthewire\oracle3
```

## Flag
2f5c4

## Continue
[Continue](./Oracle0203.md)