# Trebek Level 02 → 03 Get-WinEvent -Path .\security.evtx -FilterXPath "*[System[(EventID=4624)]] and *[EventData[Data[@Name='TargetUserName'] and (Data='Yoda')]]"

## Previous Flag
```
droid823
```

## Goal
The password for trebek4 is the IP that the user Yoda last logged in from as depicted in the event logs on the desktop PLUS the name of the text file on the user’s desktop.<br>

NOTE: If the IP address is “2.3.3.2” and the file on the desktop is named “bobby”, the password would be “2.3.3.2bobby”

## What I learned
```
Get-WinEvent -Path .\security.evtx -FilterXPath "*[System[(EventID=4624)]] and *[EventData[Data[@Name='TargetUserName'] and (Data='Yoda')]]"
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek3@groot.underthewire.tech -p 22 ⌨️
trebek3@groot.underthewire.tech's password: ⌨️ droid823

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek3\desktop> dir ⌨️

    Directory: C:\users\trebek3\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:46 AM              0 address 👀
-a----        8/30/2018   5:55 AM       99684352 security.evtx

PS C:\users\trebek3\desktop> $evt = Get-WinEvent -Path .\security.evtx -FilterXPath "*[System[(EventID=4624)]] and *[EventData[Data[@Name='TargetUserName'] and (Data='Yoda')]]" ⌨️
PS C:\users\trebek3\desktop> $evt[0].Message.Split("`n") ⌨️
An account was successfully logged on.

Subject:
        Security ID:            S-1-5-18
        Account Name:           TREBEK$
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x3E7

Logon Type:                     10

Impersonation Level:            Impersonation

New Logon:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1155
        Account Name:           yoda
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0xEEB1C
        Logon GUID:             {00000000-0000-0000-0000-000000000000}

Process Information:
        Process ID:             0xf10
        Process Name:           C:\Windows\System32\winlogon.exe

Network Information:
        Workstation Name:       TREBEK
        Source Network Address: 10.30.1.18 👀
        Source Port:            0

Detailed Authentication Information:
        Logon Process:          User32
        Authentication Package: Negotiate
        Transited Services:     -
        Package Name (NTLM only):       -
        Key Length:             0

This event is generated when a logon session is created. It is generated on the computer that was accessed.

The subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.

The logon type field indicates the kind of logon that occurred. The most common types are 2 (interactive) and 3 (network).

The New Logon fields indicate the account for whom the new logon was created, i.e. the account that was logged on.

The network fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.

The impersonation level field indicates the extent to which a process in the logon session can impersonate.

The authentication information fields provide detailed information about this specific logon request.
        - Logon GUID is a unique identifier that can be used to correlate this event with a KDC event.
        - Transited services indicate which intermediate services have participated in this logon request.
        - Package name indicates which sub-protocol was used among the NTLM protocols.
        - Key length indicates the length of the generated session key. This will be 0 if no session key was requested.

PS C:\users\trebek3\desktop> $evt[0].Message.Split("`n")[25].Split(':')[-1] ⌨️
        10.30.1.18
PS C:\users\trebek3\desktop> $evt[0].Message.Split("`n")[25].Split(':')[-1].Split("")[1] ⌨️
10.30.1.18
PS C:\users\trebek3\desktop> $evt[0].Message.Split("`n")[25].Split(':')[-1].Split("")[1] + (ls -Exclude '*.evtx').Name.ToLower() ⌨️
10.30.1.18address 🔐

PS C:\users\trebek3\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek4@groot.underthewire.tech -p 22 ⌨️
trebek4@groot.underthewire.tech's password: ⌨️ 10.30.1.18address

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek4\desktop> whoami ⌨️
underthewire\trebek4
```

## Flag
10.30.1.18address

## Continue
[Continue](./Trebek0304.md)