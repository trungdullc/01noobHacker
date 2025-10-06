# Oracle Level 09 → 10 Get-Item 'HKCU:\Software\Microsoft\Internet Explorer\TypedURLs'

## Previous Flag
```
utw_exch9229
```

## Goal
The password for oracle11 is the .biz site the user has previously navigated to.<br>

NOTE:<br>
– Don’t include the extension.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-Item 'HKCU:\Software\Microsoft\Internet Explorer\TypedURLs'
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle10@groot.underthewire.tech -p 22 ⌨️
oracle10@groot.underthewire.tech's password: ⌨️ utw_exch9229

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle10\desktop> Get-Item 'HKCU:\Software\Microsoft\Internet Explorer\TypedURLs' ⌨️

    Hive: HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer

Name                           Property
----                           --------
TypedURLs                      url1 : http://go.microsoft.com/fwlink/p/?LinkId=255141
                               url2 : http://google.com
                               url3 : http://underthewire.tech
                               url4 : http://bimmerfest.com
                               url5 : http://nba.com
                               url6 : http://yondu.biz 👀
                               url7 : http://hardknocks.edu
                               url8 : http://installation.org

PS C:\users\Oracle10\desktop> (Get-Item 'HKCU:\Software\Microsoft\Internet Explorer\TypedURLs' | Get-ItemProperty).url6.Split('/')[2].Split('\.')[0] ⌨️
yondu 🔐

PS C:\users\Oracle10\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle11@groot.underthewire.tech -p 22 ⌨️
oracle11@groot.underthewire.tech's password: ⌨️ yondu

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle11\desktop> whoami ⌨️
underthewire\oracle11
```

## Flag
yondu

## Continue
[Continue](./Oracle1011.md)