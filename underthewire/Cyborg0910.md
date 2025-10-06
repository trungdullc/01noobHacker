# Cyborg Level 09 → 10 Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections

## Previous Flag
```
onita99
```

## Goal
The password for cyborg11 is the description of the Applocker Executable deny policy for ill_be_back.exe PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the description is “green$” and the file on the desktop is called “28”, then the password is “green$28”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
AppLocker Executable Deny Policy is a Windows security control that blocks a program from running based on rules set by an administrator

Get-AppLockerPolicy -Effective -Xml
    Get-AppLockerPolicy → PowerShell cmdlet that retrieves AppLocker rules (security policies that allow/deny apps)
    -Effective → This tells it to return the currently enforced policy on the system (what’s being applied at runtime)
    -Xml → Outputs the policy in XML format (raw policy definition)
    Outputs a policy object containing all AppLocker rule collections (EXE, DLL, MSI, Script, Appx)
Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections 
    Select-Object → A cmdlet to select specific properties from objects
    -ExpandProperty RuleCollections → Instead of showing the RuleCollections property as a nested object, it expands it directly so you can see all the collections in detail (like Executable rules, Script rules)
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg10@cyborg.underthewire.tech -p 22 ⌨️
cyborg10@cyborg.underthewire.tech's password: ⌨️ onita99

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg10\desktop> dir ⌨️

    Directory: C:\users\cyborg10\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 99

# Dumps currently enforced AppLocker rules in XML format.
PS C:\users\cyborg10\desktop> Get-AppLockerPolicy -Effective -Xml ⌨️
<AppLockerPolicy Version="1"><RuleCollection Type="Appx" EnforcementMode="NotConfigured" /><RuleCollection Type="Dll" EnforcementMode="NotConfigured" /><RuleCollection Type="Exe" EnforcementMode="NotConfigured"><FilePathRule Id="cf7f9744-e5de-4189-8499-236666a32796" Name="C:\Users\cyborg10\Documents\ill_be_back.exe" Description="terminated!"👀 UserOrGroupSid="S-1-1-0" Action="Deny"><Conditions><FilePathCondition Path="C:\Users\cyborg10\Documents\ill_be_back.exe" 
/></Conditions></FilePathRule></RuleCollection><RuleCollection Type="Msi" EnforcementMode="NotConfigured" /><RuleCollection Type="Script" EnforcementMode="NotConfigured" /></AppLockerPolicy>

PS C:\users\cyborg10\desktop> Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections ⌨️

PathConditions      : {C:\Users\cyborg10\Documents\ill_be_back.exe}
PathExceptions      : {}
PublisherExceptions : {}
HashExceptions      : {}
Id                  : cf7f9744-e5de-4189-8499-236666a32796
Name                : C:\Users\cyborg10\Documents\ill_be_back.exe
Description         : terminated! 👀
UserOrGroupSid      : S-1-1-0
Action              : Deny

PS C:\users\cyborg10\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg11@cyborg.underthewire.tech -p 22 ⌨️
cyborg11@cyborg.underthewire.tech's password: ⌨️ terminated!99

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg11\desktop> whoami ⌨️
underthewire\cyborg11
```

## Flag
terminated!99

## Continue
[Continue](./Cyborg1011.md)