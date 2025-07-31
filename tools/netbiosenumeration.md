# NetBIOS Enumeration

```
NetBIOS (Network Basic Input/Output System) is a legacy networking protocol that allows computers on a local area network (LAN) to communicate and share resources

# Quick NetBIOS Enumeration Commands
nmblookup -A 10.10.10.10
nbtscan 10.10.10.10
sudo nmap -sU -sV -T4 --script nbstat.nse -p137 -Pn -n 10.10.10.10

Port 137 (NetBIOS Name Service – NBNS)
    Resolves NetBIOS names to IP addresses
    Identifies computer names, workgroup or domain names, and network shares
Port 138 (NetBIOS Datagram Service – NBDS)
    Sends datagrams like browser elections and announcements
```

# nbtstat (Windows Built-in Tool)
```
# Query remote NetBIOS Name Table (port 137)
nbtstat -A 192.168.1.10

# View local NetBIOS name table
nbtstat -n

# View active NetBIOS connections (port 138)
nbtstat -S
```

# nbtscan
```
nbtscan: tool for NetBIOS name service enumeration over port 137

# Scan an IP or subnet for NetBIOS names
nbtscan 192.168.1.0/24
```

# Interpreting NetBIOS Enumeration Results
```
When scanning NetBIOS over ports 137 and 138, look for these common flags:

    Flag	            Meaning
    <00>	            Indicates the hostname or domain name
    <20>	            Indicates the system is running file-sharing services
    <03>	            Indicates the Messenger service is active on the machine

These flags help identify the roles of systems on the network (file servers or domain controllers)
```

# Securing Ports 137 and 138
```
To protect against NetBIOS enumeration vulnerabilities:
    Disable NetBIOS over TCP/IP if not required
        This can be done in the network adapter settings (Windows)
    Block ports 137 and 138 using a firewall
        Especially important on public-facing systems
        Prevents external enumeration
    Enforce strong authentication and access controls
        Implement for all shared network resources
```

## Back to README.md
[BACK](/README.md)