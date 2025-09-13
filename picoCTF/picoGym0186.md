# picoGym Level 186: information
Source: https://play.picoctf.org/practice/challenge/186

## Goal
Files can always be changed in a secret way<br>
Can you find the flag? cat.jpg<br>
https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg

## What I learned
```
Start Forensic
file cat.jpeg
binwalk cat.jpeg                            # find appended files / signatures
hexdump -C cat.jpeg
xxd -g 1 -c 16 cat.jpg | head -n 5
exiftool cat.jpeg                           ❤️
identify -verbose cat.jpg
strings cat.jpeg
steghide extract -sf cat.jpg  
foremost -i cat.jpg -o output               # recover embedded files/carve
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg ⌨️
--2025-09-12 22:34:58--  https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 878136 (858K) [application/octet-stream]
Saving to: 'cat.jpg.1'

cat.jpg.1                                                  100%[======================================================================================================================================>] 857.55K  1.86MB/s    in 0.5s    

2025-09-12 22:34:58 (1.86 MB/s) - 'cat.jpg.1' saved [878136/878136]

# Check if valid jpg file
AsianHacker-picoctf@webshell:/tmp$ file cat.jpg 
cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
AsianHacker-picoctf@webshell:/tmp$ binwalk cat.jpg ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02

AsianHacker-picoctf@webshell:/tmp$ hexdump -C cat.jpg | head -n 10 ⌨️
00000000  ff d8 ff e0 00 10 4a 46  49 46 00 01 02 00 00 01  |......JFIF......|
00000010  00 01 00 00 ff ed 00 30  50 68 6f 74 6f 73 68 6f  |.......0Photosho|
00000020  70 20 33 2e 30 00 38 42  49 4d 04 04 00 00 00 00  |p 3.0.8BIM......|
00000030  00 13 1c 02 74 00 07 50  69 63 6f 43 54 46 1c 02  |....t..PicoCTF..|
00000040  00 00 02 00 04 00 ff e1  0b f9 68 74 74 70 3a 2f  |..........http:/|
00000050  2f 6e 73 2e 61 64 6f 62  65 2e 63 6f 6d 2f 78 61  |/ns.adobe.com/xa|
00000060  70 2f 31 2e 30 2f 00 3c  3f 78 70 61 63 6b 65 74  |p/1.0/.<?xpacket|
00000070  20 62 65 67 69 6e 3d 27  ef bb bf 27 20 69 64 3d  | begin='...' id=|
00000080  27 57 35 4d 30 4d 70 43  65 68 69 48 7a 72 65 53  |'W5M0MpCehiHzreS|
00000090  7a 4e 54 63 7a 6b 63 39  64 27 3f 3e 0a 3c 78 3a  |zNTczkc9d'?>.<x:|

# Check metadata w/ exiftool
AsianHacker-picoctf@webshell:/tmp$ exiftool cat.jpg ⌨️
ExifTool Version Number         : 12.40
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:15 18:24:46+00:00
File Access Date/Time           : 2025:09:12 22:33:09+00:00
File Inode Change Date/Time     : 2025:09:12 22:33:03+00:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 👀
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1

# Cipher Identification
https://www.dcode.fr/cipher-identifier
    Base64 Coding	
    Google Drive Link?	

# Decode in terminal
AsianHacker-picoctf@webshell:/tmp$ echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d ⌨️
picoCTF{the_m3tadata_1s_modified} 🔐
AsianHacker-picoctf@webshell:/tmp$ exiftool cat.jpg | grep License | sed  -e 's/.*: //' | base64 -d ⌨️❤️
picoCTF{the_m3tadata_1s_modified} 🔐

# Decode online
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=Y0dsamIwTlVSbnQwYUdWZmJUTjBZV1JoZEdGZk1YTmZiVzlrYVdacFpXUjk ⌨️
https://www.dcode.fr/base-64-encoding ⌨️

# Search Properties
AsianHacker-picoctf@webshell:/tmp$ identify -verbose cat.jpg ⌨️
Image:
  Filename: cat.jpg
  Format: JPEG (Joint Photographic Experts Group JFIF format)
  Mime type: image/jpeg
  Class: DirectClass
  Geometry: 2560x1598+0+0
  Units: Undefined
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianness: Undefined
  Depth: 8-bit
  Channel depth:
    red: 8-bit
    green: 8-bit
    blue: 8-bit
  Channel statistics:
    Pixels: 4090880
    Red:
      min: 0  (0)
      max: 255 (1)
      mean: 78.771 (0.308906)
      standard deviation: 66.9061 (0.262377)
      kurtosis: -0.960917
      skewness: 0.455912
      entropy: 0.9119
    Green:
      min: 0  (0)
      max: 255 (1)
      mean: 73.0792 (0.286585)
      standard deviation: 73.7457 (0.289199)
      kurtosis: -0.661505
      skewness: 0.725843
      entropy: 0.876194
    Blue:
      min: 0  (0)
      max: 255 (1)
      mean: 79.9291 (0.313447)
      standard deviation: 73.2804 (0.287374)
      kurtosis: -0.398955
      skewness: 0.803142
      entropy: 0.922943
  Image statistics:
    Overall:
      min: 0  (0)
      max: 255 (1)
      mean: 77.2597 (0.302979)
      standard deviation: 71.3107 (0.27965)
      kurtosis: -0.629883
      skewness: 0.67533
      entropy: 0.903679
  Rendering intent: Perceptual
  Gamma: 0.454545
  Chromaticity:
    red primary: (0.64,0.33)
    green primary: (0.3,0.6)
    blue primary: (0.15,0.06)
    white point: (0.3127,0.329)
  Background color: white
  Border color: srgb(223,223,223)
  Matte color: grey74
  Transparent color: black
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 2560x1598+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: JPEG
  Quality: 90
  Orientation: Undefined
  Profiles:
    Profile-8bim: 32 bytes
    Profile-iptc: 19 bytes
      Copyright String[2,116]: PicoCTF
      unknown[2,0]: 
    Profile-xmp: 3034 bytes
  Properties:
    date:create: 2025-09-12T22:33:03+00:00
    date:modify: 2021-03-15T18:24:46+00:00
    jpeg:colorspace: 2
    jpeg:sampling-factor: 2x2,1x1,1x1
    signature: 52c5450db6fa4b2a2ce58f3507230c1a74e0f1fc85884cf5e2307a3ccae66210
  Artifacts:
    filename: cat.jpg
    verbose: true
  Tainted: False
  Filesize: 878136B
  Number pixels: 4090880
  Pixels per second: 24.1806MB
  User time: 0.050u
  Elapsed time: 0:01.169
  Version: ImageMagick 6.9.11-60 Q16 x86_64 2021-01-25 https://imagemagick.org

AsianHacker-picoctf@webshell:~$ strings cat.jpg | head -n 5 ⌨️
JFIF
0Photoshop 3.0
8BIM
PicoCTF
http://ns.adobe.com/xap/1.0/

AsianHacker-picoctf@webshell:~$ xxd -g 1 -c 16 cat.jpg | head -n 5 ⌨️
00000000: ff d8 ff e0 00 10 4a 46 49 46 00 01 02 00 00 01  ......JFIF......
00000010: 00 01 00 00 ff ed 00 30 50 68 6f 74 6f 73 68 6f  .......0Photosho
00000020: 70 20 33 2e 30 00 38 42 49 4d 04 04 00 00 00 00  p 3.0.8BIM......
00000030: 00 13 1c 02 74 00 07 50 69 63 6f 43 54 46 1c 02  ....t..PicoCTF..
00000040: 00 00 02 00 04 00 ff e1 0b f9 68 74 74 70 3a 2f  ..........http:/

AsianHacker-picoctf@webshell:~$ steghide extract -sf cat.jpg ⌨️
Enter passphrase: 
steghide: could not extract any data with that passphrase!

AsianHacker-picoctf@webshell:~$ foremost -i cat.jpg -o foremost_output ⌨️
Processing: cat.jpg
|*|
AsianHacker-picoctf@webshell:~$ cd foremost_output/ ⌨️
AsianHacker-picoctf@webshell:~/foremost_output$ ls ⌨️
audit.txt  jpg
AsianHacker-picoctf@webshell:~/foremost_output$ cat audit.txt 
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Fri Sep 12 23:00:06 2025
Invocation: foremost -i cat.jpg -o foremost_output 
Output directory: /home/AsianHacker-picoctf/foremost_output
Configuration file: /etc/foremost.conf
------------------------------------------------------------------
File: cat.jpg
Start: Fri Sep 12 23:00:06 2025
Length: 857 KB (878136 bytes)
 
Num      Name (bs=512)         Size      File Offset     Comment 

0:      00000000.jpg         857 KB               0      
Finish: Fri Sep 12 23:00:06 2025

1 FILES EXTRACTED

jpg:= 1
------------------------------------------------------------------

Foremost finished at Fri Sep 12 23:00:06 2025
AsianHacker-picoctf@webshell:~/foremost_output$ cd jpg/ ⌨️
AsianHacker-picoctf@webshell:~/foremost_output/jpg$ ls ⌨️
00000000.jpg
AsianHacker-picoctf@webshell:~/foremost_output/jpg$ file 00000000.jpg ⌨️ 
00000000.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
```

## Flag
picoCTF{the_m3tadata_1s_modified}

## Continue
[Continue](./picoGym044.md)