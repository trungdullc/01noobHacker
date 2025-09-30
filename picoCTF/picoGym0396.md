# picoGym Level 396: GDB baby step 2
Source: https://play.picoctf.org/practice/challenge/396

## Goal
Can you figure out what is in the eax register at the end of the main function?<br>
Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base.<br>
If the answer was 0x11 your flag would be picoCTF{17}.<br>
Debug this.<br>
https://artifacts.picoctf.net/c/520/debugger0_b

## What I learned
```
Reverse Engineering
gdb

rax
    eax is subset of rax

EIP register or RIP register in x64 because it always contains the memory address of the instruction that will be executed
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/520/debugger0_b ⌨️
--2025-09-28 03:27:39--  https://artifacts.picoctf.net/c/520/debugger0_b
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.33, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16304 (16K) [application/octet-stream]
Saving to: 'debugger0_b'

debugger0_b                                                100%[======================================================================================================================================>]  15.92K  --.-KB/s    in 0s      

2025-09-28 03:27:39 (337 MB/s) - 'debugger0_b' saved [16304/16304]

AsianHacker-picoctf@webshell:~$ file debugger0_b ⌨️
debugger0_b: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=95b0203be2982e75dbc01d1cc25b1309f7aec5f7, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ ls -la debugger0_b ⌨️
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 16304 Aug  4  2023 debugger0_b
AsianHacker-picoctf@webshell:~$ chmod +x debugger0_b ⌨️
AsianHacker-picoctf@webshell:~$ gdb -q debugger0_b ⌨️
Reading symbols from debugger0_b...
(No debugging symbols found in debugger0_b)                 # Optional
(gdb) info functions ⌨️                                     (gdb) set disassembly-flavor intel ⌨️
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
0x0000000000401150  __libc_csu_init
0x00000000004011c0  __libc_csu_fini
0x00000000004011c8  _fini
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64 
   0x000000000040110a <+4>:     push   %rbp
   0x000000000040110b <+5>:     mov    %rsp,%rbp
   0x000000000040110e <+8>:     mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:    mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:    movl   $0x1e0da,-0x4(%rbp)
   0x000000000040111c <+22>:    movl   $0x25f,-0xc(%rbp)
   0x0000000000401123 <+29>:    movl   $0x0,-0x8(%rbp)
   0x000000000040112a <+36>:    jmp    0x401136 <main+48>
   0x000000000040112c <+38>:    mov    -0x8(%rbp),%eax
   0x000000000040112f <+41>:    add    %eax,-0x4(%rbp)
   0x0000000000401132 <+44>:    addl   $0x1,-0x8(%rbp)
   0x0000000000401136 <+48>:    mov    -0x8(%rbp),%eax
   0x0000000000401139 <+51>:    cmp    -0xc(%rbp),%eax
   0x000000000040113c <+54>:    jl     0x40112c <main+38>
   0x000000000040113e <+56>:    mov    -0x4(%rbp),%eax 👀 remember this not intel need next line at least
   0x0000000000401141 <+59>:    pop    %rbp
   0x0000000000401142 <+60>:    ret    
End of assembler dump.
(gdb) break *(main+60) ⌨️                                   (gdb) break main ⌨️
Breakpoint 1 at 0x401142                                    (gdb) layout asm ⌨️
(gdb) run ⌨️
Starting program: /home/AsianHacker-picoctf/debugger0_b 
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
                                                            # Note: where ret was
Breakpoint 1, 0x0000000000401142 in main ()                 (gdb) break *0x401142 ⌨️
(gdb) print/x $eax ⌨️                                       (gdb) c ⌨️
$1 = 0x4af4b                                                # Content of the instruction pointer register (RIP)
(gdb) print/d $eax ⌨️                                      (gdb) info registers rip ⌨️
$2 = 307019 🔐
(gdb) info registers ⌨️
rax            0x4af4b             307019 🔐
rbx            0x0                 0
rcx            0x401150            4198736
rdx            0x7ffd217d20c8      140725165301960
rsi            0x7ffd217d20b8      140725165301944
rdi            0x1                 1
rbp            0x1                 0x1
rsp            0x7ffd217d1fa8      0x7ffd217d1fa8
r8             0x7f9aea767f10      140303335325456
r9             0x7f9aea791040      140303335493696
r10            0x7f9aea78b908      140303335471368
r11            0x7f9aea7a6660      140303335581280
r12            0x7ffd217d20b8      140725165301944
r13            0x401106            4198662
r14            0x0                 0
r15            0x7f9aea7c5040      140303335706688
rip            0x401142            0x401142 <main+60>
eflags         0x246               [ PF ZF IF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0
k0             0x1000000           16777216
k1             0x80001000          2147487744
k2             0x0                 0
k3             0x0                 0
k4             0x0                 0
k5             0x0                 0
k6             0x0                 0
k7             0x0                 0
(gdb) info registers eax ⌨️
eax            0x4af4b             307019 🔐
```

## Flag
picoCTF{307019}

## Continue
[Continue](./picoGym0397.md)