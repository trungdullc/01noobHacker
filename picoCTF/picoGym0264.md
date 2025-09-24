# picoGym Level 264: Eavesdrop
Source: https://play.picoctf.org/practice/challenge/264

## Goal
Download this packet capture and find the flag<br>
https://artifacts.picoctf.net/c/133/capture.flag.pcap

## What I learned
```
openssl
xxd                     # convert hex to binary

wireshark
```

## Solution
```
https://webshell.picoctf.org/

# Method 1: Wireshark
Filter: tcp contains "picoCTF" ⌨️
Result: Nothing
Filter: Filter: frame matches "[a-zA-Z]{7}\\{" ⌨️
Result: Nothing

Filter: tcp.stream eq 0 ⌨️
    Hey, how do you decrypt this file again?
    You're serious?
    Yeah, I'm serious
    *sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123 👀
    Ok, great, thanks.
    Let's use Discord next time, it's more secure.
    C'mon, no one knows we use this program like this!
    Whatever.
    Hey.
    Yeah?
    Could you transfer the file to me again?
    Oh great. Ok, over 9002? 👀
    Yeah, listening.
    Sent it
    Got it.
    You're unbelievable

Filter: tcp.port == 9002 ⌨️
54	205.301478	10.0.2.15	10.0.2.4	TCP	74	56370 → 9002 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM TSval=3517420531 TSecr=0 WS=128
55	205.302375	10.0.2.4	10.0.2.15	TCP	74	9002 → 56370 [SYN, ACK] Seq=0 Ack=1 Win=65160 Len=0 MSS=1460 SACK_PERM TSval=1765870695 TSecr=3517420531 WS=128
56	205.302451	10.0.2.15	10.0.2.4	TCP	66	56370 → 9002 [ACK] Seq=1 Ack=1 Win=64256 Len=0 TSval=3517420531 TSecr=1765870695
57	205.302713	10.0.2.15	10.0.2.4	TCP	114	56370 → 9002 [PSH, ACK] Seq=1 Ack=1 Win=64256 Len=48 👀 TSval=3517420532 TSecr=1765870695
58	205.303662	10.0.2.4	10.0.2.15	TCP	66	9002 → 56370 [ACK] Seq=1 Ack=49 Win=65152 Len=0 TSval=1765870696 TSecr=3517420532
61	217.183803	10.0.2.4	10.0.2.15	TCP	66	9002 → 56370 [FIN, ACK] Seq=1 Ack=49 Win=65152 Len=0 TSval=1765882575 TSecr=3517420532
62	217.184036	10.0.2.15	10.0.2.4	TCP	66	56370 → 9002 [FIN, ACK] Seq=49 Ack=2 Win=64256 Len=0 TSval=3517432413 TSecr=1765882575
63	217.184826	10.0.2.4	10.0.2.15	TCP	66	9002 → 56370 [ACK] Seq=2 Ack=50 Win=65152 Len=0 TSval=1765882577 TSecr=3517432413

Frame 57: 114 bytes on wire (912 bits), 114 bytes captured (912 bits)
Ethernet II, Src: PCSSystemtec_af:39:9f (08:00:27:af:39:9f), Dst: PCSSystemtec_93:ce:73 (08:00:27:93:ce:73)
Internet Protocol Version 4, Src: 10.0.2.15, Dst: 10.0.2.4
Transmission Control Protocol, Src Port: 56370, Dst Port: 9002, Seq: 1, Ack: 1, Len: 48
Data (48 bytes)
    Data: 53616c7465645f5fd30c863ca650da1fff4fbe72a086457e63626beda615c692cdd27026ae7deea6d1e918b3d40a7f46 👀
    [Length: 48]

0000   08 00 27 93 ce 73 08 00 27 af 39 9f 08 00 45 00   ..'..s..'.9...E.
0010   00 64 ac 90 40 00 40 06 75 f1 0a 00 02 0f 0a 00   .d..@.@.u.......
0020   02 04 dc 32 23 2a 5e a2 8b c7 40 5f 54 6d 80 18   ...2#*^...@_Tm..
0030   01 f6 18 69 00 00 01 01 08 0a d1 a7 93 f4 69 41   ...i..........iA
0040   0c 67 53 61 6c 74 65 64 5f 5f d3 0c 86 3c a6 50   .gSalted__...<.P
0050   da 1f ff 4f be 72 a0 86 45 7e 63 62 6b ed a6 15   ...O.r..E~cbk...
0060   c6 92 cd d2 70 26 ae 7d ee a6 d1 e9 18 b3 d4 0a   ....p&.}........
0070   7f 46👀                                           .F 👀

# Right Click Copy Value and save into input.txt
53616c7465645f5fd30c863ca650da1fff4fbe72a086457e63626beda615c692cdd27026ae7deea6d1e918b3d40a7f46

# Reads hex string(s) in input.txt and converts them into raw binary, saving result in file.des3
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat input.txt ⌨️ 
53616c7465645f5fd30c863ca650da1fff4fbe72a086457e63626beda615c692cdd27026ae7deea6d1e918b3d40a7f46
AsianHacker-picoctf@webshell:/tmp$ xxd -r -p input.txt file.des3 ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat file.des3 ⌨️
Salted__
        <POrE~cbkƒp&}
Fi
ѧiA
   gSalted__
            <POrE~cbkƒp&}
F

# Decrypt
AsianHacker-picoctf@webshell:/tmp$ openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123 ⌨️
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
80ABE2C8CC7F0000:error:1C80006B:Provider routines:ossl_cipher_generic_block_final:wrong final block length:../providers/implementations/ciphers/ciphercommon.c:429:
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
file.des3  file.txt 👀  hsperfdata_root  input.txt  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ cat file.txt ⌨️
picoCTF{nc_73115_411_5786acc3}oqXseyq%Hܾ$JR~f$cs}( 🔐

# Method 2: tshark
AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/133/capture.flag.pcap ⌨️
--2025-09-18 05:53:14--  https://artifacts.picoctf.net/c/133/capture.flag.pcap
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.33, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7518 (7.3K) [application/octet-stream]
Saving to: 'capture.flag.pcap'

capture.flag.pcap                                          100%[======================================================================================================================================>]   7.34K  --.-KB/s    in 0s      

2025-09-18 05:53:15 (127 MB/s) - 'capture.flag.pcap' saved [7518/7518]

# Analyze Streams
AsianHacker-picoctf@webshell:~$ tshark -r capture.flag.pcap -q -z conv,tcp ⌨️
================================================================================
TCP Conversations
Filter:<No Filter>
                                                           |       <-      | |       ->      | |     Total     |    Relative    |   Duration   |
                                                           | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |
10.0.2.15:57876            <-> 10.0.2.4:9001                   17 1330 bytes      18 1411 bytes      35 2741 bytes    15.175413000       224.2402
10.0.2.15:43928            <-> 35.224.170.84:80                 5 442 bytes       5 377 bytes      10 819 bytes   165.383043000         0.5623
10.0.2.15:56370            <-> 10.0.2.4:9002                    4 272 bytes       4 320 bytes       8 592 bytes   205.301478000        11.8833
================================================================================

AsianHacker-picoctf@webshell:~$ tshark -r capture.flag.pcap -q -z follow,tcp,ascii,0 ⌨️
===================================================================
Follow: tcp,ascii
Filter: tcp.stream eq 0
Node 0: 10.0.2.15:57876
Node 1: 10.0.2.4:9001
        41
Hey, how do you decrypt this file again?

16
You're serious?

        18
Yeah, I'm serious

83
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123 👀

        19
Ok, great, thanks.

47
Let's use Discord next time, it's more secure.

        51
C'mon, no one knows we use this program like this!

10
Whatever.

        5
Hey.

6
Yeah?

        41
Could you transfer the file to me again?

25
Oh great. Ok, over 9002? 👀

        17
Yeah, listening.

8
Sent it

        8
Got it.

20
You're unbelievable

AsianHacker-picoctf@webshell:~$ tshark -r capture.flag.pcap -Y "tcp.port == 9002" ⌨️❤️❤️❤️❤️❤️
   54 205.301478    10.0.2.15 ? 10.0.2.4     TCP 74 56370 ? 9002 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1 TSval=3517420531 TSecr=0 WS=128
   55 205.302375     10.0.2.4 ? 10.0.2.15    TCP 74 9002 ? 56370 [SYN, ACK] Seq=0 Ack=1 Win=65160 Len=0 MSS=1460 SACK_PERM=1 TSval=1765870695 TSecr=3517420531 WS=128
   56 205.302451    10.0.2.15 ? 10.0.2.4     TCP 66 56370 ? 9002 [ACK] Seq=1 Ack=1 Win=64256 Len=0 TSval=3517420531 TSecr=1765870695
   57 205.302713    10.0.2.15 ? 10.0.2.4     TCP 114 56370 ? 9002 [PSH, ACK] Seq=1 Ack=1 Win=64256 Len=48 TSval=3517420532 TSecr=1765870695
   58 205.303662     10.0.2.4 ? 10.0.2.15    TCP 66 9002 ? 56370 [ACK] Seq=1 Ack=49 Win=65152 Len=0 TSval=1765870696 TSecr=3517420532
   61 217.183803     10.0.2.4 ? 10.0.2.15    TCP 66 9002 ? 56370 [FIN, ACK] Seq=1 Ack=49 Win=65152 Len=0 TSval=1765882575 TSecr=3517420532
   62 217.184036    10.0.2.15 ? 10.0.2.4     TCP 66 56370 ? 9002 [FIN, ACK] Seq=49 Ack=2 Win=64256 Len=0 TSval=3517432413 TSecr=1765882575
   63 217.184826     10.0.2.4 ? 10.0.2.15    TCP 66 9002 ? 56370 [ACK] Seq=2 Ack=50 Win=65152 Len=0 TSval=1765882577 TSecr=3517432413

AsianHacker-picoctf@webshell:~$ tshark -r capture.flag.pcap -q -z follow,tcp,ascii,2 ⌨️
===================================================================
Follow: tcp,ascii
Filter: tcp.stream eq 2
Node 0: 10.0.2.15:56370
Node 1: 10.0.2.4:9002
48
Salted__...<.P...O.r..E~cbk.......p&.}.......
.F 👀
===================================================================

AsianHacker-picoctf@webshell:~$ tshark -r capture.flag.pcap -q -z follow,tcp,raw,2 | tail -n +7 | head -n 1 | xxd -r -p > file.des3 ⌨️
AsianHacker-picoctf@webshell:~$ openssl des3 -d -salt -in file.des3 -k supersecretpassword123 ⌨️
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
picoCTF{nc_73115_411_5786acc3} 🔐
```

## Flag
picoCTF{nc_73115_411_5786acc3}

## Continue
[Continue](./picoGym0087.md)