# picoGym Level 458: perplexed
Source: https://play.picoctf.org/practice/challenge/458

## Goal
Download the binary here<br>
https://challenge-files.picoctf.net/c_verbal_sleep/2326718ce11c5c89056a46fce49a5e46ab80e02d551d87744306ae43a4767e06/perplexed

## What I learned
```
Reverse Engineering

IDA
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_verbal_sleep/ 2326718ce11c5c89056a46fce49a5e46ab80e02d551d87744306ae43a4767e06/perplexed ⌨️
--2025-09-30 07:40:07--  https://challenge-files.picoctf.net/c_verbal_sleep/2326718ce11c5c89056a46fce49a5e46ab80e02d551d87744306ae43a4767e06/perplexed
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.95, 3.160.5.40, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16848 (16K) [application/octet-stream]
Saving to: 'perplexed'

perplexed                                                  100%[======================================================================================================================================>]  16.45K  --.-KB/s    in 0s      

2025-09-30 07:40:07 (54.6 MB/s) - 'perplexed' saved [16848/16848]

AsianHacker-picoctf@webshell:~$ file perplexed ⌨️
perplexed: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=85480b12e666f376909d57d282a1ef0f30e93db4, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ chmod u+x perplexed ⌨️
AsianHacker-picoctf@webshell:~$ strings -n 8 perplexed | grep picoCTF{ ⌨️
AsianHacker-picoctf@webshell:~$ strings -n 8 perplexed | grep flag ⌨️
AsianHacker-picoctf@webshell:~$ strings  perplexed | grep == ⌨️
AsianHacker-picoctf@webshell:~$ ./perplexed ⌨️
Enter the password: x ⌨️
Wrong :(

AsianHacker-picoctf@webshell:~$ gdb -q perplexed ⌨️
Reading symbols from perplexed...
(No debugging symbols found in perplexed)
(gdb) info functions ⌨️
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401030  puts@plt
0x0000000000401040  strlen@plt
0x0000000000401050  printf@plt
0x0000000000401060  fgets@plt
0x0000000000401070  _start
0x00000000004010a0  _dl_relocate_static_pie
0x00000000004010b0  deregister_tm_clones
0x00000000004010e0  register_tm_clones
0x0000000000401120  __do_global_dtors_aux
0x0000000000401150  frame_dummy
0x0000000000401156  check 👀
0x00000000004012a5  main 👀
0x000000000040144c  _fini

(gdb) disassemble main ⌨️
Dump of assembler code for function main:
   0x00000000004012a5 <+0>:     push   %rbp
   0x00000000004012a6 <+1>:     mov    %rsp,%rbp
   0x00000000004012a9 <+4>:     sub    $0x110,%rsp
   0x00000000004012b0 <+11>:    movq   $0x0,-0x110(%rbp)
   0x00000000004012bb <+22>:    movq   $0x0,-0x108(%rbp)
   0x00000000004012c6 <+33>:    movq   $0x0,-0x100(%rbp)
   0x00000000004012d1 <+44>:    movq   $0x0,-0xf8(%rbp)
   0x00000000004012dc <+55>:    movq   $0x0,-0xf0(%rbp)
   0x00000000004012e7 <+66>:    movq   $0x0,-0xe8(%rbp)
   0x00000000004012f2 <+77>:    movq   $0x0,-0xe0(%rbp)
   0x00000000004012fd <+88>:    movq   $0x0,-0xd8(%rbp)
   0x0000000000401308 <+99>:    movq   $0x0,-0xd0(%rbp)
   0x0000000000401313 <+110>:   movq   $0x0,-0xc8(%rbp)
   0x000000000040131e <+121>:   movq   $0x0,-0xc0(%rbp)
   0x0000000000401329 <+132>:   movq   $0x0,-0xb8(%rbp)
   0x0000000000401334 <+143>:   movq   $0x0,-0xb0(%rbp)
   0x000000000040133f <+154>:   movq   $0x0,-0xa8(%rbp)
   0x000000000040134a <+165>:   movq   $0x0,-0xa0(%rbp)
   0x0000000000401355 <+176>:   movq   $0x0,-0x98(%rbp)
   0x0000000000401360 <+187>:   movq   $0x0,-0x90(%rbp)
   0x000000000040136b <+198>:   movq   $0x0,-0x88(%rbp)
   0x0000000000401376 <+209>:   movq   $0x0,-0x80(%rbp)
   0x000000000040137e <+217>:   movq   $0x0,-0x78(%rbp)
   0x0000000000401386 <+225>:   movq   $0x0,-0x70(%rbp)
   0x000000000040138e <+233>:   movq   $0x0,-0x68(%rbp)
   0x0000000000401396 <+241>:   movq   $0x0,-0x60(%rbp)
   0x000000000040139e <+249>:   movq   $0x0,-0x58(%rbp)
   0x00000000004013a6 <+257>:   movq   $0x0,-0x50(%rbp)
   0x00000000004013ae <+265>:   movq   $0x0,-0x48(%rbp)
   0x00000000004013b6 <+273>:   movq   $0x0,-0x40(%rbp)
   0x00000000004013be <+281>:   movq   $0x0,-0x38(%rbp)
   0x00000000004013c6 <+289>:   movq   $0x0,-0x30(%rbp)
   0x00000000004013ce <+297>:   movq   $0x0,-0x28(%rbp)
   0x00000000004013d6 <+305>:   movq   $0x0,-0x20(%rbp)
   0x00000000004013de <+313>:   movq   $0x0,-0x18(%rbp)
   0x00000000004013e6 <+321>:   mov    $0x402010,%edi
   0x00000000004013eb <+326>:   mov    $0x0,%eax
   0x00000000004013f0 <+331>:   call   0x401050 <printf@plt>
   0x00000000004013f5 <+336>:   mov    0x2c34(%rip),%rdx        # 0x404030 <stdin@GLIBC_2.2.5>
   0x00000000004013fc <+343>:   lea    -0x110(%rbp),%rax
   0x0000000000401403 <+350>:   mov    $0x100,%esi
   0x0000000000401408 <+355>:   mov    %rax,%rdi
   0x000000000040140b <+358>:   call   0x401060 <fgets@plt>
   0x0000000000401410 <+363>:   lea    -0x110(%rbp),%rax
   0x0000000000401417 <+370>:   mov    %rax,%rdi
   0x000000000040141a <+373>:   call   0x401156 <check> 👀
--Type <RET> for more, q to quit, c to continue without paging--c
   0x000000000040141f <+378>:   mov    %eax,-0x4(%rbp)
   0x0000000000401422 <+381>:   cmpl   $0x1,-0x4(%rbp)
   0x0000000000401426 <+385>:   jne    0x401439 <main+404>
   0x0000000000401428 <+387>:   mov    $0x402025,%edi
   0x000000000040142d <+392>:   call   0x401030 <puts@plt>
   0x0000000000401432 <+397>:   mov    $0x1,%eax
   0x0000000000401437 <+402>:   jmp    0x401448 <main+419>
   0x0000000000401439 <+404>:   mov    $0x40202e,%edi
   0x000000000040143e <+409>:   call   0x401030 <puts@plt>
   0x0000000000401443 <+414>:   mov    $0x0,%eax
   0x0000000000401448 <+419>:   leave  
   0x0000000000401449 <+420>:   ret    
End of assembler dump.

(gdb) disassemble check ⌨️
Dump of assembler code for function check:
   0x0000000000401156 <+0>:     push   %rbp
   0x0000000000401157 <+1>:     mov    %rsp,%rbp
   0x000000000040115a <+4>:     push   %rbx
   0x000000000040115b <+5>:     sub    $0x58,%rsp
   0x000000000040115f <+9>:     mov    %rdi,-0x58(%rbp)
   0x0000000000401163 <+13>:    mov    -0x58(%rbp),%rax
   0x0000000000401167 <+17>:    mov    %rax,%rdi
   0x000000000040116a <+20>:    call   0x401040 <strlen@plt>
   0x000000000040116f <+25>:    cmp    $0x1b,%rax
   0x0000000000401173 <+29>:    je     0x40117f <check+41>
   0x0000000000401175 <+31>:    mov    $0x1,%eax
   0x000000000040117a <+36>:    jmp    0x40129f <check+329>
   0x000000000040117f <+41>:    movabs $0x617b2375f81ea7e1,%rax 👀
   0x0000000000401189 <+51>:    movabs $0xd269df5b5afc9db9,%rdx 👀
   0x0000000000401193 <+61>:    mov    %rax,-0x50(%rbp)
   0x0000000000401197 <+65>:    mov    %rdx,-0x48(%rbp)
   0x000000000040119b <+69>:    movabs $0xf467edf4ed1bfed2,%rax 👀 # NOTICE: starts at -0x41, overlaps previous (d2 not used)
   0x00000000004011a5 <+79>:    mov    %rax,-0x41(%rbp)
   0x00000000004011a9 <+83>:    movl   $0x0,-0x14(%rbp)
   0x00000000004011b0 <+90>:    movl   $0x0,-0x18(%rbp)
   0x00000000004011b7 <+97>:    movl   $0x0,-0x24(%rbp)
   0x00000000004011be <+104>:   movl   $0x0,-0x1c(%rbp)
   0x00000000004011c5 <+111>:   jmp    0x40128e <check+312>
   0x00000000004011ca <+116>:   movl   $0x0,-0x20(%rbp)
   0x00000000004011d1 <+123>:   jmp    0x401280 <check+298>
   0x00000000004011d6 <+128>:   cmpl   $0x0,-0x18(%rbp)
   0x00000000004011da <+132>:   jne    0x4011e0 <check+138>
   0x00000000004011dc <+134>:   addl   $0x1,-0x18(%rbp)
   0x00000000004011e0 <+138>:   mov    $0x7,%eax
   0x00000000004011e5 <+143>:   sub    -0x20(%rbp),%eax
   0x00000000004011e8 <+146>:   mov    $0x1,%edx
   0x00000000004011ed <+151>:   mov    %eax,%ecx
   0x00000000004011ef <+153>:   shl    %cl,%edx
   0x00000000004011f1 <+155>:   mov    %edx,%eax
   0x00000000004011f3 <+157>:   mov    %eax,-0x28(%rbp)
   0x00000000004011f6 <+160>:   mov    $0x7,%eax
   0x00000000004011fb <+165>:   sub    -0x18(%rbp),%eax
   0x00000000004011fe <+168>:   mov    $0x1,%edx
   0x0000000000401203 <+173>:   mov    %eax,%ecx
   0x0000000000401205 <+175>:   shl    %cl,%edx
   0x0000000000401207 <+177>:   mov    %edx,%eax
   0x0000000000401209 <+179>:   mov    %eax,-0x2c(%rbp)
   0x000000000040120c <+182>:   mov    -0x1c(%rbp),%eax
   0x000000000040120f <+185>:   cltq   
   0x0000000000401211 <+187>:   movzbl -0x50(%rbp,%rax,1),%eax
   0x0000000000401216 <+192>:   movsbl %al,%eax
--Type <RET> for more, q to quit, c to continue without paging--c
   0x0000000000401219 <+195>:   and    -0x28(%rbp),%eax
   0x000000000040121c <+198>:   test   %eax,%eax
   0x000000000040121e <+200>:   setg   %cl
   0x0000000000401221 <+203>:   mov    -0x14(%rbp),%eax
   0x0000000000401224 <+206>:   movslq %eax,%rdx
   0x0000000000401227 <+209>:   mov    -0x58(%rbp),%rax
   0x000000000040122b <+213>:   add    %rdx,%rax
   0x000000000040122e <+216>:   movzbl (%rax),%eax
   0x0000000000401231 <+219>:   movsbl %al,%eax
   0x0000000000401234 <+222>:   and    -0x2c(%rbp),%eax
   0x0000000000401237 <+225>:   test   %eax,%eax
   0x0000000000401239 <+227>:   setg   %al
   0x000000000040123c <+230>:   xor    %ecx,%eax
   0x000000000040123e <+232>:   test   %al,%al
   0x0000000000401240 <+234>:   je     0x401249 <check+243>
   0x0000000000401242 <+236>:   mov    $0x1,%eax
   0x0000000000401247 <+241>:   jmp    0x40129f <check+329>
   0x0000000000401249 <+243>:   addl   $0x1,-0x18(%rbp)
   0x000000000040124d <+247>:   cmpl   $0x8,-0x18(%rbp)
   0x0000000000401251 <+251>:   jne    0x40125e <check+264>
   0x0000000000401253 <+253>:   movl   $0x0,-0x18(%rbp)
   0x000000000040125a <+260>:   addl   $0x1,-0x14(%rbp)
   0x000000000040125e <+264>:   mov    -0x14(%rbp),%eax
   0x0000000000401261 <+267>:   movslq %eax,%rbx
   0x0000000000401264 <+270>:   mov    -0x58(%rbp),%rax
   0x0000000000401268 <+274>:   mov    %rax,%rdi
   0x000000000040126b <+277>:   call   0x401040 <strlen@plt>
   0x0000000000401270 <+282>:   cmp    %rax,%rbx
   0x0000000000401273 <+285>:   jne    0x40127c <check+294>
   0x0000000000401275 <+287>:   mov    $0x0,%eax
   0x000000000040127a <+292>:   jmp    0x40129f <check+329>
   0x000000000040127c <+294>:   addl   $0x1,-0x20(%rbp)
   0x0000000000401280 <+298>:   cmpl   $0x7,-0x20(%rbp)
   0x0000000000401284 <+302>:   jle    0x4011d6 <check+128>
   0x000000000040128a <+308>:   addl   $0x1,-0x1c(%rbp)
   0x000000000040128e <+312>:   mov    -0x1c(%rbp),%eax
   0x0000000000401291 <+315>:   cmp    $0x16,%eax
   0x0000000000401294 <+318>:   jbe    0x4011ca <check+116>
   0x000000000040129a <+324>:   mov    $0x0,%eax
   0x000000000040129f <+329>:   mov    -0x8(%rbp),%rbx
   0x00000000004012a3 <+333>:   leave  
   0x00000000004012a4 <+334>:   ret    
End of assembler dump.

AsianHacker-picoctf@webshell:~$ vi main.c ⌨️
AsianHacker-picoctf@webshell:~$ cat main.c ⌨️
#include <stdio.h>
#include <string.h>
#include <stdint.h>

char* extract_flag_from_dump() {
    unsigned char memory_dump[] = {
        0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61,
        0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2,
        0xfe, 0x1b, 0xed, 0xf4, 0xed, 0x67, 0xf4, 0x00 
    };
    
    static char flag[28] = {0};
    int flagIndex = 0; 
    int bitInByte = 0;
    unsigned char currentByte = 0;
    
    for (unsigned int i = 0; i <= 22; ++i) {
        for (int j = 0; j <= 7; ++j) {
            if (!bitInByte)
                bitInByte = 1;
            
            int constBit = 1 << (7 - j);
            int flagBit = 1 << (7 - bitInByte);
            
            unsigned char constByte = memory_dump[i];
            
            if ((constBit & constByte) > 0) {
                currentByte |= flagBit;
            }
            
            ++bitInByte;
            if (bitInByte == 8) {
                flag[flagIndex] = currentByte;
                currentByte = 0;
                bitInByte = 0;
                ++flagIndex;
                
                if (flagIndex >= 27)
                    break;
            }
        }
        
        if (flagIndex >= 27)
            break;
    }
    
    flag[27] = '\0';
    return flag;
}

int main() {
    char* flag = extract_flag_from_dump();
    printf("flag: %s\n", flag);
   
    return 0;
}

AsianHacker-picoctf@webshell:~$ gcc main.c ⌨️
AsianHacker-picoctf@webshell:~$ ./a.out ⌨️
flag: picoCTF{0n3_bi7_4t_a_7im3} 🔐

Method 2:
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
# Hardcoded 23-byte reference sequence from the binary
reference = [0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61, 0xb9, 0x9d, 0xfc,
             0x5a, 0x5b, 0xdf, 0x69, 0xd2, 0xfe, 0x1b, 0xed, 0xf4, 0xed, 0x67, 0xf4]

# Extract 184 bits from reference (MSB to LSB)
ref_bits = [((byte >> (7 - j)) & 1) for byte in reference for j in range(8)]

# Simulate the bit mapping sequence
v1, v2 = 0, 0
sequence = []
for i in range(23):
    for v5 in range(8):
        if v1 == 0:
            v1 = 1
        bit_pos = 7 - v1
        sequence.append((v2, bit_pos))
        v1 += 1
        if v1 == 8:
            v1, v2 = 0, v2 + 1

# Initialize 27-byte password array
str_bytes = [0] * 27
for k in range(184):
    v2, bit_pos = sequence[k]
    str_bytes[v2] |= (ref_bits[k] << bit_pos)

# Convert bytes to characters, append newline
password = ''.join(chr(b) for b in str_bytes[:-1]) + '\n'
print(password)

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
picoCTF{0n3_bi7_4t_a_7im3} 🔐
```

## Flag
picoCTF{0n3_bi7_4t_a_7im3}

## Continue
[Continue](./picoGym0466.md)