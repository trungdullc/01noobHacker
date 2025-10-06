# Cyborg Level 13 → 14 Get-CimInstance -ClassName Win32_DCOMApplication -Filter 'AppID like "%59B8AFA0-229E-46D9-B980-DDA2C817EC7E%"' | Select-Object *

## Previous Flag
```
22_days
```

## Goal
The password for cyborg15 is the caption for the DCOM application setting for application ID {59B8AFA0-229E-46D9-B980-DDA2C817EC7E} PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the caption is “dcom” and the file on the desktop is called “_address”, then the password is “dcom_address”.<br>
– The password will be lowercase no matter how it appears on screen.

## What I learned
```
DCOM (Distributed Component Object Model) is a Microsoft technology used to allow software components (applications) to communicate over a network
   Think of it as an extension of COM (Component Object Model) that works locally
   DCOM lets applications on different computers call methods, create objects, and exchange data as if they were running on the same machine
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg14@cyborg.underthewire.tech -p 22 ⌨️
cyborg14@cyborg.underthewire.tech's password: ⌨️ 22_days

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg14\desktop> dir ⌨️

    Directory: C:\users\cyborg14\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _objects 👀

PS C:\users\cyborg14\desktop> Get-CimInstance -ClassName Win32_DCOMApplication -Filter 'AppID like "%59B8AFA0-229E-46D9-B980-DDA2C817EC7E%"' ⌨️

AppID                                  Name     InstallDate
-----                                  ----     -----------
{59B8AFA0-229E-46d9-B980-DDA2C817EC7E} propshts

PS C:\users\cyborg14\desktop> Get-CimInstance -ClassName Win32_DCOMApplication -Filter 'AppID like "%59B8AFA0-229E-46D9-B980-DDA2C817EC7E%"' | Get-Member ⌨️

   TypeName: Microsoft.Management.Infrastructure.CimInstance#root/cimv2/Win32_DCOMApplication

Name                      MemberType  Definition
----                      ----------  ----------
Clone                     Method      System.Object ICloneable.Clone()
Dispose                   Method      void Dispose(), void IDisposable.Dispose()
Equals                    Method      bool Equals(System.Object obj)
GetCimSessionComputerName Method      string GetCimSessionComputerName()
GetCimSessionInstanceId   Method      guid GetCimSessionInstanceId()
GetHashCode               Method      int GetHashCode()
GetObjectData             Method      void GetObjectData(System.Runtime.Serialization.SerializationInfo info, System.Runtime.Serialization.StreamingCon... 
GetType                   Method      type GetType()
ToString                  Method      string ToString()
AppID                     Property    string AppID {get;}
Caption                   Property    string Caption {get;}
Description               Property    string Description {get;}
InstallDate               Property    CimInstance#DateTime InstallDate {get;}
Name                      Property    string Name {get;}
PSComputerName            Property    string PSComputerName {get;}
Status                    Property    string Status {get;}
PSStatus                  PropertySet PSStatus {Name, Status}

PS C:\users\cyborg14\desktop> Get-CimInstance -ClassName Win32_DCOMApplication -Filter 'AppID like "%59B8AFA0-229E-46D9-B980-DDA2C817EC7E%"' | Select-Object * ⌨️

Name                  : propshts
Status                :
Caption               : propshts 👀
Description           : propshts
InstallDate           :
AppID                 : {59B8AFA0-229E-46d9-B980-DDA2C817EC7E}
PSComputerName        :
CimClass              : root/cimv2:Win32_DCOMApplication      
CimInstanceProperties : {Caption, Description, InstallDate, Name...}
CimSystemProperties   : Microsoft.Management.Infrastructure.CimSystemProperties

PS C:\users\cyborg14\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg15@cyborg.underthewire.tech -p 22 ⌨️
cyborg15@cyborg.underthewire.tech's password: ⌨️ propshts_objects

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg15\desktop> whoami ⌨️
underthewire\cyborg15
```

## Flag
propshts_objects

## Continue
[Continue](./Cyborg1415.md)