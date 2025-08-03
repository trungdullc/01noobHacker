# Bandit Level 9 → Level 10 The ‘strings’ command. Find human-readable strings in a file

## Previous Flag
<b>FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey</b>

## Goal
Use previous password to log in SSH with user <b>bandit10</b> on port <b>2220</b>.  Password stored in <b>data.txt</b>, which contains <b>base64 encoded data</b>.

## What I learned
![alt text](/static/base64.jpg)
```
Base64 is not encryption it is just encoding
                                ASCII DEC   Binary
echo -n "at" | base64             97      01100001
YXQ=                              116     01100001
          2^6=64  Split by 6, Pad 2 🛞's on R: 
                                011000 010110 0001🛞🛞
                                  24     23     16
                                  Y      X      Q
          Note: at: 2 char but end w/ 3 (YXQ) need pad w/ =   
echo "YXQ=" | base64 -d
at
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit10@bandit.labs.overthewire.org -p 2220 ⌨️
bandit10@bandit:~$ ls ⌨️
data.txt
bandit10@bandit:~$ whatis base64 ⌨️
base64 (1)    - base64 encode/decode data and print to standard output
bandit10@bandit:~$ base64 --help ⌨️
Usage: base64 [OPTION]... [FILE] 👀
Base64 encode or decode FILE, or standard input, to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -d, --decode          decode data 👀
bandit10@bandit:~$ base64 -d data.txt ⌨️ 
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr 🔐
```

## Flag
<b>dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr</b>

## Continue
[Continue](/overthewire/Bandit1011.md)