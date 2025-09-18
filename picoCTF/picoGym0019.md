# picoGym Level 19: So Meta
Source: https://play.picoctf.org/practice/challenge/19

## Goal
Find the flag in this picture.<br>
https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png

## What I learned
```
exiftool
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png ⌨️
--2025-09-15 23:50:34--  https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 108795 (106K) [application/octet-stream]
Saving to: 'pico_img.png'

pico_img.png                                               100%[======================================================================================================================================>] 106.25K  --.-KB/s    in 0.05s   

2025-09-15 23:50:34 (2.17 MB/s) - 'pico_img.png' saved [108795/108795]

# Method 1: strings
AsianHacker-picoctf@webshell:~$ strings pico_img.png | grep "picoCTF" ⌨️
picoCTF{s0_m3ta_d8944929}K 🔐

# Method 2: exiftool
AsianHacker-picoctf@webshell:~$ exiftool pico_img.png ⌨️
ExifTool Version Number         : 12.40
File Name                       : pico_img.png
Directory                       : .
File Size                       : 106 KiB
File Modification Date/Time     : 2020:10:26 18:38:23+00:00
File Access Date/Time           : 2025:09:15 23:50:54+00:00
File Inode Change Date/Time     : 2025:09:15 23:50:34+00:00
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_d8944929} 🔐
Image Size                      : 600x600
Megapixels                      : 0.360

AsianHacker-picoctf@webshell:~$ exiftool pico_img.png | grep pico ⌨️
File Name                       : pico_img.png
Artist                          : picoCTF{s0_m3ta_d8944929} 🔐
```

## Flag
picoCTF{s0_m3ta_d8944929}

## Continue
[Continue](./picoGym0129.md)