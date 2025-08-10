# Leviathan Level 3 → Level 4 ASCII

## Previous Flag
<b>WG1egElCvO</b>

## Goal
Use previous password to log in SSH with user <b>leviathan4</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org
Du Hint: Solve the output of the binary file

## What I learned
```
ASCII uses 7 bits to represent one character
01000001 → 65 → A
01100001 → 97 → a
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh leviathan4@leviathan.labs.overthewire.org -p 2223 ⌨️
leviathan4@leviathan:~$ ls -la ⌨️
total 24
drwxr-xr-x   3 root root       4096 Jul 28 19:05 .
drwxr-xr-x 150 root root       4096 Jul 28 19:06 ..
-rw-r--r--   1 root root        220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root root       3851 Jul 28 18:47 .bashrc     
-rw-r--r--   1 root root        807 Mar 31  2024 .profile    
dr-xr-x---   2 root leviathan4 4096 Jul 28 19:05 .trash
leviathan4@leviathan:~$ cd .trash/ ⌨️
leviathan4@leviathan:~/.trash$ ls -la ⌨️
total 24
dr-xr-x--- 2 root       leviathan4  4096 Jul 28 19:05 .  
drwxr-xr-x 3 root       root        4096 Jul 28 19:05 .. 
-r-sr-x--- 1 leviathan5 leviathan4 14940 Jul 28 19:05 bin           # Note: SUID binary belong to leviathan5
leviathan4@leviathan:~/.trash$ file bin ⌨️
bin: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=52e379ac2e364243895250cb84038a8bf5d3e4e5, for GNU/Linux 3.2.0, not stripped
leviathan4@leviathan:~/.trash$ ./bin ⌨️
00110000 01100100 01111001 01111000 01010100 00110111 01000110 00110100 01010001 01000100 00001010
leviathan4@leviathan:~/.trash$ ltrace ./bin ⌨️ 
__libc_start_main(0x80490ad, 1, 0xffffd454, 0 <unfinished ...>
fopen("/etc/leviathan_pass/leviathan5", "r")                                           = 0
+++ exited (status 255) +++

# Note: Don't put spaces or wrong
Method 1: Perl
leviathan4@leviathan:~/.trash$ echo "00110000 01100100 01111001 01111000 01010100 00110111 01000110 00110100 01010001 01000100 00001010" | perl -lpe '$_=pack"B*",$_'
02OAhQ"
leviathan4@leviathan:~/.trash$ echo "0011000001100100011110010111100001010100001101110100011000110100010100010100010000001010" | perl -lpe '$_=pack"B*",$_' ⌨️
0dyxT7F4QD 🔐

Method 2: bash
leviathan4@leviathan:~/.trash$ echo "0011000001100100011110010111100001010100001101110100011000110100010100010100010000001010" | \
>   sed 's/.\{8\}/& /g' | \
>   xargs -n1 bash -c 'echo "ibase=2; $0" | bc' | \
>   awk '{printf "%c", $1}' ⌨️
0dyxT7F4QD 🔐

Method 3: CyberChef (From Binary)
https://cyberchef.io/#recipe=From_Binary('Space',8)&input=MDAxMTAwMDAgMDExMDAxMDAgMDExMTEwMDEgMDExMTEwMDAgMDEwMTAxMDAgMDAxMTAxMTEgMDEwMDAxMTAgMDAxMTAxMDAgMDEwMTAwMDEgMDEwMDAxMDAgMDAwMDEwMTA
```

## Flag
<b>0dyxT7F4QD</b>

## Continue
[Continue](./Leviathan0405.md)