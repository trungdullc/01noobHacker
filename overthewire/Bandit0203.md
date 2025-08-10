# Bandit Level 2 → Level 3 Hidden Files

## Previous Flag
<b>MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx</b>

## Goal
Use previous password to log in SSH with user <b>bandit3</b> on port <b>2220</b>.  Password for next level is stored in a hidden file in <b>inhere</b> directory.

## What I learned
```
cd to change directory
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit3@bandit.labs.overthewire.org -p 2220 ⌨️
bandit3@bandit:~$ ls ⌨️
inhere
bandit3@bandit:~$ cd inhere/ ⌨️
bandit3@bandit:~/inhere$ ls -la ⌨️
total 12
drwxr-xr-x 2 root    root    4096 Apr 10 14:23 .
drwxr-xr-x 3 root    root    4096 Apr 10 14:23 ..
-rw-r----- 1 bandit4 bandit3   33 Apr 10 14:23 ...Hiding-From-You 👀
bandit3@bandit:~/inhere$ cat ...Hiding-From-You ⌨️
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ 🔐
```

## Flag
<b>2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ</b>

## Continue
[Continue](./Bandit0304.md)