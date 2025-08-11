# gcc
```
Description:
Convert c/c++ to ASM and vice versa

-m32	                            Generate 32-bit output
-S	                                Compile only up to assembly stage (don’t assemble or link)

# C to ASM
gcc -m32 -S asm4.c                  clang -S -m32 asm4.c                gcc -S -masm=intel asm4.c -o asm4.s

# ASM to C
gcc -m32 -o a asm4.S                gcc -m32 -o a asm4.c asm4.S
./a
```

## asm4.c
```c
 #include<stdio.h>
 extern int asm4(char* s);

 int main(){
    char *str = "picoCTF_d899a";
    printf("%X", asm4(str));

    return 0;
 }
```

## asm4.S
```
 .intel_syntax noprefix
 .global asm4
 asm4:
 	push   ebp
 	mov    ebp,esp
 	push   ebx
 	sub    esp,0x10
 	mov    DWORD PTR [ebp-0x10],0x27d
 	mov    DWORD PTR [ebp-0xc],0x0
 	jmp    label2
 label1:
 	add    DWORD PTR [ebp-0xc],0x1
 label2:
 	mov    edx,DWORD PTR [ebp-0xc]
 	mov    eax,DWORD PTR [ebp+0x8]
 	add    eax,edx
 	movzx  eax,BYTE PTR [eax]
 	test   al,al
 	jne    label1
 	mov    DWORD PTR [ebp-0x8],0x1
 	jmp    label3
 label4:
 	mov    edx,DWORD PTR [ebp-0x8]
 	mov    eax,DWORD PTR [ebp+0x8]
 	add    eax,edx
 	movzx  eax,BYTE PTR [eax]
 	movsx  edx,al
 	mov    eax,DWORD PTR [ebp-0x8]
 	lea    ecx,[eax-0x1]
 	mov    eax,DWORD PTR [ebp+0x8]
 	add    eax,ecx
 	movzx  eax,BYTE PTR [eax]
 	movsx  eax,al
 	sub    edx,eax
 	mov    eax,edx
 	mov    edx,eax
 	mov    eax,DWORD PTR [ebp-0x10]
 	lea    ebx,[edx+eax*1]
 	mov    eax,DWORD PTR [ebp-0x8]
 	lea    edx,[eax+0x1]
 	mov    eax,DWORD PTR [ebp+0x8]
 	add    eax,edx
 	movzx  eax,BYTE PTR [eax]
 	movsx  edx,al
 	mov    ecx,DWORD PTR [ebp-0x8]
 	mov    eax,DWORD PTR [ebp+0x8]
 	add    eax,ecx
 	movzx  eax,BYTE PTR [eax]
 	movsx  eax,al
 	sub    edx,eax
 	mov    eax,edx
 	add    eax,ebx
 	mov    DWORD PTR [ebp-0x10],eax
 	add    DWORD PTR [ebp-0x8],0x1
 label3:
 	mov    eax,DWORD PTR [ebp-0xc]
 	sub    eax,0x1
 	cmp    DWORD PTR [ebp-0x8],eax
 	jl     label4
 	mov    eax,DWORD PTR [ebp-0x10]
 	add    esp,0x10
 	pop    ebx
 	pop    ebp
 	ret
```

# objdump
```
# Compile normally
gcc -m32 -o asm4 asm4.c

# Disassemble w/o source                            Disassemble w/ source
objdump -d asm4 > disassembly.asm                   objdump -dS asm4 > with_source.asm
```

# nasm/yasm
```
nasm -f elf32 ams4.asm
```

# radare2 (r2) or Hopper or Ghidra
```
r2 -A ./a.out
> pdf @ main                                        print disassembly of main
```

## Back to README.md
[BACK](../README.md)