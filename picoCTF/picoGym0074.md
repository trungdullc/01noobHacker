# picoGym Level 74: What Lies Within
Source: https://play.picoctf.org/practice/challenge/74

## Goal
There's something in the building. Can you retrieve the flag?<br>
https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png

## What I learned
```
steghide does not support PNG files—it only works with JPEG, BMP, WAV, and AU files
zsteg
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png ⌨️
--2025-09-16 22:55:05--  https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 625219 (611K) [application/octet-stream]
Saving to: 'buildings.png'

buildings.png                                      100%[=============================================================================================================>] 610.57K  1.87MB/s    in 0.3s    

2025-09-16 22:55:06 (1.87 MB/s) - 'buildings.png' saved [625219/625219]

AsianHacker-picoctf@webshell:~$ file buildings.png ⌨️
buildings.png: PNG image data, 657 x 438, 8-bit/color RGBA, non-interlaced
AsianHacker-picoctf@webshell:~$ binwalk buildings.png ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 657 x 438, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed

AsianHacker-picoctf@webshell:~$ exiftool buildings.png ⌨️
ExifTool Version Number         : 12.40
File Name                       : buildings.png
Directory                       : .
File Size                       : 611 KiB
File Modification Date/Time     : 2020:10:26 18:30:20+00:00
File Access Date/Time           : 2025:09:16 22:55:10+00:00
File Inode Change Date/Time     : 2025:09:16 22:55:06+00:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 657
Image Height                    : 438
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 657x438
Megapixels                      : 0.288
AsianHacker-picoctf@webshell:~$ strings buildings.png | grep "picoCTF" ⌨️
AsianHacker-picoctf@webshell:~$ steghide --extract -sf buildings.png ⌨️
Enter passphrase:
steghide: the file format of the file "buildings.png" is not supported.

# Optional: https://book.hacktricks.wiki/en/crypto-and-stego/stego-tricks.html ❤️❤️❤️❤️❤️

# Method 1: zsteg
AsianHacker-picoctf@webshell:~$ zsteg buildings.png ⌨️
b1,r,lsb,xy         .. text: "^5>R5YZrG"
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}" 🔐
b1,abgr,msb,xy      .. file: PGP Secret Sub-key -
b2,b,lsb,xy         .. text: "XuH}p#8Iy="
b3,abgr,msb,xy      .. text: "t@Wp-_tH_v\r"
b4,r,lsb,xy         .. text: "fdD\"\"\"\" "
b4,r,msb,xy         .. text: "%Q#gpSv0c05"
b4,g,lsb,xy         .. text: "fDfffDD\"\""
b4,g,msb,xy         .. text: "f\"fff\"\"DD"
b4,b,lsb,xy         .. text: "\"$BDDDDf"
b4,b,msb,xy         .. text: "wwBDDDfUU53w"
b4,rgb,msb,xy       .. text: "dUcv%F#A`"
b4,bgr,msb,xy       .. text: " V\"c7Ga4"
b4,abgr,msb,xy      .. text: "gOC_$_@o"
AsianHacker-picoctf@webshell:~$ zsteg -a buildings.png | grep "picoCTF"
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}" 🔐

# Method 2: Aperi'Solve: https://www.aperisolve.com/
```

## Flag
picoCTF{h1d1ng_1n_th3_b1t5}

## Continue
[Continue](./picoGym0051.md)