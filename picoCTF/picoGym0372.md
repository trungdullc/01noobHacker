# picoGym Level 372: Reverse
Source: https://play.picoctf.org/practice/challenge/372

## Goal
Try reversing this file? Can ya?<br>
I forgot the password to this file. Please find it for me?<br>
https://artifacts.picoctf.net/c/276/ret

## What I learned
```
Reverse Engineering
gdb
x/s $rsi
    x → examine memory
    /s → interpret memory contents as a null-terminated string
    $rsi → value of rsi register (on x86-64, rsi often holds second argument to a function according to calling convention)

Note: Memory loaded in little endian
Hex	    ASCII
70	    p
69	    i
63	    c
6f	    o
43	    C
54	    T
46	    F
7b	    {

11e4: 48 b8 70 69 63 6f 43 54 46 43 6f 63 69 70    movabs $0x7b4654436f636970,%rax      -> corresponds to: picoCTF{
11ee: 48 ba 33 6c 66 5f 72 33 76 33                movabs $0x337633725f666c33,%rdx      -> 3lf_r3v3
1200: 48 b8 72 35 69 6e 67 5f 73 75                movabs $0x75735f676e693572,%rax      -> ing_suc
120a: 48 ba 63 63 65 35 35 66 75 6c                movabs $0x6c75663535656363,%rdx      -> ce55ful
121c: 48 b8 5f 39 61 65 38 35 32 38                movabs $0x383235386561395f,%rax      -> 9ae8528

Other:
    strace
    ltrace
    Ghidra
    BinaryNinja
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/276/ret ⌨️
--2025-09-27 03:23:09--  https://artifacts.picoctf.net/c/276/ret
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16888 (16K) [application/octet-stream]
Saving to: 'ret'

ret                                                        100%[======================================================================================================================================>]  16.49K  --.-KB/s    in 0.004s  

2025-09-27 03:23:09 (3.76 MB/s) - 'ret' saved [16888/16888]

AsianHacker-picoctf@webshell:~$ file ret ⌨️
ret: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6c43c1779ecbf9a8df208682dd85fdba5bf8110f, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ ls -la ret ⌨️ 
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 16888 Mar 16  2023 ret
AsianHacker-picoctf@webshell:~$ chmod +x ret ⌨️
AsianHacker-picoctf@webshell:~$ strings ret | grep picoCTF ⌨️
picoCTF{H
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_9ae85289} 🔐

# Method 1: objdump
AsianHacker-picoctf@webshell:~$ objdump -d ret ⌨️

ret:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:       f3 0f 1e fa             endbr64 
    1004:       48 83 ec 08             sub    $0x8,%rsp
    1008:       48 8b 05 d9 2f 00 00    mov    0x2fd9(%rip),%rax        # 3fe8 <__gmon_start__>
    100f:       48 85 c0                test   %rax,%rax
    1012:       74 02                   je     1016 <_init+0x16>
    1014:       ff d0                   call   *%rax
    1016:       48 83 c4 08             add    $0x8,%rsp
    101a:       c3                      ret    

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:       ff 35 7a 2f 00 00       push   0x2f7a(%rip)        # 3fa0 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:       f2 ff 25 7b 2f 00 00    bnd jmp *0x2f7b(%rip)        # 3fa8 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:       0f 1f 00                nopl   (%rax)
    1030:       f3 0f 1e fa             endbr64 
    1034:       68 00 00 00 00          push   $0x0
    1039:       f2 e9 e1 ff ff ff       bnd jmp 1020 <.plt>
    103f:       90                      nop
    1040:       f3 0f 1e fa             endbr64 
    1044:       68 01 00 00 00          push   $0x1
    1049:       f2 e9 d1 ff ff ff       bnd jmp 1020 <.plt>
    104f:       90                      nop
    1050:       f3 0f 1e fa             endbr64 
    1054:       68 02 00 00 00          push   $0x2
    1059:       f2 e9 c1 ff ff ff       bnd jmp 1020 <.plt>
    105f:       90                      nop
    1060:       f3 0f 1e fa             endbr64 
    1064:       68 03 00 00 00          push   $0x3
    1069:       f2 e9 b1 ff ff ff       bnd jmp 1020 <.plt>
    106f:       90                      nop
    1070:       f3 0f 1e fa             endbr64 
    1074:       68 04 00 00 00          push   $0x4
    1079:       f2 e9 a1 ff ff ff       bnd jmp 1020 <.plt>
    107f:       90                      nop

Disassembly of section .plt.got:

0000000000001080 <__cxa_finalize@plt>:
    1080:       f3 0f 1e fa             endbr64 
    1084:       f2 ff 25 6d 2f 00 00    bnd jmp *0x2f6d(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    108b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

Disassembly of section .plt.sec:

0000000000001090 <puts@plt>:
    1090:       f3 0f 1e fa             endbr64 
    1094:       f2 ff 25 15 2f 00 00    bnd jmp *0x2f15(%rip)        # 3fb0 <puts@GLIBC_2.2.5>
    109b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

00000000000010a0 <__stack_chk_fail@plt>:
    10a0:       f3 0f 1e fa             endbr64 
    10a4:       f2 ff 25 0d 2f 00 00    bnd jmp *0x2f0d(%rip)        # 3fb8 <__stack_chk_fail@GLIBC_2.4>
    10ab:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

00000000000010b0 <printf@plt>:
    10b0:       f3 0f 1e fa             endbr64 
    10b4:       f2 ff 25 05 2f 00 00    bnd jmp *0x2f05(%rip)        # 3fc0 <printf@GLIBC_2.2.5>
    10bb:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

00000000000010c0 <strcmp@plt>:
    10c0:       f3 0f 1e fa             endbr64 
    10c4:       f2 ff 25 fd 2e 00 00    bnd jmp *0x2efd(%rip)        # 3fc8 <strcmp@GLIBC_2.2.5>
    10cb:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

00000000000010d0 <__isoc99_scanf@plt>:
    10d0:       f3 0f 1e fa             endbr64 
    10d4:       f2 ff 25 f5 2e 00 00    bnd jmp *0x2ef5(%rip)        # 3fd0 <__isoc99_scanf@GLIBC_2.7>
    10db:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

Disassembly of section .text:

00000000000010e0 <_start>:
    10e0:       f3 0f 1e fa             endbr64 
    10e4:       31 ed                   xor    %ebp,%ebp
    10e6:       49 89 d1                mov    %rdx,%r9
    10e9:       5e                      pop    %rsi
    10ea:       48 89 e2                mov    %rsp,%rdx
    10ed:       48 83 e4 f0             and    $0xfffffffffffffff0,%rsp
    10f1:       50                      push   %rax
    10f2:       54                      push   %rsp
    10f3:       4c 8d 05 46 02 00 00    lea    0x246(%rip),%r8        # 1340 <__libc_csu_fini>
    10fa:       48 8d 0d cf 01 00 00    lea    0x1cf(%rip),%rcx        # 12d0 <__libc_csu_init>
    1101:       48 8d 3d c1 00 00 00    lea    0xc1(%rip),%rdi        # 11c9 <main>
    1108:       ff 15 d2 2e 00 00       call   *0x2ed2(%rip)        # 3fe0 <__libc_start_main@GLIBC_2.2.5>
    110e:       f4                      hlt    
    110f:       90                      nop

0000000000001110 <deregister_tm_clones>:
    1110:       48 8d 3d f9 2e 00 00    lea    0x2ef9(%rip),%rdi        # 4010 <__TMC_END__>
    1117:       48 8d 05 f2 2e 00 00    lea    0x2ef2(%rip),%rax        # 4010 <__TMC_END__>
    111e:       48 39 f8                cmp    %rdi,%rax
    1121:       74 15                   je     1138 <deregister_tm_clones+0x28>
    1123:       48 8b 05 ae 2e 00 00    mov    0x2eae(%rip),%rax        # 3fd8 <_ITM_deregisterTMCloneTable>
    112a:       48 85 c0                test   %rax,%rax
    112d:       74 09                   je     1138 <deregister_tm_clones+0x28>
    112f:       ff e0                   jmp    *%rax
    1131:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)
    1138:       c3                      ret    
    1139:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000001140 <register_tm_clones>:
    1140:       48 8d 3d c9 2e 00 00    lea    0x2ec9(%rip),%rdi        # 4010 <__TMC_END__>
    1147:       48 8d 35 c2 2e 00 00    lea    0x2ec2(%rip),%rsi        # 4010 <__TMC_END__>
    114e:       48 29 fe                sub    %rdi,%rsi
    1151:       48 89 f0                mov    %rsi,%rax
    1154:       48 c1 ee 3f             shr    $0x3f,%rsi
    1158:       48 c1 f8 03             sar    $0x3,%rax
    115c:       48 01 c6                add    %rax,%rsi
    115f:       48 d1 fe                sar    %rsi
    1162:       74 14                   je     1178 <register_tm_clones+0x38>
    1164:       48 8b 05 85 2e 00 00    mov    0x2e85(%rip),%rax        # 3ff0 <_ITM_registerTMCloneTable>
    116b:       48 85 c0                test   %rax,%rax
    116e:       74 08                   je     1178 <register_tm_clones+0x38>
    1170:       ff e0                   jmp    *%rax
    1172:       66 0f 1f 44 00 00       nopw   0x0(%rax,%rax,1)
    1178:       c3                      ret    
    1179:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000001180 <__do_global_dtors_aux>:
    1180:       f3 0f 1e fa             endbr64 
    1184:       80 3d 85 2e 00 00 00    cmpb   $0x0,0x2e85(%rip)        # 4010 <__TMC_END__>
    118b:       75 2b                   jne    11b8 <__do_global_dtors_aux+0x38>
    118d:       55                      push   %rbp
    118e:       48 83 3d 62 2e 00 00    cmpq   $0x0,0x2e62(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1195:       00 
    1196:       48 89 e5                mov    %rsp,%rbp
    1199:       74 0c                   je     11a7 <__do_global_dtors_aux+0x27>
    119b:       48 8b 3d 66 2e 00 00    mov    0x2e66(%rip),%rdi        # 4008 <__dso_handle>
    11a2:       e8 d9 fe ff ff          call   1080 <__cxa_finalize@plt>
    11a7:       e8 64 ff ff ff          call   1110 <deregister_tm_clones>
    11ac:       c6 05 5d 2e 00 00 01    movb   $0x1,0x2e5d(%rip)        # 4010 <__TMC_END__>
    11b3:       5d                      pop    %rbp
    11b4:       c3                      ret    
    11b5:       0f 1f 00                nopl   (%rax)
    11b8:       c3                      ret    
    11b9:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

00000000000011c0 <frame_dummy>:
    11c0:       f3 0f 1e fa             endbr64 
    11c4:       e9 77 ff ff ff          jmp    1140 <register_tm_clones>

00000000000011c9 <main>:
    11c9:       f3 0f 1e fa             endbr64 
    11cd:       55                      push   %rbp
    11ce:       48 89 e5                mov    %rsp,%rbp
    11d1:       48 83 ec 60             sub    $0x60,%rsp
    11d5:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
    11dc:       00 00 
    11de:       48 89 45 f8             mov    %rax,-0x8(%rbp)
    11e2:       31 c0                   xor    %eax,%eax
    11e4:       48 b8 70 69 63 6f 43    movabs $0x7b4654436f636970,%rax 👀
    11eb:       54 46 7b 
    11ee:       48 ba 33 6c 66 5f 72    movabs $0x337633725f666c33,%rdx 👀
    11f5:       33 76 33 
    11f8:       48 89 45 d0             mov    %rax,-0x30(%rbp)
    11fc:       48 89 55 d8             mov    %rdx,-0x28(%rbp)
    1200:       48 b8 72 35 69 6e 67    movabs $0x75735f676e693572,%rax 👀
    1207:       5f 73 75 
    120a:       48 ba 63 63 65 35 35    movabs $0x6c75663535656363,%rdx 👀
    1211:       66 75 6c 
    1214:       48 89 45 e0             mov    %rax,-0x20(%rbp)
    1218:       48 89 55 e8             mov    %rdx,-0x18(%rbp)
    121c:       48 b8 5f 39 61 65 38    movabs $0x383235386561395f,%rax 👀
    1223:       35 32 38 
    1226:       48 89 45 f0             mov    %rax,-0x10(%rbp)
    122a:       48 8d 3d d7 0d 00 00    lea    0xdd7(%rip),%rdi        # 2008 <_IO_stdin_used+0x8>
    1231:       b8 00 00 00 00          mov    $0x0,%eax
    1236:       e8 75 fe ff ff          call   10b0 <printf@plt>
    123b:       48 8d 45 a0             lea    -0x60(%rbp),%rax
    123f:       48 89 c6                mov    %rax,%rsi
    1242:       48 8d 3d e8 0d 00 00    lea    0xde8(%rip),%rdi        # 2031 <_IO_stdin_used+0x31>
    1249:       b8 00 00 00 00          mov    $0x0,%eax
    124e:       e8 7d fe ff ff          call   10d0 <__isoc99_scanf@plt>
    1253:       48 8d 45 a0             lea    -0x60(%rbp),%rax
    1257:       48 89 c6                mov    %rax,%rsi
    125a:       48 8d 3d d3 0d 00 00    lea    0xdd3(%rip),%rdi        # 2034 <_IO_stdin_used+0x34>
    1261:       b8 00 00 00 00          mov    $0x0,%eax
    1266:       e8 45 fe ff ff          call   10b0 <printf@plt>
    126b:       48 8d 55 d0             lea    -0x30(%rbp),%rdx
    126f:       48 8d 45 a0             lea    -0x60(%rbp),%rax
    1273:       48 89 d6                mov    %rdx,%rsi
    1276:       48 89 c7                mov    %rax,%rdi
    1279:       e8 42 fe ff ff          call   10c0 <strcmp@plt>
    127e:       85 c0                   test   %eax,%eax
    1280:       75 1a                   jne    129c <main+0xd3>
    1282:       48 8d 3d bf 0d 00 00    lea    0xdbf(%rip),%rdi        # 2048 <_IO_stdin_used+0x48>
    1289:       e8 02 fe ff ff          call   1090 <puts@plt>
    128e:       48 8d 45 d0             lea    -0x30(%rbp),%rax
    1292:       48 89 c7                mov    %rax,%rdi
    1295:       e8 f6 fd ff ff          call   1090 <puts@plt>
    129a:       eb 0c                   jmp    12a8 <main+0xdf>
    129c:       48 8d 3d f3 0d 00 00    lea    0xdf3(%rip),%rdi        # 2096 <_IO_stdin_used+0x96>
    12a3:       e8 e8 fd ff ff          call   1090 <puts@plt>
    12a8:       b8 00 00 00 00          mov    $0x0,%eax
    12ad:       48 8b 4d f8             mov    -0x8(%rbp),%rcx
    12b1:       64 48 33 0c 25 28 00    xor    %fs:0x28,%rcx
    12b8:       00 00 
    12ba:       74 05                   je     12c1 <main+0xf8>
    12bc:       e8 df fd ff ff          call   10a0 <__stack_chk_fail@plt>
    12c1:       c9                      leave  
    12c2:       c3                      ret    
    12c3:       66 2e 0f 1f 84 00 00    cs nopw 0x0(%rax,%rax,1)
    12ca:       00 00 00 
    12cd:       0f 1f 00                nopl   (%rax)

00000000000012d0 <__libc_csu_init>:
    12d0:       f3 0f 1e fa             endbr64 
    12d4:       41 57                   push   %r15
    12d6:       4c 8d 3d bb 2a 00 00    lea    0x2abb(%rip),%r15        # 3d98 <__frame_dummy_init_array_entry>
    12dd:       41 56                   push   %r14
    12df:       49 89 d6                mov    %rdx,%r14
    12e2:       41 55                   push   %r13
    12e4:       49 89 f5                mov    %rsi,%r13
    12e7:       41 54                   push   %r12
    12e9:       41 89 fc                mov    %edi,%r12d
    12ec:       55                      push   %rbp
    12ed:       48 8d 2d ac 2a 00 00    lea    0x2aac(%rip),%rbp        # 3da0 <__do_global_dtors_aux_fini_array_entry>
    12f4:       53                      push   %rbx
    12f5:       4c 29 fd                sub    %r15,%rbp
    12f8:       48 83 ec 08             sub    $0x8,%rsp
    12fc:       e8 ff fc ff ff          call   1000 <_init>
    1301:       48 c1 fd 03             sar    $0x3,%rbp
    1305:       74 1f                   je     1326 <__libc_csu_init+0x56>
    1307:       31 db                   xor    %ebx,%ebx
    1309:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)
    1310:       4c 89 f2                mov    %r14,%rdx
    1313:       4c 89 ee                mov    %r13,%rsi
    1316:       44 89 e7                mov    %r12d,%edi
    1319:       41 ff 14 df             call   *(%r15,%rbx,8)
    131d:       48 83 c3 01             add    $0x1,%rbx
    1321:       48 39 dd                cmp    %rbx,%rbp
    1324:       75 ea                   jne    1310 <__libc_csu_init+0x40>
    1326:       48 83 c4 08             add    $0x8,%rsp
    132a:       5b                      pop    %rbx
    132b:       5d                      pop    %rbp
    132c:       41 5c                   pop    %r12
    132e:       41 5d                   pop    %r13
    1330:       41 5e                   pop    %r14
    1332:       41 5f                   pop    %r15
    1334:       c3                      ret    
    1335:       66 66 2e 0f 1f 84 00    data16 cs nopw 0x0(%rax,%rax,1)
    133c:       00 00 00 00 

0000000000001340 <__libc_csu_fini>:
    1340:       f3 0f 1e fa             endbr64 
    1344:       c3                      ret    

Disassembly of section .fini:

0000000000001348 <_fini>:
    1348:       f3 0f 1e fa             endbr64 
    134c:       48 83 ec 08             sub    $0x8,%rsp
    1350:       48 83 c4 08             add    $0x8,%rsp
    1354:       c3                      ret    

AsianHacker-picoctf@webshell:~$ ./ret ⌨️                                                    
Enter the password to unlock this file: picoCTF{3lf_r3v3r5ing_succe55ful_9ae8528 ⌨️
You entered: picoCTF{3lf_r3v3r5ing_succe55ful_9ae8528
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_9ae85289} 🔐
picoCTF{3lf_r3v3r5ing_succe55ful_9ae8528

# Method 2: gdb
AsianHacker-picoctf@webshell:~$ gdb --quiet ./ret ⌨️
Reading symbols from ./ret...
(No debugging symbols found in ./ret)
(gdb) start ⌨️
Temporary breakpoint 1 at 0x11d1
Starting program: /home/AsianHacker-picoctf/ret 
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Temporary breakpoint 1, 0x000055abdf1681d1 in main ()
(gdb) break strcmp ⌨️
Breakpoint 2 at 0x7fb02c1657e0: strcmp. (2 locations)
(gdb) c ⌨️
Continuing.
Enter the password to unlock this file: abcdefghijklmnop ⌨️
You entered: abcdefghijklmnop

Breakpoint 2, __strcmp_evex () at ../sysdeps/x86_64/multiarch/strcmp-evex.S:100
100     ../sysdeps/x86_64/multiarch/strcmp-evex.S: No such file or directory.
(gdb) info reg ⌨️
rax            0x7fff70de00d0      140735086985424
rbx            0x0                 0
rcx            0x1                 1
rdx            0x7fff70de0100      140735086985472
rsi            0x7fff70de0100      140735086985472 👀 what cmp to
rdi            0x7fff70de00d0      140735086985424 👀 input
rbp            0x7fff70de0130      0x7fff70de0130
rsp            0x7fff70de00c8      0x7fff70de00c8
r8             0x0                 0
r9             0x7fffffff          2147483647
r10            0x0                 0
r11            0x246               582
r12            0x7fff70de0248      140735086985800
r13            0x55abdf1681c9      94196670562761
r14            0x0                 0
r15            0x7fb02c22d040      140394631450688
rip            0x7fb02c1657e0      0x7fb02c1657e0 <__strcmp_evex>
eflags         0x202               [ IF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0
k0             0x1e                30
k1             0x880               2176
k2             0x0                 0
k3             0x0                 0
k4             0x0                 0
k5             0x0                 0
k6             0x0                 0
k7             0x0                 0

(gdb) x/s $rsi ⌨️
0x7fff70de0100: "picoCTF{3lf_r3v3r5ing_succe55ful_9ae8528" 👀
(gdb) x/s $rdi ⌨️
0x7fff70de00d0: "abcdefghijklmnop"
```

## Flag
picoCTF{3lf_r3v3r5ing_succe55ful_9ae85289}

## Continue
[Continue](./picoGym0273.md)