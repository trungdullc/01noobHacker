# Bandit Level 13 → Level 14 Netcat and first network communication

## Previous Flag
<b>MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS</b>

## Goal
Use previous password to log in SSH with user <b>bandit14</b> on port <b>2220</b>.  Password retrieved by submitting the password of the current level to <b>port 30000 on localhost</b>

## What I learned
```
netcat not a systemd service (ssh, apache2, nginx)

# Start simple always true netcat Listener
while true; do echo "Hi Hacker" | nc -lvp 30000; done

# Another terminal in same local network, could do something similar with telnet
nc localhost 30000
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit14@bandit.labs.overthewire.org -p 2220 ⌨️
bandit14@bandit:~$ systemctl status nc
Unit nc.service could not be found.
bandit14@bandit:~$ which nc ⌨️
/usr/bin/nc
bandit14@bandit:~$ ps aux | grep 'nc' ⌨️
bandit14 1536463  0.0  0.0   3436  2176 ?        S    Jul25   0:00 nc localhost 30000 👀
bandit14 1537094  0.0  0.0   3436  2176 ?        S    Jul25   0:00 nc localhost 30000
bandit14 3057937  0.0  0.0   3436  2176 pts/33   S+   Jul25   0:00 nc -N localhost 30000
bandit14@bandit:~$ cat /etc/hosts ⌨️
127.0.0.1 localhost
127.0.0.1 bandit bandit.labs.overthewire.org
bandit14@bandit:~$ nc localhost 30000 ⌨️
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS ⌨️
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo 🔐
```

## Flag
<b>8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo</b>

## Continue
[Continue](./Bandit1415.md)