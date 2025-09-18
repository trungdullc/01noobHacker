# picoGym Level 311: Torrent Analyze
Source: https://play.picoctf.org/practice/challenge/311

## Goal
SOS, someone is torrenting on our network.<br>
One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like picoCTF{filename}. Captured traffic.<br>
https://artifacts.picoctf.net/c/165/torrent.pcap

## What I learned
```
wireshark: Analyze → Enable Protocols ❤️
bt-dht
```

## Solution
```
https://webshell.picoctf.org/

# Optional
Analyze → Enable Protocols ❤️

Filter: bt-dht and ip.src == 192.168.73.132 ⌨️
36060	18.777685557	192.168.73.132	5.189.157.90	BT-DHT	327	Response Nodes=8
47877	19.922378992	192.168.73.132	138.197.143.248	BT-DHT	100	Ping
51080	20.689763723	192.168.73.132	107.181.231.146	BT-DHT	139	Get_peers Info_hash=e2467cbf021192c241367b892230dc1e05c0580e 👀
51081	20.689807803	192.168.73.132	159.89.144.30	BT-DHT	139	Get_peers Info_hash=e2467cbf021192c241367b892230dc1e05c0580e
51082	20.689828638	192.168.73.132	18.190.61.127	BT-DHT	139	Get_peers Info_hash=e2467cbf021192c241367b892230dc1e05c0580e
51179	20.748056557	192.168.73.132	77.183.44.118	BT-DHT	139	Get_peers Info_hash=e2467cbf021192c241367b892230dc1e05c0580e
51212	20.776335262	192.168.73.132	181.114.168.101	BT-DHT	139	Get_peers Info_hash=e2467cbf021192c241367b892230dc1e05c0580e
51464	20.883349377	192.168.73.132	37.187.123.154	BT-DHT	139	Get_peers Info_hash=e2467cbf021192c241367b892230dc1e05c0580e
51519	20.909443842	192.168.73.132	5.167.155.85	BT-DHT	139	Get_peers Info_hash=e2467cbf021192c241367b892230dc1e05c0580e

Frame 51080: 139 bytes on wire (1112 bits), 139 bytes captured (1112 bits) on interface eth0, id 0
Ethernet II, Src: VMware_2d:4b:5e (00:0c:29:2d:4b:5e), Dst: VMware_f5:e4:05 (00:50:56:f5:e4:05)
Internet Protocol Version 4, Src: 192.168.73.132, Dst: 107.181.231.146
User Datagram Protocol, Src Port: 51413, Dst Port: 2169
BitTorrent DHT Protocol
    Request arguments: Dictionary...
        Key: a
        Value: Dictionary...
            id: 17c1ec414b95fc775d7dddcb686693b7863ac1aa
                Key: id
                Value: 17c1ec414b95fc775d7dddcb686693b7863ac1aa
            info_hash: e2467cbf021192c241367b892230dc1e05c0580e 👀
                Key: info_hash
                Value: e2467cbf021192c241367b892230dc1e05c0580e 👀
            Terminator: e
    Request type: get_peers
        Key: q
        Value: get_peers
    Transaction ID: 6770c723
        Key: t
        Value: 6770c723
    Message type: Request
        Key: y
        Value: q
    Terminator: e

# Note: Used to be easy to search
Google: e2467cbf021192c241367b892230dc1e05c0580e ⌨️
https://linuxtracker.org/?page=torrent-details&id=e2467cbf021192c241367b892230dc1e05c0580e
Update: Bad Id

Still Works: https://www.infotorr.com/ ⌨️
ubuntu-19.10-desktop-amd64.iso 🔐
```

## Flag
picoCTF{ubuntu-19.10-desktop-amd64.iso}

## Continue
[Continue](./picoGym0264.md)