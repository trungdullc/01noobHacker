# picoGym Level 0411: Commitment Issues
Source: https://play.picoctf.org/practice/challenge/411

## Goal
I accidentally wrote the flag down. Good thing I deleted it! Download the challenge zip file. 

## What I learned
```
git log
git reflog
git checkout
git show
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c_titan/76/challenge.zip ⌨️
--2025-08-18 21:23:21--  https://artifacts.picoctf.net/c_titan/76/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.128, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 19201 (19K) [application/octet-stream]
Saving to: 'challenge.zip'

challenge.zip                                              100%[======================================================================================================================================>]  18.75K  --.-KB/s    in 0.006s  

2025-08-18 21:23:22 (3.31 MB/s) - 'challenge.zip' saved [19201/19201]

AsianHacker-picoctf@webshell:/tmp$ unzip challenge.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
challenge.zip  drop-in  hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ rm challenge.zip ⌨️ 
AsianHacker-picoctf@webshell:/tmp$ cd drop-in/ ⌨️
AsianHacker-picoctf@webshell:/tmp/drop-in$ ls ⌨️
message.txt
AsianHacker-picoctf@webshell:/tmp/drop-in$ file message.txt ⌨️ 
message.txt: ASCII text
AsianHacker-picoctf@webshell:/tmp/drop-in$ cat message.txt ⌨️
TOP SECRET
AsianHacker-picoctf@webshell:/tmp/drop-in$ ls -la ⌨️
total 8
drwxr-xr-x 3 AsianHacker-picoctf AsianHacker-picoctf   49 Mar  9  2024 .
drwxrwxrwt 1 root                root                  29 Aug 18 21:24 ..
drwxr-xr-x 8 AsianHacker-picoctf AsianHacker-picoctf 4096 Mar  9  2024 .git 👀
-rw-r--r-- 1 AsianHacker-picoctf AsianHacker-picoctf   11 Mar  9  2024 message.txt

# Work w/ .git
AsianHacker-picoctf@webshell:/tmp/drop-in$ git status ⌨️
On branch master
nothing to commit, working tree clean
AsianHacker-picoctf@webshell:/tmp/drop-in$ git log ⌨️
commit a6dca68e4310585eac3b5c9caf0f75967dfe972c (HEAD -> master) 👀 Currently
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:06 2024 +0000

    remove sensitive info

commit e720dc26a1a55405fbdf4d338d465335c439fb3e 👀 Older data
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:06 2024 +0000

    create flag
(END)
AsianHacker-picoctf@webshell:/tmp/drop-in$ git show ⌨️
commit a6dca68e4310585eac3b5c9caf0f75967dfe972c (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:06 2024 +0000

    remove sensitive info

diff --git a/message.txt b/message.txt
index d263841..d552d1e 100644
--- a/message.txt
+++ b/message.txt
@@ -1 +1 @@
-picoCTF{s@n1t1z3_7246792d} 🔐
+TOP SECRET

AsianHacker-picoctf@webshell:/tmp/drop-in$ git reflog ⌨️
a6dca68 (HEAD -> master) HEAD@{0}: commit: remove sensitive info
e720dc2 HEAD@{1}: commit (initial): create flag
(END)
AsianHacker-picoctf@webshell:/tmp/drop-in$ git checkout e720dc26a1a55405fbdf4d338d465335c439fb3e ⌨️
Note: switching to 'e720dc26a1a55405fbdf4d338d465335c439fb3e'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at e720dc2 create flag 
AsianHacker-picoctf@webshell:/tmp/drop-in$ git status ⌨️
HEAD detached at e720dc2
nothing to commit, working tree clean
AsianHacker-picoctf@webshell:/tmp/drop-in$ ls ⌨️
message.txt
AsianHacker-picoctf@webshell:/tmp/drop-in$ cat message.txt ⌨️ 
picoCTF{s@n1t1z3_7246792d} 🔐
AsianHacker-picoctf@webshell:/tmp/drop-in$ cd .. ⌨️
AsianHacker-picoctf@webshell:/tmp$ rm -rf drop-in/ ⌨️
```

## Flag
picoCTF{s@n1t1z3_7246792d}

## Continue
[Continue](./picoGym0250.md)