# Bandit Level 10 → Level 11 Rot13 substitution cipher as Linux command w/ tr

## Previous Flag
<b>dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr</b>

## Goal
Use previous password to log in SSH with user <b>bandit11</b> on port <b>2220</b>.  Password stored <b>data.txt</b>, where all <b>lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions</b>.

## What I learned
```
First Column A to Z (original), A to M 13 and N to Z 13 now map it in 2nd column to get cipher table (N-ZA-M)
A -> N
M -> Z
N -> A
Z -> M
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit11@bandit.labs.overthewire.org -p 2220 ⌨️
bandit11@bandit:~$ whatis tr ⌨️
tr (1)               - translate or delete characters
bandit11@bandit:~$ ls ⌨️
data.txt
bandit11@bandit:~$ cat data.txt ⌨️ 
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4 👀
bandit11@bandit:~$ tr '[:upper:][:lower:]' 'N-ZA-Mn-za-m' < data.txt ⌨️
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4 🔐
bandit11@bandit:~$ tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt ⌨️
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4 🔐
```

## Flag
<b>7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4</b>

## Continue
[Continue](/overthewire/Bandit1112.md)