# Cyborg Level 11 → 12 [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes("c:\windows\system32\cmd.exe"))

## Previous Flag
```
spaceballs
```

## Goal
The password for cyborg13 is the first four characters of the base64 encoded full path to the file that started the i_heart_robots service PLUS the name of the file on the desktop.<br>

NOTE:<br>
– An example of a full path would be ‘c:\some_folder\test.exe’.<br>
– Be sure to use ‘unicode’ in your encoding.<br>
– If the encoded base64 is “rwmed2fdreewrt34t” and the file on the desktop is called “_address”, then the password is “rwme_address”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-CimInstance win32_service -Filter 'Name like "i_heart_robots"'
    Get-CimInstance → PowerShell cmdlet queries Windows Management Instrumentation (WMI) / CIM (Common Information Model) classes
    win32_service → class being queried, Win32_Service represents Windows services (same things you see in services.msc)
    -Filter →   filter server-side (WMI-side) instead of fetching all services and filtering in PowerShell
                accepts a WMI Query Language (WQL) filter string — similar to SQL’s WHERE
    'Name like "i_heart_robots"' → WQL condition, matches service by name
        Name → property of Win32_Service (service name, not the display name)
        like → WQL operator, similar to SQL LIKE. You can use wildcards (%) with it

# encode (Unicode / UTF-16LE) ❤️
[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes("c:\windows\system32\cmd.exe"))

# encode (UTF8)
[Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("c:\windows\system32\cmd.exe"))

# decode a Unicode (UTF-16LE) base64 string
[System.Text.Encoding]::Unicode.GetString([Convert]::FromBase64String("cgB3AG0AZQBfAGEAZABkAHIAZQBzAHMA"))

# decode a UTF8 base64 string
[System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("cndtZV9hZGRyZXNz"))
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg12@cyborg.underthewire.tech -p 22 ⌨️
cyborg12@cyborg.underthewire.tech's password: ⌨️ spaceballs

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg12\desktop> dir ⌨️

    Directory: C:\users\cyborg12\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:45 AM              0 _heart 👀

PS C:\users\cyborg12\desktop> Get-CimInstance win32_service -Filter 'Name like "i_heart_robots"' ⌨️

ProcessId Name           StartMode State   Status ExitCode
--------- ----           --------- -----   ------ --------
0         i_heart_robots Disabled  Stopped OK     1077

PS C:\users\cyborg12\desktop> Get-CimInstance win32_service -Filter 'Name like "i_heart_robots"' | Select-Object PathName  ⌨️

PathName
--------
c:\windows\system32\cmd.exe 👀

PS C:\users\cyborg12\desktop> [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes("c:\windows\system32\cmd.exe")) ⌨️
YwA6AFwAdwBpAG4AZABvAHcAcwBcAHMAeQBzAHQAZQBtADMAMgBcAGMAbQBkAC4AZQB4AGUA

# Extract first 4 char
PS C:\users\cyborg12\desktop> -join[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes((Get-CimInstance win32_service -Filter 'Name like "i_heart_robots"').PathName)).ToLower()[0..3] + (ls -File).Name
ywa6_heart 🔐

PS C:\users\cyborg12\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg13@cyborg.underthewire.tech -p 22 ⌨️
cyborg13@cyborg.underthewire.tech's password: ⌨️ ywa6_heart

Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg13\desktop> whoami ⌨️
underthewire\cyborg13
```

## Flag
ywa6_heart

## Continue
[Continue](./Cyborg1213.md)