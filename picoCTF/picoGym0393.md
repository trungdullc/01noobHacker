# picoGym Level 393: Bit-O-Asm-3
Source: https://play.picoctf.org/practice/challenge/393

## Goal
Can you figure out what is in the eax register?<br>
Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base.<br>
If the answer was 0x11 your flag would be picoCTF{17}.<br>
Download the assembly dump here.<br>
https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt ⌨️
--2025-09-30 03:01:24--  https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 461 [application/octet-stream]
Saving to: 'disassembler-dump0_c.txt'

disassembler-dump0_c.txt                                   100%[======================================================================================================================================>]     461  --.-KB/s    in 0s      

2025-09-30 03:01:24 (251 MB/s) - 'disassembler-dump0_c.txt' saved [461/461]

AsianHacker-picoctf@webshell:~$ cat disassembler-dump0_c.txt ⌨️
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a        # [rbp-0xc] = 654874
<+22>:    mov    DWORD PTR [rbp-0x8],0x4            # [rbp-0x8] = 4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]            # eax = 654874
<+32>:    imul   eax,DWORD PTR [rbp-0x8]            # eax = eax * 4 = 2619496
<+36>:    add    eax,0x1f5                          # eax = eax + 501 = 2619997
<+41>:    mov    DWORD PTR [rbp-0x4],eax            # [rbp-0x4] = 2619997
<+44>:    mov    eax,DWORD PTR [rbp-0x4]            # eax = 2619997 🔐
<+47>:    pop    rbp
<+48>:    ret
```

## Flag
picoCTF{2619997}

## Continue
[Continue](./picoGym0394.md)