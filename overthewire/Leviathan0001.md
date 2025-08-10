# Leviathan Level 0 → Level 1 ltrance and setuid root binaries

## Previous Flag
<b>3QJ3TgzHDq</b>

## Goal
Use previous password to log in SSH with user <b>leviathan0</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org
Du Hint: Password in /etc/leviathan_pass/leviathan2 but must gain access via binary file check

## What I learned
```
ltrace          Linux tool that lets you see what library calls a program makes while it runs
library call    happens when a program uses a function from a shared library
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh leviathan1@leviathan.labs.overthewire.org -p 2223 ⌨️
leviathan1@leviathan:~$ ls -la ⌨️
total 36
drwxr-xr-x   2 root       root        4096 Jul 28 19:05 .
drwxr-xr-x 150 root       root        4096 Jul 28 19:06 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Jul 28 18:47 .bashrc     
-r-sr-x---   1 leviathan2 leviathan1 15084 Jul 28 19:05 check       
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan1@leviathan:~$ file check ⌨️
check: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=990fa9b7d511205601669835610d587780d0195e, for GNU/Linux 3.2.0, not stripped
leviathan1@leviathan:~$ whatis strings ltrace ⌨️
strings (1)          - print the sequences of printable characters in files
ltrace (1)           - A library call tracer
leviathan1@leviathan:~$ ./check ⌨️
password: hacker ⌨️
Wrong password, Good Bye ...
leviathan1@leviathan:~$ strings check ⌨️
td8
/lib/ld-linux.so.2
_IO_stdin_used    
puts
__stack_chk_fail  
system
getchar
__libc_start_main 
printf
setreuid
strcmp
geteuid
libc.so.6
GLIBC_2.4
GLIBC_2.34
GLIBC_2.0
__gmon_start__
secr
love
password:
/bin/sh
leviathan1@leviathan:~$ ltrace ./check ⌨️❤️❤️❤️❤️❤️
__libc_start_main(0x80490ed, 1, 0xffffd474, 0 <unfinished ...>
printf("password: ")                                                                   = 10
getchar(0, 0, 0x786573, 0x646f67password: hacker ⌨️
)                                                      = 104
getchar(0, 104, 0x786573, 0x646f67)                                                    = 97
getchar(0, 0x6168, 0x786573, 0x646f67)                                                 = 99
strcmp("hac", "sex") 👀                                                                = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                   = 29
+++ exited (status 0) +++
leviathan1@leviathan:~$ ./check ⌨️
password: sex ⌨️
$ whoami ⌨️
leviathan2
$ cat /etc/leviathan_pass/leviathan2 ⌨️
NsN1HwFoyN 🔐
$ exit ⌨️
leviathan1@leviathan:~$ whoami ⌨️
leviathan1
leviathan1@leviathan:~$ exit ⌨️
logout
Connection to leviathan.labs.overthewire.org closed.
```

## Flag
<b>NsN1HwFoyN</b>

## Continue
[Continue](./Leviathan0102.md)