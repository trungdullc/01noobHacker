# Bandit Level 21 → Level 22 Cronjobs

## Previous Flag
<b>tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q</b>

## Goal
Use previous password to log in SSH with user <b>bandit22</b> on port <b>2220</b>. A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in <b>/etc/cron.d/</b> for the configuration and see what command is being executed.

## What I learned
```
# BASH                          # cmd.exe                       # PS
var_name=var_value              set var_name=var_value          $var_name = "var_value"
echo $var_name                  echo %var_name%                 Write-Output $var_name

md5sum: Hash Fx
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit22@bandit.labs.overthewire.org -p 2220 ⌨️
bandit22@bandit:~$ cd /etc/cron.d/ ⌨️
bandit22@bandit:/etc/cron.d$ ls ⌨️
behemoth4_cleanup  cronjob_bandit22  cronjob_bandit24  leviathan5_cleanup    otw-tmp-dir
clean_tmp          cronjob_bandit23  e2scrub_all       manpage3_resetpw_job  sysstat
bandit22@bandit:/etc/cron.d$ ps -ef | grep cron ⌨️
bandit22 3482347 3403914  0 22:11 pts/43   00:00:00 grep --color=auto cron
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23 ⌨️
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh ⌨️
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:/etc/cron.d$ echo "I am user bandit23" | md5sum | cut -d ' ' -f 1 ⌨️
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349 ⌨️
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga 🔐
```

## Flag
<b>0Zf11ioIjMVN551jX3CmStKLYqjk54Ga</b>

## Continue
[Continue](/overthewire/Bandit2223.md)