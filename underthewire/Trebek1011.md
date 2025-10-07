# Trebek Level 10 → 11 Property

## Previous Flag
```
ackbar2121
```

## Goal
The password for trebek12 is the username of the user who was created on 11 May 17 at 26 minutes after the hour, as depicted in the event logs on the desktop PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the username is “john.doe” and the file on the desktop is named “1234”, the password would be “john.doe1234”<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Microsoft Learn: 4720(S) A user account was created. - Windows 10

Property can be used with . after variable name
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek11@groot.underthewire.tech -p 22 ⌨️
trebek11@groot.underthewire.tech's password: ⌨️ ackbar2121

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek11\desktop> dir ⌨️

    Directory: C:\users\trebek11\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:49 AM              0 100 👀
-a----        8/30/2018   5:55 AM       99684352 security.evtx

PS C:\users\trebek11\desktop> Get-Command "Get-*Event*" ⌨️

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

PS C:\users\trebek11\desktop> Get-Help Get-WinEvent ⌨️
PS C:\users\trebek11\desktop> $evt = Get-WinEvent -Path .\security.evtx -FilterXPath "*[System[EventID=4720]]" ⌨️
PS C:\users\trebek11\desktop> $evt.Count ⌨️
53
PS C:\users\trebek11\desktop> $evt | Select-Object -First 10 ⌨️

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

PS C:\users\trebek11\desktop> $evt | Get-Member "Time*" ⌨️

   TypeName: System.Diagnostics.Eventing.Reader.EventLogRecord     

Name        MemberType Definition
----        ---------- ----------
TimeCreated Property   System.Nullable[datetime] TimeCreated {get;}

PS C:\users\trebek11\desktop> $evt.TimeCreated | Get-Member ⌨️

   TypeName: System.DateTime

Name                 MemberType     Definition
----                 ----------     ----------
Add                  Method         datetime Add(timespan value)
AddDays              Method         datetime AddDays(double value)
AddHours             Method         datetime AddHours(double value)
AddMilliseconds      Method         datetime AddMilliseconds(double value)
AddMinutes           Method         datetime AddMinutes(double value)
AddMonths            Method         datetime AddMonths(int months)
AddSeconds           Method         datetime AddSeconds(double value)
AddTicks             Method         datetime AddTicks(long value)
AddYears             Method         datetime AddYears(int value)
CompareTo            Method         int CompareTo(System.Object value), int CompareTo(datetime value), int IComparable.CompareTo(System.Object obj), in... 
Equals               Method         bool Equals(System.Object value), bool Equals(datetime value), bool IEquatable[datetime].Equals(datetime other)        
GetDateTimeFormats   Method         string[] GetDateTimeFormats(), string[] GetDateTimeFormats(System.IFormatProvider provider), string[] GetDateTimeFo... 
GetHashCode          Method         int GetHashCode()
GetObjectData        Method         void ISerializable.GetObjectData(System.Runtime.Serialization.SerializationInfo info, System.Runtime.Serialization.... 
GetType              Method         type GetType()
GetTypeCode          Method         System.TypeCode GetTypeCode(), System.TypeCode IConvertible.GetTypeCode()
IsDaylightSavingTime Method         bool IsDaylightSavingTime()
Subtract             Method         timespan Subtract(datetime value), datetime Subtract(timespan value)
ToBinary             Method         long ToBinary()
ToBoolean            Method         bool IConvertible.ToBoolean(System.IFormatProvider provider)
ToByte               Method         byte IConvertible.ToByte(System.IFormatProvider provider)
ToChar               Method         char IConvertible.ToChar(System.IFormatProvider provider)
ToDateTime           Method         datetime IConvertible.ToDateTime(System.IFormatProvider provider)
ToDecimal            Method         decimal IConvertible.ToDecimal(System.IFormatProvider provider)
ToDouble             Method         double IConvertible.ToDouble(System.IFormatProvider provider)
ToFileTime           Method         long ToFileTime()
ToFileTimeUtc        Method         long ToFileTimeUtc()
ToInt16              Method         int16 IConvertible.ToInt16(System.IFormatProvider provider)
ToInt32              Method         int IConvertible.ToInt32(System.IFormatProvider provider)
ToInt64              Method         long IConvertible.ToInt64(System.IFormatProvider provider)
ToLocalTime          Method         datetime ToLocalTime()
ToLongDateString     Method         string ToLongDateString()
ToLongTimeString     Method         string ToLongTimeString()
ToOADate             Method         double ToOADate()
ToSByte              Method         sbyte IConvertible.ToSByte(System.IFormatProvider provider)
ToShortDateString    Method         string ToShortDateString()
ToShortTimeString    Method         string ToShortTimeString()
ToSingle             Method         float IConvertible.ToSingle(System.IFormatProvider provider)
ToString             Method         string ToString(), string ToString(string format), string ToString(System.IFormatProvider provider), string ToStrin... 
ToType               Method         System.Object IConvertible.ToType(type conversionType, System.IFormatProvider provider)
ToUInt16             Method         uint16 IConvertible.ToUInt16(System.IFormatProvider provider)
ToUInt32             Method         uint32 IConvertible.ToUInt32(System.IFormatProvider provider)
ToUInt64             Method         uint64 IConvertible.ToUInt64(System.IFormatProvider provider)
ToUniversalTime      Method         datetime ToUniversalTime()
Date                 Property       datetime Date {get;}
Day                  Property       int Day {get;}
DayOfWeek            Property       System.DayOfWeek DayOfWeek {get;}
DayOfYear            Property       int DayOfYear {get;}
Hour                 Property       int Hour {get;}
Kind                 Property       System.DateTimeKind Kind {get;}
Millisecond          Property       int Millisecond {get;}
Minute               Property       int Minute {get;}
Month                Property       int Month {get;}
Second               Property       int Second {get;}
Ticks                Property       long Ticks {get;}
TimeOfDay            Property       timespan TimeOfDay {get;}
Year                 Property       int Year {get;}
DateTime             ScriptProperty System.Object DateTime {get=if ((& { Set-StrictMode -Version 1; $this.DisplayHint }) -ieq  "Date")...

PS C:\users\trebek11\desktop> $evt[0].TimeCreated.Month ⌨️
5
PS C:\users\trebek11\desktop> $evt[0].TimeCreated.Day ⌨️
11
PS C:\users\trebek11\desktop> $evt[0].TimeCreated.Second ⌨️
51
PS C:\users\trebek11\desktop> $evt.Where({$_.TimeCreated.Day -eq 11 -and $_.TimeCreated.Minute -eq 26}) ⌨️

   ProviderName: Microsoft-Windows-Security-Auditing

TimeCreated                     Id LevelDisplayName Message
-----------                     -- ---------------- -------
5/11/2017 6:26:08 PM          4720 Information      A user account was created....

PS C:\users\trebek11\desktop> $evt.Where({$_.TimeCreated.Day -eq 11 -and $_.TimeCreated.Minute -eq 26}).Message ⌨️
A user account was created.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1150
        Account Name:           poe.dameron
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x1235812

New Account:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1152
        Account Name:           general.hux 👀
        Account Domain:         UNDERTHEWIRE

Attributes:
        SAM Account Name:       general.hux
        Display Name:           Hux, General
        User Principal Name:    general.hux@underthewire.tech
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

PS C:\users\trebek11\desktop> $evt.Where({$_.TimeCreated.Day -eq 11 -and $_.TimeCreated.Minute -eq 26}).Message.Split("`n")[10].Split("")[4] ⌨️
general.hux
PS C:\users\trebek11\desktop> $evt.Where({$_.TimeCreated.Day -eq 11 -and $_.TimeCreated.Minute -eq 26}).Message.Split("`n")[10].Split("")[4].ToLower() + (ls -Exclude '*.evtx').Name.ToLower() ⌨️
general.hux100 🔐

PS C:\users\trebek11\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek12@groot.underthewire.tech -p 22 ⌨️
trebek12@groot.underthewire.tech's password: ⌨️general.hux100

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek12\desktop> whoami ⌨️
underthewire\trebek12
```

## Flag
general.hux100

## Continue
[Continue](./Trebek1112.md)