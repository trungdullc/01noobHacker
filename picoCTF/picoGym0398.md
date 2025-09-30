# picoGym Level 398: GDB baby step 4
Source: https://play.picoctf.org/practice/challenge/398

## Goal
main calls a function that multiplies eax by a constant.<br>
The flag for this challenge is that constant in decimal base.<br>
If the constant you find is 0x1000, the flag will be picoCTF{4096}.<br>
Debug this.<br>
https://artifacts.picoctf.net/c/532/debugger0_d

## What I learned
```
Reverse Engineering
gdb
    disassemble func1

Architecture:
    On x86 (32-bit) processors, eax is the 32-bit accumulator register. It’s often used for arithmetic operations, function return values, and system calls.
In 64-bit mode (x86-64):
    The full 64-bit register is called rax
    eax = the lower 32 bits of rax
    ax = the lower 16 bits of eax
    al / ah = the low and high 8 bits of ax
In GDB:
    info registers eax → shows the current 32-bit value in the eax register
    If you modify eax, the upper 32 bits of rax are automatically cleared to zero (on x86-64 CPUs)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/532/debugger0_d ⌨️
--2025-09-28 15:36:36--  https://artifacts.picoctf.net/c/532/debugger0_d
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16328 (16K) [application/octet-stream]
Saving to: 'debugger0_d'

debugger0_d                                                100%[======================================================================================================================================>]  15.95K  --.-KB/s    in 0.004s  

2025-09-28 15:36:36 (3.97 MB/s) - 'debugger0_d' saved [16328/16328]

AsianHacker-picoctf@webshell:~$ file debugger0_d ⌨️
debugger0_d: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=96ad8d8a802a567a7a1a27cf9b7231e2f7fa15f7, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ gdb -q debugger0_d ⌨️
Reading symbols from debugger0_d...
(No debugging symbols found in debugger0_d)
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
0x0000000000401106  func1
0x000000000040111c  main 👀
0x0000000000401150  __libc_csu_init
0x00000000004011c0  __libc_csu_fini
0x00000000004011c8  _fini
(gdb) set disassembly-flavor intel ⌨️
(gdb) disassemble main ⌨️
Dump of assembler code for function main:
   0x000000000040111c <+0>:     endbr64 
   0x0000000000401120 <+4>:     push   rbp
   0x0000000000401121 <+5>:     mov    rbp,rsp
   0x0000000000401124 <+8>:     sub    rsp,0x20
   0x0000000000401128 <+12>:    mov    DWORD PTR [rbp-0x14],edi
   0x000000000040112b <+15>:    mov    QWORD PTR [rbp-0x20],rsi
   0x000000000040112f <+19>:    mov    DWORD PTR [rbp-0x4],0x28e
   0x0000000000401136 <+26>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040113d <+33>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401140 <+36>:    mov    edi,eax
   0x0000000000401142 <+38>:    call   0x401106 <func1> 👀
   0x0000000000401147 <+43>:    mov    DWORD PTR [rbp-0x8],eax
   0x000000000040114a <+46>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040114d <+49>:    leave  
   0x000000000040114e <+50>:    ret    
End of assembler dump.
(gdb) break main ⌨️
Breakpoint 1 at 0x401124
(gdb) info break ⌨️
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x0000000000401124 <main+8>
(gdb) run ⌨️
Starting program: /home/AsianHacker-picoctf/debugger0_d 
warning: Error disabling address space randomization: Operation not permitted
/bin/bash: line 1: /home/AsianHacker-picoctf/debugger0_d: Permission denied
/bin/bash: line 1: exec: /home/AsianHacker-picoctf/debugger0_d: cannot execute: Permission denied ⚠️
During startup program exited with code 126.
(gdb) delete 1 ⌨️
(gdb) info break ⌨️
No breakpoints or watchpoints.
Breakpoint 2 at 0x40110e
(gdb) exit ⌨️

AsianHacker-picoctf@webshell:~$ chmod u+x debugger0_d ⌨️
(gdb) disassemble func1 ⌨️
Dump of assembler code for function func1:
   0x0000000000401106 <+0>:     endbr64 
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000401111 <+11>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401114 <+14>:    imul   eax,eax,0x3269 👀
   0x000000000040111a <+20>:    pop    rbp
   0x000000000040111b <+21>:    ret    
End of assembler dump.
(gdb) print/d 0x3269 ⌨️ 
$1 = 12905 🔐
```

## Flag
picoCTF{12905}

## Continue
[Continue](./picoGym0160.md)