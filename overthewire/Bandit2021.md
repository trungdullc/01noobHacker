# Bandit Level 20 → Level 21 Cronjobs

## Previous Flag
<b>EeoULMCra2q0dSkYj561DX7s1CpBuOBt</b>

## Goal
Use previous password to log in SSH with user <b>bandit21</b> on port <b>2220</b>.  A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in <b>/etc/cron.d/</b> for the configuration and see what command is being executed.

## What I learned
```
cron is the time-based job scheduler in Linux and Unix-like systems
crond daemon: background service that runs and checks schedules
crontab (cron table):  A file that lists what to run and when to run it

0 2 * * * /home/user/backup.sh                # runs every day at 2am
│ │ │ │ │
│ │ │ │ └── Day of the week (0–7) (Sun=0 or 7)
│ │ │ └──── Month (1–12)
│ │ └────── Day of month (1–31)
│ └──────── Hour (0–23)
└────────── Minute (0–59)

crontab -l	            List your crontab
crontab -e	            Edit your crontab
crontab -r	            Remove your crontab
sudo crontab -e	        Edit root’s crontab
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit21@bandit.labs.overthewire.org -p 2220 ⌨️
bandit21@bandit:/etc/cron.d$ ls ⌨️
behemoth4_cleanup  cronjob_bandit22  cronjob_bandit24  leviathan5_cleanup    otw-tmp-dir
clean_tmp          cronjob_bandit23  e2scrub_all       manpage3_resetpw_job  sysstat
bandit21@bandit:/etc/cron.d$ ps -ef | grep cron ⌨️
bandit21 2010376 1386850  0 21:46 pts/45   00:00:00 grep --color=auto cron
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22 ⌨️
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh ⌨️
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv ⌨️
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q 🔐
```

## Flag
<b>tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q</b>

## Continue
[Continue](/overthewire/Bandit2122.md)