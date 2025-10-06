# Oracle Level 06 → 07 Get-Command Get-ADTrust -Syntax, Get-ADTrust -Filter *

## Previous Flag
```
t-50_97
```

## Goal
The password for oracle8 is the name of the domain that a trust is built with PLUS the name of the file on the user’s desktop.<br>

NOTE:<br>
– The password will be lowercase no matter how it appears on the screen.<br>
– If the name of the trust is “blob” and the file on the desktop is named “1234”, the password would be “blob1234”.

## What I learned
```
Get-ADTrust -Filter *

Difference between a flag (parameter) and a property (output field)
    # See all available parameters
    Get-Command Get-ADTrust -Syntax

    # Properties are values of the object returned after the command runs
    Get-ADTrust -Filter * | Select-Object Name, Direction, TrustType
    Get-ADTrust -Filter * | Get-Member -MemberType Property
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle7@groot.underthewire.tech -p 22 ⌨️
oracle7@groot.underthewire.tech's password: ⌨️ t-50_97

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle7\desktop> dir ⌨️

    Directory: C:\users\Oracle7\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:50 AM              0 111 👀

PS C:\users\Oracle7\desktop> Get-Help Get-ADTrust ⌨️
PS C:\users\Oracle7\desktop> Get-Command Get-ADTrust -Syntax ⌨️❤️❤️❤️❤️❤️

Get-ADTrust -Filter <string>👀 [-AuthType <ADAuthType>] [-Credential <pscredential>] [-Properties <string[]>] [-Server <string>] [<CommonParameters>]     

Get-ADTrust [-Identity] <ADTrust> [-AuthType <ADAuthType>] [-Credential <pscredential>] [-Properties <string[]>] [-Server <string>] [<CommonParameters>]

Get-ADTrust -InputObject <Object> [-AuthType <ADAuthType>] [-Credential <pscredential>] [-Properties <string[]>] [-Server <string>] [<CommonParameters>]

Get-ADTrust -LDAPFilter <string> [-AuthType <ADAuthType>] [-Credential <pscredential>] [-Properties <string[]>] [-Server <string>] [<CommonParameters>] 

PS C:\users\Oracle7\desktop> Get-ADTrust -Filter * ⌨️

Direction               : Outbound
DisallowTransivity      : True
DistinguishedName       : CN=multiverse,CN=System,DC=underthewire,DC=tech
ForestTransitive        : False
IntraForest             : False
IsTreeParent            : False
IsTreeRoot              : False
Name                    : multiverse 👀
ObjectClass             : trustedDomain
ObjectGUID              : bbfcc0ca-e586-4058-9aef-c6b4a6b32708
SelectiveAuthentication : False
SIDFilteringForestAware : False
SIDFilteringQuarantined : False
Source                  : DC=underthewire,DC=tech
Target                  : multiverse
TGTDelegation           : False
TrustAttributes         : 1
TrustedPolicy           :
TrustingPolicy          :
TrustType               : MIT
UplevelOnly             : False
UsesAESKeys             : False
UsesRC4Encryption       : False

PS C:\users\Oracle7\desktop> (Get-ADTrust -Filter *).Name.ToLower() + (dir -File).Name.ToLower() ⌨️
multiverse111 🔐

PS C:\users\Oracle7\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle8@groot.underthewire.tech -p 22 ⌨️
oracle8@groot.underthewire.tech's password: ⌨️ multiverse111

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle8\desktop> whoami ⌨️
underthewire\oracle8
```

## Flag
multiverse111

## Continue
[Continue](./Oracle0708.md)