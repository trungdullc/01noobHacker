# Century Level 00 → 01 (Get-Host).Version.ToString()

## Previous Flag
```
century1
```

## Goal
The password for Century2 is the build version of the instance of PowerShell installed on this system.

NOTE:<br>
– The format is as follows: **.*.*****.****<br>
– Include all periods<br>
– Be sure to look for build version and NOT PowerShell version

## What I learned
```
Get-Host                                                info about shell instead of the server
Get-CimInstance -ClassName Win32_OperatingSystem        information about the operating system
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century1@century.underthewire.tech -p 22 ⌨️
century1@century.underthewire.tech's password: ⌨️ century1

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

# Practice PS Syntax
# Google: microsoft learn build version of the instance of PowerShell installed on this system 

PS C:\users\century1\desktop> Get-Variable PSVersionTable ⌨️      

Name                           Value
----                           -----
PSVersionTable                 {PSVersion👀, PSEdition, PSCompatibleVersions, BuildVersion👀❤️...}

PS C:\users\century1\desktop> $PSVersionTable ⌨️

Name                           Value
----                           -----
PSVersion                      5.1.14393.8422 👀
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.14393.8422 👀❤️
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1

PS C:\users\century1\desktop> $PSVersionTable.PSVersion ⌨️

Major  Minor  Build  Revision
-----  -----  -----  --------
5      1      14393  8422  

PS C:\users\century1\desktop> $PSVersionTable.PSVersion | Get-Member ⌨️

   TypeName: System.Version

Name          MemberType Definition
----          ---------- ----------
Clone         Method     System.Object Clone(), System.Object ICloneable.Clone()
CompareTo     Method     int CompareTo(System.Object version), int CompareTo(version value), int IComparable.CompareTo(System.Object obj), int ICompara... 
Equals        Method     bool Equals(System.Object obj), bool Equals(version obj), bool IEquatable[version].Equals(version other)
GetHashCode   Method     int GetHashCode()
GetType       Method     type GetType()
ToString      Method     string ToString(), string ToString(int fieldCount) 👀 When use method include () ❤️❤️❤️❤️❤️
Build         Property   int Build {get;}
Major         Property   int Major {get;}
MajorRevision Property   int16 MajorRevision {get;}
Minor         Property   int Minor {get;}
MinorRevision Property   int16 MinorRevision {get;}
Revision      Property   int Revision {get;}

PS C:\users\century1\desktop> $PSVersionTable.PSVersion.ToString() ⌨️
5.1.14393.8422

# Practice PS Syntax
PS C:\users\century1\desktop> Get-Host ⌨️

Name             : ConsoleHost
Version          : 5.1.14393.8422 👀
InstanceId       : 327c947c-8a45-4288-8812-67202b936f84
UI               : System.Management.Automation.Internal.Host.InternalHostUserInterface
CurrentCulture   : en-US
CurrentUICulture : en-US
PrivateData      : Microsoft.PowerShell.ConsoleHost+ConsoleColorProxy
DebuggerEnabled  : True
IsRunspacePushed : False
Runspace         : System.Management.Automation.Runspaces.LocalRunspace

# Note: Need () around Get-Host ❤️❤️❤️❤️❤️
PS C:\users\century1\desktop> (Get-Host).Version.ToString()
5.1.14393.8422

# Method 1:
PS C:\users\century1\desktop> $PSVersionTable.BuildVersion ⌨️    

Major  Minor  Build  Revision
-----  -----  -----  --------
10     0      14393  8422

PS C:\users\century1\desktop> $PSVersionTable.BuildVersion.ToString() ⌨️
10.0.14393.8422 🔐

# Method 2: Worst Way
PS C:\users\century1\desktop> Get-CimInstance -ClassName Win32_OperatingSystem ⌨️

SystemDirectory     Organization BuildNumber RegisteredUser SerialNumber            Version   
---------------     ------------ ----------- -------------- ------------            -------   
C:\Windows\system32 OVH SAS      14393       UTW_Team       00377-60000-00000-AA934 10.0.14393 👀

# Note: Missing some numbers so combine both
PS C:\users\century1\desktop> (Get-CimInstance -ClassName Win32_OperatingSystem).Version
10.0.14393
# Manually Edit
10.0.14393.8422 🔐

PS C:\users\century1\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century2@century.underthewire.tech -p 22 ⌨️
century2@century.underthewire.tech's password: ⌨️ 10.0.14393.8422
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century2\desktop> whoami ⌨️
underthewire\century2
```

## Flag
10.0.14393.8422

## Continue
[Continue](./Century0102.md)