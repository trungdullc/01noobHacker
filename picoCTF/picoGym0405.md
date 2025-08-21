# picoGym Level 0405: Blame Game 
Source: https://play.picoctf.org/practice/challenge/405

## Goal
Someone's commits seems to be preventing the program from working. Who is it?

## What I learned
```
git blame
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c_titan/158/challenge.zip ⌨️
--2025-08-18 21:56:49--  https://artifacts.picoctf.net/c_titan/158/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.16, 3.160.22.128, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.16|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 294455 (288K) [application/octet-stream]
Saving to: 'challenge.zip'

challenge.zip                                              100%[======================================================================================================================================>] 287.55K  1.87MB/s    in 0.2s    

2025-08-18 21:56:49 (1.87 MB/s) - 'challenge.zip' saved [294455/294455]

AsianHacker-picoctf@webshell:/tmp$ unzip challenge.zip 
Archive:  challenge.zip
   creating: drop-in/
 extracting: drop-in/message.py
AsianHacker-picoctf@webshell:/tmp$ rm challenge.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ cd drop-in/ ⌨️
AsianHacker-picoctf@webshell:/tmp/drop-in$ ls -la ⌨️
total 8
drwxr-xr-x 3 AsianHacker-picoctf AsianHacker-picoctf   48 Mar 12  2024 .
drwxrwxrwt 1 root                root                  21 Aug 18 21:57 ..
drwxr-xr-x 8 AsianHacker-picoctf AsianHacker-picoctf 4096 Mar 12  2024 .git
-rw-r--r-- 1 AsianHacker-picoctf AsianHacker-picoctf   22 Mar 12  2024 message.py
AsianHacker-picoctf@webshell:/tmp/drop-in$ cat message.py ⌨️
print("Hello, World!"
AsianHacker-picoctf@webshell:/tmp/drop-in$ git log --oneline ⌨️
7c7008a important business work
f8517f4 important business work
9bf8138 important business work
c511564 important business work
5628bfc important business work
f4c2033 important business work
f39d8f6 important business work
4dae740 important business work
ad09e34 important business work
c44b476 important business work
7200e12 important business work
6f9f8fc important business work
8c83358 optimize file size of prod code
caa9458 create top secret project
AsianHacker-picoctf@webshell:/tmp/drop-in$ git show 8c83358 ⌨️
commit 8c83358c32daee3f8b597d2b853c1d1966b23f0a
Author: picoCTF{@sk_th3_1nt3rn_2c6bf174}🔐 <ops@picoctf.com>
Date:   Tue Mar 12 00:07:11 2024 +0000

    optimize file size of prod code

diff --git a/message.py b/message.py
index 7df869a..326544a 100644
--- a/message.py
+++ b/message.py
@@ -1 +1 @@
-print("Hello, World!")
+print("Hello, World!"
(END)

# Method 2: See last modified that file
AsianHacker-picoctf@webshell:/tmp/drop-in$ git blame message.py ⌨️❤️
8c83358c (picoCTF{@sk_th3_1nt3rn_2c6bf174🔐} 2024-03-12 00:07:11 +0000 1) print("Hello, World!"
(END)
```

## Flag
picoCTF{@sk_th3_1nt3rn_2c6bf174}

## Continue
[Continue](./picoGym0410.md)