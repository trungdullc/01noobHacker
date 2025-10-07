# Trebek Level 05 → 06 (Get-ChildItem -Recurse -Filter '*.dll' 'C:\program files\adobe\').Count.ToString()

## Previous Flag
```
wlms
```

## Goal
The password for trebek7 is the total number of DLLs within the “C:\program files\adobe\” folder and it’s subfolders PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the count is “9999” and the file on the desktop is named “_abc”, then the password would be “9999_abc”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
(Get-ChildItem -Recurse -Filter '*.dll' 'C:\program files\adobe\').Count.ToString()
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek6@groot.underthewire.tech -p 22 ⌨️
trebek6@groot.underthewire.tech's password: ⌨️ wlms

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek6\desktop> dir ⌨️

    Directory: C:\users\trebek6\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:47 AM              0 _reader 👀

PS C:\users\trebek6\desktop> Get-ChildItem -Recurse -Filter '*.dll' 'C:\program files\adobe\'  ⌨️

    Directory: C:\program files\adobe\Reader 11.0\Esl

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM         218136 AiodLite.dll

    Directory: C:\program files\adobe\Reader 11.0\Reader

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM         196120 A3DUtils.dll
-a----        8/30/2018   5:52 AM         949784 ACE.dll
-a----        8/30/2018   5:53 AM          60552 Acrofx32.dll
-a----        8/30/2018   5:52 AM       30938648 AcroRd32.dll
-a----        8/30/2018   5:53 AM          91784 AcroRdIF.dll
-a----        8/30/2018   5:53 AM          86040 AcroSup64.dll
-a----        8/30/2018   5:53 AM         484232 AdobeLinguistic.dll
-a----        8/30/2018   5:53 AM         259608 adoberfp.dll
-a----        8/30/2018   5:53 AM         304248 AdobeXMP.dll
-a----        8/30/2018   5:52 AM        4907544 AGM.dll
-a----        8/30/2018   5:53 AM         272096 ahclient.dll
-a----        8/30/2018   5:52 AM         175128 AXE8SharedExpat.dll
-a----        8/30/2018   5:52 AM         605720 AXSLE.dll
-a----        8/30/2018   5:53 AM         120344 BIB.dll
-a----        8/30/2018   5:53 AM         159768 BIBUtils.dll
-a----        8/30/2018   5:53 AM         227328 ccme_asym.dll
-a----        8/30/2018   5:53 AM         379904 ccme_base.dll
-a----        8/30/2018   5:53 AM         208384 ccme_base_non_fips.dll
-a----        8/30/2018   5:53 AM         564736 ccme_ecc.dll
-a----        8/30/2018   5:53 AM         471552 ccme_ecdrbg.dll
-a----        8/30/2018   5:53 AM        2809368 CoolType.dll
-a----        8/30/2018   5:53 AM         291328 cryptocme.dll
-a----        8/30/2018   5:53 AM         662672 ExtendScript.dll
-a----        8/30/2018   5:53 AM         853128 icucnv40.dll
-a----        8/30/2018   5:53 AM          97928 icudt40.dll
-a----        8/30/2018   5:53 AM         667672 JP2KLib.dll
-a----        8/30/2018   5:53 AM         594552 logsession.dll
-a----        8/30/2018   5:53 AM       14588632 NPSWF32.dll
-a----        8/30/2018   5:53 AM         770272 Onix32.dll
-a----        8/30/2018   5:53 AM          99408 PDFPrevHndlr.dll
-a----        8/30/2018   5:53 AM        1346176 pe.dll
-a----        8/30/2018   5:54 AM        1552096 rt3d.dll
-a----        8/30/2018   5:53 AM         588936 ScCore.dll
-a----        8/30/2018   5:54 AM         313992 sqlite.dll
-a----        8/30/2018   5:53 AM          18056 ViewerPS.dll

    Directory: C:\program files\adobe\Reader 11.0\Reader\AcroExt

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM       10002288 icudt.dll
-a----        8/30/2018   5:52 AM       41313648 libcef.dll

    Directory: C:\program files\adobe\Reader 11.0\Reader\AIR

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM         253976 nppdf32.dll

    Directory: C:\program files\adobe\Reader 11.0\Reader\Browser

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:53 AM         253976 nppdf32.dll

PS C:\users\trebek6\desktop> (Get-ChildItem -Recurse -Filter '*.dll' 'C:\program files\adobe\').Count ⌨️
40 👀
PS C:\users\trebek6\desktop> (Get-ChildItem -Recurse -Filter '*.dll' 'C:\program files\adobe\').Count.ToString() ⌨️
40
PS C:\users\trebek6\desktop> (Get-ChildItem -Recurse -Filter '*.dll' 'C:\program files\adobe\').Count.ToString() + (ls -File).Name.ToLower() ⌨️
40_reader 🔐

PS C:\users\trebek6\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek7@groot.underthewire.tech -p 22 ⌨️
trebek7@groot.underthewire.tech's password: ⌨️ 40_reader

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek7\desktop> whoami ⌨️
underthewire\trebek7
```

## Flag
40_reader

## Continue
[Continue](./Trebek0607.md)