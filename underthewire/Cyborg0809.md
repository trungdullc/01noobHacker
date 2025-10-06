# Cyborg Level 08 → 09 Get-ADUser -Filter * -Properties * | Select-Object GivenName, *Phone | Select-String '876-5309'

## Previous Flag
```
4
```

## Goal
The password for cyborg10 is the first name of the user with the phone number of 876-5309 listed in Active Directory PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the first name “chris” and the file on the desktop is called “23”, then the password is “chris23”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
In PowerShell, $_ is a special automatic variable used inside a pipeline
It represents the current object being passed down the pipeline ❤️

Get-ADUser -Filter * -Properties * | Select-Object GivenName, *Phone | Select-String '876-5309'
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg9@cyborg.underthewire.tech -p 22 ⌨️
cyborg9@cyborg.underthewire.tech's password: ⌨️ 4

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg9\desktop> dir ⌨️

    Directory: C:\users\cyborg9\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 99 👀

PS C:\users\cyborg9\desktop> Get-ADUser -Filter * -Properties * | Select-Object GivenName, *Phone | Select-String '876-5309' ⌨️

@{GivenName=Onita; HomePhone=; MobilePhone=; OfficePhone=876-5309} 👀

PS C:\users\cyborg9\desktop> Get-ADUser -Filter * -Properties GivenName,HomePhone,MobilePhone,OfficePhone | Select-Object GivenName, HomePhone, MobilePhone, OfficePhone -First 10 ⌨️

GivenName HomePhone MobilePhone OfficePhone
--------- --------- ----------- -----------




century
century
century
century
century
century

PS C:\users\cyborg9\desktop> Get-ADUser -Filter {(GivenName -like "*Onita*") -and (OfficePhone -like "*876-5309*")} ` -Properties GivenName, HomePhone, MobilePhone, OfficePhone | Select-Object GivenName, HomePhone, MobilePhone, OfficePhone ⌨️

GivenName HomePhone MobilePhone OfficePhone
--------- --------- ----------- -----------
Onita 👀                          876-5309 

PS C:\users\cyborg9\desktop> Get-ADUser -Filter * -Properties GivenName,HomePhone,MobilePhone,OfficePhone | Where-Object { $_.HomePhone -or $_.MobilePhone -or $_.OfficePhone } | Select-Object GivenName, HomePhone, MobilePhone, OfficePhone -First 5 ⌨️

GivenName HomePhone MobilePhone OfficePhone
--------- --------- ----------- -----------
Onita 👀                          876-5309

PS C:\users\cyborg9\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg10@cyborg.underthewire.tech -p 22 ⌨️
cyborg10@cyborg.underthewire.tech's password: ⌨️ onita99

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg10\desktop> whoami ⌨️
underthewire\cyborg10
```

## Flag
onita99

## Continue
[Continue](./Cyborg0910.md)