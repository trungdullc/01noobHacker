# Narnia Level 8 → Level 9

## Previous Flag
<b>1FFD4HnU4K</b>

## Goal
Use previous password to log in SSH with user <b>narnia9</b> and port <b>2226</b> accessed on narnia.labs.overthewire.org to see if password correct. Level 10 does not exist.

## What I learned
```
Nothing
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh narnia9@narnia.labs.overthewire.org -p 2226 ⌨️
narnia9@narnia:~$ ls -la
total 24
drwxr-xr-x   2 root    root    4096 Jul 28 19:06 .
drwxr-xr-x 150 root    root    4096 Jul 28 19:06 ..
-rw-r--r--   1 root    root     220 Mar 31  2024 .bash_logout   
-rw-r--r--   1 root    root    3851 Jul 28 18:47 .bashrc        
-r--r-----   1 narnia9 narnia9  118 Jul 28 19:06 CONGRATULATIONS 👀
-rw-r--r--   1 root    root     807 Mar 31  2024 .profile
narnia9@narnia:~$ cat CONGRATULATIONS
you are l33t! next plz...

(Please don't post writeups, solutions or spoilers about the games on the web. Thank you!)
```

## Flag
N/A

## Continue
[Continue](./Behemoth0000.md)