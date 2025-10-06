# Cyborg Level 01 → 02 dig CYBORG718W100N.underthewire.tech, nslookup CYBORG718W100N.underthewire.tech, host CYBORG718W100N.underthewire.tech

## Previous Flag
```
kansas
```

## Goal
The password for cyborg3 is the host A record IP address for CYBORG718W100N PLUS the name of the file on the desktop.<br>

NOTE:<br>
– If the IP is “10.10.1.5” and the file on the desktop is called “_address”, then the password is “10.10.1.5_address”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Get-Help Resolve-DnsName

WMI or cmdlets
Each domain client has its own specific Zone Name
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg2@cyborg.underthewire.tech -p 22 ⌨️
cyborg2@cyborg.underthewire.tech's password: ⌨️ kansas

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg2\desktop> dir ⌨️

    Directory: C:\users\cyborg2\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2/26/2022   2:14 PM              0 _ipv4 👀

PS C:\users\cyborg2\desktop> Resolve-DnsName CYBORG718W100N ⌨️⚠️
Resolve-DnsName : CYBORG718W100N : DNS name does not exist
At line:1 char:1
+ Resolve-DnsName CYBORG718W100N
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceUnavailable: (CYBORG718W100N:String) [Resolve-DnsName], Win32Exception
    + FullyQualifiedErrorId : DNS_ERROR_RCODE_NAME_ERROR,Microsoft.DnsClient.Commands.ResolveDnsName 

PS C:\users\cyborg2\desktop> ping CYBORG718W100N ⌨️
Ping request could not find host CYBORG718W100N. Please check the name and try again.

⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️ Suppose see something like this ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
Name                                           Type   TTL   Section    IPAddress
----                                           ----   ---   -------    ---------
CYBORG718W100N.underthewire.tech               A      3600  Answer     172.31.45.167 👀
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

PS C:\users\cyborg2\desktop> Get-CimInstance -ClassName Win32_OperatingSystem -ComputerName CYBORG718W100N ⌨️
Get-CimInstance : WinRM cannot process the request. The following error occurred while using Kerberos authentication: Cannot find the computer 
CYBORG718W100N. Verify that the computer exists on the network and that the name provided is spelled correctly.
At line:1 char:1
+ Get-CimInstance -ClassName Win32_OperatingSystem -ComputerName CYBORG ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (root\cimv2:Win32_OperatingSystem:String) [Get-CimInstance], CimException
    + FullyQualifiedErrorId : HRESULT 0x80070035,Microsoft.Management.Infrastructure.CimCmdlets.GetCimInstanceCommand
    + PSComputerName        : CYBORG718W100N

PS C:\users\cyborg2\desktop> Get-NetIPConfiguration ⌨️

InterfaceAlias       : Ethernet Instance 0
InterfaceIndex       : 4
InterfaceDescription : Red Hat VirtIO Ethernet Adapter #2
NetProfile.Name      : underthewire.tech
IPv4Address          : 192.99.167.156
IPv6DefaultGateway   :
IPv4DefaultGateway   : 192.99.167.1
DNSServer            : 213.186.33.99

PS C:\users\cyborg2\desktop> (Resolve-DnsName 'CYBORG718W100N').IPAddress.ToString() + (Get-ChildItem -File).Name ⌨️
Resolve-DnsName : CYBORG718W100N : DNS name does not exist
At line:1 char:2
+ (Resolve-DnsName 'CYBORG718W100N').IPAddress.ToString() + (Get-ChildI ...
+  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceUnavailable: (CYBORG718W100N:String) [Resolve-DnsName], Win32Exception
    + FullyQualifiedErrorId : DNS_ERROR_RCODE_NAME_ERROR,Microsoft.DnsClient.Commands.ResolveDnsName        
 
You cannot call a method on a null-valued expression.
At line:1 char:1
+ (Resolve-DnsName 'CYBORG718W100N').IPAddress.ToString() + (Get-ChildI ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : InvokeMethodOnNull

PS C:\users\cyborg2\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg3@cyborg.underthewire.tech -p 22 ⌨️
cyborg3@cyborg.underthewire.tech's password: ⌨️ 172.31.45.167_ipv4
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg3\desktop> whoami ⌨️
underthewire\cyborg3
```

## Flag
172.31.45.167_ipv4 (Challenge Broken needed to look at past writeup) ⚠️

## Continue
[Continue](./Cyborg0203.md)