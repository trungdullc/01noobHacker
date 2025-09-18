# picoGym Level 53: c0rrupt
Source: https://play.picoctf.org/practice/challenge/53

## Goal
We found this file. Recover the flag.<br>
https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery

## What I learned
```
Corrupted Data
IHDR chunk is blueprint of the image — tells decoder how to interpret pixel data that follows

Magic Byte: https://en.wikipedia.org/wiki/List_of_file_signatures
Hex Editor Online: https://hexed.it/ ⭐⭐⭐⭐⭐
bvi <file> ⭐⭐⭐⭐⭐
    :set memmove ❤️❤️❤️❤️❤️

seek=8      dd skip 8 bytes into output file before writing
    write starts exactly at offset 0x08 (9th byte, since counting starts at 0)
count=8     dd write 8 bytes total from stdin into the file

pngcheck ⭐⭐⭐⭐⭐

Google: png file format wiki
https://en.wikipedia.org/wiki/PNG#/media/File:PNG-Gradient_hex.png
https://www.w3.org/TR/png/#5ChunkOrdering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery ⌨️
--2025-09-16 20:31:56--  https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 202940 (198K) [application/octet-stream]
Saving to: 'mystery'

mystery                                            100%[=============================================================================================================>] 198.18K  --.-KB/s    in 0.1s    

2025-09-16 20:31:56 (1.99 MB/s) - 'mystery' saved [202940/202940]

AsianHacker-picoctf@webshell:~$ file mystery ⌨️
mystery: data 
AsianHacker-picoctf@webshell:~$ exiftool mystery ⌨️
ExifTool Version Number         : 12.40
File Name                       : mystery
Directory                       : .
File Size                       : 198 KiB
File Modification Date/Time     : 2020:10:26 18:30:20+00:00
File Access Date/Time           : 2025:09:16 20:32:03+00:00
File Inode Change Date/Time     : 2025:09:16 20:31:56+00:00
File Permissions                : -rw-rw-r--
Error                           : Unknown file type 👀

AsianHacker-picoctf@webshell:~$ binwalk mystery ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
91            0x5B            Zlib compressed data, compressed
AsianHacker-picoctf@webshell:~$ xxd mystery | head -n 10 ⌨️
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4👀........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..

# Method 1: dd
# Step 1: Fixing Magic Numbers
AsianHacker-picoctf@webshell:~$ printf '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' | dd of=mystery bs=1 seek=0 count=8 conv=notrunc ⌨️
8+0 records in
8+0 records out
8 bytes copied, 8.8005e-05 s, 90.9 kB/s
AsianHacker-picoctf@webshell:~$ xxd mystery | head -n 10 ⌨️
00000000: 8950 4e47 0d0a 1a0a👀0000 000d 4322 4452  .PNG👀........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..

# Step 2: Correcting IHDR Chunk
AsianHacker-picoctf@webshell:~$ printf '\x00\x00\x00\x0D\x49\x48\x44\x52' | dd of=mystery bs=1 seek=8 count=8 conv=notrunc ⌨️
8+0 records in
8+0 records out
8 bytes copied, 9.7051e-05 s, 82.4 kB/s
AsianHacker-picoctf@webshell:~$ xxd mystery | head -n 10 ⌨️
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452👀.PNG........IHDR👀
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..

# Note Now identifies as png file
AsianHacker-picoctf@webshell:~$ file mystery ⌨️
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced

# Step 3: Resolving Remaining Errors
AsianHacker-picoctf@webshell:~$ pngcheck -c -v mystery 2>/dev/null ⌨️❤️❤️❤️❤️❤️
AsianHacker-picoctf@webshell:~$ pngcheck --version ⌨️
-bash: pngcheck: command not found

# Temporary using custom script but need install pngcheck it better
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
import struct, zlib

def validate_png(filename):
    with open(filename,"rb") as f:
        data = f.read()
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        print("Invalid PNG signature")
        return
    pos = 8
    while pos < len(data):
        if pos+8 > len(data):
            print("Unexpected end of file")
            return
        length = struct.unpack(">I", data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8]
        if pos+12+length > len(data):
            print(f"Chunk {chunk_type} exceeds file size")
            return
        chunk_data = data[pos+8:pos+8+length]
        crc_stored = struct.unpack(">I", data[pos+8+length:pos+12+length])[0]
        crc_calc = zlib.crc32(chunk_type + chunk_data) & 0xffffffff
        if crc_stored != crc_calc:
            print(f"CRC mismatch in chunk {chunk_type}")
        pos += length + 12
    if data[-12:-4] != b'IEND':
        print("IEND chunk missing or corrupted")
    print("PNG validation finished")
validate_png("mystery")

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️      
CRC mismatch in chunk b'pHYs' 👀
Chunk b'\xabDET' exceeds file size

AsianHacker-picoctf@webshell:~$ printf '\x38\xD8\x2C\x82' | dd of=mystery bs=1 seek=79 count=4 conv=notrunc ⌨️
4+0 records in
4+0 records out
4 bytes copied, 7.7398e-05 s, 51.7 kB/s
AsianHacker-picoctf@webshell:~$ xxd mystery | head -n 20 ⌨️
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0138  ..pHYs...%...%.8
00000050: d82c 82👀aa aaff a5ab 4445 5478 5eec bd3f  .,......DET👀x^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..
000000a0: 3871 2232 eb4f 57cf 14e6 25ff e5ff 5b2c  8q"2.OW...%...[,
000000b0: 168b c562 b158 2c16 8bc5 62b1 582c 161d  ...b.X,...b.X,..
000000c0: d6d7 678b c562 b158 2c16 8bc5 62b1 582c  ..g..b.X,...b.X,
000000d0: 168b 4597 f5f5 d962 b158 2c16 8bc5 62b1  ..E....b.X,...b.
000000e0: 582c 168b c562 d165 7d7d b658 2c16 8bc5  X,...b.e}}.X,...
000000f0: 62b1 582c 168b c562 b158 7459 5f9f 2d16  b.X,...b.XtY_.-.
00000100: 8bc5 62b1 582c 168b c562 b158 2c16 5dd6  ..b.X,...b.X,.].
00000110: d767 8bc5 62b1 582c 168b c562 b158 2c16  .g..b.X,...b.X,.
00000120: 8b45 97f5 f5d9 62b1 582c 168b c562 b158  .E....b.X,...b.X
00000130: 2c16 8bc5 62d1 657d 7db6 582c 168b c562  ,...b.e}}.X,...b

# Step 4: pngcheck -c -v mystery 2>/dev/null, Fixing the invalid Chunk Length
# -s flag followed by 0x53 specifies the starting point
AsianHacker-picoctf@webshell:~$ xxd -g 1 -s 0x53 -l 77 mystery | head ⌨️
00000053: aa aa ff a5 ab 44 45 54 78 5e ec bd 3f 8e 64 cd  .....DETx^..?.d.
00000063: 71 bd 2d 8b 20 20 80 90 41 83 02 08 d0 f9 ed 40  q.-.  ..A......@
00000073: a0 f3 6e 40 7b 90 23 8f 1e d7 20 8b 3e b7 c1 0d  ..n@{.#... .>...
00000083: 70 03 74 b5 03 ae 41 6b f8 be a8 fb dc 3e 7d 2a  p.t...Ak.....>}*
00000093: 22 33 6f de 5b 55 dd 3d 3d f9 20 91 88           "3o.[U.==. ..

AsianHacker-picoctf@webshell:~$ printf '\x49\x44\x41\x54' | dd of=mystery bs=1 seek=87 count=4 conv=notrunc ⌨️
4+0 records in
4+0 records out
4 bytes copied, 0.000687262 s, 5.8 kB/s
AsianHacker-picoctf@webshell:~$ xxd mystery | head -n 30 ⌨️
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0138  ..pHYs...%...%.8
00000050: d82c 82aa aaff a549 4441 54👀78 5eec bd3f  .,.....IDAT👀x^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..
000000a0: 3871 2232 eb4f 57cf 14e6 25ff e5ff 5b2c  8q"2.OW...%...[,
000000b0: 168b c562 b158 2c16 8bc5 62b1 582c 161d  ...b.X,...b.X,..
000000c0: d6d7 678b c562 b158 2c16 8bc5 62b1 582c  ..g..b.X,...b.X,
000000d0: 168b 4597 f5f5 d962 b158 2c16 8bc5 62b1  ..E....b.X,...b.
000000e0: 582c 168b c562 d165 7d7d b658 2c16 8bc5  X,...b.e}}.X,...
000000f0: 62b1 582c 168b c562 b158 7459 5f9f 2d16  b.X,...b.XtY_.-.
00000100: 8bc5 62b1 582c 168b c562 b158 2c16 5dd6  ..b.X,...b.X,.].
00000110: d767 8bc5 62b1 582c 168b c562 b158 2c16  .g..b.X,...b.X,.
00000120: 8b45 97f5 f5d9 62b1 582c 168b c562 b158  .E....b.X,...b.X
00000130: 2c16 8bc5 62d1 657d 7db6 582c 168b c562  ,...b.e}}.X,...b
00000140: b158 2c16 8bc5 62b1 5874 595f 9f2d 168b  .X,...b.XtY_.-..
00000150: c562 b158 2c16 8bc5 62b1 582c 165d d6d7  .b.X,...b.X,.]..
00000160: 678b c562 b158 2c16 8bc5 62b1 582c 168b  g..b.X,...b.X,..
00000170: 4597 f5f5 d962 b158 2c16 8bc5 62b1 582c  E....b.X,...b.X,
00000180: 168b c562 d165 7d7d b658 2c16 8bc5 62b1  ...b.e}}.X,...b.
00000190: 582c 168b c562 b158 7459 5f9f 2d16 8bc5  X,...b.XtY_.-...
000001a0: 62b1 582c 168b c562 b158 2c16 5dd6 d767  b.X,...b.X,.]..g
000001b0: 8bc5 62b1 582c 168b c562 b158 2c16 8b45  ..b.X,...b.X,..E
000001c0: 97f5 f5d9 62b1 582c 168b c562 b158 2c16  ....b.X,...b.X,.
000001d0: 8bc5 62d1 657d 7db6 582c 168b c562 b158  ..b.e}}.X,...b.X
AsianHacker-picoctf@webshell:~$ mv mystery mystery.png ⌨️
AsianHacker-picoctf@webshell:~$ sz mystery.png ⌨️

# Open png
picoCTF{c0rrupt10n_1847995} 🔐

# Method 2: Edit in https://hexed.it/ instead of dd

# Method 3: Edit in bvi (last resort)
```

## Flag
picoCTF{c0rrupt10n_1847995}

## Continue
[Continue](./picoGym0074.md)