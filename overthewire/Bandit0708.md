# Bandit Level 7 → Level 8 sort then uniq -u rule

## Previous Flag
<b>dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc</b>

## Goal
Use previous password to log in SSH with user <b>bandit8</b> on port <b>2220</b>.  Password stored in file <b>data.txt</b> and is the <b>only line of text that occurs only once</b>

## What I learned
```
MUST sort before using uniq
uniq -u     displays only unique entries
uniq -d     displays duplicate (default)
uniq -c     displays on left count of duplicate w/ entry
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit8@bandit.labs.overthewire.org -p 2220 ⌨️
bandit8@bandit:~$ whatis uniq sort ⌨️
uniq (1)             - report or omit repeated lines
sort (1)             - sort lines of text files
bandit8@bandit:~$ ls ⌨️
data.txt
bandit8@bandit:~$ head -n 5 data.txt ⌨️
L3ZCH71RRxt8Kmy3X3R0NqQTmebcmkQ4
NknAyxnPgpoEcWHizP4TA8ALeIyco1VT
Fmt5ODm3V6Qf1oTF3qEJNWlVcHFdpbuz
nOu0uI9qll3ws9FtaQt7mE4ngAmMAsfE
ksiDcx6JXM6yZSfpf1TlIIlABpb97SAy
bandit8@bandit:~$ sort data.txt | uniq -u ⌨️
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM 🔐
```

## Flag
<b>4CKMh1JI91bUIZZPXDqGanal4xvAg0JM</b>

## Continue
[Continue](./Bandit0809.md)