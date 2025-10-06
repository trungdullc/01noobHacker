# Oracle Level 08 → 09 Get-DnsServerResourceRecord -ZoneName 'underthewire.tech'

## Previous Flag
```
star-lord
```

## Goal
The password for oracle10 is the computer name of the DNS record of the mail server listed in the UnderTheWire.tech zone PLUS the name of the file on the user’s desktop.<br>

NOTE:<br>
– If the server name is “some_blob” and the file on the desktop is named “1234”, the password would be “some_blob1234”.<br>
– Only submit the computer name and not the fully qualified domain name.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Get-Command Get-*dns*
Get-DnsServerResourceRecord -ZoneName 'underthewire.tech'
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle9@groot.underthewire.tech -p 22 ⌨️
oracle9@groot.underthewire.tech's password: ⌨️ star-lord

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle9\desktop> dir ⌨️

    Directory: C:\users\Oracle9\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:51 AM              0 9229 👀

PS C:\users\Oracle9\desktop> Get-Command Get-*dns* ⌨️

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           Get-DnsServerRRL                                   2.0.0.0    DnsServer
Function        Get-DnsClient                                      1.0.0.0    DnsClient
Function        Get-DnsClientCache                                 1.0.0.0    DnsClient
Function        Get-DnsClientGlobalSetting                         1.0.0.0    DnsClient
Function        Get-DnsClientNrptGlobal                            1.0.0.0    DnsClient
Function        Get-DnsClientNrptPolicy                            1.0.0.0    DnsClient
Function        Get-DnsClientNrptRule                              1.0.0.0    DnsClient
Function        Get-DnsClientServerAddress                         1.0.0.0    DnsClient
Function        Get-DnsServer                                      2.0.0.0    DnsServer
Function        Get-DnsServerCache                                 2.0.0.0    DnsServer
Function        Get-DnsServerClientSubnet                          2.0.0.0    DnsServer
Function        Get-DnsServerDiagnostics                           2.0.0.0    DnsServer
Function        Get-DnsServerDirectoryPartition                    2.0.0.0    DnsServer
Function        Get-DnsServerDnsSecZoneSetting                     2.0.0.0    DnsServer
Function        Get-DnsServerDsSetting                             2.0.0.0    DnsServer
Function        Get-DnsServerEDns                                  2.0.0.0    DnsServer
Function        Get-DnsServerForwarder                             2.0.0.0    DnsServer
Function        Get-DnsServerGlobalNameZone                        2.0.0.0    DnsServer
Function        Get-DnsServerGlobalQueryBlockList                  2.0.0.0    DnsServer
Function        Get-DnsServerQueryResolutionPolicy                 2.0.0.0    DnsServer
Function        Get-DnsServerRecursion                             2.0.0.0    DnsServer
Function        Get-DnsServerRecursionScope                        2.0.0.0    DnsServer
Function        Get-DnsServerResourceRecord                        2.0.0.0    DnsServer 👀
Function        Get-DnsServerResponseRateLimiting                  2.0.0.0    DnsServer
Function        Get-DnsServerResponseRateLimitingExceptionlist     2.0.0.0    DnsServer
Function        Get-DnsServerRootHint                              2.0.0.0    DnsServer
Function        Get-DnsServerScavenging                            2.0.0.0    DnsServer
Function        Get-DnsServerSetting                               2.0.0.0    DnsServer
Function        Get-DnsServerSigningKey                            2.0.0.0    DnsServer
Function        Get-DnsServerStatistics                            2.0.0.0    DnsServer
Function        Get-DnsServerTrustAnchor                           2.0.0.0    DnsServer
Function        Get-DnsServerTrustPoint                            2.0.0.0    DnsServer
Function        Get-DnsServerVirtualizationInstance                2.0.0.0    DnsServer
Function        Get-DnsServerZone                                  2.0.0.0    DnsServer
Function        Get-DnsServerZoneAging                             2.0.0.0    DnsServer
Function        Get-DnsServerZoneDelegation                        2.0.0.0    DnsServer
Function        Get-DnsServerZoneScope                             2.0.0.0    DnsServer
Function        Get-DnsServerZoneTransferPolicy                    2.0.0.0    DnsServer
Function        Get-NetDnsTransitionConfiguration                  1.0.0.0    NetworkTransition
Function        Get-NetDnsTransitionMonitoring                     1.0.0.0    NetworkTransition
Function        Get-UalDns                                         1.0.0.0    UserAccessLogging

PS C:\users\Oracle9\desktop> Get-Help Get-DnsServerResourceRecord ⌨️
PS C:\users\Oracle9\desktop> Get-DnsServerResourceRecord -ZoneName 'underthewire.tech' ⌨️

HostName                  RecordType Type       Timestamp            TimeToLive      RecordData
--------                  ---------- ----       ---------            ----------      ----------
@                         A          1          4/25/2025 4:00:00 AM 00:10:00        192.99.167.156
@                         NS         2          0                    01:00:00        utw.underthewire.tech.
@                         SOA        6          0                    01:00:00        [9817][utw.underthewire.tech.][hostmaster.under...
_msdcs                    NS         2          0                    01:00:00        utw.underthewire.tech.
_gc._tcp.Default-First... SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][3268][utw.underthewire.tech.]
_kerberos._tcp.Default... SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][88][utw.underthewire.tech.]
_ldap._tcp.Default-Fir... SRV        33         4/25/2025 3:00:00 AM 00:10:00        [0][100][389][utw.underthewire.tech.]
_gc._tcp                  SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][3268][utw.underthewire.tech.]
_kerberos._tcp            SRV        33         4/25/2025 4:00:00 AM 00:10:00        [0][100][88][utw.underthewire.tech.]
_kpasswd._tcp             SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][464][utw.underthewire.tech.]
_ldap._tcp                SRV        33         4/25/2025 3:00:00 AM 00:10:00        [0][100][389][utw.underthewire.tech.]
_kerberos._udp            SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][88][utw.underthewire.tech.]
_kpasswd._udp             SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][464][utw.underthewire.tech.]
CYBORG718W100N            A          1          0                    01:00:00        172.31.45.167
DomainDnsZones            A          1          4/25/2025 2:00:00 AM 00:10:00        192.99.167.156
_ldap._tcp.Default-Fir... SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][389][utw.underthewire.tech.]
_ldap._tcp.DomainDnsZones SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][389][utw.underthewire.tech.]
ForestDnsZones            A          1          4/25/2025 2:00:00 AM 00:10:00        192.99.167.156
_ldap._tcp.Default-Fir... SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][389][utw.underthewire.tech.]
_ldap._tcp.ForestDnsZones SRV        33         4/25/2025 2:00:00 AM 00:10:00        [0][100][389][utw.underthewire.tech.]
utw                       A          1          0                    01:00:00        192.99.167.156
utw_exch 👀              MX         15         0                    01:00:00        [10][mail.utw_exch.]

PS C:\users\Oracle9\desktop> (Get-DnsServerResourceRecord -ZoneName 'underthewire.tech' -RRType MX).HostName.ToLower() + (ls -File).Name.ToLower() ⌨️
utw_exch9229 🔐

PS C:\users\Oracle9\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle10@groot.underthewire.tech -p 22⌨️
oracle10@groot.underthewire.tech's password: ⌨️ utw_exch9229

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle10\desktop> whoami ⌨️
underthewire\oracle10
```

## Flag
utw_exch9229

## Continue
[Continue](./Oracle0910.md)