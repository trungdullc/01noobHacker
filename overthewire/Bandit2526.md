# Bandit Level 25 → Level 26 Breaking out of a restricted environment with more and vim and SUID Binary

## Previous Flag
<b>s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ</b>, not really used could be used to log in bandit26 but kicked out

## Goal
You are already log in as bandit26. Now hurry and grab the password for bandit27!

## What I learned
```
Nothing was review
```

## Solution
```
bandit26@bandit:~$ ls ⌨️
bandit27-do  text.txt
bandit26@bandit:~$ cat text.txt ⌨️ 
  _                     _ _ _   ___   __  
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \ 
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/ 
bandit26@bandit:~$ file bandit27-do ⌨️
bandit27-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=35d353cf6d732f515a73f50ed205265fe1e68f90, for GNU/Linux 3.2.0, not stripped
bandit26@bandit:~$ ./bandit27-do ⌨️
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27 ⌨️
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB 🔐
```

## Flag
<b>upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB</b>

## Continue
[Continue](/overthewire/Bandit2627.md)