# picoGym Level 416: FactCheck
Source: https://play.picoctf.org/practice/challenge/416

## Goal
This binary is putting together some important piece of information...<br>
Can you uncover that information?<br>
Examine this file. Do you understand its inner workings?<br>
https://artifacts.picoctf.net/c_titan/187/bin

## What I learned
```
Reverse Engineering

Ghidra
Binary Ninja

Youtube Solution: https://www.youtube.com/watch?v=NCJ7Dbxt9p0
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/187/bin
--2025-10-01 02:00:12--  https://artifacts.picoctf.net/c_titan/187/bin
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.72, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17952 (18K) [application/octet-stream]
Saving to: 'bin'

bin                                                        100%[======================================================================================================================================>]  17.53K  --.-KB/s    in 0.005s  

2025-10-01 02:00:12 (3.64 MB/s) - 'bin' saved [17952/17952]

AsianHacker-picoctf@webshell:~$ file bin
bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ba87dd5805704ffe3d15a1e136c290a83fe95dba, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ chmod u+x bin
AsianHacker-picoctf@webshell:~$ ./bin
AsianHacker-picoctf@webshell:~$ strings -n 7 bin | grep picoCTF{
picoCTF{wELF_d0N3_mate_

AsianHacker-picoctf@webshell:~$ gdb -q bin
Reading symbols from bin...
(No debugging symbols found in bin)
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x00000000000010e0  __cxa_finalize@plt
0x00000000000010f0  std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string()@plt
0x0000000000001100  std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::operator+=(char)@plt
0x0000000000001110  __cxa_atexit@plt
0x0000000000001120  std::allocator<char>::~allocator()@plt
0x0000000000001130  __stack_chk_fail@plt
0x0000000000001140  std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::operator+=(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)@plt
0x0000000000001150  std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(char const*, std::allocator<char> const&)@plt
0x0000000000001160  std::ios_base::Init::Init()@plt
0x0000000000001170  _Unwind_Resume@plt
0x0000000000001180  std::allocator<char>::allocator()@plt
0x0000000000001190  std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::operator[](unsigned long)@plt
0x00000000000011a0  _start
0x00000000000011d0  deregister_tm_clones
0x0000000000001200  register_tm_clones
0x0000000000001240  __do_global_dtors_aux
0x0000000000001280  frame_dummy
0x0000000000001289  main
0x0000000000001c54  __static_initialization_and_destruction_0(int, int)
0x0000000000001ca1  _GLOBAL__sub_I_main
0x0000000000001cc0  __libc_csu_init
0x0000000000001d30  __libc_csu_fini
0x0000000000001d38  _fini
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001289 <+0>:     endbr64 
   0x000000000000128d <+4>:     push   %rbp
   0x000000000000128e <+5>:     mov    %rsp,%rbp
   0x0000000000001291 <+8>:     push   %rbx
   0x0000000000001292 <+9>:     sub    $0x248,%rsp
   0x0000000000001299 <+16>:    mov    %fs:0x28,%rax
   0x00000000000012a2 <+25>:    mov    %rax,-0x18(%rbp)
   0x00000000000012a6 <+29>:    xor    %eax,%eax
   0x00000000000012a8 <+31>:    lea    -0x241(%rbp),%rax
   0x00000000000012af <+38>:    mov    %rax,%rdi
   0x00000000000012b2 <+41>:    call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x00000000000012b7 <+46>:    lea    -0x241(%rbp),%rdx
   0x00000000000012be <+53>:    lea    -0x240(%rbp),%rax
   0x00000000000012c5 <+60>:    lea    0xd39(%rip),%rsi        # 0x2005
   0x00000000000012cc <+67>:    mov    %rax,%rdi
   0x00000000000012cf <+70>:    call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x00000000000012d4 <+75>:    lea    -0x241(%rbp),%rax
   0x00000000000012db <+82>:    mov    %rax,%rdi
   0x00000000000012de <+85>:    call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000012e3 <+90>:    lea    -0x241(%rbp),%rax
   0x00000000000012ea <+97>:    mov    %rax,%rdi
   0x00000000000012ed <+100>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x00000000000012f2 <+105>:   lea    -0x241(%rbp),%rdx
   0x00000000000012f9 <+112>:   lea    -0x220(%rbp),%rax
   0x0000000000001300 <+119>:   lea    0xd16(%rip),%rsi        # 0x201d
   0x0000000000001307 <+126>:   mov    %rax,%rdi
   0x000000000000130a <+129>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x000000000000130f <+134>:   lea    -0x241(%rbp),%rax
   0x0000000000001316 <+141>:   mov    %rax,%rdi
   0x0000000000001319 <+144>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x000000000000131e <+149>:   lea    -0x241(%rbp),%rax
   0x0000000000001325 <+156>:   mov    %rax,%rdi
   0x0000000000001328 <+159>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x000000000000132d <+164>:   lea    -0x241(%rbp),%rdx
   0x0000000000001334 <+171>:   lea    -0x200(%rbp),%rax
   0x000000000000133b <+178>:   lea    0xcdd(%rip),%rsi        # 0x201f
   0x0000000000001342 <+185>:   mov    %rax,%rdi
   0x0000000000001345 <+188>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x000000000000134a <+193>:   lea    -0x241(%rbp),%rax
   0x0000000000001351 <+200>:   mov    %rax,%rdi
   0x0000000000001354 <+203>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001359 <+208>:   lea    -0x241(%rbp),%rax
   0x0000000000001360 <+215>:   mov    %rax,%rdi
   0x0000000000001363 <+218>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x0000000000001368 <+223>:   lea    -0x241(%rbp),%rdx
   0x000000000000136f <+230>:   lea    -0x1e0(%rbp),%rax
--Type <RET> for more, q to quit, c to continue without paging--c
   0x0000000000001376 <+237>:   lea    0xca4(%rip),%rsi        # 0x2021
   0x000000000000137d <+244>:   mov    %rax,%rdi
   0x0000000000001380 <+247>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x0000000000001385 <+252>:   lea    -0x241(%rbp),%rax
   0x000000000000138c <+259>:   mov    %rax,%rdi
   0x000000000000138f <+262>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001394 <+267>:   lea    -0x241(%rbp),%rax
   0x000000000000139b <+274>:   mov    %rax,%rdi
   0x000000000000139e <+277>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x00000000000013a3 <+282>:   lea    -0x241(%rbp),%rdx
   0x00000000000013aa <+289>:   lea    -0x1c0(%rbp),%rax
   0x00000000000013b1 <+296>:   lea    0xc6b(%rip),%rsi        # 0x2023
   0x00000000000013b8 <+303>:   mov    %rax,%rdi
   0x00000000000013bb <+306>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x00000000000013c0 <+311>:   lea    -0x241(%rbp),%rax
   0x00000000000013c7 <+318>:   mov    %rax,%rdi
   0x00000000000013ca <+321>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000013cf <+326>:   lea    -0x241(%rbp),%rax
   0x00000000000013d6 <+333>:   mov    %rax,%rdi
   0x00000000000013d9 <+336>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x00000000000013de <+341>:   lea    -0x241(%rbp),%rdx
   0x00000000000013e5 <+348>:   lea    -0x1a0(%rbp),%rax
   0x00000000000013ec <+355>:   lea    0xc32(%rip),%rsi        # 0x2025
   0x00000000000013f3 <+362>:   mov    %rax,%rdi
   0x00000000000013f6 <+365>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x00000000000013fb <+370>:   lea    -0x241(%rbp),%rax
   0x0000000000001402 <+377>:   mov    %rax,%rdi
   0x0000000000001405 <+380>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x000000000000140a <+385>:   lea    -0x241(%rbp),%rax
   0x0000000000001411 <+392>:   mov    %rax,%rdi
   0x0000000000001414 <+395>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x0000000000001419 <+400>:   lea    -0x241(%rbp),%rdx
   0x0000000000001420 <+407>:   lea    -0x180(%rbp),%rax
   0x0000000000001427 <+414>:   lea    0xbf9(%rip),%rsi        # 0x2027
   0x000000000000142e <+421>:   mov    %rax,%rdi
   0x0000000000001431 <+424>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x0000000000001436 <+429>:   lea    -0x241(%rbp),%rax
   0x000000000000143d <+436>:   mov    %rax,%rdi
   0x0000000000001440 <+439>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001445 <+444>:   lea    -0x241(%rbp),%rax
   0x000000000000144c <+451>:   mov    %rax,%rdi
   0x000000000000144f <+454>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x0000000000001454 <+459>:   lea    -0x241(%rbp),%rdx
   0x000000000000145b <+466>:   lea    -0x160(%rbp),%rax
   0x0000000000001462 <+473>:   lea    0xbbe(%rip),%rsi        # 0x2027
   0x0000000000001469 <+480>:   mov    %rax,%rdi
   0x000000000000146c <+483>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x0000000000001471 <+488>:   lea    -0x241(%rbp),%rax
   0x0000000000001478 <+495>:   mov    %rax,%rdi
   0x000000000000147b <+498>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001480 <+503>:   lea    -0x241(%rbp),%rax
   0x0000000000001487 <+510>:   mov    %rax,%rdi
   0x000000000000148a <+513>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x000000000000148f <+518>:   lea    -0x241(%rbp),%rdx
   0x0000000000001496 <+525>:   lea    -0x140(%rbp),%rax
   0x000000000000149d <+532>:   lea    0xb85(%rip),%rsi        # 0x2029
   0x00000000000014a4 <+539>:   mov    %rax,%rdi
   0x00000000000014a7 <+542>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x00000000000014ac <+547>:   lea    -0x241(%rbp),%rax
   0x00000000000014b3 <+554>:   mov    %rax,%rdi
   0x00000000000014b6 <+557>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000014bb <+562>:   lea    -0x241(%rbp),%rax
   0x00000000000014c2 <+569>:   mov    %rax,%rdi
   0x00000000000014c5 <+572>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x00000000000014ca <+577>:   lea    -0x241(%rbp),%rdx
   0x00000000000014d1 <+584>:   lea    -0x120(%rbp),%rax
   0x00000000000014d8 <+591>:   lea    0xb4a(%rip),%rsi        # 0x2029
   0x00000000000014df <+598>:   mov    %rax,%rdi
   0x00000000000014e2 <+601>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x00000000000014e7 <+606>:   lea    -0x241(%rbp),%rax
   0x00000000000014ee <+613>:   mov    %rax,%rdi
   0x00000000000014f1 <+616>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000014f6 <+621>:   lea    -0x241(%rbp),%rax
   0x00000000000014fd <+628>:   mov    %rax,%rdi
   0x0000000000001500 <+631>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x0000000000001505 <+636>:   lea    -0x241(%rbp),%rdx
   0x000000000000150c <+643>:   lea    -0x100(%rbp),%rax
   0x0000000000001513 <+650>:   lea    0xb07(%rip),%rsi        # 0x2021
   0x000000000000151a <+657>:   mov    %rax,%rdi
   0x000000000000151d <+660>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x0000000000001522 <+665>:   lea    -0x241(%rbp),%rax
   0x0000000000001529 <+672>:   mov    %rax,%rdi
   0x000000000000152c <+675>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001531 <+680>:   lea    -0x241(%rbp),%rax
   0x0000000000001538 <+687>:   mov    %rax,%rdi
   0x000000000000153b <+690>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x0000000000001540 <+695>:   lea    -0x241(%rbp),%rdx
   0x0000000000001547 <+702>:   lea    -0xe0(%rbp),%rax
   0x000000000000154e <+709>:   lea    0xad6(%rip),%rsi        # 0x202b
   0x0000000000001555 <+716>:   mov    %rax,%rdi
   0x0000000000001558 <+719>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x000000000000155d <+724>:   lea    -0x241(%rbp),%rax
   0x0000000000001564 <+731>:   mov    %rax,%rdi
   0x0000000000001567 <+734>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x000000000000156c <+739>:   lea    -0x241(%rbp),%rax
   0x0000000000001573 <+746>:   mov    %rax,%rdi
   0x0000000000001576 <+749>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x000000000000157b <+754>:   lea    -0x241(%rbp),%rdx
   0x0000000000001582 <+761>:   lea    -0xc0(%rbp),%rax
   0x0000000000001589 <+768>:   lea    0xa99(%rip),%rsi        # 0x2029
   0x0000000000001590 <+775>:   mov    %rax,%rdi
   0x0000000000001593 <+778>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x0000000000001598 <+783>:   lea    -0x241(%rbp),%rax
   0x000000000000159f <+790>:   mov    %rax,%rdi
   0x00000000000015a2 <+793>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000015a7 <+798>:   lea    -0x241(%rbp),%rax
   0x00000000000015ae <+805>:   mov    %rax,%rdi
   0x00000000000015b1 <+808>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x00000000000015b6 <+813>:   lea    -0x241(%rbp),%rdx
   0x00000000000015bd <+820>:   lea    -0xa0(%rbp),%rax
   0x00000000000015c4 <+827>:   lea    0xa62(%rip),%rsi        # 0x202d
   0x00000000000015cb <+834>:   mov    %rax,%rdi
   0x00000000000015ce <+837>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x00000000000015d3 <+842>:   lea    -0x241(%rbp),%rax
   0x00000000000015da <+849>:   mov    %rax,%rdi
   0x00000000000015dd <+852>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000015e2 <+857>:   lea    -0x241(%rbp),%rax
   0x00000000000015e9 <+864>:   mov    %rax,%rdi
   0x00000000000015ec <+867>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x00000000000015f1 <+872>:   lea    -0x241(%rbp),%rdx
   0x00000000000015f8 <+879>:   lea    -0x80(%rbp),%rax
   0x00000000000015fc <+883>:   lea    0xa2c(%rip),%rsi        # 0x202f
   0x0000000000001603 <+890>:   mov    %rax,%rdi
   0x0000000000001606 <+893>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x000000000000160b <+898>:   lea    -0x241(%rbp),%rax
   0x0000000000001612 <+905>:   mov    %rax,%rdi
   0x0000000000001615 <+908>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x000000000000161a <+913>:   lea    -0x241(%rbp),%rax
   0x0000000000001621 <+920>:   mov    %rax,%rdi
   0x0000000000001624 <+923>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x0000000000001629 <+928>:   lea    -0x241(%rbp),%rdx
   0x0000000000001630 <+935>:   lea    -0x60(%rbp),%rax
   0x0000000000001634 <+939>:   lea    0x9f6(%rip),%rsi        # 0x2031
   0x000000000000163b <+946>:   mov    %rax,%rdi
   0x000000000000163e <+949>:   call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x0000000000001643 <+954>:   lea    -0x241(%rbp),%rax
   0x000000000000164a <+961>:   mov    %rax,%rdi
   0x000000000000164d <+964>:   call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001652 <+969>:   lea    -0x241(%rbp),%rax
   0x0000000000001659 <+976>:   mov    %rax,%rdi
   0x000000000000165c <+979>:   call   0x1180 <_ZNSaIcEC1Ev@plt>
   0x0000000000001661 <+984>:   lea    -0x241(%rbp),%rdx
   0x0000000000001668 <+991>:   lea    -0x40(%rbp),%rax
   0x000000000000166c <+995>:   lea    0x9c0(%rip),%rsi        # 0x2033
   0x0000000000001673 <+1002>:  mov    %rax,%rdi
   0x0000000000001676 <+1005>:  call   0x1150 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@plt>
   0x000000000000167b <+1010>:  lea    -0x241(%rbp),%rax
   0x0000000000001682 <+1017>:  mov    %rax,%rdi
   0x0000000000001685 <+1020>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x000000000000168a <+1025>:  lea    -0x200(%rbp),%rax
   0x0000000000001691 <+1032>:  mov    $0x0,%esi
   0x0000000000001696 <+1037>:  mov    %rax,%rdi
   0x0000000000001699 <+1040>:  call   0x1190 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEixEm@plt>
   0x000000000000169e <+1045>:  movzbl (%rax),%eax
   0x00000000000016a1 <+1048>:  cmp    $0x41,%al
   0x00000000000016a3 <+1050>:  setle  %al
   0x00000000000016a6 <+1053>:  test   %al,%al
   0x00000000000016a8 <+1055>:  je     0x16c3 <main+1082>
   0x00000000000016aa <+1057>:  lea    -0xc0(%rbp),%rdx
   0x00000000000016b1 <+1064>:  lea    -0x240(%rbp),%rax
   0x00000000000016b8 <+1071>:  mov    %rdx,%rsi
   0x00000000000016bb <+1074>:  mov    %rax,%rdi
   0x00000000000016be <+1077>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x00000000000016c3 <+1082>:  lea    -0xa0(%rbp),%rax
   0x00000000000016ca <+1089>:  mov    $0x0,%esi
   0x00000000000016cf <+1094>:  mov    %rax,%rdi
   0x00000000000016d2 <+1097>:  call   0x1190 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEixEm@plt>
   0x00000000000016d7 <+1102>:  movzbl (%rax),%eax
   0x00000000000016da <+1105>:  cmp    $0x41,%al
   0x00000000000016dc <+1107>:  setne  %al
   0x00000000000016df <+1110>:  test   %al,%al
   0x00000000000016e1 <+1112>:  je     0x16f9 <main+1136>
   0x00000000000016e3 <+1114>:  lea    -0x60(%rbp),%rdx
   0x00000000000016e7 <+1118>:  lea    -0x240(%rbp),%rax
   0x00000000000016ee <+1125>:  mov    %rdx,%rsi
   0x00000000000016f1 <+1128>:  mov    %rax,%rdi
   0x00000000000016f4 <+1131>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x00000000000016f9 <+1136>:  lea    0x935(%rip),%rdx        # 0x2035
   0x0000000000001700 <+1143>:  lea    0x934(%rip),%rax        # 0x203b
   0x0000000000001707 <+1150>:  cmp    %rax,%rdx
   0x000000000000170a <+1153>:  jne    0x1725 <main+1180>
   0x000000000000170c <+1155>:  lea    -0x1e0(%rbp),%rdx
   0x0000000000001713 <+1162>:  lea    -0x240(%rbp),%rax
   0x000000000000171a <+1169>:  mov    %rdx,%rsi
   0x000000000000171d <+1172>:  mov    %rax,%rdi
   0x0000000000001720 <+1175>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x0000000000001725 <+1180>:  lea    -0x1c0(%rbp),%rax
   0x000000000000172c <+1187>:  mov    $0x0,%esi
   0x0000000000001731 <+1192>:  mov    %rax,%rdi
   0x0000000000001734 <+1195>:  call   0x1190 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEixEm@plt>
   0x0000000000001739 <+1200>:  movzbl (%rax),%eax
   0x000000000000173c <+1203>:  movsbl %al,%ebx
   0x000000000000173f <+1206>:  lea    -0x140(%rbp),%rax
   0x0000000000001746 <+1213>:  mov    $0x0,%esi
   0x000000000000174b <+1218>:  mov    %rax,%rdi
   0x000000000000174e <+1221>:  call   0x1190 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEixEm@plt>
   0x0000000000001753 <+1226>:  movzbl (%rax),%eax
   0x0000000000001756 <+1229>:  movsbl %al,%eax
   0x0000000000001759 <+1232>:  sub    %eax,%ebx
   0x000000000000175b <+1234>:  mov    %ebx,%eax
   0x000000000000175d <+1236>:  cmp    $0x3,%eax
   0x0000000000001760 <+1239>:  sete   %al
   0x0000000000001763 <+1242>:  test   %al,%al
   0x0000000000001765 <+1244>:  je     0x1780 <main+1271>
   0x0000000000001767 <+1246>:  lea    -0x1c0(%rbp),%rdx
   0x000000000000176e <+1253>:  lea    -0x240(%rbp),%rax
   0x0000000000001775 <+1260>:  mov    %rdx,%rsi
   0x0000000000001778 <+1263>:  mov    %rax,%rdi
   0x000000000000177b <+1266>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x0000000000001780 <+1271>:  lea    -0x1e0(%rbp),%rdx
   0x0000000000001787 <+1278>:  lea    -0x240(%rbp),%rax
   0x000000000000178e <+1285>:  mov    %rdx,%rsi
   0x0000000000001791 <+1288>:  mov    %rax,%rdi
   0x0000000000001794 <+1291>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x0000000000001799 <+1296>:  lea    -0x180(%rbp),%rdx
   0x00000000000017a0 <+1303>:  lea    -0x240(%rbp),%rax
   0x00000000000017a7 <+1310>:  mov    %rdx,%rsi
   0x00000000000017aa <+1313>:  mov    %rax,%rdi
   0x00000000000017ad <+1316>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x00000000000017b2 <+1321>:  lea    -0x160(%rbp),%rax
   0x00000000000017b9 <+1328>:  mov    $0x0,%esi
   0x00000000000017be <+1333>:  mov    %rax,%rdi
   0x00000000000017c1 <+1336>:  call   0x1190 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEixEm@plt>
   0x00000000000017c6 <+1341>:  movzbl (%rax),%eax
   0x00000000000017c9 <+1344>:  cmp    $0x47,%al
   0x00000000000017cb <+1346>:  sete   %al
   0x00000000000017ce <+1349>:  test   %al,%al
   0x00000000000017d0 <+1351>:  je     0x17eb <main+1378>
   0x00000000000017d2 <+1353>:  lea    -0x160(%rbp),%rdx
   0x00000000000017d9 <+1360>:  lea    -0x240(%rbp),%rax
   0x00000000000017e0 <+1367>:  mov    %rdx,%rsi
   0x00000000000017e3 <+1370>:  mov    %rax,%rdi
   0x00000000000017e6 <+1373>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x00000000000017eb <+1378>:  lea    -0x1a0(%rbp),%rdx
   0x00000000000017f2 <+1385>:  lea    -0x240(%rbp),%rax
   0x00000000000017f9 <+1392>:  mov    %rdx,%rsi
   0x00000000000017fc <+1395>:  mov    %rax,%rdi
   0x00000000000017ff <+1398>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x0000000000001804 <+1403>:  lea    -0x80(%rbp),%rdx
   0x0000000000001808 <+1407>:  lea    -0x240(%rbp),%rax
   0x000000000000180f <+1414>:  mov    %rdx,%rsi
   0x0000000000001812 <+1417>:  mov    %rax,%rdi
   0x0000000000001815 <+1420>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x000000000000181a <+1425>:  lea    -0x220(%rbp),%rdx
   0x0000000000001821 <+1432>:  lea    -0x240(%rbp),%rax
   0x0000000000001828 <+1439>:  mov    %rdx,%rsi
   0x000000000000182b <+1442>:  mov    %rax,%rdi
   0x000000000000182e <+1445>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x0000000000001833 <+1450>:  lea    -0x120(%rbp),%rdx
   0x000000000000183a <+1457>:  lea    -0x240(%rbp),%rax
   0x0000000000001841 <+1464>:  mov    %rdx,%rsi
   0x0000000000001844 <+1467>:  mov    %rax,%rdi
   0x0000000000001847 <+1470>:  call   0x1140 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLERKS4_@plt>
   0x000000000000184c <+1475>:  lea    -0x240(%rbp),%rax
   0x0000000000001853 <+1482>:  mov    $0x7d,%esi
   0x0000000000001858 <+1487>:  mov    %rax,%rdi
   0x000000000000185b <+1490>:  call   0x1100 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLEc@plt>
   0x0000000000001860 <+1495>:  mov    $0x0,%ebx
   0x0000000000001865 <+1500>:  lea    -0x40(%rbp),%rax
   0x0000000000001869 <+1504>:  mov    %rax,%rdi
   0x000000000000186c <+1507>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001871 <+1512>:  lea    -0x60(%rbp),%rax
   0x0000000000001875 <+1516>:  mov    %rax,%rdi
   0x0000000000001878 <+1519>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x000000000000187d <+1524>:  lea    -0x80(%rbp),%rax
   0x0000000000001881 <+1528>:  mov    %rax,%rdi
   0x0000000000001884 <+1531>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001889 <+1536>:  lea    -0xa0(%rbp),%rax
   0x0000000000001890 <+1543>:  mov    %rax,%rdi
   0x0000000000001893 <+1546>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001898 <+1551>:  lea    -0xc0(%rbp),%rax
   0x000000000000189f <+1558>:  mov    %rax,%rdi
   0x00000000000018a2 <+1561>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x00000000000018a7 <+1566>:  lea    -0xe0(%rbp),%rax
   0x00000000000018ae <+1573>:  mov    %rax,%rdi
   0x00000000000018b1 <+1576>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x00000000000018b6 <+1581>:  lea    -0x100(%rbp),%rax
   0x00000000000018bd <+1588>:  mov    %rax,%rdi
   0x00000000000018c0 <+1591>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x00000000000018c5 <+1596>:  lea    -0x120(%rbp),%rax
   0x00000000000018cc <+1603>:  mov    %rax,%rdi
   0x00000000000018cf <+1606>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x00000000000018d4 <+1611>:  lea    -0x140(%rbp),%rax
   0x00000000000018db <+1618>:  mov    %rax,%rdi
   0x00000000000018de <+1621>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x00000000000018e3 <+1626>:  lea    -0x160(%rbp),%rax
   0x00000000000018ea <+1633>:  mov    %rax,%rdi
   0x00000000000018ed <+1636>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x00000000000018f2 <+1641>:  lea    -0x180(%rbp),%rax
   0x00000000000018f9 <+1648>:  mov    %rax,%rdi
   0x00000000000018fc <+1651>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001901 <+1656>:  lea    -0x1a0(%rbp),%rax
   0x0000000000001908 <+1663>:  mov    %rax,%rdi
   0x000000000000190b <+1666>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001910 <+1671>:  lea    -0x1c0(%rbp),%rax
   0x0000000000001917 <+1678>:  mov    %rax,%rdi
   0x000000000000191a <+1681>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x000000000000191f <+1686>:  lea    -0x1e0(%rbp),%rax
   0x0000000000001926 <+1693>:  mov    %rax,%rdi
   0x0000000000001929 <+1696>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x000000000000192e <+1701>:  lea    -0x200(%rbp),%rax
   0x0000000000001935 <+1708>:  mov    %rax,%rdi
   0x0000000000001938 <+1711>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x000000000000193d <+1716>:  lea    -0x220(%rbp),%rax
   0x0000000000001944 <+1723>:  mov    %rax,%rdi
   0x0000000000001947 <+1726>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x000000000000194c <+1731>:  lea    -0x240(%rbp),%rax
   0x0000000000001953 <+1738>:  mov    %rax,%rdi
   0x0000000000001956 <+1741>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x000000000000195b <+1746>:  mov    %ebx,%eax
   0x000000000000195d <+1748>:  mov    -0x18(%rbp),%rcx
   0x0000000000001961 <+1752>:  xor    %fs:0x28,%rcx
   0x000000000000196a <+1761>:  je     0x1c4a <main+2497>
   0x0000000000001970 <+1767>:  jmp    0x1c45 <main+2492>
   0x0000000000001975 <+1772>:  endbr64 
   0x0000000000001979 <+1776>:  mov    %rax,%rbx
   0x000000000000197c <+1779>:  lea    -0x241(%rbp),%rax
   0x0000000000001983 <+1786>:  mov    %rax,%rdi
   0x0000000000001986 <+1789>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x000000000000198b <+1794>:  mov    %rbx,%rax
   0x000000000000198e <+1797>:  mov    %rax,%rdi
   0x0000000000001991 <+1800>:  call   0x1170 <_Unwind_Resume@plt>
   0x0000000000001996 <+1805>:  endbr64 
   0x000000000000199a <+1809>:  mov    %rax,%rbx
   0x000000000000199d <+1812>:  lea    -0x241(%rbp),%rax
   0x00000000000019a4 <+1819>:  mov    %rax,%rdi
   0x00000000000019a7 <+1822>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000019ac <+1827>:  jmp    0x1c2b <main+2466>
   0x00000000000019b1 <+1832>:  endbr64 
   0x00000000000019b5 <+1836>:  mov    %rax,%rbx
   0x00000000000019b8 <+1839>:  lea    -0x241(%rbp),%rax
   0x00000000000019bf <+1846>:  mov    %rax,%rdi
   0x00000000000019c2 <+1849>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000019c7 <+1854>:  jmp    0x1c1c <main+2451>
   0x00000000000019cc <+1859>:  endbr64 
   0x00000000000019d0 <+1863>:  mov    %rax,%rbx
   0x00000000000019d3 <+1866>:  lea    -0x241(%rbp),%rax
   0x00000000000019da <+1873>:  mov    %rax,%rdi
   0x00000000000019dd <+1876>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000019e2 <+1881>:  jmp    0x1c0d <main+2436>
   0x00000000000019e7 <+1886>:  endbr64 
   0x00000000000019eb <+1890>:  mov    %rax,%rbx
   0x00000000000019ee <+1893>:  lea    -0x241(%rbp),%rax
   0x00000000000019f5 <+1900>:  mov    %rax,%rdi
   0x00000000000019f8 <+1903>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x00000000000019fd <+1908>:  jmp    0x1bfe <main+2421>
   0x0000000000001a02 <+1913>:  endbr64 
   0x0000000000001a06 <+1917>:  mov    %rax,%rbx
   0x0000000000001a09 <+1920>:  lea    -0x241(%rbp),%rax
   0x0000000000001a10 <+1927>:  mov    %rax,%rdi
   0x0000000000001a13 <+1930>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001a18 <+1935>:  jmp    0x1bef <main+2406>
   0x0000000000001a1d <+1940>:  endbr64 
   0x0000000000001a21 <+1944>:  mov    %rax,%rbx
   0x0000000000001a24 <+1947>:  lea    -0x241(%rbp),%rax
   0x0000000000001a2b <+1954>:  mov    %rax,%rdi
   0x0000000000001a2e <+1957>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001a33 <+1962>:  jmp    0x1be0 <main+2391>
   0x0000000000001a38 <+1967>:  endbr64 
   0x0000000000001a3c <+1971>:  mov    %rax,%rbx
   0x0000000000001a3f <+1974>:  lea    -0x241(%rbp),%rax
   0x0000000000001a46 <+1981>:  mov    %rax,%rdi
   0x0000000000001a49 <+1984>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001a4e <+1989>:  jmp    0x1bd1 <main+2376>
   0x0000000000001a53 <+1994>:  endbr64 
   0x0000000000001a57 <+1998>:  mov    %rax,%rbx
   0x0000000000001a5a <+2001>:  lea    -0x241(%rbp),%rax
   0x0000000000001a61 <+2008>:  mov    %rax,%rdi
   0x0000000000001a64 <+2011>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001a69 <+2016>:  jmp    0x1bc2 <main+2361>
   0x0000000000001a6e <+2021>:  endbr64 
   0x0000000000001a72 <+2025>:  mov    %rax,%rbx
   0x0000000000001a75 <+2028>:  lea    -0x241(%rbp),%rax
   0x0000000000001a7c <+2035>:  mov    %rax,%rdi
   0x0000000000001a7f <+2038>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001a84 <+2043>:  jmp    0x1bb3 <main+2346>
   0x0000000000001a89 <+2048>:  endbr64 
   0x0000000000001a8d <+2052>:  mov    %rax,%rbx
   0x0000000000001a90 <+2055>:  lea    -0x241(%rbp),%rax
   0x0000000000001a97 <+2062>:  mov    %rax,%rdi
   0x0000000000001a9a <+2065>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001a9f <+2070>:  jmp    0x1ba4 <main+2331>
   0x0000000000001aa4 <+2075>:  endbr64 
   0x0000000000001aa8 <+2079>:  mov    %rax,%rbx
   0x0000000000001aab <+2082>:  lea    -0x241(%rbp),%rax
   0x0000000000001ab2 <+2089>:  mov    %rax,%rdi
   0x0000000000001ab5 <+2092>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001aba <+2097>:  jmp    0x1b95 <main+2316>
   0x0000000000001abf <+2102>:  endbr64 
   0x0000000000001ac3 <+2106>:  mov    %rax,%rbx
   0x0000000000001ac6 <+2109>:  lea    -0x241(%rbp),%rax
   0x0000000000001acd <+2116>:  mov    %rax,%rdi
   0x0000000000001ad0 <+2119>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001ad5 <+2124>:  jmp    0x1b86 <main+2301>
   0x0000000000001ada <+2129>:  endbr64 
   0x0000000000001ade <+2133>:  mov    %rax,%rbx
   0x0000000000001ae1 <+2136>:  lea    -0x241(%rbp),%rax
   0x0000000000001ae8 <+2143>:  mov    %rax,%rdi
   0x0000000000001aeb <+2146>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001af0 <+2151>:  jmp    0x1b77 <main+2286>
   0x0000000000001af5 <+2156>:  endbr64 
   0x0000000000001af9 <+2160>:  mov    %rax,%rbx
   0x0000000000001afc <+2163>:  lea    -0x241(%rbp),%rax
   0x0000000000001b03 <+2170>:  mov    %rax,%rdi
   0x0000000000001b06 <+2173>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001b0b <+2178>:  jmp    0x1b68 <main+2271>
   0x0000000000001b0d <+2180>:  endbr64 
   0x0000000000001b11 <+2184>:  mov    %rax,%rbx
   0x0000000000001b14 <+2187>:  lea    -0x241(%rbp),%rax
   0x0000000000001b1b <+2194>:  mov    %rax,%rdi
   0x0000000000001b1e <+2197>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001b23 <+2202>:  jmp    0x1b5c <main+2259>
   0x0000000000001b25 <+2204>:  endbr64 
   0x0000000000001b29 <+2208>:  mov    %rax,%rbx
   0x0000000000001b2c <+2211>:  lea    -0x241(%rbp),%rax
   0x0000000000001b33 <+2218>:  mov    %rax,%rdi
   0x0000000000001b36 <+2221>:  call   0x1120 <_ZNSaIcED1Ev@plt>
   0x0000000000001b3b <+2226>:  jmp    0x1b50 <main+2247>
   0x0000000000001b3d <+2228>:  endbr64 
   0x0000000000001b41 <+2232>:  mov    %rax,%rbx
   0x0000000000001b44 <+2235>:  lea    -0x40(%rbp),%rax
   0x0000000000001b48 <+2239>:  mov    %rax,%rdi
   0x0000000000001b4b <+2242>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001b50 <+2247>:  lea    -0x60(%rbp),%rax
   0x0000000000001b54 <+2251>:  mov    %rax,%rdi
   0x0000000000001b57 <+2254>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001b5c <+2259>:  lea    -0x80(%rbp),%rax
   0x0000000000001b60 <+2263>:  mov    %rax,%rdi
   0x0000000000001b63 <+2266>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001b68 <+2271>:  lea    -0xa0(%rbp),%rax
   0x0000000000001b6f <+2278>:  mov    %rax,%rdi
   0x0000000000001b72 <+2281>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001b77 <+2286>:  lea    -0xc0(%rbp),%rax
   0x0000000000001b7e <+2293>:  mov    %rax,%rdi
   0x0000000000001b81 <+2296>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001b86 <+2301>:  lea    -0xe0(%rbp),%rax
   0x0000000000001b8d <+2308>:  mov    %rax,%rdi
   0x0000000000001b90 <+2311>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001b95 <+2316>:  lea    -0x100(%rbp),%rax
   0x0000000000001b9c <+2323>:  mov    %rax,%rdi
   0x0000000000001b9f <+2326>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001ba4 <+2331>:  lea    -0x120(%rbp),%rax
   0x0000000000001bab <+2338>:  mov    %rax,%rdi
   0x0000000000001bae <+2341>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001bb3 <+2346>:  lea    -0x140(%rbp),%rax
   0x0000000000001bba <+2353>:  mov    %rax,%rdi
   0x0000000000001bbd <+2356>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001bc2 <+2361>:  lea    -0x160(%rbp),%rax
   0x0000000000001bc9 <+2368>:  mov    %rax,%rdi
   0x0000000000001bcc <+2371>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001bd1 <+2376>:  lea    -0x180(%rbp),%rax
   0x0000000000001bd8 <+2383>:  mov    %rax,%rdi
   0x0000000000001bdb <+2386>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001be0 <+2391>:  lea    -0x1a0(%rbp),%rax
   0x0000000000001be7 <+2398>:  mov    %rax,%rdi
   0x0000000000001bea <+2401>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001bef <+2406>:  lea    -0x1c0(%rbp),%rax
   0x0000000000001bf6 <+2413>:  mov    %rax,%rdi
   0x0000000000001bf9 <+2416>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001bfe <+2421>:  lea    -0x1e0(%rbp),%rax
   0x0000000000001c05 <+2428>:  mov    %rax,%rdi
   0x0000000000001c08 <+2431>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001c0d <+2436>:  lea    -0x200(%rbp),%rax
   0x0000000000001c14 <+2443>:  mov    %rax,%rdi
   0x0000000000001c17 <+2446>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001c1c <+2451>:  lea    -0x220(%rbp),%rax
   0x0000000000001c23 <+2458>:  mov    %rax,%rdi
   0x0000000000001c26 <+2461>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001c2b <+2466>:  lea    -0x240(%rbp),%rax
   0x0000000000001c32 <+2473>:  mov    %rax,%rdi
   0x0000000000001c35 <+2476>:  call   0x10f0 <_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@plt>
   0x0000000000001c3a <+2481>:  mov    %rbx,%rax
   0x0000000000001c3d <+2484>:  mov    %rax,%rdi
   0x0000000000001c40 <+2487>:  call   0x1170 <_Unwind_Resume@plt>
   0x0000000000001c45 <+2492>:  call   0x1130 <__stack_chk_fail@plt>
   0x0000000000001c4a <+2497>:  add    $0x248,%rsp
   0x0000000000001c51 <+2504>:  pop    %rbx
   0x0000000000001c52 <+2505>:  pop    %rbp
   0x0000000000001c53 <+2506>:  ret    
End of assembler dump.
```

## Flag


## Continue
[Continue](./picoGym0416.md)