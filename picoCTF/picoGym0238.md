# picoGym Level 0238: Codebook
Source: https://play.picoctf.org/practice/challenge/238

## Goal
Run the Python script code.py in the same directory as codebook.txt

## What I learned
```
python3 arguments
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/2/code.py ⌨️
--2025-08-19 00:53:37--  https://artifacts.picoctf.net/c/2/code.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.128, 3.160.22.43, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1278 (1.2K) [application/octet-stream]
Saving to: 'code.py'

code.py                                                    100%[======================================================================================================================================>]   1.25K  --.-KB/s    in 0s      

2025-08-19 00:53:38 (332 MB/s) - 'code.py' saved [1278/1278]

AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/2/codebook.txt ⌨️
--2025-08-19 00:53:49--  https://artifacts.picoctf.net/c/2/codebook.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.128, 3.160.22.43, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27 [application/octet-stream]
Saving to: 'codebook.txt'

codebook.txt                                               100%[======================================================================================================================================>]      27  --.-KB/s    in 0s      

2025-08-19 00:53:49 (30.0 MB/s) - 'codebook.txt' saved [27/27]
AsianHacker-picoctf@webshell:/tmp$ cat codebook.txt ⌨️
azbycxdwevfugthsirjqkplomn
AsianHacker-picoctf@webshell:/tmp$ python3 code.py ⌨️
picoCTF{c0d3b00k_455157_7d102d7a} 🔐
```

## Flag
picoCTF{c0d3b00k_455157_7d102d7a}

## Continue
[Continue](./picoGym0404.md)