# picoGym Level 348: FindAndOpen
Source: https://play.picoctf.org/practice/challenge/348

## Goal
Someone might have hidden the password in the trace file<br>
Find the key to unlock this file <br>
https://artifacts.picoctf.net/c/492/flag.zip<br>
This tracefile might be good to analyze<br>
https://artifacts.picoctf.net/c/492/dump.pcap

## What I learned
```
tshark -r dump.pcap -y EN10MB -Y "frame.number==48" -V -x ⌨️
    -r dump.pcap → read packets from capture.pcap
    -y EN10MB → interpret frames as Ethernet
    -Y "frame.number==48" → filter so only frame 48 is shown
    -V → show verbose protocol breakdown
    -x → show hex+ASCII dump
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/492/flag.zip https://artifacts.picoctf.net/c/492/dump.pcap ⌨️
--2025-09-20 02:36:32--  https://artifacts.picoctf.net/c/492/flag.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 231 [application/octet-stream]
Saving to: 'flag.zip'

flag.zip                                                   100%[======================================================================================================================================>]     231  --.-KB/s    in 0s      

2025-09-20 02:36:32 (68.8 MB/s) - 'flag.zip' saved [231/231]

--2025-09-20 02:36:32--  https://artifacts.picoctf.net/c/492/dump.pcap
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 7413 (7.2K) [application/octet-stream]
Saving to: 'dump.pcap'

dump.pcap                                                  100%[======================================================================================================================================>]   7.24K  --.-KB/s    in 0s      

2025-09-20 02:36:32 (2.15 GB/s) - 'dump.pcap' saved [7413/7413]

FINISHED --2025-09-20 02:36:32--
Total wall clock time: 0.2s
Downloaded: 2 files, 7.5K in 0s (1.11 GB/s)

AsianHacker-picoctf@webshell:~$ unzip flag.zip ⌨️
Archive:  flag.zip
[flag.zip] flag password: ⌨️
   skipping: flag                    incorrect password ⚠️

# Method 1: Find password via Wireshark
# Note: This one sticks out because of hidden color and Payload length was bigger than 33 it was 56
48	24.240874	50:4a:47:54:46:52	41:41:42:42:48:48	0x4c4b	70	Ethernet II

Frame 48: 70 bytes on wire (560 bits), 70 bytes captured (560 bits)
Ethernet II, Src: 50:4a:47:54:46:52 (50:4a:47:54:46:52), Dst: 41:41:42:42:48:48 (41:41:42:42:48:48)
Data (56 bytes)
    Data: 564768706379427063794230614755676332566a636d56304f69427761574e76513152476531497a4e45524a546b64665445394c5a46383d 👀
    [Length: 56]

0000   41 41 42 42 48 48 50 4a 47 54 46 52 4c 4b 👀56 47   AABBHHPJGTFRLK👀VG
0010   68 70 63 79 42 70 63 79 42 30 61 47 55 67 63 32   hpcyBpcyB0aGUgc2
0020   56 6a 63 6d 56 30 4f 69 42 77 61 57 4e 76 51 31   VjcmV0OiBwaWNvQ1
0030   52 47 65 31 49 7a 4e 45 52 4a 54 6b 64 66 54 45   RGe1IzNERJTkdfTE
0040   39 4c 5a 46 38 3d                                 9LZF8=

# Important Concept: Data = ASCII Dump ❤️❤️❤️❤️❤️
https://cyberchef.io/#recipe=From_Hex('Auto')&input=NTY0NzY4NzA2Mzc5NDI3MDYzNzk0MjMwNjE0NzU1Njc2MzMyNTY2YTYzNmQ1NjMwNGY2OTQyNzc2MTU3NGU3NjUxMzE1MjQ3NjUzMTQ5N2E0ZTQ1NTI0YTU0NmI2NDY2NTQ0NTM5NGM1YTQ2MzgzZA

# ASCII Dump is Base64 Encoded
https://cyberchef.io/#recipe=From_Hex('Auto')From_Base64('A-Za-z0-9%2B/%3D',true)&input=NTY0NzY4NzA2Mzc5NDI3MDYzNzk0MjMwNjE0NzU1Njc2MzMyNTY2YTYzNmQ1NjMwNGY2OTQyNzc2MTU3NGU3NjUxMzE1MjQ3NjUzMTQ5N2E0ZTQ1NTI0YTU0NmI2NDY2NTQ0NTM5NGM1YTQ2MzgzZA

This is the secret: picoCTF{R34DING_LOKd_ 👀

# Method 2: tshark
AsianHacker-picoctf@webshell:~$ tshark -r dump.pcap -Y 'frame.number==48' -Vx  ⌨️
Frame 48: 70 bytes on wire (560 bits), 70 bytes captured (560 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Oct 22, 2022 07:33:33.157638000 UTC
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1666424013.157638000 seconds
    [Time delta from previous captured frame: 9.165145000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 24.240874000 seconds]
    Frame Number: 48
    Frame Length: 70 bytes (560 bits)
    Capture Length: 70 bytes (560 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:data]
Ethernet II, Src: 50:4a:47:54:46:52 (50:4a:47:54:46:52), Dst: 41:41:42:42:48:48 (41:41:42:42:48:48)
    Destination: 41:41:42:42:48:48 (41:41:42:42:48:48)
        Address: 41:41:42:42:48:48 (41:41:42:42:48:48)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
    Source: 50:4a:47:54:46:52 (50:4a:47:54:46:52)
        Address: 50:4a:47:54:46:52 (50:4a:47:54:46:52)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: Unknown (0x4c4b)
Data (56 bytes)
    Data: 564768706379427063794230614755676332566a636d56304f69427761574e7651315247? 👀⚠️⚠️⚠️⚠️⚠️
    [Length: 56]

0000  41 41 42 42 48 48 50 4a 47 54 46 52 4c 4b 56 47   AABBHHPJGTFRLKVG
0010  68 70 63 79 42 70 63 79 42 30 61 47 55 67 63 32   hpcyBpcyB0aGUgc2
0020  56 6a 63 6d 56 30 4f 69 42 77 61 57 4e 76 51 31   VjcmV0OiBwaWNvQ1
0030  52 47 65 31 49 7a 4e 45 52 4a 54 6b 64 66 54 45   RGe1IzNERJTkdfTE
0040  39 4c 5a 46 38 3d                                 9LZF8=

# Note: ? didn't get full data 564768706379427063794230614755676332566a636d56304f69427761574e7651315247? 

AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
import base64

def decrypt_hex() -> None:
    encoded_hex = "564768706379427063794230614755676332566a636d56304f69427761574e76513152476531497a4e45524a546b64665445394c5a46383d"
    encoded_byte = bytes.fromhex(encoded_hex)                         # Decode from hex to bytes
    encoded_string = encoded_byte.decode('utf-8', errors='ignore')    # Convert bytes to string
    print(encoded_string)

    decoded_string = base64.b64decode(encoded_string)
    print(decoded_string)

if __name__ == "__main__":
    decrypt_hex()

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
b'This is the secret: picoCTF{R34DING_LOKd_' 👀

# After get secret use on flag.zip
# Note: Order matters when doing -P ❤️
AsianHacker-picoctf@webshell:~$ unzip -P "picoCTF{R34DING_LOKd_" flag.zip ⌨️
Archive:  flag.zip
 extracting: flag                    
AsianHacker-picoctf@webshell:~$ file flag ⌨️
flag: ASCII text
AsianHacker-picoctf@webshell:~$ cat flag ⌨️
picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6} 🔐
```

## Flag
picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6}

## Continue
[Continue](./picoGym0420.md)