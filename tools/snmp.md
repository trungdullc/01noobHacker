# snmp
```
Description: SNMP is used by network devices (routers, printers, switches, servers) to report system information
PORT: UDP PORT 161

# Install SNMP service and tools
sudo apt update
sudo apt install snmpd snmp -y

sudo nano /etc/snmp/snmpd.conf
    rocommunity public
    sysLocation "Lab Server"
    sysContact admin@ctf.local
    agentAddress udp:161

sudo systemctl restart snmpd
sudo netstat -anu | grep 161
```

# Client Side
```
# snmpwalk (built-in Kali/Linux)                        # Install snmp-check Tool (alternative to snmpwalk)
# Find system info only                                 sudo apt install snmpcheck
snmpwalk -v1 -c public 10.10.10.125 1.3.6.1.2.1.1       snmp-check 10.10.10.125

# Basic query with community string 'public'
snmpwalk -v1 -c public 10.10.10.125
```

## Back to README.md
[BACK](/README.md)