# picoGym Level 359: MSB
Source: https://play.picoctf.org/practice/challenge/359

## Goal
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...<br>
Download the image here<br>
https://artifacts.picoctf.net/c/305/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png

## What I learned
```
MSB normally affects image since it the most imporant vs LSB
stegsolve
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/305/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png ⌨️
--2025-09-21 07:16:01--  https://artifacts.picoctf.net/c/305/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.18, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3354311 (3.2M) [application/octet-stream]
Saving to: 'Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png'

Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png    100%[======================================================================================================================================>]   3.20M  1.82MB/s    in 1.8s    

2025-09-21 07:16:03 (1.82 MB/s) - 'Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png' saved [3354311/3354311]

AsianHacker-picoctf@webshell:~$ file Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png ⌨️
Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png: PNG image data, 1074 x 1500, 8-bit/color RGB, non-interlaced
AsianHacker-picoctf@webshell:~$ binwalk Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1074 x 1500, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, default compression

AsianHacker-picoctf@webshell:~$ exiftool Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png ⌨️
ExifTool Version Number         : 12.40
File Name                       : Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
Directory                       : .
File Size                       : 3.2 MiB
File Modification Date/Time     : 2023:08:04 21:26:07+00:00
File Access Date/Time           : 2025:09:21 07:16:32+00:00
File Inode Change Date/Time     : 2025:09:21 07:16:03+00:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1074
Image Height                    : 1500
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1074x1500
Megapixels                      : 1.6
AsianHacker-picoctf@webshell:~$ zsteg Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png ⌨️
imagedata           .. text: "~~~|||}}}"
b1,g,lsb,xy         .. file: Common Data Format (Version 2.5 or earlier) data
b1,g,msb,xy         .. file: Common Data Format (Version 2.5 or earlier) data
b2,r,lsb,xy         .. text: ["U" repeated 8 times]
b2,g,lsb,xy         .. file: Matlab v4 mat-file (little endian) \252\252\252\252\252\252\252\252, numeric, rows 4294967295, columns 4294967295
b2,g,msb,xy         .. file: Matlab v4 mat-file (little endian) UUUUUUUU, numeric, rows 4294967295, columns 4294967295
b2,b,lsb,xy         .. text: ["U" repeated 8 times]
b4,r,lsb,xy         .. text: ["w" repeated 8 times]
b4,r,msb,xy         .. text: ["U" repeated 12 times]
b4,g,msb,xy         .. text: ["w" repeated 16 times]
b4,b,lsb,xy         .. text: "\"\"\"\"\"\"\"\"4DC\""
b4,b,msb,xy         .. text: "wwwwwwww3333"
AsianHacker-picoctf@webshell:~$ strings Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png | grep "picoCTF" ⌨️
AsianHacker-picoctf@webshell:~$ strings Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png | grep "flag" ⌨️
AsianHacker-picoctf@webshell:~$ xxd Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png | head -n 10 ⌨️
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0432 0000 05dc 0802 0000 005f f239  ...2........._.9
00000020: 3100 0100 0049 4441 5478 9c9c fdd9 9624  1....IDATx.....$
00000030: 3976 2008 5e00 22aa 66e6 114c d6d2 d57d  9v .^.".f..L...}
00000040: ce7c c57c c84c 378b 6c9e 4a32 63f7 7077  .|.|.L7.l.J2c.pw
00000050: 3377 db75 9505 b880 88aa 9979 4426 a7ba  3w.u.......yD&..
00000060: 6a1e a6e7 653e a79f bac9 2e92 c564 666c  j...e>.......dfl
00000070: beda bee8 ae22 0260 1e20 22aa 1e99 5553  .....".`. "...US
00000080: 67cc cdd5 5445 4580 8b7b 2f80 bb83 3cbd  g...TEE..{/...<.
00000090: df47 4404 4404 4040 4004 0440 0400 4080  .GD.D.@@@..@..@.
AsianHacker-picoctf@webshell:~$ xxd Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png | tail -n 10 ⌨️
00332e30: bcfa 43fb c14f 1e92 366f c3da 7a2e da65  ..C..O..6o..z..e
00332e40: 82cf 7c32 f2fb 03d8 d89f 31b3 3f7c fd9b  ..|2......1.?|..
00332e50: 591f 66fe b7f2 2a7f befe 7cfd baab 5580  Y.f...*...|...U.
00332e60: ff9d e443 fec0 f5df f20a fc9b d1b7 b83e  ...C...........>
00332e70: 7e9d 4f94 69fc eb3e 807d f3bf e8f7 fef9  ~.O.i..>.}......
00332e80: fab7 71fd ab9d c757 3990 3ff0 bda8 156a  ..q....W9.?....j
00332e90: 7f22 22e8 ed5c 3a64 d2d2 1db7 d96c eae7  .""..\:d.....l..
00332ea0: 6b6c 9d73 8ea9 f1fc 2f5f fdea 54fe d145  kl.s..../_..T..E
00332eb0: f8ff 0083 ab68 0526 764d cc00 0000 0049  .....h.&vM.....I
00332ec0: 454e 44ae 4260 82                        END.B`.

# Method 1: python script
# Google: extract data from MSB
https://github.com/Pulho/sigBits
    # Requirements
    pip3 install Pillow
    # DL python file
    wget https://raw.githubusercontent.com/Pulho/sigBits/master/sigBits.py
    # Usage
    python sigBits.py [OPTIONS] [FILE]
    python3 sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png

AsianHacker-picoctf@webshell:~$ mv Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png /tmp ⌨️
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ pip3 install Pillow ⌨️
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: Pillow in /usr/local/lib/python3.10/dist-packages (11.1.0)
WARNING: Error parsing dependencies of send2trash: Expected matching RIGHT_PARENTHESIS for LEFT_PARENTHESIS, after version specifier
    sys-platform (=="darwin") ; extra == 'objc'
                 ~^

[notice] A new release of pip is available: 25.0.1 -> 25.2
[notice] To update, run: python3 -m pip install --upgrade pip
AsianHacker-picoctf@webshell:/tmp$ wget https://raw.githubusercontent.com/Pulho/sigBits/master/sigBits.py ⌨️
--2025-09-21 07:29:10--  https://raw.githubusercontent.com/Pulho/sigBits/master/sigBits.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.111.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7008 (6.8K) [text/plain]
Saving to: 'sigBits.py'

sigBits.py                                                 100%[======================================================================================================================================>]   6.84K  --.-KB/s    in 0.001s  

2025-09-21 07:29:10 (4.86 MB/s) - 'sigBits.py' saved [7008/7008]

AsianHacker-picoctf@webshell:/tmp$ python3 sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png ⌨️
Done, check the output file!

# Using regex to add 50 characters after the "picoCTF" prefix
AsianHacker-picoctf@webshell:/tmp$ cat outputSB.txt | grep -o -E "picoCTF.{0,50}" ⌨️❤️❤️❤️❤️❤️
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_572ad5fe}"Thou h 🔐

Method 2: stegsolve
Analyse → Data Extract ❤️
Check 7 on RGB and Preview and Save Text outputSB.txt
Ctrl + F: picoCTF{
```

## Flag
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_572ad5fe}

## Continue
[Continue](./picoGym0362.md)