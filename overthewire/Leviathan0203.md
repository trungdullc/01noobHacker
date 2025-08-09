# Leviathan Level 2 → Level 3 ltrance and setuid root binaries

## Previous Flag
<b>f0n8h2iWLP</b>

## Goal
Use previous password to log in SSH with user <b>leviathan3</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org
Du Hint: Use binary file to gain access to /etc/leviathan_pass/leviathan4 w/ setuid vulnerability

## What I learned
```
Review of previous material
```

## Side Quest
```
# setuid_shell.cpp
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <unistd.h>

int main() {
    // Simulated "password"
    const char* correct = "pikachu";
    char input[256];

    std::cout << "Enter the password> ";
    std::cin.getline(input, sizeof(input));

    if (strcmp(input, correct) == 0) {
        std::cout << "[Access Granted - Spawning shell]\n";

        // Drop into a shell (keeps effective UID if setuid bit is set)
        execl("/bin/sh", "sh", (char *)nullptr);
    } else {
        std::cout << "Wrong password!\n";
    }

    return 0;
}

g++ setuid_shell.cpp -o myprogram
# Make it owned by another user (user2) and set setuid bit
sudo chown user2:user2 myprogram
sudo chmod u+s myprogram
# Switch to a lower-privileged user (e.g., user1) and run it
su user1
./myprogram
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh leviathan3@leviathan.labs.overthewire.org -p 2223 ⌨️
leviathan3@leviathan:~$ ls -la ⌨️
total 40
drwxr-xr-x   2 root       root        4096 Jul 28 19:05 .
drwxr-xr-x 150 root       root        4096 Jul 28 19:06 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Jul 28 18:47 .bashrc     
-r-sr-x---   1 leviathan4 leviathan3 18100 Jul 28 19:05 level3      
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile
leviathan3@leviathan:~$ file level3 ⌨️
level3: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=5f6860c1ad35cc89c2397be07b3684c8b6222d84, for GNU/Linux 3.2.0, with debug_info, not stripped
leviathan3@leviathan:~$ ./level3 ⌨️
Enter the password> hi ⌨️
bzzzzzzzzap. WRONG  
leviathan3@leviathan:~$ ltrace ./level3 ⌨️ 
__libc_start_main(0x80490ed, 1, 0xffffd464, 0 <unfinished ...>
strcmp("h0no33", "kakaka")                                                             = -1
printf("Enter the password> ")                                                         = 20
fgets(Enter the password> hi ⌨️
"hi\n", 256, 0xf7fab5c0)                                                         = 0xffffd23c
strcmp("hi\n", "snlprintf\n") 👀                                                       = -1  
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                                             = 19
+++ exited (status 0) +++
leviathan3@leviathan:~$ ./level3 ⌨️
Enter the password> snlprintf ⌨️
[You've got shell]!
$ whoami ⌨️
leviathan4
$ cat /etc/leviathan_pass/leviathan4 ⌨️
WG1egElCvO 🔐
$ exit
leviathan3@leviathan:~$ exit ⌨️
logout
Connection to leviathan.labs.overthewire.org closed.
```

## Flag
<b>WG1egElCvO</b>

## Continue
[Continue](/overthewire/Leviathan0304.md)