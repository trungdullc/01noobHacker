# picoGym Level 350: hideme
Source: https://play.picoctf.org/practice/challenge/350

## Goal
The SOC analyst saw one image been sent back and forth between two people.<br>
They decided to investigate and found out that there was more than what meets the eye here.<br>
https://artifacts.picoctf.net/c/258/flag.png

## What I learned
```
binwalk -e
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/258/flag.png ⌨️
--2025-09-20 00:45:25--  https://artifacts.picoctf.net/c/258/flag.png
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 42937 (42K) [application/octet-stream]
Saving to: 'flag.png'

flag.png                                                   100%[======================================================================================================================================>]  41.93K  --.-KB/s    in 0.01s   

2025-09-20 00:45:25 (2.91 MB/s) - 'flag.png' saved [42937/42937]

AsianHacker-picoctf@webshell:~$ file flag.png ⌨️
flag.png: PNG image data, 512 x 504, 8-bit/color RGBA, non-interlaced
AsianHacker-picoctf@webshell:~$ exiftool flag.png 
ExifTool Version Number         : 12.40
File Name                       : flag.png
Directory                       : .
File Size                       : 42 KiB
File Modification Date/Time     : 2023:03:16 03:16:18+00:00
File Access Date/Time           : 2025:09:20 00:45:34+00:00
File Inode Change Date/Time     : 2025:09:20 00:45:25+00:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 512
Image Height                    : 504
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 512x504
Megapixels                      : 0.258

AsianHacker-picoctf@webshell:~$ binwalk flag.png ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/ 👀
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2876, uncompressed size: 3029, name: secret/flag.png 👀
42915         0xA7A3          End of Zip archive, footer length: 22

AsianHacker-picoctf@webshell:~$ binwalk -e flag.png ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2876, uncompressed size: 3029, name: secret/flag.png
42915         0xA7A3          End of Zip archive, footer length: 22

AsianHacker-picoctf@webshell:~$ tree .⌨️
-bash: tree: command not found
AsianHacker-picoctf@webshell:~$ cd _flag.png.extracted/ ⌨️
AsianHacker-picoctf@webshell:~/_flag.png.extracted$ ls ⌨️
29  29.zlib  9B3B.zip  secret 👀
AsianHacker-picoctf@webshell:~/_flag.png.extracted$ cd secret/ ⌨️
AsianHacker-picoctf@webshell:~/_flag.png.extracted/secret$ ls ⌨️
flag.png 👀
AsianHacker-picoctf@webshell:~/_flag.png.extracted/secret$ sz flag.png ⌨️ 
AsianHacker-picoctf@webshell:~/_flag.png.extracted/secret$ cd ../.. ⌨️

AsianHacker-picoctf@webshell:~$ zsteg flag.png ⌨️
[?] 3198 bytes of extra data after image end (IEND), offset = 0x9b3b
extradata:0         .. file: Zip archive data, at least v1.0 to extract, compression method=store
    00000000: 50 4b 03 04 0a 00 00 00  00 00 39 10 70 56 00 00  |PK........9.pV..|
    00000010: 00 00 00 00 00 00 00 00  00 00 07 00 1c 00 73 65  |..............se|
    00000020: 63 72 65 74 2f 55 54 09  00 03 8d 78 12 64 8d 78  |cret/UT....x.d.x|
    00000030: 12 64 75 78 0b 00 01 04  00 00 00 00 04 00 00 00  |.dux............|
    00000040: 00 50 4b 03 04 14 00 00  00 08 00 39 10 70 56 0f  |.PK........9.pV.|
    00000050: 5a d1 78 3c 0b 00 00 d5  0b 00 00 0f 00 1c 00 73  |Z.x<...........s|
    00000060: 65 63 72 65 74 2f 66 6c  61 67 2e 70 6e 67 55 54  |ecret/flag.pngUT| 👀
    00000070: 09 00 03 8d 78 12 64 8d  78 12 64 75 78 0b 00 01  |....x.d.x.dux...|
    00000080: 04 00 00 00 00 04 00 00  00 00 cd 56 55 5c d3 8d  |...........VU\..|
    00000090: 1a fe 83 0a a3 27 48 7c  84 80 94 32 7a 12 32 a9  |.....'H|...2z.2.|
    000000a0: 09 92 03 1c 29 21 21 30  69 a4 26 35 40 42 90 54  |....)!!0i.&5@B.T|
    000000b0: 3f 44 40 24 86 c0 a8 d1  08 23 94 10 46 c8 87 12  |?D@$.....#..F...|
    000000c0: d2 18 1b 63 a4 92 92 67  e7 dc 9d 8b 73 7f de 8b  |...c...g....s...|
    000000d0: 37 9f f7 e6 f9 3d ef ef  f7 26 9b 9b ea b3 31 f3  |7....=...&....1.|
    000000e0: 33 03 00 c0 66 68 a0 8b  04 00 7a 5b 5a ae 04 a6  |3...fh....z[Z...|
    000000f0: 39 60 d7 57 d2 9a 16 ce  a3 74 10 3a 00 50 97 c1  |9`.W.....t.:.P..|

AsianHacker-picoctf@webshell:~$ xxd flag.png | tail -n 10 ⌨️
0000a720: 0000 0000 0000 0010 00ed 4100 0000 0073  ..........A....s
0000a730: 6563 7265 742f 5554 0500 038d 7812 6475  ecret/UT....x.du
0000a740: 780b 0001 0400 0000 0004 0000 0000 504b  x.............PK
0000a750: 0102 1e03 1400 0000 0800 3910 7056 0f5a  ..........9.pV.Z
0000a760: d178 3c0b 0000 d50b 0000 0f00 1800 0000  .x<.............
0000a770: 0000 0000 0000 a481 4100 0000 7365 6372  ........A...secr
0000a780: 6574 2f66 6c61 672e 706e 6755 5405 0003  et/flag.pngUT... 👀
0000a790: 8d78 1264 7578 0b00 0104 0000 0000 0400  .x.dux..........
0000a7a0: 0000 0050 4b05 0600 0000 0002 0002 00a2  ...PK...........
0000a7b0: 0000 00c6 0b00 0000 00                   .........

# Open
picoCTF{Hiddinng_An_imag3_within_@n_ima9e_d55982e8} 🔐
```

## Flag
picoCTF{Hiddinng_An_imag3_within_@n_ima9e_d55982e8}

## Continue
[Continue](./picoGym0348.md)