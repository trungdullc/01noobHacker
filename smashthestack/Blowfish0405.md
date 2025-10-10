# Blowfish Level 04 → 05

## Previous Flag
```
n3xt_l3v3l!
```

## Goal


## What I learned
```

```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa -l level4 blowfish.smashthestack.org -p 2222 ⌨️
level4@blowfish.smashthestack.org's password: ⌨️ n3xt_l3v3l!
level4@blowfish:~$ ls
exploit_level4.py  README
level4@blowfish:~$ cat README 
There is a buffer overflow in /levels/level4 exploit it and move on to the next level!

level4@blowfish:~$ cd /levels/
level4@blowfish:/levels$ ls
level10  level12    level13    level4    level5    level6    level7    level8    level9
level11  level12.c  level13.c  level4.c  level5.c  level6.c  level7.c  level8.c  tmp
level4@blowfish:/levels$ file level4
level4: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.2.0, not stripped
level4@blowfish:/levels$ cat level4.c
#include <stdio.h>

int main(int argc, char * argv[]) {

char buf[256];

if(argc == 1) {
printf("Usage: %s input\n", argv[0]);
exit(0);
}

strcpy(buf,argv[1]); 👀 unsafe
printf("%s", buf);

}

level4@blowfish:/levels$ gdb -q ./level4
(gdb) run python3 -c 'print("A"*280 + "BBBB", end="")'
Starting program: /levels/level4 python3 -c 'print("A"*280 + "BBBB", end="")'
python3
Program exited with code 07.
(gdb)  run `perl -e ‘print “A”x275,”BBBB”‘`
Starting program: /levels/level4 `perl -e ‘print “A”x275,”BBBB”‘`
Unrecognized character \xE2 in column 1 at -e line 1.
Usage: /levels/level4 input

Program exited normally.
```

## Flag


## Continue
[Continue](./Blowfish0506.md)