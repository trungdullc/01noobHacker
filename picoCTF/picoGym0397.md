# picoGym Level 397: GDB baby step 3
Source: https://play.picoctf.org/practice/challenge/397

## Goal
Now for something a little different. 0x2262c96b is loaded into memory in the main function.<br>
Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr.<br>
The flag is the four bytes as they are stored in memory.<br>
If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.<br>
Debug this.<br>
https://artifacts.picoctf.net/c/531/debugger0_c

## What I learned
```
Reverse Engineering
gdb
x/4xb $rbp-0x4
    x = examine memory
    4 → display 4 units                         Examine 4 bytes of memory, each shown as a hex byte
    x → display them in hexadecimal
    b → the unit size is 1 byte
    $rbp = value of base pointer register (frame pointer) usually points to base of current stack frame
    $rbp-4 means "the address 4 bytes below rbp"
    On x86-64, local variables are often stored at negative offsets from rbp
    $rbp-4 is most likely where the compiler stored a local int variable

Example                                         Examine: 7ffc 02b4 126c
    (gdb) x/4xb 0x7ffc02b4126c
    0x7ffc02b4126c:     0x6b    0xc9    0x62    0x22

Note: If reverse (little-endian storage), 0x2262c96b — matches value in eax ❤️
(gdb) info registers eax
eax            0x2262c96b          576899435
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/531/debugger0_c ⌨️
--2025-09-28 03:54:35--  https://artifacts.picoctf.net/c/531/debugger0_c
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.77, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16304 (16K) [application/octet-stream]
Saving to: 'debugger0_c'

debugger0_c                                                100%[======================================================================================================================================>]  15.92K  --.-KB/s    in 0.004s  

2025-09-28 03:54:35 (3.89 MB/s) - 'debugger0_c' saved [16304/16304]

AsianHacker-picoctf@webshell:~$ file debugger0_c ⌨️
debugger0_c: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a10a8fa896351748020d158a4e18bb4be15cd3aa, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ chmod u+x debugger0_c ⌨️
AsianHacker-picoctf@webshell:~$ ls -la debugger0_c ⌨️
-rwxrw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 16304 Aug  4  2023 debugger0_c
AsianHacker-picoctf@webshell:~$ gdb -q debugger0_c ⌨️
Reading symbols from debugger0_c...
(No debugging symbols found in debugger0_c)
(gdb) info functions ⌨️
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401020  _start
0x0000000000401050  _dl_relocate_static_pie
0x0000000000401060  deregister_tm_clones
0x0000000000401090  register_tm_clones
0x00000000004010d0  __do_global_dtors_aux
0x0000000000401100  frame_dummy
0x0000000000401106  main 👀
0x0000000000401130  __libc_csu_init
0x00000000004011a0  __libc_csu_fini
0x00000000004011a8  _fini
(gdb) set disassembly-flavor intel ⌨️
(gdb) disassemble main ⌨️
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64 
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x2262c96b 👀
   0x000000000040111c <+22>:    mov    eax,DWORD PTR [rbp-0x4] 👀
   0x000000000040111f <+25>:    pop    rbp
   0x0000000000401120 <+26>:    ret    
End of assembler dump.
(gdb) break main ⌨️
Breakpoint 1 at 0x40110e
(gdb) run ⌨️
Starting program: /home/AsianHacker-picoctf/debugger0_c 
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000000000040110e in main ()
(gdb) break *0x40111f ⌨️
Breakpoint 2 at 0x40111f
(gdb) c ⌨️
Continuing.

Breakpoint 2, 0x000000000040111f in main ()
(gdb) info registers eax ⌨️
eax            0x2262c96b          576899435

# Inspect actual memory content
(gdb) x/4xb $rbp ⌨️
0x7ffc02b41270: 0x01    0x00    0x00    0x00
(gdb) x/4xb $rbp-0x4 ⌨️
0x7ffc02b4126c: 0x6b    0xc9    0x62    0x22 🔐
```

## Flag
picoCTF{0x6bc96222}

## Continue
[Continue](./picoGym0398.md)