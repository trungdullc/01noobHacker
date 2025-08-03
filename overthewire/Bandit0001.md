# Bandit Level 0 → Level 1 Read a File

## Previous Flag
<b>ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If</b>

## Goal
Use previous password to log in SSH with user <b>bandit1</b> and port <b>2220</b>.  Password stored in file called - located in the home directory.

## What I learned
```
$HOME same as ~
file tells what type is it directory or not
3 ways to cat a special char file name
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit1@bandit.labs.overthewire.org -p 2220 ⌨️
bandit1@bandit:~$ whatis cd ls file ⌨️
ls (1)               - list directory contents
FILE (3type)         - input/output stream
file (1)             - determine file type
cd: nothing appropriate.
bandit1@bandit:~$ cd $HOME ⌨️
bandit1@bandit:~$ cd ~ ⌨️
bandit1@bandit:~$ ls ⌨️
-
bandit1@bandit:~$ ls -la ⌨️
total 24
-rw-r-----  1 bandit2 bandit1   33 Apr 10 14:23 -
drwxr-xr-x  2 root    root    4096 Apr 10 14:23 .
drwxr-xr-x 70 root    root    4096 Apr 10 14:24 ..
-rw-r--r--  1 root    root     807 Mar 31  2024 .profile
bandit1@bandit:~$ file - ⌨️
 
/dev/stdin: very short file (no magic)
bandit1@bandit:~$ cat ./- ⌨️
263JGJPfgU6LtdEvgfWU1XP5yac29mFx 🔐
bandit1@bandit:~$ cat /home/bandit1/- ⌨️
263JGJPfgU6LtdEvgfWU1XP5yac29mFx 🔐
bandit1@bandit:~$ cat ~/- ⌨️
263JGJPfgU6LtdEvgfWU1XP5yac29mFx 🔐
```

## Flag
<b>263JGJPfgU6LtdEvgfWU1XP5yac29mFx</b>

## Continue
[Continue](/overthewire/Bandit0102.md)