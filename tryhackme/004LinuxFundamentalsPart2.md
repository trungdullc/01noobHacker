# Linux Fundamentals Part 2
```bash
Secure Shell or SSH simply is a protocol between devices in an encrypted form. Using cryptography. any input we send in a human-readable format is encrypted for travelling over a network — where it is then unencrypted once it reaches the remote machine, such as in the diagram below.

        My Computer (AttackBox)         The Internet                    Linux Server (Start Machine)
        <==========================================================================>
        Hello World                     f6b97e414ac8a5                  Hello World

# Start Machine (Victim)
    Add 1 hour
    Terminate

tryhackme@linux2:~$ ifconfig ⌨️
inet 10.0.3.5

# Start AttackBox
AttackBox:
root@ip-10.0.3.4:~# ifconfig ⌨️
inet 10.0.3.4
root@ip-10.0.3.4:~# ssh tryhackme@10.0.3.5 ⌨️
The authenticity of host '10.0.3.5 (10.0.3.5)' can't be estabished.
ECDSA key fingerprint is SHA256:0x0w0edamthathardpassFR08jum.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.0.3.5' (ECDSA) to the list of known hosts.
tryhackme@10.0.3.5's password: tryhackme ⌨️
tryhackme@linux2:~$
```

# Task 3: Introduction to Flags and Switches
```bash
tryhackme@linux2:~$ man ls ⌨️
tryhackme@linux2:~$ ls --help ⌨️                     # ls -h
tryhackme@linux2:~$ ls -all ⌨️                        # ls -a
```

# Task 4: Filesystems Interaction Continued
```bash
tryhackme@linux2:~$ touch note
tryhackme@linux2:~$ mkdir mydirectory
tryhackme@linux2:~$ file note
note: ASCII text
tryhackme@linux2:~$ cp note note2
tryhackme@linux2:~$ mv note2 renamed3
tryhackme@linux2:~$ rm note
tryhackme@linux2:~$ rm mydirectory
rm: cannot remove 'mydirectory': Is a directory
tryhackme@linux2:~$ rm -R mydirectory                   # rm -rf mydirectory (rm all)
```

# Task 5: Permissions 101
```bash
-rwxrwxrwx
    directory
    user
    group
    others

SUID (Set User ID)
    Note: see s in user execution
SGID (Set Group ID)
    Note: see s in group execution
# Find SUID binaries
find / -perm -4000 2>/dev/null
# Find SGID binaries
find / -perm -2000 2>/dev/null

# Switches uses w/ su                       # substitute user
tryhackme@linux2:~$ su user2                # su defaults to root, su -
Password:                                   # Note: switch user kinda useless w/o login
user2@linux2:~$ pwd
/home/user2
tryhackme@linux2:~$ su -l user2             # sudo --login
Password:

# Important Linux Folders
    /etc/passwd
    /etc/sudoers
visudo -f /etc/sudoers.d/custom             # Important: vim/nano can crash sudo if syntax error

# extra sudoers rules
ls -l /etc/sudoers.d/
# Exploit via GTFOBins:
sudo vim -c ':!/bin/bash'
```

# Task 6: Common Directories
```bash
/etc                                        # system file used by OS
    /passwd                                 # encrypted sha512 pass
    /shadow                                 # encrpyted sha512 pass
    /sudoers
    /hosts                                  # localhost
/var                                        # variable data, services/application write here
    /log
/root                                       # home for root user
/tmp                                        # volatile, once computer restart deleted auto

Q: What root directory is similar to how RAM on a computer works?
/tmp
```