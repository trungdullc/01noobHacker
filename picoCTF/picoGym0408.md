# picoGym Level 408: CanYouSee
Source: https://play.picoctf.org/practice/challenge/408

## Goal
How about some hide and seek?<br>
Download this file here.<br>
https://artifacts.picoctf.net/c_titan/128/unknown.zip

## What I learned
```
Forensic
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/128/unknown.zip ⌨️
--2025-09-12 23:43:53--  https://artifacts.picoctf.net/c_titan/128/unknown.zip ⌨️
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.77, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2252108 (2.1M) [application/octet-stream]
Saving to: 'unknown.zip'

unknown.zip                                                100%[======================================================================================================================================>]   2.15M  1.83MB/s    in 1.2s    

2025-09-12 23:43:54 (1.83 MB/s) - 'unknown.zip' saved [2252108/2252108]

AsianHacker-picoctf@webshell:~$ unzip unknown.zip ⌨️
Archive:  unknown.zip
  inflating: ukn_reality.jpg         
AsianHacker-picoctf@webshell:~$ rm unknown.zip 
AsianHacker-picoctf@webshell:~$ file ukn_reality.jpg ⌨️
ukn_reality.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 4308x2875, components 3
AsianHacker-picoctf@webshell:~$ binwalk ukn_reality.jpg ⌨️ 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
AsianHacker-picoctf@webshell:~$ strings ukn_reality.jpg | grep -e "pico" ⌨️ 
AsianHacker-picoctf@webshell:~$ xxd ukn_reality.jpg > hexfile ⌨️
AsianHacker-picoctf@webshell:~$ cat hexfile | grep -e "pico" ⌨️
AsianHacker-picoctf@webshell:~$ rm hexfile ⌨️

AsianHacker-picoctf@webshell:~$ exiftool ukn_reality.jpg ⌨️ 
ExifTool Version Number         : 12.40
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Modification Date/Time     : 2024:03:12 00:05:51+00:00
File Access Date/Time           : 2025:09:12 23:44:13+00:00
File Inode Change Date/Time     : 2025:09:12 23:43:58+00:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg== 👀
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4

# Cipher Identification
https://www.dcode.fr/cipher-identifier
    Base64 Coding	
    Base62 Encoding
https://www.dcode.fr/base-64-encoding
base64	picoCTF{ME74D47A_HIDD3N_3b9209a2} 🔐
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=Y0dsamIwTlVSbnROUlRjMFJEUTNRVjlJU1VSRU0wNWZNMkk1TWpBNVlUSjlDZz09
AsianHacker-picoctf@webshell:~$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==" | base64 -d ⌨️
picoCTF{ME74D47A_HIDD3N_3b9209a2} 🔐
```

## Flag
picoCTF{ME74D47A_HIDD3N_3b9209a2} 

## Continue
[Continue](./picoGym0444.md)