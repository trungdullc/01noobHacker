# picoGym Level 129: Matryoshka doll
Source: https://play.picoctf.org/practice/challenge/129

## Goal
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another.<br>
What's the final one? Image: this<br>
https://mercury.picoctf.net/static/b6205dd933ec01c022c4e6acbdf11116/dolls.jpg

## What I learned
```
binwalk <file>
    shows offsets and file signatures
binwalk with different extract options
    binwalk -e <file>           _file.extracted/ created
    binwalk -Me <file>          recursively extracts and scans embedded files
    binwalk -D='.*' <file>      specify your own rules for extraction (for example, only extract gzip files)

Manually extract with dd or ddrescue
    dd if=file.img of=extracted.gz bs=1 skip=18246144 count=4096
    replace skip with offset and count with approximate size

Other steganography tools (hidden data not simple embedded file)
    strings                     quickly check for hidden text
    steghide                    hides/extracts files in JPEG, BMP, WAV, AU
    foremost or scalpel         carve out files by signatures (useful when binwalk misses something)

Youtube: https://www.youtube.com/watch?v=KUZVIBXfoeA&t=221s
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/b6205dd933ec01c022c4e6acbdf11116/dolls.jpg ⌨️
--2025-09-16 00:23:16--  https://mercury.picoctf.net/static/b6205dd933ec01c022c4e6acbdf11116/dolls.jpg
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 651630 (636K) [application/octet-stream]
Saving to: 'dolls.jpg'

dolls.jpg                                                  100%[======================================================================================================================================>] 636.36K  1.84MB/s    in 0.3s    

2025-09-16 00:23:17 (1.84 MB/s) - 'dolls.jpg' saved [651630/651630]

AsianHacker-picoctf@webshell:~$ steghide extract -sf dolls.jpg ⌨️
Enter passphrase: 
steghide: the file format of the file "dolls.jpg" is not supported.

AsianHacker-picoctf@webshell:~$ binwalk dolls.jpg ⌨️
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378950, uncompressed size: 383938, name: base_images/2_c.jpg
651608        0x9F158         End of Zip archive, footer length: 22

# Note: -e extracts into a folder
AsianHacker-picoctf@webshell:~$ binwalk -e dolls.jpg ⌨️❤️❤️❤️❤️❤️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378950, uncompressed size: 383938, name: base_images/2_c.jpg 👀
651608        0x9F158         End of Zip archive, footer length: 22

AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  _dolls.jpg.extracted 👀  dolls.jpg  pico_img.png
AsianHacker-picoctf@webshell:~$ cd _dolls.jpg.extracted/ ⌨️
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted$ ls ⌨️
4286C.zip  base_images 👀
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted$ cd base_images/ ⌨️
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images$ ls ⌨️
2_c.jpg
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images$ binwalk -e 2_c.jpg ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196043, uncompressed size: 201445, name: base_images/3_c.jpg 👀
383805        0x5DB3D         End of Zip archive, footer length: 22
383916        0x5DBAC         End of Zip archive, footer length: 22

AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images$ ls ⌨️
2_c.jpg  _2_c.jpg.extracted
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images$ cd _2_c.jpg.extracted/ ⌨️
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted$ ls ⌨️
2DD3B.zip  base_images 👀
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted$ cd base_images/ ⌨️
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ ls ⌨️
3_c.jpg
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ binwalk -e 3_c.jpg ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 428 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77651, uncompressed size: 79809, name: base_images/4_c.jpg 👀
201423        0x312CF         End of Zip archive, footer length: 22

AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images$ cd _3_c.jpg.extracted/base_images/ ⌨️
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images$ ls ⌨️
4_c.jpg
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images$ binwalk -e 4_c.jpg ⌨️ 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 768, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 65, uncompressed size: 81, name: flag.txt 👀
79787         0x137AB         End of Zip archive, footer length: 22

AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images$ cd _4_c.jpg.extracted/ ⌨️
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted$ ls ⌨️
136DA.zip  flag.txt 👀
AsianHacker-picoctf@webshell:~/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted$ cat flag.txt ⌨️
picoCTF{4f11048e83ffc7d342a15bd2309b47de} 🔐
```

## Flag
picoCTF{4f11048e83ffc7d342a15bd2309b47de}

## Continue
[Continue](./picoGym0052.md)