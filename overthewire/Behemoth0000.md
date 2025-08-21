# Behemoth Level 0 Stack Buffer Overflows and strings, ltrace, strace, gdb, gef, pwngdb, radare2(r2) ⭐⭐⭐

## Previous Flag
<b>behemoth0</b>

## Goal
Be able to log onto OverTheWire SSH server: behemoth.labs.overthewire.org. Given user <b>behemoth0</b> and port <b>2221</b>.

There is no information for this level, intentionally.

## What I learned
```
Behemoth teaches buffer overflows, race conditions and privilege escalation
Data for the levels can be found in /behemoth/
Passwords can be found in /etc/behemoth_pass/
find / -type file -name "behemoth1" 2>/dev/null
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh behemoth0@behemoth.labs.overthewire.org -p 2221 ⌨️
The authenticity of host '[behemoth.labs.overthewire.org]:2221 ([13.48.176.69]:2221)' can't be established.
ED25519 key fingerprint is SHA256:
This host key is known by the following other names/addresses:
    C:\Users\trung.DESKTOP-G7C81CH/.ssh/known_hosts:6: bandit.labs.overthewire.org
    C:\Users\trung.DESKTOP-G7C81CH/.ssh/known_hosts:7: [leviathan.labs.overthewire.org]:2223
    C:\Users\trung.DESKTOP-G7C81CH/.ssh/known_hosts:8: [krypton.labs.overthewire.org]:2231
    C:\Users\trung.DESKTOP-G7C81CH/.ssh/known_hosts:9: [narnia.labs.overthewire.org]:2226
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[behemoth.labs.overthewire.org]:2221' (ED25519) to the list of known hosts.

behemoth0@behemoth.labs.overthewire.org's password: ⌨️
behemoth0@behemoth:~$ cd /behemoth/ ⌨️
behemoth0@behemoth:/behemoth$ ls -la ⌨️
total 136
drwxr-xr-x  2 root      root       4096 Jul 28 19:04 .        
drwxr-xr-x 31 root      root       4096 Aug 14 22:44 ..       
-r-sr-x---  1 behemoth1 behemoth0 11696 Jul 28 19:04 behemoth0 👀
-r-sr-x---  1 behemoth2 behemoth1 11300 Jul 28 19:04 behemoth1
-r-sr-x---  1 behemoth3 behemoth2 15124 Jul 28 19:04 behemoth2
-r-sr-x---  1 behemoth4 behemoth3 11348 Jul 28 19:04 behemoth3
-r-sr-x---  1 behemoth5 behemoth4 15120 Jul 28 19:04 behemoth4
-r-sr-x---  1 behemoth6 behemoth5 15404 Jul 28 19:04 behemoth5
-r-sr-x---  1 behemoth7 behemoth6 15144 Jul 28 19:04 behemoth6
-r-xr-x---  1 behemoth7 behemoth6 14924 Jul 28 19:04 behemoth6_reader
-r-sr-x---  1 behemoth8 behemoth7 11472 Jul 28 19:04 behemoth7
behemoth0@behemoth:/behemoth$ file behemoth0 ⌨️
behemoth0: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=5bc2def88619f7c21180b306bcb4c62bd94c7ebd, for GNU/Linux 3.2.0, not stripped
behemoth0@behemoth:/behemoth$ id ⌨️
uid=13000(behemoth0) gid=13000(behemoth0) groups=13000(behemoth0)
behemoth0@behemoth:/behemoth$ ./behemoth0 ⌨️
Password: AAAA ⌨️
Access denied..
behemoth0@behemoth:/behemoth$ strings behemoth0 ⌨️
unixisbetterthanwindows
followthewhiterabbit
pacmanishighoncrack
Password:
%64s
Access granted..
/bin/sh
Access denied..
;*2$"
behemoth0@behemoth:/behemoth$ ./behemoth0 ⌨️
Password: unixisbetterthanwindows ⌨️
Access denied..
behemoth0@behemoth:/behemoth$ ./behemoth0 ⌨️
Password: followthewhiterabbit ⌨️
Access denied..
behemoth0@behemoth:/behemoth$ ./behemoth0 ⌨️
Password: pacmanishighoncrack ⌨️
Access denied..

# -------------------- Optional --------------------------------
# Optional: strace, was seeing what it did
behemoth0@behemoth:/behemoth$ strace ./behemoth0 ⌨️
execve("./behemoth0", ["./behemoth0"], 0x7fffffffe340 /* 28 vars */) = 0
[ Process PID=862165 runs in 32 bit mode. ]
brk(NULL)                               = 0x804c000
fcntl64(0, F_GETFD)                     = 0
fcntl64(1, F_GETFD)                     = 0
fcntl64(2, F_GETFD)                     = 0
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xf7fc1000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 3
statx(3, "", AT_STATX_SYNC_AS_STAT|AT_NO_AUTOMOUNT|AT_EMPTY_PATH, STATX_BASIC_STATS, {stx_mask=STATX_BASIC_STATS|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0644, stx_size=44095, ...}) = 0
mmap2(NULL, 44095, PROT_READ, MAP_PRIVATE, 3, 0) = 0xf7fb6000
close(3)                                = 0
openat(AT_FDCWD, "/lib/i386-linux-gnu/libc.so.6", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\3\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0\0O\2\0004\0\0\0"..., 512) = 512
statx(3, "", AT_STATX_SYNC_AS_STAT|AT_NO_AUTOMOUNT|AT_EMPTY_PATH, STATX_BASIC_STATS, {stx_mask=STATX_BASIC_STATS|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0755, stx_size=2313128, ...}) = 0
mmap2(NULL, 2341052, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xf7d7a000
mmap2(0xf7d9d000, 1601536, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x23000) = 0xf7d9d000
mmap2(0xf7f24000, 544768, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1aa000) = 0xf7f24000
mmap2(0xf7fa9000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x22f000) = 0xf7fa9000
mmap2(0xf7fac000, 39100, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xf7fac000
close(3)                                = 0
set_thread_area({entry_number=-1, base_addr=0xf7fc24c0, limit=0x0fffff, seg_32bit=1, contents=0, read_exec_only=0, limit_in_pages=1, seg_not_present=0, useable=1}) = 0 (entry_number=12)
set_tid_address(0xf7fc2528)             = 862165
set_robust_list(0xf7fc252c, 12)         = 0
rseq(0xf7fc2960, 0x20, 0, 0x53053053)   = 0
mprotect(0xf7fa9000, 8192, PROT_READ)   = 0
mprotect(0xf7ffb000, 8192, PROT_READ)   = 0
ugetrlimit(RLIMIT_STACK, {rlim_cur=8192*1024, rlim_max=RLIM_INFINITY}) = 0
munmap(0xf7fb6000, 44095)               = 0
statx(1, "", AT_STATX_SYNC_AS_STAT|AT_NO_AUTOMOUNT|AT_EMPTY_PATH, STATX_BASIC_STATS, {stx_mask=STATX_BASIC_STATS|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFCHR|0620, stx_size=0, ...}) = 0
getrandom("\xbd\xa9\x1b\xe8", 4, GRND_NONBLOCK) = 4
brk(NULL)                               = 0x804c000
brk(0x806d000)                          = 0x806d000
brk(0x806e000)                          = 0x806e000
statx(0, "", AT_STATX_SYNC_AS_STAT|AT_NO_AUTOMOUNT|AT_EMPTY_PATH, STATX_BASIC_STATS, {stx_mask=STATX_BASIC_STATS|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFCHR|0620, stx_size=0, ...}) = 0
write(1, "Password: ", 10Password: )              = 10
read(0, AAAAAAAAAAAAAAAAAA
"AAAAAAAAAAAAAAAAAA\n", 1024)   = 19
write(1, "Access denied..\n", 16Access denied..
)       = 16
_llseek(0, -1, 0xffffd220, SEEK_CUR)    = -1 ESPIPE (Illegal seek)
exit_group(0)                           = ?
+++ exited with 0 +++
# -------------------- Optional --------------------------------

behemoth0@behemoth:/behemoth$ ltrace ./behemoth0 ⌨️
__libc_start_main(0x80490fd, 1, 0xffffd454, 0 <unfinished ...>
printf("Password: ")                                                                      = 10
__isoc99_scanf(0x804a054, 0xffffd34f, 0x804a008, 0x804a020Password: AAAAAAAAAAAAAAAAAAAAA
)                               = 1
strlen("OK^GSYBEX^Y")👀                                                                   = 11
strcmp("AAAAAAAAAAAAAAAAAAAAA", "eatmyshorts"👀)                                          = -1
puts("Access denied.."Access denied..
)                                                                   = 16
+++ exited (status 0) +++
behemoth0@behemoth:/behemoth$ which ltrace ⌨️
/usr/bin/ltrace
behemoth0@behemoth:/behemoth$ ls -la /usr/bin/ltrace ⌨️
-rwxr-xr-x 1 root root 337392 Apr  1  2024 /usr/bin/ltrace
behemoth0@behemoth:/behemoth$ ./behemoth0 ⌨️
Password: eatmyshorts ⌨️
Access granted..
$ whoami ⌨️
behemoth1
$ cat /etc/behemoth_pass/behemoth1 ⌨️
8YpAQCAuKf 🔐

# Method2: gef
behemoth0@behemoth:/behemoth$ gef ./behemoth0 ⌨️
GNU gdb (Ubuntu 15.0.50.20240403-0ubuntu1) 15.0.50.20240403-git
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.ubuntu.com>
Enable debuginfod for this session? (y or [n]) y ⌨️
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Download failed: Permission denied.  Continuing without separate debug info for /behemoth/behemoth0.
(No debugging symbols found in ./behemoth0)
Error while writing index for `/behemoth/behemoth0': No debugging symbols
GEF for linux ready, type `gef' to start, `gef config' to configure
93 commands loaded and 5 functions added for GDB 15.0.50.20240403-git in 0.00ms using Python engine 3.12
gef➤  disassemble main ⌨️
Dump of assembler code for function main:
   0x0804920d <+0>:     push   ebp
   0x0804920e <+1>:     mov    ebp,esp
   0x08049210 <+3>:     push   ebx
   0x08049211 <+4>:     sub    esp,0x60
   0x08049214 <+7>:     mov    eax,gs:0x14
   0x0804921a <+13>:    mov    DWORD PTR [ebp-0x8],eax
   0x0804921d <+16>:    xor    eax,eax
   0x0804921f <+18>:    mov    DWORD PTR [ebp-0x55],0x475e4b4f
   0x08049226 <+25>:    mov    DWORD PTR [ebp-0x51],0x45425953
   0x0804922d <+32>:    mov    DWORD PTR [ebp-0x4d],0x595e58
   0x08049234 <+39>:    mov    DWORD PTR [ebp-0x64],0x804a008
   0x0804923b <+46>:    mov    DWORD PTR [ebp-0x60],0x804a020
   0x08049242 <+53>:    mov    DWORD PTR [ebp-0x5c],0x804a035
   0x08049249 <+60>:    push   0x804a049
   0x0804924e <+65>:    call   0x8049050 <printf@plt>
   0x08049253 <+70>:    add    esp,0x4
   0x08049256 <+73>:    lea    eax,[ebp-0x49]
   0x08049259 <+76>:    push   eax
   0x0804925a <+77>:    push   0x804a054
   0x0804925f <+82>:    call   0x80490c0 <__isoc99_scanf@plt>
   0x08049264 <+87>:    add    esp,0x8
   0x08049267 <+90>:    lea    eax,[ebp-0x55]
   0x0804926a <+93>:    push   eax
   0x0804926b <+94>:    call   0x80490b0 <strlen@plt>
   0x08049270 <+99>:    add    esp,0x4
   0x08049273 <+102>:   push   eax
   0x08049274 <+103>:   lea    eax,[ebp-0x55]
   0x08049277 <+106>:   push   eax
   0x08049278 <+107>:   call   0x80491e6 <memfrob>
   0x0804927d <+112>:   add    esp,0x8
   0x08049280 <+115>:   lea    eax,[ebp-0x55]
   0x08049283 <+118>:   push   eax
   0x08049284 <+119>:   lea    eax,[ebp-0x49]
   0x08049287 <+122>:   push   eax
   0x08049288 <+123>:   call   0x8049030 <strcmp@plt> 👀
   0x0804928d <+128>:   add    esp,0x8
   0x08049290 <+131>:   test   eax,eax
   0x08049292 <+133>:   jne    0x80492c6 <main+185>
   0x08049294 <+135>:   push   0x804a059
   0x08049299 <+140>:   call   0x8049080 <puts@plt>
   0x0804929e <+145>:   add    esp,0x4
   0x080492a1 <+148>:   call   0x8049070 <geteuid@plt>
   0x080492a6 <+153>:   mov    ebx,eax
   0x080492a8 <+155>:   call   0x8049070 <geteuid@plt>
   0x080492ad <+160>:   push   ebx
   0x080492ae <+161>:   push   eax
   0x080492af <+162>:   call   0x80490a0 <setreuid@plt>
   0x080492b4 <+167>:   add    esp,0x8
   0x080492b7 <+170>:   push   0x804a06a
   0x080492bc <+175>:   call   0x8049090 <system@plt>
   0x080492c1 <+180>:   add    esp,0x4
   0x080492c4 <+183>:   jmp    0x80492d3 <main+198>
   0x080492c6 <+185>:   push   0x804a072
   0x080492cb <+190>:   call   0x8049080 <puts@plt>
   0x080492d0 <+195>:   add    esp,0x4
   0x080492d3 <+198>:   mov    eax,0x0
   0x080492d8 <+203>:   mov    edx,DWORD PTR [ebp-0x8]
   0x080492db <+206>:   sub    edx,DWORD PTR gs:0x14
   0x080492e2 <+213>:   je     0x80492e9 <main+220>
   0x080492e4 <+215>:   call   0x8049060 <__stack_chk_fail@plt>
   0x080492e9 <+220>:   mov    ebx,DWORD PTR [ebp-0x4]
   0x080492ec <+223>:   leave
   0x080492ed <+224>:   ret
End of assembler dump.
gef➤  break *0x08049288 ⌨️
Breakpoint 1 at 0x8049288
gef➤  run ⌨️
Starting program: /behemoth/behemoth0
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Password: AAAAAA ⌨️
2 ────
    0x8049283 <main+0076>      push   eax
    0x8049284 <main+0077>      lea    eax, [ebp-0x49]
    0x8049287 <main+007a>      push   eax
●→  0x8049288 <main+007b>      call   0x8049030 <strcmp@plt>
   ↳   0x8049030 <strcmp@plt+0000> jmp    DWORD PTR ds:0x804b27c
       0x8049036 <strcmp@plt+0006> push   0x0
       0x804903b <strcmp@plt+000b> jmp    0x8049020
       0x8049040 <__libc_start_main@plt+0000> jmp    DWORD PTR ds:0x804b280
       0x8049046 <__libc_start_main@plt+0006> push   0x8
       0x804904b <__libc_start_main@plt+000b> jmp    0x8049020
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── arguments (guessed
) ────
strcmp@plt (
   [sp + 0x0] = 0xffffd32f → "AAAAAA",
   [sp + 0x4] = 0xffffd323 → "eatmyshorts" 👀
)

# Method 3: CyberChef
behemoth0@behemoth:/behemoth$ gef behemoth0 ⌨️
behemoth0@behemoth:/behemoth$ whatis memfrob ⌨️
memfrob (3)          - frobnicate (obfuscate) a memory area
behemoth0@behemoth:/behemoth$ man memfrob ⌨️
gef➤  disassemble main ⌨️
Dump of assembler code for function main:
   0x0804920d <+0>:     push   ebp
   0x0804920e <+1>:     mov    ebp,esp
   0x08049210 <+3>:     push   ebx
   0x08049211 <+4>:     sub    esp,0x60
   0x08049214 <+7>:     mov    eax,gs:0x14
   0x0804921a <+13>:    mov    DWORD PTR [ebp-0x8],eax        
   0x0804921d <+16>:    xor    eax,eax
   0x0804921f <+18>:    mov    DWORD PTR [ebp-0x55],0x475e4b4f
   0x08049226 <+25>:    mov    DWORD PTR [ebp-0x51],0x45425953
   0x0804922d <+32>:    mov    DWORD PTR [ebp-0x4d],0x595e58  
   0x08049234 <+39>:    mov    DWORD PTR [ebp-0x64],0x804a008 
   0x0804923b <+46>:    mov    DWORD PTR [ebp-0x60],0x804a020
   0x08049242 <+53>:    mov    DWORD PTR [ebp-0x5c],0x804a035
   0x08049249 <+60>:    push   0x804a049
   0x0804924e <+65>:    call   0x8049050 <printf@plt>
   0x08049253 <+70>:    add    esp,0x4
   0x08049256 <+73>:    lea    eax,[ebp-0x49]
   0x08049259 <+76>:    push   eax
   0x0804925a <+77>:    push   0x804a054
   0x0804925f <+82>:    call   0x80490c0 <__isoc99_scanf@plt>
   0x08049264 <+87>:    add    esp,0x8
   0x08049267 <+90>:    lea    eax,[ebp-0x55]
   0x0804926a <+93>:    push   eax
   0x0804926b <+94>:    call   0x80490b0 <strlen@plt>
   0x08049270 <+99>:    add    esp,0x4
   0x08049273 <+102>:   push   eax
   0x08049274 <+103>:   lea    eax,[ebp-0x55]
   0x08049277 <+106>:   push   eax
   0x08049278 <+107>:   call   0x80491e6 <memfrob>
   0x0804927d <+112>:   add    esp,0x8
   0x08049280 <+115>:   lea    eax,[ebp-0x55]
   0x08049283 <+118>:   push   eax
   0x08049284 <+119>:   lea    eax,[ebp-0x49]
   0x08049287 <+122>:   push   eax
   0x08049288 <+123>:   call   0x8049030 <strcmp@plt>
   0x0804928d <+128>:   add    esp,0x8
   0x08049290 <+131>:   test   eax,eax
   0x08049292 <+133>:   jne    0x80492c6 <main+185>
   0x08049294 <+135>:   push   0x804a059
   0x08049299 <+140>:   call   0x8049080 <puts@plt>
   0x0804929e <+145>:   add    esp,0x4
   0x080492a1 <+148>:   call   0x8049070 <geteuid@plt>
   0x080492a6 <+153>:   mov    ebx,eax
   0x080492a8 <+155>:   call   0x8049070 <geteuid@plt>
   0x080492ad <+160>:   push   ebx
   0x080492ae <+161>:   push   eax
   0x080492af <+162>:   call   0x80490a0 <setreuid@plt>
   0x080492b4 <+167>:   add    esp,0x8
   0x080492b7 <+170>:   push   0x804a06a
   0x080492bc <+175>:   call   0x8049090 <system@plt>
   0x080492c1 <+180>:   add    esp,0x4
   0x080492c4 <+183>:   jmp    0x80492d3 <main+198>
   0x080492c6 <+185>:   push   0x804a072
   0x080492cb <+190>:   call   0x8049080 <puts@plt>
   0x080492d0 <+195>:   add    esp,0x4
   0x080492d3 <+198>:   mov    eax,0x0
   0x080492d8 <+203>:   mov    edx,DWORD PTR [ebp-0x8]
   0x080492db <+206>:   sub    edx,DWORD PTR gs:0x14
   0x080492e2 <+213>:   je     0x80492e9 <main+220>
   0x080492e4 <+215>:   call   0x8049060 <__stack_chk_fail@plt>
   0x080492e9 <+220>:   mov    ebx,DWORD PTR [ebp-0x4]
   0x080492ec <+223>:   leave
   0x080492ed <+224>:   ret
End of assembler dump.
gef➤  break *main+107 ⌨️
Breakpoint 1 at 0x8049278
gef➤  run ⌨️
Starting program: /behemoth/behemoth0 
Download failed: Permission denied.  Continuing without separate debug info for system-supplied DSO at 0xf7fc7000.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Password: AAAA
s ────
memfrob (
   DWORD var_0 = 0xffffd323 → "OK^GSYBEX^Y",
   size_t var_1 = 0x0000000b
)
Solution: https://cyberchef.io/#recipe=XOR(%7B'option':'Decimal','string':'42'%7D,'Standard',false)&input=T0teR1NZQkVYXlk

Method 4: radare2
behemoth0@behemoth:/behemoth$ r2 ./behemoth0 ⌨️
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
 -- I thought we were friends. :_
[0x080490d0]> aaaa ⌨️
INFO: Analyze all flags starting with sym. and entry0 (aa)
INFO: Analyze imports (af@@@i)
INFO: Analyze entrypoint (af@ entry0)
INFO: Analyze symbols (af@@@s)
INFO: Analyze all functions arguments/locals (afva@@@F)
INFO: Analyze function calls (aac)
INFO: Analyze len bytes of instructions for references (aar)
INFO: Finding and parsing C++ vtables (avrr)
INFO: Analyzing methods (af @@ method.*)
INFO: Recovering local variables (afva@@@F)
INFO: Type matching analysis for all functions (aaft)
INFO: Propagate noreturn information (aanr)
INFO: Scanning for strings constructed in code (/azs)
INFO: Finding function preludes (aap)
INFO: Enable anal.types.constraint for experimental type propagation
[0x080490d0]> afl ⌨️                                          # Analyze Function List
0x08049030    1      6 sym.imp.strcmp
0x08049040    1      6 sym.imp.__libc_start_main
0x08049050    1      6 sym.imp.printf
0x08049060    1      6 sym.imp.__stack_chk_fail
0x08049070    1      6 sym.imp.geteuid
0x08049080    1      6 sym.imp.puts
0x08049090    1      6 sym.imp.system
0x080490a0    1      6 sym.imp.setreuid
0x080490b0    1      6 sym.imp.strlen
0x080490c0    1      6 sym.imp.__isoc99_scanf
0x080490d0    1     40 entry0
0x080490f9    1      4 fcn.080490f9
0x080491e6    4     39 sym.memfrob
0x08049130    4     40 sym.deregister_tm_clones
0x08049170    4     53 sym.register_tm_clones
0x080491b0    3     34 entry.fini0
0x080491e0    1      6 entry.init0
0x08049120    1      4 sym.__x86.get_pc_thunk.bx
0x080492f0    1     20 sym._fini
0x08049110    1      1 sym._dl_relocate_static_pie
0x0804920d    6    225 main
0x08049000    3     32 sym._init
[0x080490d0]> sf main ⌨️                                   # Select Function main
[0x0804920d]> pdf ⌨️                                       # Print Disassemble Function
            ; CODE XREF from loc.__wrap_main @ 
┌ 225: int main (int argc, char **argv, char **envp);
│ afv: vars(9:sp[0x8..0x68])
│           0x0804920d      55             push ebp
│           0x0804920e      89e5           mov ebp, esp
│           0x08049210      53             push ebx
│           0x08049211      83ec60         sub esp, 0x60
│           0x08049214      65a114000000   mov eax, dword gs:[0x14]
│           0x0804921a      8945f8         mov dword [canary], eax
│           0x0804921d      31c0           xor eax, eax
│           0x0804921f      c745ab4f4b..   mov dword [s2], 0x475e4b4f  ; 'OK^G' ; string "OKGSYBEXY"
│           0x08049226      c745af5359..   mov dword [var_51h], 0x45425953 ; 'SYBE'
│           0x0804922d      c745b3585e..   mov dword [var_4dh], 0x595e58 ; 'X^Y'
│           0x08049234      c7459c08a0..   mov dword [var_64h], str.unixisbetterthanwindows ; 0x804a008 ; "unixisbetterthanwindows"
│           0x0804923b      c745a020a0..   mov dword [var_60h], str.followthewhiterabbit ; 0x804a020 ; "followthewhiterabbit"
│           0x08049242      c745a435a0..   mov dword [var_5ch], str.pacmanishighoncrack ; 0x804a035 ; "pacmanishighoncrack"
│           0x08049249      6849a00408     push str.Password:          ; 0x804a049 ; "Password: "
│           0x0804924e      e8fdfdffff     call sym.imp.printf         ; int printf(const char *format)
│           0x08049253      83c404         add esp, 4
│           0x08049256      8d45b7         lea eax, [s1]
│           0x08049259      50             push eax
│           0x0804925a      6854a00408     push str._64s               ; 0x804a054 ; "%64s"
│           0x0804925f      e85cfeffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x08049264      83c408         add esp, 8
│           0x08049267      8d45ab         lea eax, [s2]
│           0x0804926a      50             push eax                    ; const char *s
│           0x0804926b      e840feffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│           0x08049270      83c404         add esp, 4
│           0x08049273      50             push eax                    ; int32_t arg_ch
│           0x08049274      8d45ab         lea eax, [s2]
│           0x08049277      50             push eax                    ; int32_t arg_8h
│           0x08049278      e869ffffff     call sym.memfrob
│           0x0804927d      83c408         add esp, 8
│           0x08049280      8d45ab         lea eax, [s2]
│           0x08049283      50             push eax                    ; const char *s2
│           0x08049284      8d45b7         lea eax, [s1]
│           0x08049287      50             push eax                    ; const char *s1
│           0x08049288      e8a3fdffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
│           0x0804928d      83c408         add esp, 8
│           0x08049290      85c0           test eax, eax
│       ┌─< 0x08049292      7532           jne 0x80492c6
│       │   0x08049294      6859a00408     push str.Access_granted..   ; 0x804a059 ; "Access granted.."
│       │   0x08049299      e8e2fdffff     call sym.imp.puts           ; int puts(const char *s)
│       │   0x0804929e      83c404         add esp, 4
│       │   0x080492a1      e8cafdffff     call sym.imp.geteuid        ; uid_t geteuid(void)
│       │   0x080492a6      89c3           mov ebx, eax
│       │   0x080492a8      e8c3fdffff     call sym.imp.geteuid        ; uid_t geteuid(void)
│       │   0x080492ad      53             push ebx
│       │   0x080492ae      50             push eax
│       │   0x080492af      e8ecfdffff     call sym.imp.setreuid
│       │   0x080492b4      83c408         add esp, 8
│       │   0x080492b7      686aa00408     push str._bin_sh            ; 0x804a06a ; "/bin/sh"
│       │   0x080492bc      e8cffdffff     call sym.imp.system         ; int system(const char *string)
│       │   0x080492c1      83c404         add esp, 4
│      ┌──< 0x080492c4      eb0d           jmp 0x80492d3
│      ││   ; CODE XREF from main @ 0x8049292(x)
│      │└─> 0x080492c6      6872a00408     push str.Access_denied..    ; 0x804a072 ; "Access denied.."
│      │    0x080492cb      e8b0fdffff     call sym.imp.puts           ; int puts(const char *s)
│      │    0x080492d0      83c404         add esp, 4
│      │    ; CODE XREF from main @ 0x80492c4(x)
│      └──> 0x080492d3      b800000000     mov eax, 0
│           0x080492d8      8b55f8         mov edx, dword [canary]
│           0x080492db      652b151400..   sub edx, dword gs:[0x14]
│       ┌─< 0x080492e2      7405           je 0x80492e9
│       │   0x080492e4      e877fdffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from main @ 0x80492e2(x)
│       └─> 0x080492e9      8b5dfc         mov ebx, dword [var_4h]
│           0x080492ec      c9             leave
└           0x080492ed      c3             ret
[0x0804920d]> VV ⌨️
```

## Flag
<b>8YpAQCAuKf</b>

## Continue
[Continue](./Behemoth0001.md)