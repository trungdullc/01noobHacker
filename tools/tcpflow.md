# tcpflow
```
Source: https://linux.die.net/man/1/tcpflow
Description: CLI Network Protocol Analyzer for reorganizing packets in a PCAP file and getting files out of them

Capture traffic with Wireshark/tcpdump and save as .pcap file
But raw .pcap files show data packet by packet, not easily readable
tcpflow reconstructs the original messages sent over TCP into a readable file

Packet 1: GET /login                            GET /login HTTP/1.1
Packet 2: Host: example.com                     Host: example.com
Packet 3: username=admin&password=123456        username=admin&password=123456

tcpflow -r my_file.pcap
ls -1t | head -5                                # see last 5 recently modified files
```

## Back to README.md
[BACK](../README.md)