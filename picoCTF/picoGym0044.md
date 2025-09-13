# picoGym Level 44: Glory of the Garden
Source: https://play.picoctf.org/practice/challenge/44

## Goal
This garden contains more than it seems<br>
https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg

## What I learned
```
Forensic Beta (lazy): https://29a.ch/photo-forensics/#forensic-magnifier
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg ⌨️
--2025-09-12 23:22:14--  https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2295192 (2.2M) [application/octet-stream]
Saving to: 'garden.jpg'

garden.jpg                                                 100%[======================================================================================================================================>]   2.19M  1.84MB/s    in 1.2s    

2025-09-12 23:22:15 (1.84 MB/s) - 'garden.jpg' saved [2295192/2295192]

AsianHacker-picoctf@webshell:~$ exiftool garden.jpg ⌨️
ExifTool Version Number         : 12.40
File Name                       : garden.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Modification Date/Time     : 2020:10:26 18:39:31+00:00
File Access Date/Time           : 2025:09:12 23:22:30+00:00
File Inode Change Date/Time     : 2025:09:12 23:22:15+00:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Image Width                     : 2999
Image Height                    : 2249
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2999x2249
Megapixels                      : 6.7

AsianHacker-picoctf@webshell:~$ strings garden.jpg | grep -e "pico" ⌨️
Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}" 🔐

# Note: can also redirect > output to a file
AsianHacker-picoctf@webshell:~$ xxd garden.jpg | tail -n 10 ⌨️
00230500: d9f9 9f63 4b2b c1e5 daf2 7b59 db49 4ba3  ...cK+....{Y.IK.
00230510: f43e b881 5e30 1060 8030 47d6 bacb 58cb  .>..^0.`.0G...X.
00230520: 1046 07b5 7216 df7e 5ff7 c576 363f ebab  .F..r..~_..v6?..
00230530: b70d 18ce 3ccd 6a7e 6b8d af56 b579 39ca  ....<.j~k..V.y9.
00230540: eeef 53ae 8620 31b8 751f 9514 f7fb cff5  ..S.. 1.u.......
00230550: a2bb bdac 9687 98e4 d3b2 e87f ffd9 4865  ..............He
00230560: 7265 2069 7320 6120 666c 6167 2022 7069  re is a flag "pi
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3365 4264  m33ts_the_3y3eBd
00230590: 4264 3263 637d 220a                      Bd2cc}". 🔐

AsianHacker-picoctf@webshell:~$ hexdump -c garden.jpg | tail -n 15 ⌨️
02304c0   ) 031 346 273   Y 033 234   *   s 322 276   q 275 370 227   }
02304d0 342   }   e   t 375   = 032  \b   #   ? 275   n 231 307   j 371
02304e0 342 367 375   o 374  \t 377  \0 235   o 374   + 377  \0 220 226
02304f0 255 377  \0   ] 377  \0 240 256   z   Q 215   O   h 365   V 212
0230500 331 371 237   c   K   + 301 345 332 362   {   Y 333   I   K 243
0230510 364   > 270 201   ^   0 020   ` 200   0   G 326 272 313   X 313
0230520 020   F  \a 265   r 026 337   ~   _ 367 305   v   6   ? 353 253
0230530 267  \r 030 316   < 315   j   ~   k 215 257   V 265   y   9 312
0230540 356 357   S 256 206       1 270   u 037 225 024 367 373 317 365
0230550 242 273 275 254 226 207 230 344 323 262 350 177 377 331   H   e
0230560   r   e       i   s       a       f   l   a   g       "   p   i
0230570   c   o   C   T   F   {   m   o   r   e   _   t   h   a   n   _
0230580   m   3   3   t   s   _   t   h   e   _   3   y   3   e   B   d
0230590   B   d   2   c   c   }   "  \n 🔐                               
0230598
```

## Flag
picoCTF{more_than_m33ts_the_3y3eBdBd2cc}

## Continue
[Continue](./picoGym0408.md)