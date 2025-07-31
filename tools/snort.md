# Snort

```
Source: https://www.snort.org/
Description: Network intrusion detection and prevention system for real-time traffic analysis and packet logging

snort -V

# Run Snort in Packet Sniffing Mode
snort -i eth0
snort -v -i eth0
snort -v -v -i eth0

# Log Packets to a Directory
snort -i eth0 -l /var/log/snort -K ascii

# Run Snort with a Configuration File
snort -c /etc/snort/snort.conf -i eth0

# Run Snort in IDS Mode
snort -A console -q -c /etc/snort/snort.conf -i eth0
    -A console: alerts printed to console
    -q: quiet mode (suppress banner)
    -c: config file
    -i: interface

# Test Rule Matching
snort -T -c /etc/snort/snort.conf

# Specify a pcap File for Offline Analysis
snort -r traffic.pcap
```

# Example of Writing a Simple Rule
```
# Add to /etc/snort/rules/local.rules
alert tcp any any -> any 80 (msg:"HTTP access detected"; sid:1000001; rev:1;)

# Make sure snort.conf includes this rules file
include $RULE_PATH/local.rules
```

## Back to README.md
[BACK](/README.md)