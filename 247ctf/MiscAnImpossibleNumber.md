# Misc: An Impossible Number

## Previous Flag
```
247CTF{c69287be15653ac9ab47dcd3f2fcd8fa}
```

## Goal
Can you think of a number which at the same time is one more than itself?

## What I learned
```
ChatGPT: answer: 2147483647 (INT_MAX on a 32-bit int)
impossible_number + 1 overflows and — on common two’s-complement implementations where signed overflow wraps — becomes INT_MIN (a large negative)
2147483647 > -2147483648
```

## Solution
```
DOWNLOAD CHALLENGE

AsianHacker-picoctf@webshell:~$ rz ⌨️
AsianHacker-picoctf@webshell:~$ ls ⌨️
26a4ffbf6fb2d2d01d70b92cef36e92222906e3c.zip  README.txt
AsianHacker-picoctf@webshell:~$ unzip 26a4ffbf6fb2d2d01d70b92cef36e92222906e3c.zip  ⌨️
Archive:  26a4ffbf6fb2d2d01d70b92cef36e92222906e3c.zip
  inflating: impossible_number.c     
AsianHacker-picoctf@webshell:~$ ls ⌨️
26a4ffbf6fb2d2d01d70b92cef36e92222906e3c.zip  README.txt  impossible_number.c ⌨️
AsianHacker-picoctf@webshell:~$ rm 26a4ffbf6fb2d2d01d70b92cef36e92222906e3c.zip ⌨️
AsianHacker-picoctf@webshell:~$ cat impossible_number.c ⌨️
#include <stdio.h>
int main() {
    int impossible_number;
    FILE *flag;
    char c;
    if (scanf("%d", &impossible_number)) {
        if (impossible_number > 0 && impossible_number > (impossible_number + 1)) {
            flag = fopen("flag.txt","r"); 👀
            while((c = getc(flag)) != EOF) {
                printf("%c",c);
            }
        }
    }
    return 0;
}

START CHALLENGE

tcp://ba21b18d81f622e9.247ctf.com:50340

# Note: telnet not work on virtual machinese
AsianHacker-picoctf@webshell:~$ telnet ba21b18d81f622e9.247ctf.com 50340 ⌨️
Trying 144.76.74.118...
2147483647 ⌨️

# Open on Kali Linux
┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> nc ba21b18d81f622e9.247ctf.com 50340 ⌨️
2147483647 ⌨️
247CTF{38f5daf742a4b3d74b3a7575bf4d7d1e} 🔐
```

## Flag
247CTF{38f5daf742a4b3d74b3a7575bf4d7d1e}

## Continue
[Continue](../247ctf/MiscTheFlagLottery.md)