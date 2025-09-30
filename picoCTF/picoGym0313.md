# picoGym Level 313: unpackme
Source: https://play.picoctf.org/practice/challenge/313

## Goal
Can you get the flag?<br>
Reverse engineer this binary.<br>
https://artifacts.picoctf.net/c/204/unpackme-upx

## What I learned
```
Reverse Engineering

# Check if it’s packed with UPX
upx -t unpackme-upx ⌨️

# Unpack with UPX
upx -d unpackme-upx -o unpackme-unpacked ⌨️
  -d = decompress
  -o = specify output file (optional, you can overwrite in place if you want)

# If it’s modified or UPX fails
upx -d --force unpackme-upx ⌨️

# Manual unpacking
  Run it under gdb or strace
      (gdb) start
      (gdb) info proc mappings                      # find memory regions
      (gdb) dump memory dump.bin 0x400000 0x401000   # adjust addresses
  Break after main is unpacked
  Use gcore or dump memory to save the fully unpacked process image
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/204/unpackme-upx ⌨️
--2025-09-26 21:40:17--  https://artifacts.picoctf.net/c/204/unpackme-upx
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 379188 (370K) [application/octet-stream]
Saving to: 'unpackme-upx'

unpackme-upx                                               100%[======================================================================================================================================>] 370.30K  1.90MB/s    in 0.2s    

2025-09-26 21:40:18 (1.90 MB/s) - 'unpackme-upx' saved [379188/379188]

AsianHacker-picoctf@webshell:~$ file unpackme-upx ⌨️
unpackme-upx: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
AsianHacker-picoctf@webshell:~$ strings unpackme-upx | grep picoCTF ⌨️
AsianHacker-picoctf@webshell:~$ strings unpackme-upx | grep == ⌨️
TMM==U*
w== 

# Check if it’s packed with UPX
AsianHacker-picoctf@webshell:~$ upx -t unpackme-upx ⌨️
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

testing unpackme-upx [OK] 👀

# Unpack with UPX


Tested 1 file.

AsianHacker-picoctf@webshell:~$ upx -d unpackme-upx -o unpackme-unpacked ⌨️⭐⭐⭐⭐⭐
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   1002528 <-    379188   37.82%   linux/amd64   unpackme-unpacked

Unpacked 1 file.

AsianHacker-picoctf@webshell:~$ ./unpackme-unpacked ⌨️
-bash: ./unpackme-unpacked: Permission denied
AsianHacker-picoctf@webshell:~$ chmod +x unpackme-unpacked ⌨️ 
AsianHacker-picoctf@webshell:~$ ./unpackme-unpacked ⌨️
What's my favorite number? 7 ⌨️
Sorry, that's not it!

AsianHacker-picoctf@webshell:~$ objdump -d unpackme-unpacked | head -n 40 ⌨️

unpackme-unpacked:     file format elf64-x86-64


Disassembly of section .init:

0000000000401000 <_init>:
  401000:       f3 0f 1e fa             endbr64 
  401004:       48 83 ec 08             sub    $0x8,%rsp
  401008:       48 c7 c0 00 00 00 00    mov    $0x0,%rax
  40100f:       48 85 c0                test   %rax,%rax
  401012:       74 02                   je     401016 <_init+0x16>
  401014:       ff d0                   call   *%rax
  401016:       48 83 c4 08             add    $0x8,%rsp
  40101a:       c3                      ret    

Disassembly of section .plt:

0000000000401020 <.plt>:
  401020:       f3 0f 1e fa             endbr64 
  401024:       f2 ff 25 ed df 0d 00    bnd jmp *0xddfed(%rip)        # 4df018 <_GLOBAL_OFFSET_TABLE_+0x18>
  40102b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)
  401030:       f3 0f 1e fa             endbr64 
  401034:       f2 ff 25 e5 df 0d 00    bnd jmp *0xddfe5(%rip)        # 4df020 <_GLOBAL_OFFSET_TABLE_+0x20>
  40103b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)
  401040:       f3 0f 1e fa             endbr64 
  401044:       f2 ff 25 dd df 0d 00    bnd jmp *0xddfdd(%rip)        # 4df028 <_GLOBAL_OFFSET_TABLE_+0x28>
  40104b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)
  401050:       f3 0f 1e fa             endbr64 
  401054:       f2 ff 25 d5 df 0d 00    bnd jmp *0xddfd5(%rip)        # 4df030 <_GLOBAL_OFFSET_TABLE_+0x30>
  40105b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)
  401060:       f3 0f 1e fa             endbr64 
  401064:       f2 ff 25 cd df 0d 00    bnd jmp *0xddfcd(%rip)        # 4df038 <_GLOBAL_OFFSET_TABLE_+0x38>
  40106b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)
  401070:       f3 0f 1e fa             endbr64 
  401074:       f2 ff 25 c5 df 0d 00    bnd jmp *0xddfc5(%rip)        # 4df040 <_GLOBAL_OFFSET_TABLE_+0x40>
  40107b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)
  401080:       f3 0f 1e fa             endbr64 
  401084:       f2 ff 25 bd df 0d 00    bnd jmp *0xddfbd(%rip)        # 4df048 <_GLOBAL_OFFSET_TABLE_+0x48>
  40108b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

# Method 1: gdb
AsianHacker-picoctf@webshell:~$ gdb ./unpackme-upx ⌨️
GNU gdb (Ubuntu 12.1-0ubuntu1~22.04.2) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./unpackme-upx...
(No debugging symbols found in ./unpackme-upx)
(gdb) layout asm ⌨️                                             # Optional
(gdb) disassemble main ⌨️                                       # reason for unpacking
No symbol table is loaded.  Use the "file" command. ⚠️
(gdb) exit ⌨️

AsianHacker-picoctf@webshell:~$ gdb ./unpackme-unpacked ⌨️
GNU gdb (Ubuntu 12.1-0ubuntu1~22.04.2) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./unpackme-unpacked...
(No debugging symbols found in ./unpackme-unpacked)
(gdb) disassemble main ⌨️
Dump of assembler code for function main:
   0x0000000000401e43 <+0>:     endbr64 
   0x0000000000401e47 <+4>:     push   %rbp
   0x0000000000401e48 <+5>:     mov    %rsp,%rbp
   0x0000000000401e4b <+8>:     sub    $0x50,%rsp
   0x0000000000401e4f <+12>:    mov    %edi,-0x44(%rbp)
   0x0000000000401e52 <+15>:    mov    %rsi,-0x50(%rbp)
   0x0000000000401e56 <+19>:    mov    %fs:0x28,%rax
   0x0000000000401e5f <+28>:    mov    %rax,-0x8(%rbp)
   0x0000000000401e63 <+32>:    xor    %eax,%eax
   0x0000000000401e65 <+34>:    movabs $0x4c75257240343a41,%rax
   0x0000000000401e6f <+44>:    movabs $0x30623e306b6d4146,%rdx
   0x0000000000401e79 <+54>:    mov    %rax,-0x30(%rbp)
   0x0000000000401e7d <+58>:    mov    %rdx,-0x28(%rbp)
   0x0000000000401e81 <+62>:    movabs $0x5f60643630486637,%rax
   0x0000000000401e8b <+72>:    mov    %rax,-0x20(%rbp)
   0x0000000000401e8f <+76>:    movl   $0x37666132,-0x18(%rbp)
   0x0000000000401e96 <+83>:    movw   $0x4e,-0x14(%rbp)
   0x0000000000401e9c <+89>:    lea    0xb1161(%rip),%rdi        # 0x4b3004
   0x0000000000401ea3 <+96>:    mov    $0x0,%eax
   0x0000000000401ea8 <+101>:   call   0x410ba0 <printf>
   0x0000000000401ead <+106>:   lea    -0x3c(%rbp),%rax
   0x0000000000401eb1 <+110>:   mov    %rax,%rsi
   0x0000000000401eb4 <+113>:   lea    0xb1165(%rip),%rdi        # 0x4b3020
   0x0000000000401ebb <+120>:   mov    $0x0,%eax
   0x0000000000401ec0 <+125>:   call   0x410d30 <__isoc99_scanf>
   0x0000000000401ec5 <+130>:   mov    -0x3c(%rbp),%eax
   0x0000000000401ec8 <+133>:   cmp    $0xb83cb,%eax 👀
   0x0000000000401ecd <+138>:   jne    0x401f12 <main+207>
   0x0000000000401ecf <+140>:   lea    -0x30(%rbp),%rax
   0x0000000000401ed3 <+144>:   mov    %rax,%rsi
   0x0000000000401ed6 <+147>:   mov    $0x0,%edi
   0x0000000000401edb <+152>:   call   0x401d85 <rotate_encrypt>
   0x0000000000401ee0 <+157>:   mov    %rax,-0x38(%rbp)
   0x0000000000401ee4 <+161>:   mov    0xdd7e5(%rip),%rdx        # 0x4df6d0 <stdout>
   0x0000000000401eeb <+168>:   mov    -0x38(%rbp),%rax
   0x0000000000401eef <+172>:   mov    %rdx,%rsi
   0x0000000000401ef2 <+175>:   mov    %rax,%rdi
   0x0000000000401ef5 <+178>:   call   0x420980 <fputs>
   0x0000000000401efa <+183>:   mov    $0xa,%edi
   0x0000000000401eff <+188>:   call   0x420e20 <putchar>
   0x0000000000401f04 <+193>:   mov    -0x38(%rbp),%rax
   0x0000000000401f08 <+197>:   mov    %rax,%rdi
   0x0000000000401f0b <+200>:   call   0x42ec70 <free>
   0x0000000000401f10 <+205>:   jmp    0x401f1e <main+219>
   0x0000000000401f12 <+207>:   lea    0xb110a(%rip),%rdi        # 0x4b3023
   0x0000000000401f19 <+214>:   call   0x420c40 <puts>
   --Type <RET> for more, q to quit, c to continue without paging--c
   0x0000000000401f1e <+219>:   mov    $0x0,%eax
   0x0000000000401f23 <+224>:   mov    -0x8(%rbp),%rcx
   0x0000000000401f27 <+228>:   xor    %fs:0x28,%rcx
   0x0000000000401f30 <+237>:   je     0x401f37 <main+244>
   0x0000000000401f32 <+239>:   call   0x45cba0 <__stack_chk_fail_local>
   0x0000000000401f37 <+244>:   leave  
   0x0000000000401f38 <+245>:   ret    
End of assembler dump.

# Convert hex to int
AsianHacker-picoctf@webshell:~$ python3 -c 'print(0xb83cb)' ⌨️
754635
AsianHacker-picoctf@webshell:~$ echo $((0xb83cb)) ⌨️
754635

AsianHacker-picoctf@webshell:~$ ./unpackme-unpacked ⌨️
What's my favorite number? 754635 ⌨️
picoCTF{up><_m3_f7w_e510a27f} 🔐
```

## Flag
picoCTF{up><_m3_f7w_e510a27f}

## Continue
[Continue](./picoGym0314.md)