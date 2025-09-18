# picoGym Level 52: extensions
Source: https://play.picoctf.org/practice/challenge/52

## Goal
This is a really weird text file TXT? Can you find the flag?<br>
https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt

## What I learned
```
change extensions
mv
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt ⌨️
--2025-09-16 03:37:58--  https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9984 (9.8K) [application/octet-stream]
Saving to: 'flag.txt'

flag.txt                                                   100%[======================================================================================================================================>]   9.75K  --.-KB/s    in 0s      

2025-09-16 03:37:58 (351 MB/s) - 'flag.txt' saved [9984/9984]
AsianHacker-picoctf@webshell:~$ file flag.txt ⌨️
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced 👀

AsianHacker-picoctf@webshell:~$ binwalk flag.txt ⌨️ 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1697 x 608, 8-bit/color RGB, non-interlaced 👀
91            0x5B            Zlib compressed data, compressed

AsianHacker-picoctf@webshell:~$ exiftool flag.txt ⌨️
ExifTool Version Number         : 12.40
File Name                       : flag.txt
Directory                       : .
File Size                       : 9.8 KiB
File Modification Date/Time     : 2020:10:26 18:30:20+00:00
File Access Date/Time           : 2025:09:16 03:42:01+00:00
File Inode Change Date/Time     : 2025:09:16 03:42:01+00:00
File Permissions                : -rw-rw-r--
File Type                       : PNG 👀
File Type Extension             : png 👀
MIME Type                       : image/png 👀
Image Width                     : 1697
Image Height                    : 608
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 5669
Pixels Per Unit Y               : 5669
Pixel Units                     : meters
Image Size                      : 1697x608
Megapixels                      : 1.0

AsianHacker-picoctf@webshell:~$ xxd flag.txt | head -n 5 ⌨️
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR 👀
00000010: 0000 06a1 0000 0260 0802 0000 0085 ad5e  .......`.......^
00000020: 9a00 0000 0173 5247 4200 aece 1ce9 0000  .....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 0000 1625 0000 1625 0149  ..pHYs...%...%.I

AsianHacker-picoctf@webshell:~$ mv flag.txt flag.png ⌨️
AsianHacker-picoctf@webshell:~$ sz flag.png ⌨️
AsianHacker-picoctf@webshell:~$ xdg-open flag.png ⌨️
Error: no "view" rule for type "image/png" passed its test case
       (for more information, add "--debug=1" on the command line)

# Note: Open flag.png
picoCTF{now_you_know_about_extensions} 🔐
```

## Flag
picoCTF{now_you_know_about_extensions}

## Continue
[Continue](./picoGym0265.md)