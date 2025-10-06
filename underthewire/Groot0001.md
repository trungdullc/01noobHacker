# Groot Level 00 → 01 md5sum C:\Windows\System32\drivers\etc\hosts

## Previous Flag
```
groot1
```

## Goal
The password for groot2 is the last five alphanumeric characters of the MD5 hash of this system’s hosts file.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```
cmd

Get-FileHash "C:\Windows\System32\drivers\etc\hosts" -Algorithm MD5
certutil -hashfile C:\Windows\System32\drivers\etc\hosts MD5
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot1@groot.underthewire.tech -p 22 ⌨️
groot1@groot.underthewire.tech's password: ⌨️ groot1

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot1\desktop> ls C:\Windows\System32\drivers\etc ⌨️

    Directory: C:\Windows\System32\drivers\etc

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         9/3/2018  11:01 PM            865 hosts 👀
-a----        7/16/2016   1:21 PM           3683 lmhosts.sam
-a----        7/16/2016   1:21 PM            407 networks
-a----        7/16/2016   1:21 PM           1358 protocol
-a----        7/16/2016   1:21 PM          17463 services

PS C:\users\Groot1\desktop> Get-Content  C:\Windows\System32\drivers\etc\hosts ⌨️
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost
        192.99.167.156  games.underthewire.tech

PS C:\users\Groot1\desktop> Get-FileHash "C:\Windows\System32\drivers\etc\hosts" -Algorithm MD5 ⌨️

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             6EEC08310BD5328FFC8FB72CD8E464C3 👀                                     C:\Windows\System32\drivers\etc\hosts

PS C:\users\Groot1\desktop> certutil -hashfile C:\Windows\System32\drivers\etc\hosts MD5 ⌨️
MD5 hash of file C:\Windows\System32\drivers\etc\hosts:
6eec08310bd5328ffc8fb72cd8e464c3 👀
CertUtil: -hashfile command completed successfully.

PS C:\users\Groot1\desktop> cmd ⌨️

Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

# Note: PS Changed to C:\ ❤️
C:\users\Groot1\desktop>certutil -hashfile C:\Windows\System32\drivers\etc\hosts MD5 ⌨️
MD5 hash of file C:\Windows\System32\drivers\etc\hosts:
6eec08310bd5328ffc8fb72cd8e464c3 👀
CertUtil: -hashfile command completed successfully.

C:\users\Groot1\desktop>set hash=6eec08310bd5328ffc8fb72cd8e464c3 ⌨️

C:\users\Groot1\desktop>echo %hash:~-5% ⌨️
464c3 🔐

C:\users\Groot1\desktop>exit ⌨️
PS C:\users\Groot1\desktop> $hash = "6eec08310bd5328ffc8fb72cd8e464c3" ⌨️
PS C:\users\Groot1\desktop> $hash.Substring($hash.Length - 5) ⌨️
464c3 🔐
PS C:\users\Groot1\desktop> $hash[-5..-1] -join '' ⌨️
464c3 🔐

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot2@groot.underthewire.tech -p 22 ⌨️
groot2@groot.underthewire.tech's password: ⌨️ 464c3

Windows PowerShell
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Groot2\desktop> whoami ⌨️
underthewire\groot2
```

## Flag
464c3

## Continue
[Continue](./Groot0102.md)