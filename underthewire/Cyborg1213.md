# Cyborg Level 12 → 13 (Get-DnsServerZoneAging -Name 'underthewire.tech').RefreshInterval.Days

## Previous Flag
```
ywa6_heart
```

## Goal
The password cyborg14 is the number of days the refresh interval is set to for DNS aging for the underthewire.tech zone PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the days are set to “08:00:00:00” and the file on the desktop is called “_tuesday”, then the password is “8_tuesday”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-Member

(Get-DnsServerZoneAging -Name 'underthewire.tech').RefreshInterval.Days
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg13@cyborg.underthewire.tech -p 22 ⌨️
cyborg13@cyborg.underthewire.tech's password: ⌨️ ywa6_heart

Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg13\desktop> dir ⌨️

    Directory: C:\users\cyborg13\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _days 👀

PS C:\users\cyborg13\desktop> Get-Help Get-DnsServerZone ⌨️
PS C:\users\cyborg13\desktop> Get-DnsServerZone -Name "underthewire.tech" | Select-Object Name, RefreshInterval, NoRefreshInterval ⌨️

Name RefreshInterval NoRefreshInterval
---- --------------- -----------------

PS C:\users\cyborg13\desktop> (Get-DnsServerZoneAging -Name 'underthewire.tech').RefreshInterval ⌨️                             

Days              : 22
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 0
Ticks             : 19008000000000
TotalDays         : 22 👀
TotalHours        : 528
TotalMinutes      : 31680
TotalSeconds      : 1900800
TotalMilliseconds : 1900800000

PS C:\users\cyborg13\desktop> (Get-DnsServerZoneAging -Name 'underthewire.tech').RefreshInterval.Days ⌨️
22 👀

PS C:\users\cyborg13\desktop> (Get-DnsServerZoneAging -Name 'underthewire.tech').RefreshInterval | Get-Member ⌨️                    

   TypeName: System.TimeSpan

Name              MemberType Definition
----              ---------- ----------
Add               Method     timespan Add(timespan ts)
CompareTo         Method     int CompareTo(System.Object value), int CompareTo(timespan value), int IComparable.CompareTo(System.Object obj), int IComp... 
Duration          Method     timespan Duration()
Equals            Method     bool Equals(System.Object value), bool Equals(timespan obj), bool IEquatable[timespan].Equals(timespan other)
GetHashCode       Method     int GetHashCode()
GetType           Method     type GetType()
Negate            Method     timespan Negate()
Subtract          Method     timespan Subtract(timespan ts)
ToString          Method     string ToString(), string ToString(string format), string ToString(string format, System.IFormatProvider formatProvider), ... 
Days              Property   int Days {get;} 👀
Hours             Property   int Hours {get;}
Milliseconds      Property   int Milliseconds {get;}
Minutes           Property   int Minutes {get;}
Seconds           Property   int Seconds {get;}
Ticks             Property   long Ticks {get;}
TotalDays         Property   double TotalDays {get;}
TotalHours        Property   double TotalHours {get;}
TotalMilliseconds Property   double TotalMilliseconds {get;}
TotalMinutes      Property   double TotalMinutes {get;}
TotalSeconds      Property   double TotalSeconds {get;}

# Method 2:
PS C:\users\cyborg13\desktop> $aging = Get-DnsServerZoneAging -Name 'underthewire.tech' ⌨️
PS C:\users\cyborg13\desktop> $aging | Get-Member ⌨️

   TypeName: Microsoft.Management.Infrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsServerZoneAging

Name                      MemberType     Definition
----                      ----------     ----------
Clone                     Method         System.Object ICloneable.Clone()
Dispose                   Method         void Dispose(), void IDisposable.Dispose()
Equals                    Method         bool Equals(System.Object obj)
GetCimSessionComputerName Method         string GetCimSessionComputerName()
GetCimSessionInstanceId   Method         guid GetCimSessionInstanceId()
GetHashCode               Method         int GetHashCode()
GetObjectData             Method         void GetObjectData(System.Runtime.Serialization.SerializationInfo info, System.Runtime.Serialization.Streaming... 
GetType                   Method         type GetType()
ToString                  Method         string ToString()
AgingEnabled              Property       bool AgingEnabled {get;set;}
AvailForScavengeTime      Property       CimInstance#DateTime AvailForScavengeTime {get;}
NoRefreshInterval         Property       CimInstance#DateTime NoRefreshInterval {get;set;}
PSComputerName            Property       string PSComputerName {get;}
RefreshInterval           Property       CimInstance#DateTime RefreshInterval {get;set;} 👀
ZoneName                  Property       string ZoneName {get;set;}
ScavengeServers           ScriptProperty System.Net.IPAddress[] ScavengeServers {get=[OutputType([System.Net.IPAddress[]])]...

# see all properties (refresh interval, no-refresh interval)
PS C:\users\cyborg13\desktop> $aging | Get-Member -MemberType Property ⌨️

   TypeName: Microsoft.Management.Infrastructure.CimInstance#root/Microsoft/Windows/DNS/DnsServerZoneAging

Name                 MemberType Definition
----                 ---------- ----------
AgingEnabled         Property   bool AgingEnabled {get;set;}
AvailForScavengeTime Property   CimInstance#DateTime AvailForScavengeTime {get;}
NoRefreshInterval    Property   CimInstance#DateTime NoRefreshInterval {get;set;}
PSComputerName       Property   string PSComputerName {get;}
RefreshInterval      Property   CimInstance#DateTime RefreshInterval {get;set;} 👀
ZoneName             Property   string ZoneName {get;set;}

PS C:\users\cyborg13\desktop> $aging.RefreshInterval.Days ⌨️
22 👀
PS C:\users\cyborg13\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg14@cyborg.underthewire.tech -p 22 ⌨️
cyborg14@cyborg.underthewire.tech's password: ⌨️ 22_days

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg14\desktop> whoami ⌨️
underthewire\cyborg14
```

## Flag
22_days

## Continue
[Continue](./Cyborg1314.md)