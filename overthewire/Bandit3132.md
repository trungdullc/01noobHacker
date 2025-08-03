# Bandit Level 31 → Level 32 Git Push, Commit, Ignore, Add

## Previous Flag
<b>3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K</b>

## Goal
Use previous password to log in SSH with user <b>bandit32</b> on port <b>2220</b>. After all this git stuff, it’s time for another escape. Good luck!

## What I learned
```
printenv

Local Variables
TERM          current terminal emulation
HOME          path to home directory of currently logged in user
LANG          current locales settings
PATH          directory list to be searched when executing commands
PWD           pathname of the current working directory
SHELL/0       path of the current user’s shell
USER          currently logged-in user
```

## Side Quest
```
In Unix/Linux, a user's shell is stored in /etc/passwd but we replace w/ uppershell program
  bandit32:x:1032:1032:bandit level 32:/home/bandit32:/home/bandit32/uppershell

# uppershell.c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main() {
    while (1) {
        char input[256];
        printf(">> ");
        if (fgets(input, sizeof(input), stdin) == NULL) break;

        // Strip newline
        input[strcspn(input, "\n")] = 0;

        // Convert to uppercase
        for (int i = 0; input[i]; i++) {
            input[i] = toupper((unsigned char)input[i]);
        }

        system(input);
    }
    return 0;
}

gcc uppershell.c -o uppershell
chmod +x uppershell
./uppershell                                  // Run and test before place shortcut
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit32@bandit.labs.overthewire.org -p 2220 ⌨️
WELCOME TO THE UPPERCASE SHELL
>> ls ⌨️
sh: 1: LS: Permission denied
>> $SHELL ⌨️
WELCOME TO THE UPPERCASE SHELL
>> $0 ⌨️
$ ls ⌨️
uppershell
$ file uppershell ⌨️
uppershell: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=306348187b23d7a25b64c4b18058180fe4cbc81e, for GNU/Linux 3.2.0, not stripped
$ cat /etc/bandit_pass/bandit33 ⌨️
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0 🔐
```

## Flag
<b>tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0</b>

## Continue
[Continue](/overthewire/Bandit3233.md)