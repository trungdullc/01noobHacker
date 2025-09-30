# picoGym Level 267: file-run2
Source: https://play.picoctf.org/practice/challenge/267

## Goal
Another program, but this time, it seems to want some input.<br>
What happens if you try to run it on the command line with input "Hello!"?<br>
Download the program here.<br>
https://artifacts.picoctf.net/c/155/run

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/155/run ⌨️
--2025-09-29 22:53:35--  https://artifacts.picoctf.net/c/155/run
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.72, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16816 (16K) [application/octet-stream]
Saving to: 'run'

run                                                        100%[======================================================================================================================================>]  16.42K  --.-KB/s    in 0.004s  

2025-09-29 22:53:36 (3.84 MB/s) - 'run' saved [16816/16816]

AsianHacker-picoctf@webshell:~$ file run ⌨️
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=81c058f985672af182bed8c02aeb32221256d8bb, for GNU/Linux 3.2.0, not stripped
AsianHacker-picoctf@webshell:~$ chmod u+x run ⌨️
AsianHacker-picoctf@webshell:~$ ./run ⌨️
Run this file with only one argument.
AsianHacker-picoctf@webshell:~$ ./run Hello ⌨️
Won't you say 'Hello!' to me first?
AsianHacker-picoctf@webshell:~$ ./run Hello! ⌨️
The flag is: picoCTF{F1r57_4rgum3n7_be0714da} 🔐
```

## Flag
picoCTF{F1r57_4rgum3n7_be0714da}

## Continue
[Continue](./picoGym0389.md)