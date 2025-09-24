# picoGym Level 362: PcapPoisoning
Source: https://play.picoctf.org/practice/challenge/362

## Goal
How about some hide and seek heh?<br>
Download this file and find the flag.<br>
https://artifacts.picoctf.net/c/373/trace.pcap

## What I learned
```
tshark
    -r
    -Y
    -A5 search 5 lines after
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/373/trace.pcap ⌨️
--2025-09-22 02:25:18--  https://artifacts.picoctf.net/c/373/trace.pcap
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 106715 (104K) [application/octet-stream]
Saving to: 'trace.pcap'

trace.pcap                                                 100%[======================================================================================================================================>] 104.21K  --.-KB/s    in 0.05s   

2025-09-22 02:25:19 (2.14 MB/s) - 'trace.pcap' saved [106715/106715]

AsianHacker-picoctf@webshell:~$ file trace.pcap ⌨️
trace.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Raw IPv4, capture length 65535)
AsianHacker-picoctf@webshell:~$ exiftool trace.pcap 
ExifTool Version Number         : 12.40
File Name                       : trace.pcap
Directory                       : .
File Size                       : 104 KiB
File Modification Date/Time     : 2023:03:16 03:16:09+00:00
File Access Date/Time           : 2025:09:22 02:25:34+00:00
File Inode Change Date/Time     : 2025:09:22 02:25:19+00:00
File Permissions                : -rw-rw-r--
Error                           : Unknown file type
AsianHacker-picoctf@webshell:~$ strings trace.pcap | grep "picoCTF" ⌨️
picoCTF{P64P_4N4L7S1S_SU55355FUL_4d72dfcc}9~ 🔐

Method 2: Wireshark
Filter: frame contains "picoCTF" ⌨️

507	👀 0.101836	172.16.0.2	10.253.0.6	TCP	82	[TCP Retransmission] 20 → 21 [SYN] Seq=0 Win=8192 Len=42

Frame 507 👀: 82 bytes on wire (656 bits), 82 bytes captured (656 bits)
Internet Protocol Version 4, Src: 172.16.0.2, Dst: 10.253.0.6
Transmission Control Protocol, Src Port: 20, Dst Port: 21, Seq: 0, Len: 42

0000   45 00 00 52 00 01 00 00 40 06 c3 90 ac 10 00 02   E..R....@.......
0010   0a fd 00 06 00 14 00 15 00 00 00 00 00 00 00 00   ................
0020   50 02 20 00 50 18 00 00 70 69 63 6f 43 54 46 7b   P. .P...picoCTF{
0030   50 36 34 50 5f 34 4e 34 4c 37 53 31 53 5f 53 55   P64P_4N4L7S1S_SU
0040   35 35 33 35 35 46 55 4c 5f 34 64 37 32 64 66 63   55355FUL_4d72dfc
0050   63 7d                                             c} 🔐

Method 3: tshark
# Note: 507 is packet number and 0020 is byte offset
AsianHacker-picoctf@webshell:~$ tshark -r trace.pcap -Y 'frame contains "picoCTF"' ⌨️
  507 👀  0.101836   172.16.0.2 ? 10.253.0.6   TCP 82 [TCP Retransmission] [TCP Port numbers reused] 20 ? 21 [SYN] Seq=0 Win=8192 Len=42

# -A5 search 5 lines after
AsianHacker-picoctf@webshell:~$ tshark -r trace.pcap -x | grep -A5 picoCTF ⌨️
0020  50 02 20 00 50 18 00 00 70 69 63 6f 43 54 46 7b   P. .P...picoCTF{
0030  50 36 34 50 5f 34 4e 34 4c 37 53 31 53 5f 53 55   P64P_4N4L7S1S_SU
0040  35 35 33 35 35 46 55 4c 5f 34 64 37 32 64 66 63   55355FUL_4d72dfc
0050  63 7d                                             c} 🔐

0000  45 00 00 28 00 01 00 00 40 06 64 99 0a fd 00 37   E..(....@.d....7

AsianHacker-picoctf@webshell:~$ tshark -r trace.pcap -x -Y "frame.number == 507" ⌨️
0000  45 00 00 52 00 01 00 00 40 06 c3 90 ac 10 00 02   E..R....@.......
0010  0a fd 00 06 00 14 00 15 00 00 00 00 00 00 00 00   ................
0020  50 02 20 00 50 18 00 00 70 69 63 6f 43 54 46 7b   P. .P...picoCTF{
0030  50 36 34 50 5f 34 4e 34 4c 37 53 31 53 5f 53 55   P64P_4N4L7S1S_SU
0040  35 35 33 35 35 46 55 4c 5f 34 64 37 32 64 66 63   55355FUL_4d72dfc
0050  63 7d                                             c} 🔐
```

## Flag
picoCTF{P64P_4N4L7S1S_SU55355FUL_4d72dfcc}

## Continue
[Continue](./picoGym0413.md)