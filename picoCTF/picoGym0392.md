# picoGym Level 392: Bit-O-Asm-2
Source: https://play.picoctf.org/practice/challenge/392

## Goal
Can you figure out what is in the eax register?<br>
Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base.<br>
If the answer was 0x11 your flag would be picoCTF{17}.<br>
Download the assembly dump here.<br>
https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt ⌨️
--2025-09-30 02:53:06--  https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'disassembler-dump0_b.txt'

disassembler-dump0_b.txt                                   100%[======================================================================================================================================>]     270  --.-KB/s    in 0s      

2025-09-30 02:53:06 (174 MB/s) - 'disassembler-dump0_b.txt' saved [270/270]

AsianHacker-picoctf@webshell:~$ cat disassembler-dump0_b.txt ⌨️
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a 👀
<+22>:    mov    eax,DWORD PTR [rbp-0x4] 👀
<+25>:    pop    rbp
<+26>:    ret

# Method 1:
AsianHacker-picoctf@webshell:~$ python3 ⌨️
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x9fe1a ⌨️
654874 🔐
>>> exit() ⌨️
AsianHacker-picoctf@webshell:~$ python3 -c "print(0x9fe1a)" ⌨️
654874 🔐
```

## Flag
picoCTF{654874}

## Continue
[Continue](./picoGym0393.md)