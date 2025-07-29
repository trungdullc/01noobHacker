# nmap

```
Source: https://nmap.org/
Description: Port and service scanning

# Initial Fast TCP Scan
nmap -v -sS -sV -Pn --top-ports 1000 -oA initial_scan_192.168.0.1 192.168.0.1

# Full TCP Scan
nmap -v -sS -Pn -sV -p 0-65535 -oA full_scan_192.168.0.1 192.168.0.1

# Limited Full TCP Scan (syn scan to long use with no service detection
nmap -sT -p- --min-rate 5000 --max-retries 1 192.168.0.1

# Top 100 UDP Scan
nmap -v -sU -T4 -Pn --top-ports 100 -oA top_100_UDP_192.168.0.1 192.168.0.1

# Full Vulnerability scan
nmap -v -sS  -Pn --script vuln --script-args=unsafe=1 -oA full_vuln_scan_192.168.0.1 192.168.0.1

# Vulners Vulnerability Script
nmap -v -sS  -Pn --script nmap-vulners -oA full_vuln_scan_192.168.0.1 192.168.0.1

# SMB Vulnerabitlity Scan
nmap -v -sS -p 445,139 -Pn --script smb-vuln* --script-args=unsafe=1 -oA smb_vuln_scan_192.168.0.1 192.168.0.1
```

## Back to README.md
[BACK](/README.md)