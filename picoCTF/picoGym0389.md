# picoGym Level 389: ASCII FTW
Source: https://play.picoctf.org/practice/challenge/389

## Goal
This program has constructed the flag using hex ascii values.<br>
Identify the flag text by disassembling the program.<br>
You can download the file from here.<br>
https://artifacts.picoctf.net/c/506/asciiftw

## What I learned
```
Reverse Engineering
gdb
Ghidra
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/506/asciiftw ⌨️
--2025-09-29 22:58:12--  https://artifacts.picoctf.net/c/506/asciiftw
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16752 (16K) [application/octet-stream]
Saving to: 'asciiftw'

asciiftw                                                   100%[======================================================================================================================================>]  16.36K  --.-KB/s    in 0.004s  

2025-09-29 22:58:12 (3.81 MB/s) - 'asciiftw' saved [16752/16752]

AsianHacker-picoctf@webshell:~$ file asciiftw ⌨️
asciiftw: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c29491782ee13aa7c5734d77b281865b608e46e9, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ chmod u+x asciiftw ⌨️
AsianHacker-picoctf@webshell:~$ ./asciiftw ⌨️
The flag starts with 70
AsianHacker-picoctf@webshell:~$ echo "70" | xxd -p -r ⌨️
p
AsianHacker-picoctf@webshell:~$ python3 -c 'import sys; print(bytes.fromhex(sys.argv[1]).decode("ascii"))' 70 ⌨️
p
# Beware: Wrong, decimal to ascii not hex to ascii ⚠️
AsianHacker-picoctf@webshell:~$ python3 -c "print(chr(70))" ⌨️
F

# Method 1: gdb
AsianHacker-picoctf@webshell:~$ gdb -q asciiftw ⌨️
Reading symbols from asciiftw...
(No debugging symbols found in asciiftw)
(gdb) info functions ⌨️
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001050  __cxa_finalize@plt
0x0000000000001060  __stack_chk_fail@plt
0x0000000000001070  printf@plt
0x0000000000001080  _start
0x00000000000010b0  deregister_tm_clones
0x00000000000010e0  register_tm_clones
0x0000000000001120  __do_global_dtors_aux
0x0000000000001160  frame_dummy
0x0000000000001169  main 👀
0x0000000000001240  __libc_csu_init
0x00000000000012b0  __libc_csu_fini
0x00000000000012b8  _fini

(gdb) disassemble main ⌨️                                  (gdb) layout next ⌨️
Dump of assembler code for function main:
   0x0000000000001169 <+0>:     endbr64 
   0x000000000000116d <+4>:     push   %rbp
   0x000000000000116e <+5>:     mov    %rsp,%rbp
   0x0000000000001171 <+8>:     sub    $0x30,%rsp
   0x0000000000001175 <+12>:    mov    %fs:0x28,%rax
   0x000000000000117e <+21>:    mov    %rax,-0x8(%rbp)
   0x0000000000001182 <+25>:    xor    %eax,%eax
   0x0000000000001184 <+27>:    movb   $0x70,-0x30(%rbp) 👀
   0x0000000000001188 <+31>:    movb   $0x69,-0x2f(%rbp) 👀
   0x000000000000118c <+35>:    movb   $0x63,-0x2e(%rbp) 👀
   0x0000000000001190 <+39>:    movb   $0x6f,-0x2d(%rbp) 👀
   0x0000000000001194 <+43>:    movb   $0x43,-0x2c(%rbp) 👀
   0x0000000000001198 <+47>:    movb   $0x54,-0x2b(%rbp) 👀
   0x000000000000119c <+51>:    movb   $0x46,-0x2a(%rbp) 👀
   0x00000000000011a0 <+55>:    movb   $0x7b,-0x29(%rbp) 👀
   0x00000000000011a4 <+59>:    movb   $0x41,-0x28(%rbp) 👀
   0x00000000000011a8 <+63>:    movb   $0x53,-0x27(%rbp) 👀
   0x00000000000011ac <+67>:    movb   $0x43,-0x26(%rbp) 👀
   0x00000000000011b0 <+71>:    movb   $0x49,-0x25(%rbp) 👀
   0x00000000000011b4 <+75>:    movb   $0x49,-0x24(%rbp) 👀
   0x00000000000011b8 <+79>:    movb   $0x5f,-0x23(%rbp) 👀
   0x00000000000011bc <+83>:    movb   $0x49,-0x22(%rbp) 👀
   0x00000000000011c0 <+87>:    movb   $0x53,-0x21(%rbp) 👀
   0x00000000000011c4 <+91>:    movb   $0x5f,-0x20(%rbp) 👀
   0x00000000000011c8 <+95>:    movb   $0x45,-0x1f(%rbp) 👀
   0x00000000000011cc <+99>:    movb   $0x41,-0x1e(%rbp) 👀
   0x00000000000011d0 <+103>:   movb   $0x53,-0x1d(%rbp) 👀
   0x00000000000011d4 <+107>:   movb   $0x59,-0x1c(%rbp) 👀
   0x00000000000011d8 <+111>:   movb   $0x5f,-0x1b(%rbp) 👀
   0x00000000000011dc <+115>:   movb   $0x33,-0x1a(%rbp) 👀
   0x00000000000011e0 <+119>:   movb   $0x43,-0x19(%rbp) 👀
   0x00000000000011e4 <+123>:   movb   $0x46,-0x18(%rbp) 👀
   0x00000000000011e8 <+127>:   movb   $0x34,-0x17(%rbp) 👀
   0x00000000000011ec <+131>:   movb   $0x42,-0x16(%rbp) 👀
   0x00000000000011f0 <+135>:   movb   $0x46,-0x15(%rbp) 👀
   0x00000000000011f4 <+139>:   movb   $0x41,-0x14(%rbp) 👀
   0x00000000000011f8 <+143>:   movb   $0x44,-0x13(%rbp) 👀
   0x00000000000011fc <+147>:   movb   $0x7d,-0x12(%rbp) 👀
   0x0000000000001200 <+151>:   movzbl -0x30(%rbp),%eax
   0x0000000000001204 <+155>:   movsbl %al,%eax
   0x0000000000001207 <+158>:   mov    %eax,%esi
   0x0000000000001209 <+160>:   lea    0xdf4(%rip),%rdi        # 0x2004
   0x0000000000001210 <+167>:   mov    $0x0,%eax
   0x0000000000001215 <+172>:   call   0x1070 <printf@plt>
   0x000000000000121a <+177>:   nop
   0x000000000000121b <+178>:   mov    -0x8(%rbp),%rax
--Type <RET> for more, q to quit, c to continue without paging--c
   0x000000000000121f <+182>:   xor    %fs:0x28,%rax
   0x0000000000001228 <+191>:   je     0x122f <main+198>
   0x000000000000122a <+193>:   call   0x1060 <__stack_chk_fail@plt>
   0x000000000000122f <+198>:   leave  
   0x0000000000001230 <+199>:   ret    
End of assembler dump.

# RE in Notepad++ or could of asked ChatGPT
(gdb) printf "%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c\n", 0x70, 0x69, 0x63, 0x6f, 0x43, 0x54, 0x46, 0x7b, 0x41, 0x53, 0x43, 0x49, 0x49, 0x5f, 0x49, 0x53, 0x5f, 0x45, 0x41, 0x53, 0x59, 0x5f, 0x33, 0x43, 0x46, 0x34, 0x42, 0x46, 0x41, 0x44, 0x7d ⌨️
picoCTF{ASCII_IS_EASY_3CF4BFAD} 🔐
```

## Flag
picoCTF{ASCII_IS_EASY_3CF4BFAD}

## Continue
[Continue](./picoGym0271.md)