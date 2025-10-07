# Trebek Level 11 → 12 -FilterXPath "*[System[EventID=4720]]", .Where({$_.Message -like '*Lor*'}).Message

## Previous Flag
```
general.hux100
```

## Goal
The password for trebek13 is the username of the user who created the user Lor San Tekka as depicted in the event logs on the desktop PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the username is “john.doe” and the file on the desktop is named “1234”, the password would be “john.doe1234”<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
ChatGPT instead of Microsoft Learn: 
The Windows Security event ID that means “a user account was created” is 4720.

(Useful related IDs: 4722 = account enabled, 4726 = account deleted, 4723/4724 = password change/reset attempts.)
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek12@groot.underthewire.tech -p 22 ⌨️
trebek12@groot.underthewire.tech's password: ⌨️general.hux100

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek12\desktop> dir ⌨️

    Directory: C:\users\trebek12\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:49 AM              0 53 👀
-a----        8/30/2018   5:55 AM       99684352 security.evtx

PS C:\users\trebek12\desktop> $evt = Get-WinEvent -Path .\security.evtx -FilterXPath "*[System[EventID=4720]]" ⌨️
PS C:\users\trebek12\desktop> Get-Variable evt ⌨️

Name                           Value
----                           -----
evt                            {System.Diagnostics.Eventing.Reader.EventLogRecord, System.Diagnostics.Eventing.Reader.EventLogRecord, System.Diagnostic...

PS C:\users\trebek12\desktop> $evt.Count ⌨️
53
PS C:\users\trebek12\desktop> $evt | Select-Object -First 10 ⌨️

   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/11/2017 8:36:51 PM          4720 Information      A user account was created....
5/11/2017 6:56:12 PM          4720 Information      A user account was created....
5/11/2017 6:46:25 PM          4720 Information      A user account was created....
5/11/2017 6:26:08 PM          4720 Information      A user account was created....
5/11/2017 6:19:39 PM          4720 Information      A user account was created....
5/11/2017 6:15:55 PM          4720 Information      A user account was created....
5/10/2017 11:29:12 AM         4720 Information      A user account was created....
5/10/2017 11:28:43 AM         4720 Information      A user account was created....
5/10/2017 11:28:15 AM         4720 Information      A user account was created....
5/10/2017 11:27:47 AM         4720 Information      A user account was created....

PS C:\users\trebek12\desktop> $evt.Where({$_.Message -like '*Lor*'}) ⌨️

   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/11/2017 6:19:39 PM          4720 Information      A user account was created....

PS C:\users\trebek12\desktop> $evt.Where({$_.Message -like '*Lor*'}).Message ⌨️
A user account was created.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1150
        Account Name:           poe.dameron 👀
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x1235812

New Account:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1151
        Account Name:           lor.tekka
        Account Domain:         UNDERTHEWIRE

Attributes:
        SAM Account Name:       lor.tekka
        Display Name:           Tekka, Lor San
        User Principal Name:    lor.tekka@underthewire.tech
        Home Directory:         -
        Home Drive:             -
        Script Path:            -
        Profile Path:           -
        User Workstations:      -
        Password Last Set:      <never>
        Account Expires:                <never>
        Primary Group ID:       513
        Allowed To Delegate To: -
        Old UAC Value:          0x0
        New UAC Value:          0x15
        User Account Control:
                Account Disabled
                'Password Not Required' - Enabled
                'Normal Account' - Enabled
        User Parameters:        -
        SID History:            -
        Logon Hours:            <value not set>

Additional Information:
        Privileges              -

PS C:\users\trebek12\desktop> $evt.Where({$_.Message -like '*Lor*'}).Message.Split("`n")[4] ⌨️
        Account Name:           poe.dameron
PS C:\users\trebek12\desktop> $evt.Where({$_.Message -like '*Lor*'}).Message.Split("`n")[4].Split("")[4].ToLower() + (ls -Exclude '*.evtx').Name.ToLower() ⌨️
poe.dameron53 🔐

PS C:\users\trebek12\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek13@groot.underthewire.tech -p 22 ⌨️
trebek13@groot.underthewire.tech's password: ⌨️ poe.dameron53

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek13\desktop> whoami ⌨️
underthewire\trebek13
```

## Flag
poe.dameron53

## Continue
[Continue](./Trebek1213.md)