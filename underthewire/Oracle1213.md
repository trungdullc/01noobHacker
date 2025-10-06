# Oracle Level 12 → 13 Get-WinEvent -Path .\security.evtx | Where-Object {$_.Message -like '*group*created*'} | Select-Object -ExpandProperty Message

## Previous Flag
```
192.168.2.3
```

## Goal
The password for oracle14 is the name of the user who created the Galaxy security group as depicted in the event logs on the desktop PLUS the name of the text file on the user’s desktop.<br>

NOTE:<br>
– If the user’s name is “randy” and the file on the desktop is named “1234”, the password would be “randy1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-WinEvent -Path .\security.evtx | Where-Object {$_.Message -like '*group*created*'} | Select-Object -ExpandProperty Message
```

## Solution
```
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle13@groot.underthewire.tech -p 22 ⌨️
oracle13@groot.underthewire.tech's password: ⌨️ 192.168.2.3

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle13\desktop> dir ⌨️

    Directory: C:\users\Oracle13\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 88 👀
-a----        8/30/2018   5:52 AM        2166784 security.evtx

PS C:\users\Oracle13\desktop> Get-Command "Get-*Event*" ⌨️

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        Get-NetEventNetworkAdapter                         1.0.0.0    NetEventPacketCapture
Function        Get-NetEventPacketCaptureProvider                  1.0.0.0    NetEventPacketCapture
Function        Get-NetEventProvider                               1.0.0.0    NetEventPacketCapture
Function        Get-NetEventSession                                1.0.0.0    NetEventPacketCapture
Function        Get-NetEventVFPProvider                            1.0.0.0    NetEventPacketCapture
Function        Get-NetEventVmNetworkAdapter                       1.0.0.0    NetEventPacketCapture
Function        Get-NetEventVmSwitch                               1.0.0.0    NetEventPacketCapture
Function        Get-NetEventVmSwitchProvider                       1.0.0.0    NetEventPacketCapture
Function        Get-NetEventWFPCaptureProvider                     1.0.0.0    NetEventPacketCapture
Function        Get-SMServerEvent                                  1.0.0.0    ServerManagerTasks
Cmdlet          Get-Event                                          3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Get-EventLog                                       3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Get-EventSubscriber                                3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Get-WinEvent                                       3.0.0.0    Microsoft.PowerShell.Diagnostics 👀

PS C:\users\Oracle13\desktop> Get-Help Get-WinEvent ⌨️
PS C:\users\Oracle13\desktop> Get-WinEvent -Path .\security.evtx | Where-Object {$_.Message -like '*group*created*'} ⌨️

   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/19/2017 1:18:26 AM          4727 Information      A security-enabled global group was created....
5/19/2017 1:16:17 AM          4727 Information      A security-enabled global group was created....

PS C:\users\Oracle13\desktop> Get-WinEvent -Path .\security.evtx | Where-Object {$_.Message -like '*group*created*'} | Get-Member ⌨️                          

   TypeName: System.Diagnostics.Eventing.Reader.EventLogRecord

Name                 MemberType   Definition
----                 ----------   ----------
Dispose              Method       void Dispose(), void IDisposable.Dispose()
Equals               Method       bool Equals(System.Object obj)
FormatDescription    Method       string FormatDescription(), string FormatDescription(System.Collections.Generic.IEnumerable[System.Object] values)       
GetHashCode          Method       int GetHashCode()
GetPropertyValues    Method       System.Collections.Generic.IList[System.Object] GetPropertyValues(System.Diagnostics.Eventing.Reader.EventLogProperty... 
GetType              Method       type GetType()
ToString             Method       string ToString()
ToXml                Method       string ToXml()
Message              NoteProperty string Message=A security-enabled global group was created....
ActivityId           Property     System.Nullable[guid] ActivityId {get;}
Bookmark             Property     System.Diagnostics.Eventing.Reader.EventBookmark Bookmark {get;}
ContainerLog         Property     string ContainerLog {get;}
Id                   Property     int Id {get;}
Keywords             Property     System.Nullable[long] Keywords {get;}
KeywordsDisplayNames Property     System.Collections.Generic.IEnumerable[string] KeywordsDisplayNames {get;}
Level                Property     System.Nullable[byte] Level {get;}
LevelDisplayName     Property     string LevelDisplayName {get;}
LogName              Property     string LogName {get;}
MachineName          Property     string MachineName {get;}
MatchedQueryIds      Property     System.Collections.Generic.IEnumerable[int] MatchedQueryIds {get;}
Opcode               Property     System.Nullable[int16] Opcode {get;}
OpcodeDisplayName    Property     string OpcodeDisplayName {get;}
ProcessId            Property     System.Nullable[int] ProcessId {get;}
Properties           Property     System.Collections.Generic.IList[System.Diagnostics.Eventing.Reader.EventProperty] Properties {get;}
ProviderId           Property     System.Nullable[guid] ProviderId {get;}
ProviderName         Property     string ProviderName {get;}
Qualifiers           Property     System.Nullable[int] Qualifiers {get;}
RecordId             Property     System.Nullable[long] RecordId {get;}
RelatedActivityId    Property     System.Nullable[guid] RelatedActivityId {get;}
Task                 Property     System.Nullable[int] Task {get;}
TaskDisplayName      Property     string TaskDisplayName {get;}
ThreadId             Property     System.Nullable[int] ThreadId {get;}
TimeCreated          Property     System.Nullable[datetime] TimeCreated {get;}
UserId               Property     System.Security.Principal.SecurityIdentifier UserId {get;}
Version              Property     System.Nullable[byte] Version {get;}

PS C:\users\Oracle13\desktop> Get-WinEvent -Path .\security.evtx | Where-Object {$_.Message -like '*group*created*'} | Select-Object -ExpandProperty Message ⌨️
A security-enabled global group was created.

Subject:
        Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1621
        Account Name:           gamora 👀
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0xBC24FF

New Group:
        Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1626
        Group Name:             Galaxy
        Group Domain:           UNDERTHEWIRE

Attributes:
        SAM Account Name:       Galaxy
        SID History:            -

Additional Information:
        Privileges:             -
A security-enabled global group was created.

Subject:
        Security ID:            S-1-5-21-2268727836-2773903800-2952248001-500
        Account Name:           Administrator
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0xB6B6FE

New Group:
        Security ID:            S-1-5-21-2268727836-2773903800-2952248001-1625
        Group Name:             Guardian
        Group Domain:           UNDERTHEWIRE

Attributes:
        SAM Account Name:       Guardian
        SID History:            -

Additional Information:
        Privileges:             -

PS C:\users\Oracle13\desktop> (((Get-WinEvent -Path .\security.evtx | Where-Object {$_.Message -like '*group*created*'}).Message[0].Split("`n") -match '^\s+Account Name*').Split(':')[1] -replace '\s').ToLower() + (ls -Exclude '*evtx').Name.ToLower() ⌨️
gamora88 🔐

PS C:\users\Oracle13\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle14@groot.underthewire.tech -p 22 ⌨️
oracle14@groot.underthewire.tech's password: ⌨️ gamora88

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle14\desktop> whoami ⌨️
underthewire\oracle14
```

## Flag
gamora88

## Continue
[Continue](./Oracle1314.md)