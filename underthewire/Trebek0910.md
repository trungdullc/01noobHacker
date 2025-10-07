# Trebek Level 09 → 10 .Split("")[0]

## Previous Flag
```
shoretroopers$_hiding
```

## Goal
The password for trebek11 is the last name of the user who enabled Obi-Wan Kenobi’s account as depicted in the event logs on the desktop PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the last name of the user is “johnson” and the file on the desktop is named “1234”, the password would be “johnson1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Microsoft Learn: 4722(S) A user account was enabled. - Windows 10

-like vs -eq
    -like supports wildcards (*, ?)
    -eq is an exact match operator
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek10@groot.underthewire.tech -p 22 ⌨️
trebek10@groot.underthewire.tech's password: ⌨️ shoretroopers$_hiding

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek10\desktop> dir ⌨️

    Directory: C:\users\trebek10\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:48 AM              0 2121 👀
-a----        8/30/2018   5:54 AM       99684352 security.evtx

PS C:\users\trebek10\desktop> $evt = Get-WinEvent -Path .\security.evtx -FilterXPath "*[System[EventID=4722]]" ⌨️
PS C:\users\trebek10\desktop> $evt.Count ⌨️
39
PS C:\users\trebek10\desktop> $evt | Select -First 10 ⌨️

   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/11/2017 8:36:52 PM          4722 Information      A user account was enabled....
5/11/2017 6:56:12 PM          4722 Information      A user account was enabled....
5/11/2017 6:46:25 PM          4722 Information      A user account was enabled....
5/11/2017 6:26:08 PM          4722 Information      A user account was enabled....
5/11/2017 6:19:39 PM          4722 Information      A user account was enabled....
5/11/2017 6:15:55 PM          4722 Information      A user account was enabled....
5/10/2017 11:29:12 AM         4722 Information      A user account was enabled....
5/10/2017 11:28:43 AM         4722 Information      A user account was enabled....
5/10/2017 11:28:15 AM         4722 Information      A user account was enabled....
5/10/2017 11:27:47 AM         4722 Information      A user account was enabled....

PS C:\users\trebek10\desktop> $evt.Where({$_.Message -like '*obi*'}) ⌨️

   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/11/2017 6:56:12 PM          4722 Information      A user account was enabled....

PS C:\users\trebek10\desktop> $evt.Where({$_.Message -like '*obi*'}).Message ⌨️           
A user account was enabled.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1153
        Account Name:           admiral.ackbar 👀
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x12CEFCA

Target Account:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1154
        Account Name:           obi-wan.kenobi
        Account Domain:         UNDERTHEWIRE

PS C:\users\trebek10\desktop> $evt.Where({$_.Message -like '*obi*'}).Message.Split("`n")[0] ⌨️
A user account was enabled.
PS C:\users\trebek10\desktop> $evt.Where({$_.Message -like '*obi*'}).Message.Split("`n")[4] ⌨️
        Account Name:           admiral.ackbar
PS C:\users\trebek10\desktop> $evt.Where({$_.Message -like '*obi*'}).Message.Split("`n")[4].Split(":")[1].Split("")[2].Split("\.")[1] ⌨️
ackbar
PS C:\users\trebek10\desktop> $evt.Where({$_.Message -like '*obi*'}).Message.Split("`n")[4].Split(":")[1].Split("")[2].Split("\.")[1].ToLower() + (ls -Exclude '*.evtx').Name.ToLower() ⌨️
ackbar2121 🔐

PS C:\users\trebek10\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek11@groot.underthewire.tech -p 22 ⌨️
trebek11@groot.underthewire.tech's password: ⌨️ ackbar2121

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek11\desktop> whoami ⌨️
underthewire\trebek11
```

## Flag
ackbar2121

## Continue
[Continue](./Trebek1011.md)