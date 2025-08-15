# Krypton Level 6 → Level 7

## Previous Flag
<b>LFSRISNOTRANDOM</b>

## Goal
Use previous password to log in to <b>krypton.labs.overthewire.org</b> with username <b>krypton7</b> using SSH on <b>port 2231</b> to see if password correct. Level 8 does not exist.

## What I learned
```
Nothing
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh krypton7@krypton.labs.overthewire.org -p 2231 ⌨️
krypton7@krypton:~$ cd /krypton/krypton7 ⌨️
krypton7@krypton:/krypton/krypton7$ ls -la ⌨️
total 12
drwxr-xr-x 2 root     root     4096 Jul 28 19:05 .     
drwxr-xr-x 9 root     root     4096 Jul 28 19:05 ..    
-rw-r----- 1 krypton7 krypton7   36 Jul 28 19:05 README
krypton7@krypton:/krypton/krypton7$ cat README ⌨️
Congratulations on beating Krypton!
```

## Flag
N/A

## Continue
[Continue](./Narnia0000.md)