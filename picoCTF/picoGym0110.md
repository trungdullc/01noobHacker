# picoGym Level 110: Wireshark twoo twooo two twoo...
Source: https://play.picoctf.org/practice/challenge/110

## Goal
Can you find the flag? shark2.pcapng.<br>
https://mercury.picoctf.net/static/0fe13a33318e756f71c35cb490e64c81/shark2.pcapng

## What I learned
```
wireshark
tshark
    -r shark2.pcapng → Read packets from the capture file shark2.pcapng instead of live capture
    -q → “Quiet” mode. Suppresses normal packet-by-packet output. Used when you only want statistics or summaries
    -z io,phs → Generate a statistics report
        -z produce a statistics output after processing the file
        io,phs means Protocol Hierarchy Statistics
    -y applies Wireshark Filter ❤️❤️❤️❤️❤️
```

## Solution
```
https://webshell.picoctf.org/

# Start in Statistics → Protocol Hierarchy
# Note: Mime
# Right Click: Apply as Filter → Selected

Filter: mime_multipart ⌨️
# Note: High HTTP request
# Analyze Follow HTTP Stream
# Increase stream and notice flag in stream 6

GET /flag HTTP/1.1
Host: 18.217.1.57
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 73
Server: Werkzeug/1.0.1 Python/3.6.9
Date: Mon, 10 Aug 2020 01:39:19 GMT

picoCTF{bfe48e8500c454d647c55a4471985e776a07b26cba64526713f43758599aa98b} 👀

Filter: tcp.stream eq 6 ⌨️
49	1.441753	192.168.38.104	18.217.1.57	TCP	66	63637 → 80 [SYN] Seq=0 Win=62727 Len=0 MSS=8961 WS=256 SACK_PERM
53	1.491890	18.217.1.57	192.168.38.104	TCP	66	80 → 63637 [SYN, ACK] Seq=0 Ack=1 Win=62727 Len=0 MSS=1460 SACK_PERM WS=128
54	1.491925	192.168.38.104	18.217.1.57	TCP	54	63637 → 80 [ACK] Seq=1 Ack=1 Win=262656 Len=0
739	4.768140	192.168.38.104	18.217.1.57	HTTP	477	GET /flag HTTP/1.1 
742	4.818410	18.217.1.57	192.168.38.104	TCP	54	80 → 63637 [ACK] Seq=1 Ack=424 Win=62336 Len=0
743	4.819740	18.217.1.57	192.168.38.104	TCP	71	80 → 63637 [PSH, ACK] Seq=1 Ack=424 Win=62336 Len=17 [TCP PDU reassembled in 744]
744	4.819777	18.217.1.57	192.168.38.104	HTTP	263	HTTP/1.0 200 OK  (text/html) 👀
745	4.819802	192.168.38.104	18.217.1.57	TCP	54	63637 → 80 [ACK] Seq=424 Ack=228 Win=262400 Len=0
746	4.841199	192.168.38.104	18.217.1.57	TCP	54	63637 → 80 [FIN, ACK] Seq=424 Ack=228 Win=262400 Len=0
747	4.891437	18.217.1.57	192.168.38.104	TCP	54	80 → 63637 [ACK] Seq=228 Ack=425 Win=62336 Len=0

0000   02 3b c6 1a ae f5 02 fb 68 4c e9 41 08 00 45 00   .;......hL.A..E.
0010   00 f9 96 20 40 00 24 06 c4 bc 12 d9 01 39 c0 a8   ... @.$......9..
0020   26 68 00 50 f8 95 a3 7f 71 ef bb 0b 06 d5 50 19   &h.P....q.....P.
0030   01 e7 bd 67 00 00 43 6f 6e 74 65 6e 74 2d 54 79   ...g..Content-Ty
0040   70 65 3a 20 74 65 78 74 2f 68 74 6d 6c 3b 20 63   pe: text/html; c
0050   68 61 72 73 65 74 3d 75 74 66 2d 38 0d 0a 43 6f   harset=utf-8..Co
0060   6e 74 65 6e 74 2d 4c 65 6e 67 74 68 3a 20 37 33   ntent-Length: 73
0070   0d 0a 53 65 72 76 65 72 3a 20 57 65 72 6b 7a 65   ..Server: Werkze
0080   75 67 2f 31 2e 30 2e 31 20 50 79 74 68 6f 6e 2f   ug/1.0.1 Python/
0090   33 2e 36 2e 39 0d 0a 44 61 74 65 3a 20 4d 6f 6e   3.6.9..Date: Mon
00a0   2c 20 31 30 20 41 75 67 20 32 30 32 30 20 30 31   , 10 Aug 2020 01
00b0   3a 33 39 3a 31 39 20 47 4d 54 0d 0a 0d 0a 70 69   :39:19 GMT....pi
00c0   63 6f 43 54 46 7b 62 66 65 34 38 65 38 35 30 30   coCTF{bfe48e8500
00d0   63 34 35 34 64 36 34 37 63 35 35 61 34 34 37 31   c454d647c55a4471
00e0   39 38 35 65 37 37 36 61 30 37 62 32 36 63 62 61   985e776a07b26cba
00f0   36 34 35 32 36 37 31 33 66 34 33 37 35 38 35 39   64526713f4375859
0100   39 61 61 39 38 62 7d                              9aa98b} 👀

https://www.dcode.fr/cipher-identifier
    SHA-256	👀
    Hexadecimal Data
Note: Didn't work there was also more than one picoCTF flag

# Method 1:
Filter: dns && ip.dst==18.217.1.57 && dns.qry.name contains local ⌨️
1637	9.440363	192.168.38.104	18.217.1.57	DNS	109	Standard query 0x1dd2 A cGljb0NU👀.reddshrimpandherring.com.windomain.local
2046	11.972605	192.168.38.104	18.217.1.57	DNS	109	Standard query 0xabb9 A RntkbnNf👀.reddshrimpandherring.com.windomain.local
2448	14.605726	192.168.38.104	18.217.1.57	DNS	109	Standard query 0x9e21 A M3hmMWxf👀.reddshrimpandherring.com.windomain.local
3153	16.506492	192.168.38.104	18.217.1.57	DNS	109	Standard query 0x2ee1 A ZnR3X2Rl👀.reddshrimpandherring.com.windomain.local
3442	18.340155	192.168.38.104	18.217.1.57	DNS	109	Standard query 0x2a4b A YWRiZWVm👀.reddshrimpandherring.com.windomain.local
3982	20.369626	192.168.38.104	18.217.1.57	DNS	105	Standard query 0x4068 A fQ==👀.reddshrimpandherring.com.windomain.local
4374	22.583745	192.168.38.104	18.217.1.57	DNS	105	Standard query 0x7418 A fQ==.reddshrimpandherring.com.windomain.local

# Note: cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==
https://www.dcode.fr/cipher-identifier
    Base64 Coding
https://www.dcode.fr/base-64-encoding
    base64	picoCTF{dns_3xf1l_ftw_deadbeef} 🔐

# Method 2: tshark
AsianHacker-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/0fe13a33318e756f71c35cb490e64c81/shark2.pcapng ⌨️
--2025-09-17 17:45:10--  https://mercury.picoctf.net/static/0fe13a33318e756f71c35cb490e64c81/shark2.pcapng
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3520112 (3.4M) [application/octet-stream]
Saving to: 'shark2.pcapng'

shark2.pcapng                                              100%[======================================================================================================================================>]   3.36M  1.83MB/s    in 1.8s    

2025-09-17 17:45:12 (1.83 MB/s) - 'shark2.pcapng' saved [3520112/3520112]

AsianHacker-picoctf@webshell:~$ tshark -qz io,phs -r shark2.pcapng ⌨️

===================================================================
Protocol Hierarchy Statistics
Filter: 

eth                                      frames:4831 bytes:3355920
  ip                                     frames:4829 bytes:3355822
    tcp                                  frames:3276 bytes:3120750
      tls                                frames:71 bytes:115780
        tcp.segments                     frames:2 bytes:6576
      http                               frames:802 bytes:1879844
        tcp.segments                     frames:299 bytes:1605841
        mime_multipart                   frames:309 bytes:194144
          tcp.segments                   frames:309 bytes:194144
        data-text-lines                  frames:91 bytes:23987
          tcp.segments                   frames:90 bytes:23696
        xml                              frames:1 bytes:579
    udp                                  frames:1553 bytes:235072
      gquic                              frames:41 bytes:11668
      dns                                frames:1512 bytes:223404
  arp                                    frames:2 bytes:98
===================================================================

# Scan streams
AsianHacker-picoctf@webshell:~$ tshark -qz follow,tcp,ascii,5 -r shark2.pcapng ⌨️

===================================================================
Follow: tcp,ascii
Filter: tcp.stream eq 5
Node 0: 192.168.38.104:63636
Node 1: 18.217.1.57:80
445
GET / HTTP/1.1
Host: 18.217.1.57
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9


        17
HTTP/1.0 200 OK

        235
Content-Type: text/html; charset=utf-8
Content-Length: 99
Server: Werkzeug/1.0.1 Python/3.6.9
Date: Mon, 10 Aug 2020 01:39:16 GMT

The official Red's Shrimp and Herring website is still under construction. Please check back later!

AsianHacker-picoctf@webshell:~$ tshark -nr shark2.pcapng -Y 'frame contains "pico"' -T fields -e text ⌨️
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{bfe48e8500c454d647c55a4471985e776a07b26cba64526713f43758599aa98b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{bda69bdf8f570a9aaab0e4108a0fa5f64cb26ba7d2269bb63f68af5d98b98245}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{fe83bcb6cfd43d3b79392f6a4232685f6ed4e7a789c2ce559cf3c1ab6adbe34b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{711d3893d90f100c15e10ef4842abeed3a830f8237c1257cd47389646da97810}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{3cf1e22d489fcfb6bb312a34f46c8699989ed043406134331452d11ce73cd59e}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{b4cc138bb0f7f9da7e35085e349555aa6d00bdca3b021c1fe8663c0a422ce0d7}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{41b8a1a796bd8d202016f75bc5b38889e9ea06007e6b22fc856d380fb7573133}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{9812bc4be04e6f9c803152313db3da53b3dfb799bdb05aac46fa0dd0045d2fc2}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{64cf3ede3736a340fdf2954be5151ce53bec291c5e48cbccb44faa529946e249}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{c50d259a4e172fcb2eddbabeebd272473e4882b76c9efcd12c03ac04429d884a}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{0a024b7d39603756feafa2bbaa1603b14a99eae5dcd59f1d957f511d822c8c06}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{97211eec9228bb247d762527bace8b3e4ec2110c8834af12aefd3c552cdc21b2}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{29679910c47d8afc737a1c21d7bf758cd3d81001bdbeec8c6f81a6ad88fdc279}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{996979e9540be0fe9320e80eb6336047f8140a80830700907b99741310acf08f}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{8b272a18c1005c95a420d4a0df426cb8441d29eb96210493a96fa25ac5e657aa}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{e1d0a752dc71121200f4bcb1b8cc2e03e84488df229b82196afbe0045ef025c4}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{0ba511844a2ab38fe0709bcdb2b8bdfeb37a0b466dc902e92062db4c2b3f455c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{dadda48e855421e14597ffc727943b57efd8c9a15d10bfd491f0390659162fb1}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{f4dd87795395c74f3083f8caa4ec22d1531281554a6003d1c47c5f0370984ab6}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{0f30a584680db9e70c7e1c6ca954c2f023b77f3fd2b05bd9aeee6e00dc4da5d7}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{715e4d0d167e862af8825f62d3f4ff8aef20443445a06b1c68572390a2825d29}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7654ee03f31576e8ed44799fc4fa5ee053d35050000502e878d1fb8022618923}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{068606b5faca0491d97a2b46fdca7f6f81acbd909ce691077fe77e03a3c0939a}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{64ab681ffed33c49b5e8ae0576e22857e9a10ae30cdbee415fb514b84aa58aea}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{8ae3995e726f8f2c3724e2e0522f038aba6649facd378d8965c648233d79a252}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{1c125d267b5811cd25cca2d517e022270aa60f3c8461f4097c685bcca637a6a9}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{824c298d14e1fe369df991af72ab0725d2e7c7d05b9655486873ccc467f4bd6b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{e1d8dd1b73d5fd7704a16c924ddee69dc6bf9beef14cc3a10142704b81f0fa07}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{82d260fe0670d551347b164c54183d996c52ebeebb1ccfcc2c2ebb91268dc944}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{74876fc61ebc9c902f8983979cd4c21206c69a23f0dcc0817e150dd75e446838}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{49c52d1f30973f90716bbcbe3633e11cf70b9a31ed785871ccb80473302a59db}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{89d93dbb96a3857ac87ba0cea3c10a9e4c7b34d79b2edb463cef030d34297bd0}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{5ceacdce54c13a3fddfcfb225a00247304fbb15f29f9c90434383f277567992d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{c22a40a43ed7034bd935805f59603a46d3a1f2d6b8e31281eb0721597b6c6d62}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{6071bca5da06d4f975a52357cda0cd6f0614787c1c70b1b7e1af2c7fb272d281}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{65a8b141f019506feea38a119988ad645bcab1a5fa8693efdf26e1fd3cb44b4c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{d7f5cb78a895d3805601522b95d599cb6d2689c6a856e3fbee6aac2fca0c20f3}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{739bb0f0aa17331819a0e942d37bfee757c8d9cd089cdfe32509027b92485213}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7a891e2c4ad0da374bc15ad7ad0ee081077dd376f06152781f780c201691713d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{a97d3ee943221888bd1157429e4a00ed5e9905a610e64664f7e36c7f5e0a4ef9}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{c38d2d74dc21bbb2e3a95b52e2354ee523379cfe4f8b348c9c5b5d7bd7cb871b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{e4dc886c39a53ff118bf29041067cde48dcebb89b3dae61a8aba6187d671999a}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{9fbd0d18aa1abfd289ba977ae4354b821cc74591260889afba1b0b6e7763aa31}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{3fc0801bcd36336a2c030c6e5f452f5795be1d562e00411365fb64c6a2f688ef}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{4aa86643eb2ddb5709725344cd0e63e6c52e35c2e64a39f3a4a0ee7bbd5d3ade}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{4af8df415d17e6df99a5efddebcb33a68c0c8bf26d481eed16b5f77675030d7f}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{e4f52a0d2a924906ac102a32c52ab9128bf9cd6e5294518ad3ed6748f853b0ab}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{cc104e74a9f50164ee5652d168ef38a21b7a2d5e3196062e669e3a2705f1a0d3}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{2aac620b0bdd2e6946d62c5d232ca32ba1f5a9d8ec82c060778b54ffeb8fbd1f}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{4e55be07159def207afc142954f5673a0651d5f32f5f4090fb774d960628e352}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{983e5e2703a132a49479e438bfba15ee5d02345b03d410b8163b685973937da7}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{d342a46e8179de9941720c5e0eeac0d0fae9d3014d2ddcf531a7865a997b00e5}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{2133904cfe757bc6c68c3e5f3749b37d67d7fa6ffb2768410be593d3fe8c4bd4}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{29b726b9a57d176e1487d159474ee7e6508b66c05c526a00c942a8cebb6bb496}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7302b0dca07cd890c75e38d78d7e74d7bbf2b932f555aaf5b6754f56e778e3fc}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{22e018bb8282e9d7852ed4e65f70a26524dabef78cf41e1db45c070c94621c57}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{40f366ccf0f6462f5b8b1dc4d7384a62aa95565afcaad96a937b8c1f1134099b}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{db38cbc215cde0d9cd52cbca2390defdb54303e998019a5c4ddaf9861b54efcb}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{090fa8ec995ab9fc9f97cbe9ea36cb81c4504a3ca02466ddd207cfe7f785cb5c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{947b91a983c93217304f8e5b112e93eaf619e6a9386ab93be93a9b67e53b2fda}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{a3ed2f602322f749f4cb016515e25b67749efd08ac2f2c53023596cbf0dcbd0f}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{8e625859eb325d2a69934e4a44c93fcc132e813efb3fdaaa5143147678e9cbf9}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{8d43c4889ee5b507d1785adfa2592f2fb3d7cf20ebf37ce46595edc46fba3f6d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{0020d021e9e38dbb5a5fa432175089d8b76e4a900618c95f8cae14fedaa45b63}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{69e96b10f560a6a0656a6d950e73e41bcf4226c424bb5622839dda0c66755b14}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{34c6ca47d858ab18aa2008f4ac31c31570c46186939e6b46458b19082122d4bd}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{ebfcebe696b1fdbba2abb3b003165152456bd83b6ddfbf180ca366de0dec1b0c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{aa125aaeb4723f69dceaa90125a8099a6f3fe0259e068fd82dcbeb76131448bb}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{80d65857d8d81a92769e8cd136376522d113c4298b331318ce7adcbf5e70104d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{00ae773ce4a4b3cf3287f072c13ec7139a74207de635de9d115087bc4f312bae}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7e808778b7250893922a17d53f10365b009a7624935850ac5c8140461e49d579}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{33e80d6e9f56c1f7705c73566d347ccb32b4662171f224b6dfcb6c8fce4f1601}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{5d921ffbe2709ba82d09603a095530aedae41ab96fd052140cbc64319b7ab0ac}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{977b385d5dd6abde9cb89ee940b5cfb7179d73d989c6993346d278bff003c154}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{ca7d3b029817de8f318d8fa521ad1b569f4e8a37358373193522cc7f5628ed49}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{a820680ab6444b1daf5281192f337aefb4aa95a313c9f270804ef7826ecc298c}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{998d01dadf1b44eb4ec7b7e8fa11f11bcd2d7d86f3f9e4966dde22d4a84ca113}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{cb8fe3ec65f890e2f0570c98c4edd3fe4115bc059ac2afb39300c7b66f2302c4}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{bc2af8cbe0ae0befdd28b14412295243354cd3c7cc74e88d8facb2fd5e6ef34d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{09082a0313e16fc36f8076ff86e54e83048a8568f5c2294fea5fb3bcd212e7f2}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{2386746aeb258914349dc81a85cb5de72e47930c7f11759b4ad9f864efa7b5aa}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{173306d7b886423d9f79d3d0d05209807ae7b83c445931319830e4e0ad2d2f09}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{6cb98e2295bbe1f15fd8b8b5908de360d386b98a0ce7e0407e001b453b05be22}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{132e643c8fdadb54c366072cb33940411fcfd355209fc1ce9b2022ad1cd1b060}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{044ffca72f0f191b0715ff1a9bff182c810cb2786370cbf8cdc1943c2e7aedf6}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{b278104c2602442e3db401749c30527d80ba560f9a02c939cb4ff6ea189a140d}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{7282e048d6d32383b65f3a03b1101219ac73f7f538446b78d1b2b334e0985447}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{98406c4acbf0f57b3ccbc923aab5a603d70f86d507f422d9bd8656398f53433e}
Timestamps,HTTP/1.0 200 OK\r\n,\r\n,picoCTF{3fe0b2788f30d9cb9f77d3b2752f13c554fe7f0e7a2883e57c8a44b34f35675c}

# All fake flags try another protocol dns
AsianHacker-picoctf@webshell:~$ tshark -nr shark2.pcapng -Y 'dns' | head ⌨️
  791   7.931626 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x76aa A lDqoR16q.reddshrimpandherring.com
  792   7.943025      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x76aa No such name A lDqoR16q.reddshrimpandherring.com SOA a.gtld-servers.net
  793   7.947216 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcdd5 A lDqoR16q.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
  794   7.957680      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xcdd5 No such name A lDqoR16q.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
  795   7.958549 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5d2d A lDqoR16q.reddshrimpandherring.com.windomain.local
  796   7.967998      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5d2d No such name A lDqoR16q.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
  797   7.968981 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc847 A 1Th0dQuT.reddshrimpandherring.com
  798   8.049550      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc847 No such name A 1Th0dQuT.reddshrimpandherring.com SOA a.gtld-servers.net
  799   8.050527 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x21a5 A 1Th0dQuT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
  800   8.061483      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x21a5 No such name A 1Th0dQuT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
===================================================================

# Try to access domain reddshrimpandherring.com
AsianHacker-picoctf@webshell:~$ curl http://www.reddshrimpandherring.com ⌨️
curl: (6) Could not resolve host: www.reddshrimpandherring.com

# Apply Wireshark Filter in tshark with -Y ⌨️
AsianHacker-picoctf@webshell:~$ tshark -nr shark2.pcapng -Y 'dns && ip.dst==18.217.1.57 && dns.qry.name contains "local"' ⌨️❤️❤️❤️❤️❤️
 1637   9.440363 192.168.38.104 ? 18.217.1.57  DNS 109 Standard query 0x1dd2 A cGljb0NU.reddshrimpandherring.com.windomain.local
 2046  11.972605 192.168.38.104 ? 18.217.1.57  DNS 109 Standard query 0xabb9 A RntkbnNf.reddshrimpandherring.com.windomain.local
 2448  14.605726 192.168.38.104 ? 18.217.1.57  DNS 109 Standard query 0x9e21 A M3hmMWxf.reddshrimpandherring.com.windomain.local
 3153  16.506492 192.168.38.104 ? 18.217.1.57  DNS 109 Standard query 0x2ee1 A ZnR3X2Rl.reddshrimpandherring.com.windomain.local
 3442  18.340155 192.168.38.104 ? 18.217.1.57  DNS 109 Standard query 0x2a4b A YWRiZWVm.reddshrimpandherring.com.windomain.local
 3982  20.369626 192.168.38.104 ? 18.217.1.57  DNS 105 Standard query 0x4068 A fQ==.reddshrimpandherring.com.windomain.local
 4374  22.583745 192.168.38.104 ? 18.217.1.57  DNS 105 Standard query 0x7418 A fQ==.reddshrimpandherring.com.windomain.local
```

## Flag
picoCTF{dns_3xf1l_ftw_deadbeef}

## Continue
[Continue](./picoGym0139.md)