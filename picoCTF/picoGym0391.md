# picoGym Level 391: Bit-O-Asm-1
Source: https://play.picoctf.org/practice/challenge/391

## Goal
Can you figure out what is in the eax register?<br>
Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base.<br>
If the answer was 0x11 your flag would be picoCTF{17}.<br>
Download the assembly dump here.<br>
https://artifacts.picoctf.net/c/509/disassembler-dump0_a.txt

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/509/disassembler-dump0_a.txt ⌨️
--2025-09-30 01:04:53--  https://artifacts.picoctf.net/c/509/disassembler-dump0_a.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 209 [application/octet-stream]
Saving to: 'disassembler-dump0_a.txt'

disassembler-dump0_a.txt                                   100%[======================================================================================================================================>]     209  --.-KB/s    in 0s      

2025-09-30 01:04:53 (133 MB/s) - 'disassembler-dump0_a.txt' saved [209/209]

AsianHacker-picoctf@webshell:~$ file disassembler-dump0_a.txt ⌨️
disassembler-dump0_a.txt: ASCII text
AsianHacker-picoctf@webshell:~$ cat disassembler-dump0_a.txt ⌨️
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30 👀
<+20>:    pop    rbp
<+21>:    ret
AsianHacker-picoctf@webshell:~$ python3 ⌨️
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x30
48 🔐
```

## Flag
picoCTF{48}

## Continue
[Continue](./picoGym0392.md)