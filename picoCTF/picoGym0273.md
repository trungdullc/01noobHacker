# picoGym Level 273: GDB Test Drive
Source: https://play.picoctf.org/practice/challenge/273

## Goal
Can you get the flag?<br>
Download this binary.<br>
https://artifacts.picoctf.net/c/87/gdbme<br>
Here's the test drive instructions:<br>
chmod +x gdbme <br>
gdb --quiet gdbme<br>
(gdb) layout asm<br>
(gdb) break *(main+99)<br>
(gdb) run<br>
(gdb) jump *(main+104)<br>

## What I learned
```
Reverse Engineering
gdb
    set disassembly-flavor att                          # Default
    set disassembly-flavor intel                        # Similar to ARM
    layout split                                        # Show both source and assembly side by side
    layout regs                                         # Show registers in a separate window
    layout asm (dynamic) vs disassemble main (static)
    run & start behave differently
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/87/gdbme ⌨️
--2025-09-27 06:11:15--  https://artifacts.picoctf.net/c/87/gdbme
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.72, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17048 (17K) [application/octet-stream]
Saving to: 'gdbme'

gdbme                                                      100%[======================================================================================================================================>]  16.65K  --.-KB/s    in 0.004s  

2025-09-27 06:11:15 (3.63 MB/s) - 'gdbme' saved [17048/17048]

AsianHacker-picoctf@webshell:~$ chmod +x gdbme ⌨️
AsianHacker-picoctf@webshell:~$ file gdbme ⌨️
gdbme: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=15cc42b7d1ba7d200593c720e2d9fd2e757fccca, for GNU/Linux 3.2.0, not stripped

AsianHacker-picoctf@webshell:~$ gdb --quiet gdbme ⌨️
Reading symbols from gdbme...
(No debugging symbols found in gdbme)                       # Static View
(gdb) layout asm ⌨️                                         (gdb) disassemble main ⌨️
(gdb) info breakpoints ⌨️
No breakpoints or watchpoints.
(gdb) delete ⌨️
(gdb) break *(main+99) ⌨️
Breakpoint 1 at 0x132a                                      # Important: run & start behave differently
(gdb) run ⌨️                                                (gdb) start ⌨️
Starting program: home/AsianHacker-picoctf/gdbme
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu-libthread_db.so.1".

Breakpoint 1, 0x000055e39d28832a in main()
(gdb) jump *(main+104) ⌨️
Continuing at 0x55e39d28832f.
picoCTF{d3bugg3r_dr1v3_7776d758} 🔐
(gdb) ior 1(process 303) exited normally]
```

## Flag
picoCTF{d3bugg3r_dr1v3_7776d758}

## Continue
[Continue](./picoGym0395.md)