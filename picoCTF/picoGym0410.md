# picoGym Level 0410: Collaborative Development
Source: https://play.picoctf.org/practice/challenge/410

## Goal
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together? Download the challenge file

## What I learned
```
git config --global user.name "Hacker"
git config --global user.email "Hacker@gmail.com"
# Need generate SSH Key w/ RSA (2048/4096 bits) or ed25519 and upload to GitHub/GitLab for git merge to work
ssh-keygen -t ed25519 -C "Hacker@gmail.com"
ssh-keygen -t rsa -b 4096 -C "Hacker@gmail.com"

git checkout
git switch
git merge feature/part-1
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:/tmp$ cd ⌨️
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c_titan/70/challenge.zip ⌨️
--2025-08-18 22:29:15--  https://artifacts.picoctf.net/c_titan/70/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.43, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 24662 (24K) [application/octet-stream]
Saving to: 'challenge.zip'

challenge.zip                                              100%[======================================================================================================================================>]  24.08K  --.-KB/s    in 0.01s   

2025-08-18 22:29:15 (2.27 MB/s) - 'challenge.zip' saved [24662/24662]

AsianHacker-picoctf@webshell:/tmp$ unzip challenge.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ rm challenge.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ cd drop-in/ ⌨️
AsianHacker-picoctf@webshell:/tmp/drop-in$ file flag.py ⌨️ 
flag.py: ASCII text
AsianHacker-picoctf@webshell:/tmp/drop-in$ cat flag.py ⌨️
print("Printing the flag...")
AsianHacker-picoctf@webshell:/tmp/drop-in$ git status ⌨️
On branch main
nothing to commit, working tree clean
AsianHacker-picoctf@webshell:/tmp/drop-in$ git branch ⌨️
  feature/part-1 👀
  feature/part-2 👀
  feature/part-3 👀
* main
AsianHacker-picoctf@webshell:/tmp/drop-in$ git reflog ⌨️
54c7842 (HEAD -> main) HEAD@{0}: checkout: moving from feature/part-3 to main
5c00b43 (feature/part-3) HEAD@{1}: commit: add part 3
54c7842 (HEAD -> main) HEAD@{2}: checkout: moving from main to feature/part-3 👀
54c7842 (HEAD -> main) HEAD@{3}: checkout: moving from feature/part-2 to main
d3563a2 (feature/part-2) HEAD@{4}: commit: add part 2
54c7842 (HEAD -> main) HEAD@{5}: checkout: moving from main to feature/part-2 👀
54c7842 (HEAD -> main) HEAD@{6}: checkout: moving from feature/part-1 to main
f65544e (feature/part-1) HEAD@{7}: commit: add part 1
54c7842 (HEAD -> main) HEAD@{8}: checkout: moving from main to feature/part-1 👀
54c7842 (HEAD -> main) HEAD@{9}: commit (initial): init flag printer
(END)
AsianHacker-picoctf@webshell:/tmp/drop-in$ git checkout feature/part-1 ⌨️
Switched to branch 'feature/part-1'
AsianHacker-picoctf@webshell:/tmp/drop-in$ ls ⌨️
flag.py
AsianHacker-picoctf@webshell:/tmp/drop-in$ cat flag.py ⌨️ 
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='') 👀
AsianHacker-picoctf@webshell:/tmp/drop-in$ git switch feature/part-2 ⌨️
Switched to branch 'feature/part-2'
AsianHacker-picoctf@webshell:/tmp/drop-in$ cat flag.py ⌨️
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='') 👀
AsianHacker-picoctf@webshell:/tmp/drop-in$ git switch feature/part-3 ⌨️
Switched to branch 'feature/part-3'
AsianHacker-picoctf@webshell:/tmp/drop-in$ cat flag.py ⌨️
print("Printing the flag...")

print("w0rk_7ffa0077}") 👀
```

## Flag
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_7ffa0077}

## Continue
[Continue](./picoGym0242.md)