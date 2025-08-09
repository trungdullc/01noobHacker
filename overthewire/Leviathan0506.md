# Leviathan Level 5 → Level 6

## Previous Flag
<b>szo7HDB88w</b>

## Goal
Use previous password to log in SSH with user <b>leviathan6</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org
Du Hint: 

## What I learned
```
Linux Manual Page: https://man7.org/linux/man-pages/dir_all_alphabetic.html

GDB (GNU Debugger) is a debugger for Linux. It can be used for reverse engineering. There are however also programs, like Ghidra, which are designed specifically for reverse engineering. There are also plugins for GDB, which make debugging and/or reverse engineering easier like PWNDBG.

To run GDB with a program to debug and parameter input use: gdb --args program_name params
Use disassemble func_name, to get the assembly code of a specific function
break *hex_address to set a breakpoint at a specific part of the code
Use c to continue after a breakpoint
run starts the program
info registers prints the current values of all registers
x hex_address allows you to print the value saved at the address If you google ‘gdb cheat sheet’ you will find even more helpful commands

x → examine raw memory values in various formats (numbers).
x/s → treat the memory location as pointing to a string and print it as text
x/s *((char **)$esp + 1)
0xffffd5ad:     "0000"
x/4b 0xffffd340         # View raw bytes
x/wx 0xffffd340         # View 32-bit word in hex
x/dw 0xffffd340         # View 32-bit word in decimal

There are different types of assembly: Intel and AT&T Syntax
TryHackMe Win64 Assembly for the basics of reverse engineering and assembly: https://tryhackme.com/room/win64assembly
Tutorialspoint Assembly Programming Tutorial: https://www.tutorialspoint.com/assembly_programming/index.htm

AT&T Syntax: instr source,dest
    Immediate values have $ prefix
    Registers have % prefix
    Memory addresses use parentheses, (%eax) means “contents at address in eax”

# Example 1: Add immediate value 4 to %eax
add $0x4, %eax              # Meaning: %eax = %eax + 4

# Example 2: Move the 4 bytes at memory address stored in %eax into %eax
mov (%eax), %eax            # Meaning: load the value pointed by %eax into %eax

# Example 3: Compare %eax with 10
cmp $10, %eax               # Sets CPU flags based on %eax - 10 (used for conditional jumps)

# Example 4: Jump if equal (zero flag set) to label 'equal_label'
je equal_label              # If previous cmp found equality, jump to 'equal_label'

# Example 5: Move immediate 0 into %ebx register
mov $0, %ebx                # Set %ebx = 0

# Example 6: Push %eax onto stack
push %eax                   # Save %eax on stack (decrements stack pointer and stores %eax)

# Example 7: Pop value from stack into %ebx
pop %ebx                    # Restore %ebx from stack (increments stack pointer and loads value)

# Example 8: Call function at label 'my_function'
call my_function            # Jump to 'my_function' and save return address on stack

# Example 9: Return from function
ret                         # Pop return address from stack and jump there
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh leviathan6@leviathan.labs.overthewire.org -p 2223 ⌨️
leviathan6@leviathan:~$ ls -la ⌨️
total 36
drwxr-xr-x   2 root       root        4096 Jul 28 19:05 .
drwxr-xr-x 150 root       root        4096 Jul 28 19:06 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Jul 28 18:47 .bashrc     
-r-sr-x---   1 leviathan7 leviathan6 15036 Jul 28 19:05 leviathan6  
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan6@leviathan:~$ file leviathan6 ⌨️ 
leviathan6: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=e16f2bca0c05d56ab07cd7c95324355952bb3cc5, for GNU/Linux 3.2.0, not stripped
leviathan6@leviathan:~$ ./leviathan6 ⌨️
usage: ./leviathan6 <4 digit code> 
leviathan6@leviathan:~$ ./leviathan6 0000 ⌨️
Wrong
leviathan6@leviathan:~$ ltrace ./leviathan6 0000 ⌨️
__libc_start_main(0x80490dd, 2, 0xffffd464, 0 <unfinished ...>
atoi(0xffffd5ce, 0, 0, 0)                                                              = 0
puts("Wrong"Wrong
)                                                                          = 6
+++ exited (status 0) +++

# Run debugger w/ arguments from terminal w/ --args 
leviathan6@leviathan:~$ gdb --args leviathan6 0000 ⌨️❤️❤️❤️❤️❤️
GNU gdb (Ubuntu 15.0.50.20240403-0ubuntu1) 15.0.50.20240403-git
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from leviathan6...

--Type <RET> for more, q to quit, c to continue without paging--c ⌨️
This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y ⌨️
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Download failed: Permission denied.  Continuing without separate debug info for /home/leviathan6/leviathan6.
(No debugging symbols found in leviathan6)

# Look at assembly code
(gdb) disassemble main ⌨️❤️❤️❤️❤️❤️
Dump of assembler code for function main:
   0x080491c6 <+0>:     lea    0x4(%esp),%ecx
   0x080491ca <+4>:     and    $0xfffffff0,%esp
   0x080491cd <+7>:     push   -0x4(%ecx)
   0x080491d0 <+10>:    push   %ebp
   0x080491d1 <+11>:    mov    %esp,%ebp
   0x080491d3 <+13>:    push   %ebx
   0x080491d4 <+14>:    push   %ecx
   0x080491d5 <+15>:    sub    $0x10,%esp
   0x080491d8 <+18>:    mov    %ecx,%eax
   0x080491da <+20>:    movl   $0x1bd3,-0xc(%ebp)
   0x080491e1 <+27>:    cmpl   $0x2,(%eax)
   0x080491e4 <+30>:    je     0x8049206 <main+64>
   0x080491e6 <+32>:    mov    0x4(%eax),%eax
   0x080491e9 <+35>:    mov    (%eax),%eax
   0x080491eb <+37>:    sub    $0x8,%esp
   0x080491ee <+40>:    push   %eax
--Type <RET> for more, q to quit, c to continue without paging--c ⌨️
   0x080491ef <+41>:    push   $0x804a008
   0x080491f4 <+46>:    call   0x8049040 <printf@plt>
   0x080491f9 <+51>:    add    $0x10,%esp
   0x080491fc <+54>:    sub    $0xc,%esp
   0x080491ff <+57>:    push   $0xffffffff
   0x08049201 <+59>:    call   0x8049080 <exit@plt>
   0x08049206 <+64>:    mov    0x4(%eax),%eax
   0x08049209 <+67>:    add    $0x4,%eax
   0x0804920c <+70>:    mov    (%eax),%eax
   0x0804920e <+72>:    sub    $0xc,%esp
   0x08049211 <+75>:    push   %eax
   0x08049212 <+76>:    call   0x80490a0 <atoi@plt> 👀      # Don't set bp: break atoi
   0x08049217 <+81>:    add    $0x10,%esp
   0x0804921a <+84>:    cmp    %eax,-0xc(%ebp) 🐱‍💻           # break *0x0804921a
   0x0804921d <+87>:    jne    0x804924a <main+132>
   0x0804921f <+89>:    call   0x8049050 <geteuid@plt>
   0x08049224 <+94>:    mov    %eax,%ebx
   0x08049226 <+96>:    call   0x8049050 <geteuid@plt>
   0x0804922b <+101>:   sub    $0x8,%esp
   0x0804922e <+104>:   push   %ebx
   0x0804922f <+105>:   push   %eax
   0x08049230 <+106>:   call   0x8049090 <setreuid@plt>
   0x08049235 <+111>:   add    $0x10,%esp
   0x08049238 <+114>:   sub    $0xc,%esp
   0x0804923b <+117>:   push   $0x804a022
   0x08049240 <+122>:   call   0x8049070 <system@plt>
   0x08049245 <+127>:   add    $0x10,%esp
   0x08049248 <+130>:   jmp    0x804925a <main+148>
   0x0804924a <+132>:   sub    $0xc,%esp
   0x0804924d <+135>:   push   $0x804a02a
   0x08049252 <+140>:   call   0x8049060 <puts@plt>
   0x08049257 <+145>:   add    $0x10,%esp
   0x0804925a <+148>:   mov    $0x0,%eax
   0x0804925f <+153>:   lea    -0x8(%ebp),%esp
   0x08049262 <+156>:   pop    %ecx
   0x08049263 <+157>:   pop    %ebx
   0x08049264 <+158>:   pop    %ebp
   0x08049265 <+159>:   lea    -0x4(%ecx),%esp
   0x08049268 <+162>:   ret
End of assembler dump.

# atoi function called (converts string to integer, assuming input before)
# Looking for where numbers get compared since we input 0000 - compared, compared would equal that
# Comparing value in register ’eax’ (0, inital input) and register ’ebp’ minus 0xc
(gdb) break *0x0804921a ⌨️❤️                # Note: Use * before hex when ref to memory
Breakpoint 1 at 0x804921a
(gdb) run ⌨️❤️
Starting program: /home/leviathan6/leviathan6 0000
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x0804921a in main ()
(gdb) info registers ⌨️❤️❤️❤️❤️❤️
eax            0x0                 0
ecx            0xffffd5b1          -10831
edx            0x0                 0
ebx            0xf7faae34          -134566348
esp            0xffffd350          0xffffd350
ebp            0xffffd368          0xffffd368
esi            0xffffd440          -11200
edi            0xf7ffcb60          -134231200
eip            0x804921a           0x804921a <main+84>
eflags         0x286               [ PF SF IF ]
cs             0x23                35
ss             0x2b                43
ds             0x2b                43
es             0x2b                43
fs             0x0                 0
gs             0x63                99
k0             0x0                 0
--Type <RET> for more, q to quit, c to continue without paging-- ⌨️
k1             0x0                 0
k2             0x0                 0
k3             0x0                 0
k4             0x0                 0
k5             0x0                 0
k6             0x0                 0
k7             0x0                 0

# Calculate address and then what is saved at that address in decimal (dereference)
(gdb) print $ebp-0xc ⌨️
$1 = (void *) 0xffffd35c
(gdb) x 0xffffd35c ⌨️❤️
0xffffd35c:     0x00001bd3
(gdb) print/d 0x00001bd3 ⌨️❤️
$2 = 7123 👀
(gdb) info breakpoints ⌨️❤️
Num     Type           Disp Enb Address    What     
1       breakpoint     keep y   0x0804921a <main+84>
        breakpoint already hit 1 time
(gdb) delete breakpoints ⌨️❤️
Delete all breakpoints, watchpoints, tracepoints, and catchpoints? (y or n) y
(gdb) info breakpoints ⌨️
No breakpoints, watchpoints, tracepoints, or catchpoints.
(gdb) break atoi ⌨️
Download failed: Invalid argument.  Continuing without source file ./stdlib/./stdlib/atoi.c.
Breakpoint 2 at 0xf7db7870: file ./stdlib/atoi.c, line 26.
(gdb) break main ⌨️
Breakpoint 3 at 0x80491d5
(gdb) info breakpoints ⌨️
Num     Type           Disp Enb Address    What
2       breakpoint     keep y   0xf7db7870 in __GI_atoi at ./stdlib/atoi.c:26
3       breakpoint     keep y   0x080491d5 <main+15>
(gdb) clear *0xf7db7870 ⌨️
Deleted breakpoint 2
(gdb) clear main ⌨️
Deleted breakpoint 3
(gdb) info breakpoints ⌨️
No breakpoints, watchpoints, tracepoints, or catchpoints.
(gdb) shell clear ⌨️❤️
(gdb) exit ⌨️
A debugging session is active.

        Inferior 1 [process 2300307] will be killed.

Quit anyway? (y or n) y ⌨️
leviathan6@leviathan:~$ ./leviathan6 7123 ⌨️
$ whoami ⌨️
leviathan7
$ cat /etc/leviathan_pass/leviathan7 ⌨️
qEs5Io5yM8 🔐

Method: Brute Force (Last Option)
leviathan6@leviathan:~$ for i in {0000..9999}; do ./leviathan6 $i; done ⌨️
```

## Flag
<b>qEs5Io5yM8</b>

## Continue
[Continue](/overthewire/Leviathan0607.md)