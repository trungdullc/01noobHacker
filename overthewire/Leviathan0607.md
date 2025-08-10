# Leviathan Level 6 → Level 7

## Previous Flag
<b>qEs5Io5yM8</b>

## Goal
Use previous password to log in SSH with user <b>leviathan7</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org to see if password correct. Level 8 does not exist.

## What I learned
```
Nothing
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh leviathan6@leviathan.labs.overthewire.org -p 2223 ⌨️
leviathan7@leviathan:~$ ls -la
total 24
drwxr-xr-x   2 root       root       4096 Jul 28 19:05 .
drwxr-xr-x 150 root       root       4096 Jul 28 19:06 ..
-rw-r--r--   1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root       3851 Jul 28 18:47 .bashrc
-r--r-----   1 leviathan7 leviathan7  178 Jul 28 19:05 CONGRATULATIONS 👀
-rw-r--r--   1 root       root        807 Mar 31  2024 .profile
leviathan7@leviathan:~$ file CONGRATULATIONS ⌨️
CONGRATULATIONS: ASCII text
leviathan7@leviathan:~$ cat CONGRATULATIONS ⌨️
Well Done, you seem to have used a *nix system before, now try something more serious.
(Please don't post writeups, solutions or spoilers about the games on the web. Thank you!)
```

## Flag
N/A

## Continue
[Continue](./Krypton0001.md)