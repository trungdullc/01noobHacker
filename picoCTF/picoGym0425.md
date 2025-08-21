# picoGym Level 0425: Time Machine
Source: https://play.picoctf.org/practice/challenge/425

## Goal
What was I last working on? I remember writing a note to help me remember...

## What I learned
```
git log
git reflog
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c_titan/160/challenge.zip ⌨️
--2025-08-18 23:10:49--  https://artifacts.picoctf.net/c_titan/160/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.92, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17740 (17K) [application/octet-stream]
Saving to: 'challenge.zip'

challenge.zip                                              100%[======================================================================================================================================>]  17.32K  --.-KB/s    in 0.001s  

2025-08-18 23:10:49 (23.5 MB/s) - 'challenge.zip' saved [17740/17740]

AsianHacker-picoctf@webshell:/tmp/drop-in$ git status ⌨️
On branch master
nothing to commit, working tree clean
AsianHacker-picoctf@webshell:/tmp/drop-in$ git reflog ⌨️
AsianHacker-picoctf@webshell:/tmp$ unzip challenge.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ rm challenge.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ cd drop-in/ ⌨️

89d296e (HEAD -> master) HEAD@{0}: commit (initial): picoCTF{t1m3m@ch1n3_186cd7d7} 🔐
(END)

AsianHacker-picoctf@webshell:/tmp/drop-in$ git log ⌨️
commit 89d296ef533525a1378529be66b22d6a2c01e530 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:22 2024 +0000

    picoCTF{t1m3m@ch1n3_186cd7d7} 🔐
(END)
```

## Flag
picoCTF{t1m3m@ch1n3_186cd7d7}

## Continue
[Continue](./picoGym0240.md)