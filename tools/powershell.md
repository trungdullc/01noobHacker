# PowerShell

```
Description: PowerShell different than bash

https://overthewire.org/wargames/

# Note: PS variable need $ in front or thinks it a command
In PowerShell, $_ is a special automatic variable used inside a pipeline
    It represents the current object being passed down the pipeline (this->)

% is wildcard

PS> $PSVersionTable.PSVersion
    Major  Minor  Build  Revision
    -----  -----  -----  --------
    5      1      14393  8422

YouTube Tutorials:
    https://www.youtube.com/watch?v=ZOoCaWyifmI
    https://www.youtube.com/watch?v=vI1i8Tb3IXI&list=PLKHIhZJiQ5Akf3P2e4Tik18n9g1UKApSL&pp=0gcJCaIEOCosWNin
    https://www.youtube.com/watch?v=UVUd9_k9C6A&pp=ygUWcG93ZXJzaGVsbCBmdWxsIGNvdXJzZQ%3D%3D
    https://www.youtube.com/watch?v=K4YDHFalAK8&pp=ygUWcG93ZXJzaGVsbCBmdWxsIGNvdXJzZQ%3D%3D
    https://www.youtube.com/watch?v=SmHpKgKashg&pp=ygUWcG93ZXJzaGVsbCBmdWxsIGNvdXJzZdIHCQn7CQGHKiGM7w%3D%3D
```

## Side Quest: PowerShell cmdlets (VERB-NOUN) ❤️❤️❤️
```
Basic Cmdlets
    Get-Help <cmdlet> -Full             Shows help for cmdlets, Get-Help Get-Process
    Get-Command	                        Lists available cmdlets, functions, and aliases
    Get-Member	                        Shows properties and methods of objects
    Get-ChildItem                                       (ls, dir) List files in current directory
    Get-ChildItem -Path . -Recurse -Filter *.txt        List all .txt files recursively
    Get-ChildItem | Where-Object { $_.Length -gt 1MB }  List files with size > 1MB
    Set-Location                        (cd) Changes current directory
    Get-Content                         (cat, type)	Reads file content
    Set-Content	                        Writes content to a file
    Clear-Host                          (cls) Clears the console

Process & System Management
    Get-Process	                        Lists running processes
    Stop-Process	                    Terminates a process
    Start-Process	                    Starts a new process
    Get-Service	                        Lists services and status
    Start-Service / Stop-Service	    Control Windows services
    Get-EventLog	                    Reads event logs
    Get-WmiObject / Get-CimInstance	    Query WMI/CIM objects (hardware, OS info)

File & Text Handling
    Copy-Item	                        Copy files/folders
    Move-Item	                        Move files/folders
    Remove-Item (rm, del)	            Delete files/folders
    Select-String	                    Search text in files (like grep)
    Measure-Object	                    Count or sum objects (lines, words, etc.)
    Out-File	                        Redirect output to a file
    Format-Table / Format-List	        Format output nicely

Networking / DNS
    Test-Connection                     Ping a host
    Resolve-DnsName                     Resolve DNS names (like nslookup)
    Get-NetIPAddress	                Show IP configuration
    Get-NetRoute	                    Show routing table

Active Directory (RSAT module)
    Get-ADUser	                                Get AD user objects
    Get-ADGroup	                                Get AD groups
    Get-ADGroupMember	                        List members of an AD group
    Get-ADComputer	                            List AD computers
    New-ADUser / Set-ADUser / Remove-ADUser	    Manage AD users
    New-ADGroup / Set-ADGroup / Remove-ADGroup	Manage AD groups

Objects & Pipelines
    Where-Object	                            Filter objects (Where-Object {$_.Name -like "*test*"})
    ForEach-Object	                            Iterate over objects
    Sort-Object	                                Sort objects
    Select-Object	                            Choose object properties
    Group-Object	                            Group objects by property
```

## SideQuest: Powershell common "post-pipeline" operations ❤️❤️❤️❤️❤️
```
Exploration / Inspection
    Get-Member	        Shows all properties and methods of the objects flowing through the pipeline
                        This is like peeking inside the object’s “class definition.”
    Select-Object *	    Expands and displays all properties of the object. (By default, PowerShell often shows only a few.)
    Format-List *	    Formats and lists all properties in a vertical list instead of a table
    Format-Table	    Displays objects in a table; you can pick properties (Format-Table Name, Status)
    Out-GridView	    Opens results in an interactive grid window (GUI)
Filtering
    Where-Object { $_.Property -eq "Value" }	Filters objects based on a condition. $_ means “the current object in the pipeline.”
    Select-String "pattern"	                    Filters text streams (works like grep). Returns lines containing the pattern
    ? { ... }	                                Alias for Where-Object
Projection / Picking
    Select-Object Property1, Property2	    Picks specific properties
    Select-Object -First 5	                Takes only the first N objects
    Select-Object -Last 5	                Takes the last N objects
    Select-Object -Unique	                Removes duplicates
Sorting & Grouping
    Sort-Object Property	Sorts by property
    Group-Object Property	Groups objects by property value and shows counts
    Measure-Object	        Counts objects or measures numeric properties (min, max, avg)
Output / Export
    Out-File file.txt	    Writes pipeline results to a text file
    Export-Csv file.csv	    Saves objects into CSV format
    ConvertTo-Json	        Converts objects to JSON
    ConvertTo-Html	        Makes HTML table output

# Examples
# 1. Inspect what properties a service object has
Get-Service | Get-Member

# 2. Show all properties of the first service
Get-Service | Select-Object -First 1 | Format-List *

# 3. Filter services that are running
Get-Service | Where-Object { $_.Status -eq 'Running' }

# 4. Sort running services by DisplayName
Get-Service | Where-Object Status -eq Running | Sort-Object DisplayName

# 5. Count how many services are running
Get-Service | Where-Object Status -eq Running | Measure-Object
```

## Side Quest: Power Shell Operators ❤️❤️❤️❤️❤️
```
Array/String Operators
    # -join → joins elements of an array into one string
    -join (1,2,3)                       # "123"
    (1,2,3) -join ","                   # "1,2,3"

    # -split → splits a string into an array
    "a,b,c" -split ","                  # "a","b","c"

    # -replace → regex replace
    "hello123" -replace "\d",""         # "hello"

    # -match / -notmatch` → regex pattern test
    "hello123" -match "\d"              # True

    # -like / -notlike → wildcard test (* and ?)
    "file.txt" -like "*.txt"            # True

Comparison Operators
    # -eq / -ne → equal / not equal
    # -gt / -lt / -ge / -le → greater/less (than/equal)
    5 -gt 3                             # True
    "a" -eq "a"                         # True

Type/Null Operators
    # -is / -isnot → test type
    "hello" -is [string]   # True

    # -contains / -notcontains → test if a collection contains a value
    1..5 -contains 3                    # True

    # -in / -notin → reverse contains
    3 -in (1,2,3,4)                     # True

Redirection / Output Operators
    # > → overwrite file
    # >> → append to file
    # | → pipeline operator (send output to next command)
    #.. → range operator
    1..5                                # 1,2,3,4,5

Logical Operators
    # -and / -or / -not → boolean logic
    ($true -and $false)                 # False
```

## Side Quest: Du's Investigation
```
# When Declare variables don't forget $ in front or acts as a command ⭐⭐⭐⭐⭐
$var="hi"

# Important: When using Property don't forget (). ⭐⭐⭐⭐⭐
Get-Help Get-ChildItem ❤️❤️❤️❤️❤️             # short summary + parameters
Get-Help Get-ChildItem -Examples                # examples only
Get-Help Get-ChildItem -Full                    # full help
Get-Help Get-ChildItem -Online                  # open official docs in browser (if available)

# Note: * multiple wild card, ? one char wild card
# Select-Object gets the column
Get-Alias ls ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐
Get-Variable ls ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐
Get-Command "Get-*Event*" ❤️❤️❤️❤️❤️
Get-Command ls | Select-Object Name, CommandType, Definition, Module ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐
Get-Command Get-ChildItem -Syntax ❤️❤️❤️❤️❤️
ls | Get-Member ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐

# -match (RE) vs -like (wild cards * and ?) vs -eq (no Regular Expression)
# Note: When using Where-Object need use {}
# $_. is current object
| Where-Object {$_.Message -like '*group*created*'}
| Select-Object -ExpandProperty
Get-ChildItem -File -Recurse | Where-Object { $_.Name -match '^readme' }

Get-ADUser -Filter * -Properties * | Select-Object -First 1 | Format-List *
    Get-ADUser
    Get-ADComputer
    Get-ADTrust
    Get-ADGroup

# -split
((Get-WmiObject Win32_ComputerSystem).Domain -split '\.')[0]
# -join
-join((Get-CimInstance win32_service -Filter 'DisplayName like "Windows Update"').Description.Split(' ')[9,7].ToLower() + (ls -File).Name)

+ (ls -Exclude '*.evtx').Name.ToLower()
(Get-Content .\unique.txt | Sort-Object -Unique).Count
Get-Content .\Downloads\Readme.txt
(cat .\Word_File.txt) -split ' ' | Select-Object -Index 160
(Get-Content Word_File.txt) -replace '^(\S+\s+){160}'
```

## CTF
[century0000: ssh century1@century.underthewire.tech -p 22](../underthewire/Century0000.md)<br>
[century0001: (Get-Host).Version.ToString(), Get-CimInstance -ClassName Win32_OperatingSystem](../underthewire/Century0001.md)<br>
[century0405: Get-WmiObject Win32_ComputerSystem](../underthewire/Century0405.md)<br>
[century0102: dir, Invoke-Webrequest ❤️❤️❤️❤️](../underthewire/Century0102.md)<br>
[century0203: (Get-ChildItem -File).Count](../underthewire/Century0203.md)<br>
[century0304: | Where-Object {$_.Directory.Name -like '* *'} ❤️❤️❤️❤️](../underthewire/Century0304.md)<br>
[century0506: (Get-ChildItem -Directory).Count](../underthewire/Century0506.md)<br>
[century0607: Get-ChildItem -Recurse -File -Filter "readme*" , Get-Content](../underthewire/Century0607.md)<br>
[century0708: (Get-Content unique.txt | Sort-Object | Group-Object | Where-Object { $_.Count -eq 1 } | ForEach-Object { $_.Name }).Count](../underthewire/Century0708.md)<br>
[century0809: (Get-Content Word_File.txt) -replace '^(\S+\s+){160}'](../underthewire/Century0809.md)<br>
[century1011: Get-ChildItem -Recurse -Hidden -Exclude "desktop.ini" 2>$null](../underthewire/Century1011.md)<br>
[century1112: Get-ADDomainController, Get-ADComputer -Identity "UTW" -Properties *](../underthewire/Century1112.md)<br>
[century1314: (Get-Content countpolos -Raw) -split '\b' | Where-Object {$_ -eq 'polo'} | Measure-Object | Select -Expand Count](../underthewire/Century1314.md)<br>
[cyborg0001: Get-Module -ListAvailable, Get-ADUser -Identity chris.rogers -Properties * | Format-List](../underthewire/Cyborg0001.md)<br>
[cyborg0102: Resolve-DnsName](../underthewire/Cyborg0102.md)<br>
[cyborg0203: (Get-ADGroup -Filter 'Name -like "Cyborg"' | Get-ADGroupMember).Count](../underthewire/Cyborg0203.md)<br>
[cyborg0304: Get-Module -ListAvailable | Where-Object { $_.Version -eq "8.9.8.9" }](../underthewire/Cyborg0304.md)<br>
[cyborg0405: variable= ❤️❤️❤️](../underthewire/Cyborg0405.md)<br>
[cyborg0506: [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String("YwB5AGIAZQByAGcAZQBkAGQAbwBuAA==")), custom fx ❤️❤️❤️❤️❤️](../underthewire/Cyborg0506.md)<br>
[cyborg0607: Get-CimInstance Win32_StartupCommand](../underthewire/Cyborg0607.md)<br>
[cyborg0708: Get-Content -Path "1_qs5nwlcl7f_-SwNlQvOrAw.png" -Stream Zone.Identifier](../underthewire/Cyborg0708.md)<br>
[cyborg0809: Get-ADUser -Filter * -Properties * | Select-Object GivenName, *Phone | Select-String '876-5309'](../underthewire/Cyborg0809.md)<br>
[cyborg0910: Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections](../underthewire/Cyborg0910.md)<br>
[cyborg1011: Get-Content C:\inetpub\logs\logfiles\w3svc1\u_ex160413.log | Where-Object { $_ -notlike '*mozilla*' -and $_ -notlike '*opera*' }](../underthewire/Cyborg1011.md)<br>
[cyborg1112: Base64-Unicode](../underthewire/Cyborg1112.md)<br>
[cyborg1213: Get-Member ❤️❤️❤️❤️❤️](../underthewire/Cyborg1213.md)<br>
[cyborg1314: Get-CimInstance -ClassName Win32_DCOMApplication -Filter 'AppID like "%59B8AFA0-229E-46D9-B980-DDA2C817EC7E%"' | Select-Object *](../underthewire/Cyborg1314.md)<br>
[groot0001: cmd, Get-FileHash "C:\Windows\System32\drivers\etc\hosts" -Algorithm MD5, certutil -hashfile C:\Windows\System32\drivers\etc\hosts MD5](../underthewire/Groot0001.md)<br>
[groot0102: -join(Get-Content elements.txt)[1481110..1481117] ❤️❤️❤️](../underthewire/Groot0102.md)<br>
[groot0203: (Select-String -Path "C:\Users\Groot1\Desktop\elements.txt" -Pattern '\bbeetle\b' -AllMatches | ForEach-Object { $_.Matches.Count } | Measure-Object -Sum).Sum](../underthewire/Groot0203.md)<br>
[groot0304: Get-ChildItem HKCU:\ -Recurse -ErrorAction SilentlyContinue | Where-Object {$_.Name -like '*Drax*'}](../underthewire/Groot0304.md)<br>
[groot0405: -Properties * | Format-List *](../underthewire/Groot0405.md)<br>
[groot0506: Get-CimInstance Win32_StartupCommand](../underthewire/Groot0506.md)<br>
[groot0607: Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Services' | Where-Object {$_.Name -like '*applocker*'}](../underthewire/Groot0607.md)<br>
[groot0708: Get-NetFirewallRule -Action Block | Where-Object {$_.DisplayName -like '*mysql*'}](../underthewire/Groot0708.md)<br>
[groot0809: Get-ADOrganizationalUnit -Filter * -Properties ProtectedFromAccidentalDeletion | Where-Object {-not $_.ProtectedFromAccidentalDeletion}](../underthewire/Groot0809.md)<br>
[groot0910: Compare-Object (Get-Content old.txt) (Get-Content new.txt)](../underthewire/Groot0910.md)<br>
[groot1011: Get-Content TPS_Reports04.pdf -Raw -Stream secret](../underthewire/Groot1011.md)<br>
[groot1112: Get-Acl "Nine Realms"](../underthewire/Groot1112.md)<br>
[groot1213: Get-Item "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Get-ItemProperty -Name "RegisteredOwner"](../underthewire/Groot1213.md)<br>
[groot1314: Get-SmbShare -Name "*task*"](../underthewire/Groot1314.md)<br>
[oracle0001: (Get-TimeZone).Id.ToLower()](../underthewire/Oracle0001.md)<br>
[oracle0102: Get-ChildItem -File | Get-FileHash -Algorithm MD5 | Sort-Object Hash](../underthewire/Oracle0102.md)<br>
[oracle0203: Get-WinEvent -Path .\Oracle3_Security.evtx](../underthewire/Oracle0203.md)<br>
[oracle0304: Get-GPO -All | Sort-Object CreationTime -Descending | Select-Object -First 1](../underthewire/Oracle0304.md)<br>
[oracle0405: Get-GPO -All | Where-Object {$_.Description -eq 'I_AM_GROOT'}](../underthewire/Oracle0405.md)<br>
[oracle0506: (Get-ADOrganizationalUnit -Filter 'Name -notlike "Groups"' -Properties * | Where-Object {-not $_.gPLink}).Name](../underthewire/Oracle0506.md)<br>
[oracle0607: Get-Command Get-ADTrust -Syntax, Get-ADTrust -Filter * ❤️❤️❤️❤️❤️](../underthewire/Oracle0607.md)<br>
[oracle0708: (cat .\logs.txt | Select-String 'guardian.galaxy.com').ToString()](../underthewire/Oracle0708.md)<br>
[oracle0809: Get-Command Get-*dns*, Get-DnsServerResourceRecord -ZoneName 'underthewire.tech' ❤️❤️](../underthewire/Oracle0809.md)<br>
[oracle0910: Get-Item 'HKCU:\Software\Microsoft\Internet Explorer\TypedURLs'](../underthewire/Oracle0910.md)<br>
[oracle1011: Get-SmbMapping](../underthewire/Oracle1011.md)<br>
[oracle1112: Get-ChildItem 'HKCU:\Software\Microsoft\Terminal Server Client](../underthewire/Oracle1112.md)<br>
[oracle1213: Get-WinEvent -Path .\security.evtx | Where-Object {$_.Message -like '*group*created*'} | Select-Object -ExpandProperty Message](../underthewire/Oracle1213.md)<br>
[oracle1314: Get-Alias](../underthewire/Oracle1314.md)<br>
[trebek0001: -Flags ❤️❤️❤️❤️](../underthewire/Trebek0001.md)<br>
[trebek0102: Get-CimInstance Win32_Service -Filter 'Name like "C-3PO"' | Select-Object *](../underthewire/Trebek0102.md)<br>
[trebek0203: Get-WinEvent -Path .\security.evtx -FilterXPath "*[System[(EventID=4624)]] and *[EventData[Data[@Name='TargetUserName'] and (Data='Yoda')]]"](../underthewire/Trebek0203.md)<br>
[trebek0304: Get-ChildItem "C:\Windows\Prefetch" -Filter '*access*'](../underthewire/Trebek0304.md)<br>
[trebek0405](../underthewire/Trebek0405.md)<br>
[trebek0708: -join[System.IO.File]::ReadAllBytes((ls .\Clone_Trooper_data.pdf).FullName)[0..7]](../underthewire/Trebek0708.md)<br>
[trebek0809: Get-SmbShare](../underthewire/Trebek0809.md)<br>
[trebek0910: .Split("")[0]](../underthewire/Trebek0910.md)<br>
[trebek1011: Property ❤️❤️❤️❤️](../underthewire/Trebek1011.md)<br>
[trebek1112: -FilterXPath "*[System[EventID=4720]]", .Where({$_.Message -like '*Lor*'}).Message](../underthewire/Trebek1112.md)<br>
[trebek1213: (Get-ADUser -Filter * -Properties City).Where({$_.City})](../underthewire/Trebek1213.md)<br>
[trebek1314: (Get-ADUser -Filter * -Properties City).Where({$_.City}).City](../underthewire/Trebek1314.md)<br>


## Back to README.md
[BACK](../README.md)