# picoGym Level 160: ARMssembly 0
Source: https://play.picoctf.org/practice/challenge/160

## Goal
What integer does this program print with arguments 1765227561 and 1830628817?<br>
File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})<br>
https://mercury.picoctf.net/static/37069d9462289016ea1869ef4c993912/chall.S

## What I learned
```
Reverse Engineering
x86 assembly (AT&T syntax) different than ARMv8 or x86 (intel syntax)

ARMv8A64QuickReference: https://courses.cs.washington.edu/courses/cse469/19wi/arm64.pdf

chall.S is ARMv8 assembly, not x86. You need either:
    a cross-compiler (aarch64-linux-gnu-gcc)
    or original chall.c on your x86 shell

default gcc on picoCTF webshell is an x86-64 toolchain doesn’t understand ARM instructions like ldr w0, [sp, 8] or directives like .arch armv8-a

AsianHacker-picoctf@webshell:~$ gcc chall.S -o chall 
chall.S: Assembler messages:
chall.S:1: Error: no such architecture: `armv8'
chall.S:1: Error: junk at end of line, first unrecognized character is `-'
chall.c:8: Error: too many memory references for `sub'
chall.c:9: Error: too many memory references for `str'
chall.c:10: Error: too many memory references for `str'
chall.c:11: Error: no such instruction: `ldr w1,[sp,12]'
chall.c:12: Error: no such instruction: `ldr w0,[sp,8]'
chall.c:13: Error: too many memory references for `cmp'
chall.c:14: Error: no such instruction: `bls .L2'
chall.c:15: Error: no such instruction: `ldr w0,[sp,12]'
chall.c:16: Error: no such instruction: `b .L3'
chall.c:18: Error: no such instruction: `ldr w0,[sp,8]'
chall.c:20: Error: too many memory references for `add'
chall.c:24: Error: alignment not a power of 2
chall.c:32: Error: no such instruction: `stp x29,x30,[sp,-48]!'
chall.c:33: Error: too many memory references for `add'
chall.c:34: Error: too many memory references for `str'
chall.c:35: Error: too many memory references for `str'
chall.c:36: Error: too many memory references for `str'
chall.c:37: Error: no such instruction: `ldr x0,[x29,32]'
chall.c:38: Error: too many memory references for `add'
chall.c:39: Error: no such instruction: `ldr x0,[x0]'
chall.c:40: Error: no such instruction: `bl atoi'
chall.c:41: Error: too many memory references for `mov'
chall.c:42: Error: no such instruction: `ldr x0,[x29,32]'
chall.c:43: Error: too many memory references for `add'
chall.c:44: Error: no such instruction: `ldr x0,[x0]'
chall.c:45: Error: no such instruction: `bl atoi'
chall.c:46: Error: too many memory references for `mov'
chall.c:47: Error: too many memory references for `mov'
chall.c:48: Error: no such instruction: `bl func1'
chall.c:49: Error: too many memory references for `mov'
chall.c:50: Error: no such instruction: `adrp x0,.LC0'
chall.c:51: Error: too many memory references for `add'
chall.c:52: Error: no such instruction: `bl printf'
chall.c:53: Error: too many memory references for `mov'
chall.c:54: Error: no such instruction: `ldr x19,[sp,16]'
chall.c:55: Error: no such instruction: `ldp x29,x30,[sp],48'
```

## SideQuest
```
        .arch armv8-a               # Target architecture: ARMv8-A
        .file   "chall.c"           # Source filename for debug/info
        .text                       # Switch to code (text) section
        .align  2                   # Align following code to 2^2 = 4-byte boundary
        .global func1               # Make symbol 'func1' visible to linker
        .type   func1, %function    # Mark 'func1' as a function symbol
func1:
        sub     sp, sp, #16         # Allocate 16 bytes on the stack (make space for locals/temps)
        str     w0, [sp, 12]        # Store 32-bit w0 at stack offset sp+12  (comment: "sp12 = 1830628817" in file)
        str     w1, [sp, 8]         # Store 32-bit w1 at stack offset sp+8   (comment: "sp8 = 1765227561")
        ldr     w1, [sp, 12]        # Load the value at sp+12 into w1 (w1 = original w0)
        ldr     w0, [sp, 8]         # Load the value at sp+8  into w0 (w0 = original w1)
        cmp     w1, w0              # Compare w1 with w0 (sets condition flags)
        bls     .L2                 # Branch to .L2 if w1 <= w0 (BLending: "branch if lower or same" — unsigned <=)
        ldr     w0, [sp, 12]        # (not taken if branched) Load sp+12 into w0 — choose the larger (unsigned) value
        b       .L3                 # Unconditional branch to .L3 (skip .L2)
.L2:
        ldr     w0, [sp, 8]         # (taken path) Load sp+8 into w0 — choose the other value when w1 <= w0
.L3:
        add     sp, sp, 16          # Deallocate 16 bytes from stack (restore sp to original)
        ret                         # Return from func1; return value is in w0
        .size   func1, .-func1      # Set size metadata for func1
        .section        .rodata     # Switch to read-only data section (constants)
        .align  3                   # Align to 2^3 = 8-byte boundary for the string
.LC0:
        .string "Result: %ld\n"     # C string used later by printf
        .text                       # Back to code section
        .align  2                   # Align next function
        .global main                # Export main
        .type   main, %function     # Mark main as a function
main:
        stp     x29, x30, [sp, -48]!    # Push frame pointer (x29) and link register (x30) and allocate 48 bytes (new SP)
                                        # (pre-index store pair; SP = SP - 48 then store)
        add     x29, sp, 0              # Set frame pointer x29 = sp (establish stack frame)
        str     x19, [sp, 16]           # Save callee-saved register x19 at stack offset (frame local storage)
        str     w0, [x29, 44]           # Store argc (w0) at frame offset x29+44
        str     x1, [x29, 32]           # Store argv pointer (x1) at frame offset x29+32
        ldr     x0, [x29, 32]           # Load argv pointer into x0   (preparing to fetch argv[1])
        add     x0, x0, 8               # x0 = argv + 8  -> address of argv[1] (pointer size = 8 bytes)
        ldr     x0, [x0]                # x0 = * (argv + 8) -> pointer to the string argv[1]
        bl      atoi                    # call atoi(argv[1]) -> returns int in w0
        mov     w19, w0                 # Save returned int from atoi(argv[1]) into w19 (first number)
        ldr     x0, [x29, 32]           # Load argv pointer again into x0
        add     x0, x0, 16              # x0 = argv + 16 -> address of argv[2]
        ldr     x0, [x0]                # x0 = *(argv + 16) -> pointer to the string argv[2]
        bl      atoi                    # call atoi(argv[2]) -> returns int in w0
        mov     w1, w0                  # Move atoi(argv[2]) result into w1 (second number), ready for func1
        mov     w0, w19                 # Move saved first number into w0 (first arg for func1)
        bl      func1                   # Call func1(w0=first, w1=second); result returned in w0
        mov     w1, w0                  # Move func1's return (w0) into w1 for printf's second argument
        adrp    x0, .LC0                # Load page address of .LC0 into x0 (upper bits) — prepare printf format pointer
        add     x0, x0, :lo12:.LC0      # Add low 12 bits to x0 to get full address of .LC0 (x0 = &"Result: %ld\n")
        bl      printf                  # Call printf(x0, w1) -> prints "Result: <value>\n"
        mov     w0, 0                   # Set return value 0 (int) in w0 for main's exit code
        ldr     x19, [sp, 16]           # Restore saved callee-saved register x19
        ldp     x29, x30, [sp], 48      # Restore x29 and x30 and deallocate 48 bytes (post-index load pair)
        ret                             # Return from main
        .size   main, .-main            # Set size metadata for main
        .ident  "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"  # Compiler identification
        .section        .note.GNU-stack,"",@progbits  # Section attribute (executable stack flag)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/37069d9462289016ea1869ef4c993912/chall.S ⌨️
--2025-09-29 03:34:26--  https://mercury.picoctf.net/static/37069d9462289016ea1869ef4c993912/chall.S
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 917 [application/octet-stream]
Saving to: 'chall.S'

chall.S                                                    100%[======================================================================================================================================>]     917  --.-KB/s    in 0s      

2025-09-29 03:34:26 (374 MB/s) - 'chall.S' saved [917/917]

AsianHacker-picoctf@webshell:~$ file chall.S ⌨️
chall.S: assembler source, ASCII text
AsianHacker-picoctf@webshell:~$ cat chall.S ⌨️
        .arch armv8-a 👀❤️ ARMv8
        .file   "chall.c"
        .text
        .align  2
        .global func1
        .type   func1, %function
func1:
        sub     sp, sp, #16
        str     w0, [sp, 12]            # sp12 = 1830628817
        str     w1, [sp, 8]             # sp8 = 1765227561
        ldr     w1, [sp, 12]            # w1 = 1830628817
        ldr     w0, [sp, 8]             # w2 = 1765227561
        cmp     w1, w0
        bls     .L2                     # bls is jump if less than or equal
        ldr     w0, [sp, 12]            # w0 = 1830628817
        b       .L3
.L2:
        ldr     w0, [sp, 8]
.L3:
        add     sp, sp, 16
        ret
        .size   func1, .-func1
        .section        .rodata
        .align  3
.LC0:
        .string "Result: %ld\n"
        .text
        .align  2
        .global main
        .type   main, %function
main:
        stp     x29, x30, [sp, -48]!
        add     x29, sp, 0
        str     x19, [sp, 16]
        str     w0, [x29, 44]
        str     x1, [x29, 32]
        ldr     x0, [x29, 32]               # arg0
        add     x0, x0, 8                   # arg1 (move 8 bit over)
        ldr     x0, [x0]                    # x0 = "1765227561"
        bl      atoi                        # ascii to int
        mov     w19, w0                     # w19 = 1765227561 (lower bit of x0)
        ldr     x0, [x29, 32]
        add     x0, x0, 16                  # arg2 (move 16 bit over)
        ldr     x0, [x0]                    # x0 = "1830628817"
        bl      atoi                        # ascii to int
        mov     w1, w0                      # w1 = 1830628817
        mov     w0, w19                     # w0 = w19 = 1765227561
        bl      func1
        mov     w1, w0
        adrp    x0, .LC0
        add     x0, x0, :lo12:.LC0
        bl      printf
        mov     w0, 0
        ldr     x19, [sp, 16]
        ldp     x29, x30, [sp], 48
        ret
        .size   main, .-main
        .ident  "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
        .section        .note.GNU-stack,"",@progbits

# Method 1: Manual Labor
# Convert 4134207980 into a 32 bit hex string

AsianHacker-picoctf@webshell:~$ printf "%x\n" 1830628817 ⌨️
6d1d2dd1 🔐
AsianHacker-picoctf@webshell:~$ echo "obase=16; 1830628817" | bc ⌨️
6D1D2DD1 🔐
AsianHacker-picoctf@webshell:~$ python3 -c "print(hex(1830628817).lower())" ⌨️
0x6d1d2dd1 🔐

# Method 2: Compile code and execute:
# Note: Disclaimer: this does not work on WSL
# Install a cross-compiler to compile .S code
sudo apt install binutils-aarch64-linux-gnu gcc-aarch64-linux-gnu ⌨️

# Compile .S code
aarch64-linux-gnu-as -o chall.o chall.S ⌨️
aarch64-linux-gnu-gcc -static -o chall chall.o ⌨️
chmod u+x ./chall.o ⌨️

# Install QEMU to emulate ARM to run code
sudo apt install qemu-user-static ⌨️

./chall 1765227561 1830628817 ⌨️
Result: 1830628817
```

## Flag
picoCTF{6d1d2dd1}

## Continue
[Continue](./picoGym0111.md)