# picoGym Level 460: RED
Source: https://play.picoctf.org/practice/challenge/460

## Goal
RED, RED, RED, RED<br>
Download the image: red.png<br>
https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png

## What I learned
```
zsteg is a Ruby tool for detecting and extracting steganography from PNG/BMP images

zsteg red.png runs many different checks (LSB and MSB/various planes/channels)
    --lsb restricts the tests to LSB-type extractions only
    b1, b2, ... = bit plane (b1 is the least-significant bit plane, b2 the next bit)
    rgba, rgb, g, b, ... = channel(s) used for extraction
    lsb / msb = whether it read least-significant or most-significant bits
    xy = the scan/order used (x-y scanning)
    So b1,rgba,lsb,xy means “read the LSB (bit 0) from the R,G,B,A channels in XY order.”

AperiSolve used many methods on the file but online results:
https://www.aperisolve.com/fbe65d07ba29998b16639b8b586444f7 ❤️❤️❤️❤️❤️

Image Modifier (not good):
https://www.georgeom.net/StegOnline/image
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_verbal_sleep/ 831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png ⌨️
--2025-09-13 03:38:35--  https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.95, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 796 [application/octet-stream]
Saving to: 'red.png'

red.png                                                    100%[======================================================================================================================================>]     796  --.-KB/s    in 0s      

2025-09-13 03:38:35 (201 MB/s) - 'red.png' saved [796/796]

AsianHacker-picoctf@webshell:~$ steghide extract -sf red.png ⌨️
Enter passphrase: 
steghide: the file format of the file "red.png" is not supported.

AsianHacker-picoctf@webshell:~$ strings red.png ⌨️
IHDR
tEXtPoem
Crimson heart, vibrant and bold, 👀
Hearts flutter at your sight.
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke.x 👀
IDATx
IEND

AsianHacker-picoctf@webshell:~$ exiftool red.png ⌨️
ExifTool Version Number         : 12.40
File Name                       : red.png
Directory                       : .
File Size                       : 796 bytes
File Modification Date/Time     : 2025:03:06 03:34:15+00:00
File Access Date/Time           : 2025:09:13 03:39:38+00:00
File Inode Change Date/Time     : 2025:09:13 03:38:35+00:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 128
Image Height                    : 128
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke. 👀
Image Size                      : 128x128
Megapixels                      : 0.016

AsianHacker-picoctf@webshell:~$ hexdump -C red.png ⌨️
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
00000010  00 00 00 80 00 00 00 80  08 06 00 00 00 c3 3e 61  |..............>a|
00000020  cb 00 00 00 e7 74 45 58  74 50 6f 65 6d 00 43 72  |.....tEXtPoem.Cr| 👀
00000030  69 6d 73 6f 6e 20 68 65  61 72 74 2c 20 76 69 62  |imson heart, vib|
00000040  72 61 6e 74 20 61 6e 64  20 62 6f 6c 64 2c 0a 48  |rant and bold,.H|
00000050  65 61 72 74 73 20 66 6c  75 74 74 65 72 20 61 74  |earts flutter at|
00000060  20 79 6f 75 72 20 73 69  67 68 74 2e 0a 45 76 65  | your sight..Eve|
00000070  6e 69 6e 67 73 20 67 6c  6f 77 20 73 6f 66 74 6c  |nings glow softl|
00000080  79 20 72 65 64 2c 0a 43  68 65 72 72 69 65 73 20  |y red,.Cherries |
00000090  62 75 72 73 74 20 77 69  74 68 20 73 77 65 65 74  |burst with sweet|
000000a0  20 6c 69 66 65 2e 0a 4b  69 73 73 65 73 20 6c 69  | life..Kisses li|
000000b0  6e 67 65 72 20 77 69 74  68 20 79 6f 75 72 20 77  |nger with your w|
000000c0  61 72 6d 74 68 2e 0a 4c  6f 76 65 20 64 65 65 70  |armth..Love deep|
000000d0  20 61 73 20 6d 65 72 6c  6f 74 2e 0a 53 63 61 72  | as merlot..Scar|
000000e0  6c 65 74 20 6c 65 61 76  65 73 20 66 61 6c 6c 69  |let leaves falli|
000000f0  6e 67 20 73 6f 66 74 6c  79 2c 0a 42 6f 6c 64 20  |ng softly,.Bold |
00000100  69 6e 20 65 76 65 72 79  20 73 74 72 6f 6b 65 2e  |in every stroke.|
00000110  78 95 9d 15 00 00 01 f0  49 44 41 54 78 9c ed d2  |x.......IDATx...|
00000120  4b 72 02 31 00 03 51 29  f7 3f 33 ca c2 1e 92 22  |Kr.1..Q).?3...."|
00000130  b9 41 f7 db 50 30 fe 8c  4d f7 d5 be b2 34 dd 92  |.A..P0..M....4..|
00000140  36 c9 9a dd 9f 92 35 c9  92 24 4d b6 34 69 9a 9d  |6.....5..$M.4i..|
00000150  27 c7 7a 7f 4f f6 8c 4b  db 2d 6b d6 a4 3b c3 97  |'.z.O..K.-k..;..|
00000160  ae cf f8 3b 39 4d ba 24  5d b6 f7 fa bf 3d df fa  |...;9M.$]....=..|
00000170  bc 4d f3 1e bf 76 d9 ce  b3 9f 95 72 17 69 96 8f  |.M...v.....r.i..|
00000180  d5 9e e9 e7 3d df e7 79  ce 7b e7 f5 bf f5 97 ee  |....=..y.{......|
00000190  8c 5f 7a 4e db 7b 59 d9  99 bf 8f f7 5f bb 73 fc  |._zN.{Y....._.s.|
000001a0  e7 79 ee 21 ef fd dc 7d  da 67 bf 3b 2d f7 be ef  |.y.!...}.g.;-...|
000001b0  fc fb 52 e7 78 f7 7e b3  9f fd f6 eb 6e fa 79 e0  |..R.x.~.....n.y.|
000001c0  e7 6f cd dd 38 db f9 fc  fa 3b 50 24 06 00 67 00  |.o..8....;P$..g.|
000001d0  70 06 00 67 00 70 06 00  67 00 70 06 00 67 00 70  |p..g.p..g.p..g.p|
000001e0  06 00 67 00 70 06 00 67  00 70 06 00 67 00 70 06  |..g.p..g.p..g.p.|
000001f0  00 67 00 70 06 00 67 00  70 06 00 67 00 70 06 00  |.g.p..g.p..g.p..|
00000200  67 00 70 06 00 67 00 70  06 00 67 00 70 06 00 67  |g.p..g.p..g.p..g|
00000210  00 70 06 00 67 00 70 06  00 67 00 70 06 00 67 00  |.p..g.p..g.p..g.|
00000220  70 06 00 67 00 70 06 00  67 00 70 06 00 67 00 70  |p..g.p..g.p..g.p|
00000230  06 00 67 00 70 06 00 67  00 70 06 00 67 00 70 06  |..g.p..g.p..g.p.|
00000240  00 67 00 70 06 00 67 00  70 06 00 67 00 70 06 00  |.g.p..g.p..g.p..|
00000250  67 00 70 06 00 67 00 70  06 00 67 00 70 06 00 67  |g.p..g.p..g.p..g|
00000260  00 70 06 00 67 00 70 06  00 67 00 70 06 00 67 00  |.p..g.p..g.p..g.|
00000270  70 06 00 67 00 70 06 00  67 00 70 06 00 67 00 70  |p..g.p..g.p..g.p|
00000280  06 00 67 00 70 06 00 67  00 70 06 00 67 00 70 06  |..g.p..g.p..g.p.|
00000290  00 67 00 70 06 00 67 00  70 06 00 67 00 70 06 00  |.g.p..g.p..g.p..|
000002a0  67 00 70 06 00 67 00 70  06 00 67 00 70 06 00 67  |g.p..g.p..g.p..g|
000002b0  00 70 06 00 67 00 70 06  00 67 00 70 06 00 67 00  |.p..g.p..g.p..g.|
000002c0  70 06 00 67 00 70 06 00  67 00 70 06 00 67 00 70  |p..g.p..g.p..g.p|
000002d0  06 00 67 00 70 06 00 67  00 70 06 00 67 00 70 06  |..g.p..g.p..g.p.|
000002e0  00 67 00 70 06 00 67 00  70 06 00 67 00 70 06 00  |.g.p..g.p..g.p..|
000002f0  67 00 70 06 00 67 00 70  06 00 67 00 70 06 00 67  |g.p..g.p..g.p..g|
00000300  00 70 06 00 67 00 70 df  b1 fb 76 ff 26 9b d6 91  |.p..g.p...v.&...|
00000310  00 00 00 00 49 45 4e 44  ae 42 60 82              |....IEND.B`.|
0000031c

# The above found nothing but maybe a hint
# Look at uppercase and spells out: CHECK LSB 👀👀👀👀👀

# Method 1:
# Use zsteg
AsianHacker-picoctf@webshell:~$ zsteg red.png ⌨️
meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."
b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ== 👀"
b1,rgba,msb,xy      .. file: OpenPGP Public Key
b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"
b2,rgb,lsb,xy       .. file: OpenPGP Secret Key
b2,bgr,msb,xy       .. file: OpenPGP Public Key
b2,rgba,lsb,xy      .. file: OpenPGP Secret Key
b2,rgba,msb,xy      .. text: "CIkiiiII"
b2,abgr,lsb,xy      .. file: OpenPGP Secret Key
b2,abgr,msb,xy      .. text: "iiiaakikk"
b3,rgba,msb,xy      .. text: "#wb#wp#7p"
b3,abgr,msb,xy      .. text: "7r'wb#7p"
b4,b,lsb,xy         .. file: 0421 Alliant compact executable not stripped
AsianHacker-picoctf@webshell:~$ zsteg --lsb red.png ⌨️❤️
meta Poem           .. text: "Crimson heart, vibrant and bold,\nHearts flutter at your sight.\nEvenings glow softly red,\nCherries burst with sweet life.\nKisses linger with your warmth.\nLove deep as merlot.\nScarlet leaves falling softly,\nBold in every stroke."
b1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ== 👀"
b2,g,lsb,xy         .. text: "ET@UETPETUUT@TUUTD@PDUDDDPE"
b2,rgb,lsb,xy       .. file: OpenPGP Secret Key
b2,rgba,lsb,xy      .. file: OpenPGP Secret Key
b2,abgr,lsb,xy      .. file: OpenPGP Secret Key
b4,b,lsb,xy         .. file: 0421 Alliant compact executable not stripped

AsianHacker-picoctf@webshell:~$ echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d ⌨️
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_} 🔐

Method 2: CyberChef open file as input
# Note: Don't click remove image
https://cyberchef.io/#recipe=Extract_LSB('R','G','B','A','Row',0)From_Base64('A-Za-z0-9%2B/%3D',true)

picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_} 🔐
```

## Flag
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

## Continue
[Continue](./picoGym0459.md)