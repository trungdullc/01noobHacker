# picoGym Level 0347: chrono
Source: https://play.picoctf.org/practice/challenge/347

## Goal
How to automate tasks to run at intervals on linux servers?<br>
Use ssh to connect to this server:<br>
Server: saturn.picoctf.net<br>
Port: 50731<br>
Username: picoplayer<br>
Password: ENAFb6zfzn

## What I learned
```
System-wide cron jobs:
    /etc/crontab → main system crontab
    /etc/cron.d/ → directory with individual cron job files
    /etc/cron.hourly/, /etc/cron.daily/, /etc/cron.weekly/, /etc/cron.monthly/

cat /etc/crontab ⌨️❤️
ls -la /etc/cron.d/ ⌨️
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh picoplayer@saturn.picoctf.net -p 50731 ⌨️
picoplayer@saturn.picoctf.net's password: ⌨️
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

picoplayer@challenge:~$ ls -la ⌨️
total 12
drwxr-xr-x 1 picoplayer picoplayer   20 Aug 20 03:42 .
drwxr-xr-x 1 root       root         24 Aug  4  2023 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Aug 20 03:42 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile

# Edit crontab
picoplayer@challenge:~$ crontab -e ⌨️
no crontab for picoplayer - using an empty one
update-alternatives: error: no alternatives for editor
/usr/bin/sensible-editor: 25: editor: not found
/usr/bin/sensible-editor: 28: nano: not found
/usr/bin/sensible-editor: 31: nano-tiny: not found
/usr/bin/sensible-editor: 34: vi: not found
Couldn't find an editor!
Set the $EDITOR environment variable to your desired editor.
crontab: "/usr/bin/sensible-editor" exited with status 1

# Start cron
picoplayer@challenge:~$ systemctl status cron ⌨️
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
picoplayer@challenge:~$ sudo systemctl start cron ⌨️
[sudo] password for picoplayer: 
picoplayer is not in the sudoers file.  This incident will be reported.
picoplayer@challenge:~$ sudo systemctl enable cron ⌨️
[sudo] password for picoplayer: 
picoplayer is not in the sudoers file.  This incident will be reported.

# List all cronjob for current user
picoplayer@challenge:~$ crontab -l ⌨️
no crontab for picoplayer

# View system-wide cronjobs
picoplayer@challenge:~$ cat /etc/crontab ⌨️
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_1d781160}
```

## Flag
picoCTF{Sch3DUL7NG_T45K3_L1NUX_1d781160}

## Continue
[Continue](./picoGym0091.md)