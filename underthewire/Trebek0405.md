# Trebek Level 04 → 05

## Previous Flag
```
01/05/2017_red
```

## Goal
The password for trebek6 is the name of the executable that is starting at 3/23/2017 8:08:53 PM via the Software Protection service as depicted in the event log on the desktop.<br>

NOTE:<br>
– Don’t include the file extension (i.e.- .exe).<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Google and ChatGPT
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek5@groot.underthewire.tech -p 22 ⌨️
trebek5@groot.underthewire.tech's password: ⌨️ 01/05/2017_red

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek5\desktop> dir ⌨️

    Directory: C:\users\trebek5\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:55 AM        5312512 application.evtx

# ChatGPT
Here are some common Event IDs associated with the Software Protection / Software Protection Platform (SPP / sppsvc / “Security-SPP”) services:

Event ID	Meaning / Description
900	        The Software Protection service is starting.
903	        The Software Protection service has stopped. 
902	        The Software Protection service has started. 
16384	    Successfully scheduled Software Protection service for restart (Rules Engine).
16394	    Offline down-level migration succeeded (Security SPP) 
12288	    A KMS activation request event under SPP / licensing context (client request)
1003	    Licensing status check completed (SPP) 

PS C:\users\trebek5\desktop> $evt = Get-WinEvent -Path .\application.evtx -FilterXPath "*[System[(EventID=900)]] or *[System[(EventID=16384)]] or *[System[(EventID=16394)]]" ⌨️
PS C:\users\trebek5\desktop> Get-Variable evt ⌨️

Name                           Value
----                           -----
evt                            {System.Diagnostics.Eventing.Reader.EventLogRecord, System.Diagnostics.Eventing.Reader.EventLogRecord, System.Diagnostic...

PS C:\users\trebek5\desktop> $evt.Count ⌨️
1853
PS C:\users\trebek5\desktop> $evt | Select -First 10 ⌨️

   ProviderName: Microsoft-Windows-Security-SPP

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/11/2017 8:40:37 PM         16384 Information      Successfully scheduled Software Protection service for re-start at 2017-05-12T20:39:37Z. Reason: TBL.  
5/11/2017 8:40:06 PM           900 Information      The Software Protection service is starting....
5/11/2017 8:35:16 PM         16384 Information      Successfully scheduled Software Protection service for re-start at 2017-05-12T20:34:15Z. Reason: TBL.  
5/11/2017 8:34:45 PM           900 Information      The Software Protection service is starting....
5/11/2017 8:12:54 PM         16384 Information      Successfully scheduled Software Protection service for re-start at 2017-05-12T20:11:53Z. Reason: TBL.  
5/11/2017 8:12:11 PM           900 Information      The Software Protection service is starting....
5/11/2017 8:11:11 PM         16384 Information      Successfully scheduled Software Protection service for re-start at 2017-05-12T20:09:10Z. Reason: TBL.  
5/17/2017 8:10:00 PM           900 Information      The Software Protection service is starting....
5/17/2017 7:46:59 PM         16384 Information      Successfully scheduled Software Protection service for re-start at 2017-05-18T19:45:45Z. Reason: TBL.  
5/17/2017 7:46:03 PM           900 Information      The Software Protection service is starting....

PS C:\users\trebek5\desktop> $evt.Where({$_.TimeCreated -eq (Get-Date '3/23/2017 8:08:53 PM')}) ⌨️

   ProviderName: Microsoft-Windows-Security-SPP

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
3/23/2017 8:08:53 PM           900 Information      The Software Protection service is starting....

PS C:\users\trebek5\desktop> $evt.Where({$_.TimeCreated -eq (Get-Date '3/23/2017 8:08:53 PM')}).Message ⌨️
The Software Protection service is starting.
Parameters:caller=wlms.exe 👀
PS C:\users\trebek5\desktop> $evt.Where({$_.TimeCreated -eq (Get-Date '3/23/2017 8:08:53 PM')}).Message.Split("`n")[-1].Split('=')[1].Split('\.')[0]
wlms 🔐

PS C:\users\trebek5\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek6@groot.underthewire.tech -p 22 ⌨️
trebek6@groot.underthewire.tech's password: ⌨️ wlms

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek6\desktop> whoami ⌨️
underthewire\trebek6
```

## Flag
wlms

## Continue
[Continue](./Trebek0506.md)