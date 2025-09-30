# picoGym Level 111: ARMssembly 1
Source: https://play.picoctf.org/practice/challenge/111

## Goal
For what argument does this program print `win` with variables 68, 2 and 3?<br>
File: chall_1.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})<br>
https://mercury.picoctf.net/static/d6c56d724795c006b319c6aa6a09140e/chall_1.S

## What I learned
```
Reverse Engineering
lsl is left shift
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/d6c56d724795c006b319c6aa6a09140e/chall_1.S ⌨️
--2025-09-29 21:11:04--  https://mercury.picoctf.net/static/d6c56d724795c006b319c6aa6a09140e/chall_1.S
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1108 (1.1K) [application/octet-stream]
Saving to: 'chall_1.S'

chall_1.S                                                  100%[======================================================================================================================================>]   1.08K  --.-KB/s    in 0s      

2025-09-29 21:11:04 (304 MB/s) - 'chall_1.S' saved [1108/1108]

AsianHacker-picoctf@webshell:~$ file chall_1.S ⌨️
chall_1.S: assembler source, ASCII text
AsianHacker-picoctf@webshell:~$ cat chall_1.S ⌨️
        .arch armv8-a 👀
        .file   "chall_1.c"
        .text
        .align  2
        .global func
        .type   func, %function
func:
        sub     sp, sp, #32
        str     w0, [sp, 12]
        mov     w0, 68
        str     w0, [sp, 16]
        mov     w0, 2
        str     w0, [sp, 20]
        mov     w0, 3
        str     w0, [sp, 24]
        ldr     w0, [sp, 20]
        ldr     w1, [sp, 16]
        lsl     w0, w1, w0              # left shift << 3
        str     w0, [sp, 28]
        ldr     w1, [sp, 28]
        ldr     w0, [sp, 24]
        sdiv    w0, w1, w0
        str     w0, [sp, 28]
        ldr     w1, [sp, 28]
        ldr     w0, [sp, 12]
        sub     w0, w1, w0
        str     w0, [sp, 28]
        ldr     w0, [sp, 28]
        add     sp, sp, 32
        ret
        .size   func, .-func
        .section        .rodata
        .align  3
.LC0:
        .string "You win!"
        .align  3
.LC1:
        .string "You Lose :("
        .text
        .align  2
        .global main
        .type   main, %function
main:
        stp     x29, x30, [sp, -48]!
        add     x29, sp, 0
        str     w0, [x29, 28]
        str     x1, [x29, 16]
        ldr     x0, [x29, 16]
        add     x0, x0, 8
        ldr     x0, [x0]
        bl      atoi
        str     w0, [x29, 44]
        ldr     w0, [x29, 44]
        bl      func
        cmp     w0, 0
        bne     .L4
        adrp    x0, .LC0
        add     x0, x0, :lo12:.LC0
        bl      puts
        b       .L6
.L4:
        adrp    x0, .LC1
        add     x0, x0, :lo12:.LC1
        bl      puts
.L6:
        nop
        ldp     x29, x30, [sp], 48
        ret
        .size   main, .-main
        .ident  "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
        .section        .note.GNU-stack,"",@progbits

Method 1: ChatGPT
Analyze func:
        Stores input at [sp+12]
        Sets 68 at [sp+16], 2 at [sp+20], 3 at [sp+24]
        Does lsl w0, w1, w0 → 68 << 2 = 272
        sdiv w0, 272, 3 → 272 / 3 = 90 (integer division)
        Computes w0 = 90 - input and returns that
Convert 90 to the required 32-bit, lowercase, zero-padded hex (8 hex digits)
picoCTF{0000005a} 🔐
```

## Flag
picoCTF{0000005a}

## Continue
[Continue](./picoGym0020.md)