# Groot Level 07 → 08 Get-NetFirewallRule -Action Block | Where-Object {$_.DisplayName -like '*mysql*'}

## Previous Flag
```
srpapi_home
```

## Goal
The password for groot9 is the description of the firewall rule blocking MySQL PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the description of the rule is “blue” and the file on the desktop is named “_bob”, the password would be “blue_bob”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-NetFirewallRule -Action Block | Where-Object {$_.DisplayName -like '*mysql*'}
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot8@groot.underthewire.tech -p 22 ⌨️
groot8@groot.underthewire.tech's password: ⌨️ srpapi_home

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot8\desktop> dir ⌨️

    Directory: C:\users\Groot8\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 _starlord 👀

PS C:\users\Groot8\desktop> Get-Help Get-NetFirewallRule ⌨️
PS C:\users\Groot8\desktop> Get-NetFirewallRule -Action Block | Where-Object {$_.DisplayName -like '*mysql*'} ⌨️

Name                  : {8ce6b97d-5c1d-4347-a7fd-1792feb42355}
DisplayName           : MySQL
Description           : call_me 👀
DisplayGroup          :
Group                 :
Enabled               : True
Profile               : Any
Platform              : {}
Direction             : Inbound
Action                : Block
EdgeTraversalPolicy   : Block
LooseSourceMapping    : False
LocalOnlyMapping      : False
Owner                 :
PrimaryStatus         : OK
Status                : The rule was parsed successfully from the store. (65536)
EnforcementStatus     : NotApplicable
PolicyStoreSource     : PersistentStore
PolicyStoreSourceType : Local

# Option 1: Using Select-Object
PS C:\users\Groot8\desktop> Get-NetFirewallRule -Action Block | Where-Object {$_.DisplayName -like '*mysql*'} | Select-Object -ExpandProperty Description ⌨️
call_me

# Option 2: Using ForEach-Object
PS C:\users\Groot8\desktop> Get-NetFirewallRule -Action Block | Where-Object {$_.DisplayName -like '*mysql*'} | ForEach-Object { $_.Description } ⌨️
call_me

# Option 3: Access property directly (if only one object)
PS C:\users\Groot8\desktop> (Get-NetFirewallRule -Action Block | Where-Object { $_.DisplayName -like '*mysql*' }).Description ⌨️
call_me

PS C:\users\Groot8\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot9@groot.underthewire.tech -p 22 ⌨️
groot9@groot.underthewire.tech's password: ⌨️ call_me_starlord

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot9\desktop> whoami ⌨️
underthewire\groot9
```

## Flag
call_me_starlord

## Continue
[Continue](./Groot0809.md)