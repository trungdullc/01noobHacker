# picoGym Level 394: Bit-O-Asm-4
Source: https://play.picoctf.org/practice/challenge/394

## Goal
Can you figure out what is in the eax register?<br>
Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base.<br>
If the answer was 0x11 your flag would be picoCTF{17}.<br>
Download the assembly dump here.<br>
https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt ⌨️
--2025-09-30 03:12:43--  https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.77, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 482 [application/octet-stream]
Saving to: 'disassembler-dump0_d.txt'

disassembler-dump0_d.txt                                   100%[======================================================================================================================================>]     482  --.-KB/s    in 0s      

2025-09-30 03:12:43 (415 MB/s) - 'disassembler-dump0_d.txt' saved [482/482]

AsianHacker-picoctf@webshell:~$ cat disassembler-dump0_d.txt ⌨️
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a        # [rbp-0x4] = 654874
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710         # 654874 != 10000
<+29>:    jle    0x55555555514e <main+37>           # Jump if Less or Equal (False, skip)
<+31>:    sub    DWORD PTR [rbp-0x4],0x65           # [rbp-0x4] = [rbp-0x4] - 101 = 654773
<+35>:    jmp    0x555555555152 <main+41>           # Jump to main+41
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]            # eax = 654773 🔐
<+44>:    pop    rbp
<+45>:    ret
```

## Flag
picoCTF{654773}

## Continue
[Continue](./picoGym0421.md)