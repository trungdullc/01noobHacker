# xxd

```
Source: https://www.commandlinux.com/man-page/man1/xxd.1.html
Description: Modify hex dump from a file
hex dump is a byte-by-byte view of data from a file or memory, shown in hexadecimal (base-16) format, often alongside its ASCII representation

00000000  48 65 6c 6c 6f 20 77 6f 72 6c 64 21 0a        |Hello world!.|
    00000000:       Offset (byte address in file/memory)
    48 65 6c ...:   Hex values (each 2-digit hex = 1 byte)
    Hello world!.:  ASCII translation of the bytes

xxd FILE.txt
```

## CTF
[picoGym0186: Forensic](../picoCTF/picoGym0186.md)<br>
[picoGym0415: xxd -r -p](../picoCTF/picoGym0415.md)

[BACK](../README.md)