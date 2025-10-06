# Oracle Level 00 → 01 (Get-TimeZone).Id.ToLower()

## Previous Flag
```
oracle1
```

## Goal
The password for oracle2 is the timezone in which this system is set to.<br>

NOTE:<br>
– The password is the abbreviation of the timezone. For example, if it is listed as being in the Eastern timezone, the answer is est.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
(Get-TimeZone).Id.ToLower()
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle1@groot.underthewire.tech -p 22 ⌨️
oracle1@groot.underthewire.tech's password: ⌨️ oracle1

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle1\desktop> Get-Help Get-TimeZone ⌨️
PS C:\users\Oracle1\desktop> Get-TimeZone ⌨️

Id                         : UTC 👀
DisplayName                : (UTC) Coordinated Universal Time
StandardName               : Coordinated Universal Time
DaylightName               : Coordinated Universal Time
BaseUtcOffset              : 00:00:00
SupportsDaylightSavingTime : False

PS C:\users\Oracle1\desktop> (Get-TimeZone).Id.ToLower() ⌨️
utc

PS C:\users\Oracle1\desktop> Get-TimeZone | Get-Member

   TypeName: System.TimeZoneInfo

Name                       MemberType Definition
----                       ---------- ----------
Equals                     Method     bool Equals(System.TimeZoneInfo other), bool Equals(System.Object obj), bool IEquatable[TimeZoneInfo].Equals(Syst... 
GetAdjustmentRules         Method     System.TimeZoneInfo+AdjustmentRule[] GetAdjustmentRules()
GetAmbiguousTimeOffsets    Method     timespan[] GetAmbiguousTimeOffsets(System.DateTimeOffset dateTimeOffset), timespan[] GetAmbiguousTimeOffsets(date...
GetHashCode                Method     int GetHashCode()
GetObjectData              Method     void ISerializable.GetObjectData(System.Runtime.Serialization.SerializationInfo info, System.Runtime.Serializatio... 
GetType                    Method     type GetType()
GetUtcOffset               Method     timespan GetUtcOffset(System.DateTimeOffset dateTimeOffset), timespan GetUtcOffset(datetime dateTime)
HasSameRules               Method     bool HasSameRules(System.TimeZoneInfo other)
IsAmbiguousTime            Method     bool IsAmbiguousTime(System.DateTimeOffset dateTimeOffset), bool IsAmbiguousTime(datetime dateTime)
IsDaylightSavingTime       Method     bool IsDaylightSavingTime(System.DateTimeOffset dateTimeOffset), bool IsDaylightSavingTime(datetime dateTime)        
IsInvalidTime              Method     bool IsInvalidTime(datetime dateTime)
OnDeserialization          Method     void IDeserializationCallback.OnDeserialization(System.Object sender)
ToSerializedString         Method     string ToSerializedString()
ToString                   Method     string ToString()
BaseUtcOffset              Property   timespan BaseUtcOffset {get;}
DaylightName               Property   string DaylightName {get;}
DisplayName                Property   string DisplayName {get;}
Id                         Property   string Id {get;} 👀
StandardName               Property   string StandardName {get;}
SupportsDaylightSavingTime Property   bool SupportsDaylightSavingTime {get;}

PS C:\users\Oracle1\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle2@groot.underthewire.tech -p 22 ⌨️
oracle2@groot.underthewire.tech's password: ⌨️ utc

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle2\desktop> whoami ⌨️
underthewire\oracle2
```

## Flag
utc

## Continue
[Continue](./Oracle0102.md)