# picoGym Level 0250: runme.py
Source: https://play.picoctf.org/practice/challenge/250

## Goal
Run the runme.py script to get the flag. Download the script with your browser or with wget in the webshell.

## What I learned
```
wget
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/34/runme.py ⌨️
--2025-08-18 21:50:20--  https://artifacts.picoctf.net/c/34/runme.py 
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.16, 3.160.22.43, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.16|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 270 [application/octet-stream]
Saving to: 'runme.py'

runme.py                                                   100%[======================================================================================================================================>]     270  --.-KB/s    in 0s      

2025-08-18 21:50:20 (233 MB/s) - 'runme.py' saved [270/270]

AsianHacker-picoctf@webshell:/tmp$ file runme.py ⌨️
runme.py: Python script, ASCII text executable
AsianHacker-picoctf@webshell:/tmp$ cat runme.py ⌨️
#!/usr/bin/python3
################################################################################
# Python script which just prints the flag
################################################################################

flag ='picoCTF{run_s4n1ty_run}' 🔐
print(flag)

AsianHacker-picoctf@webshell:/tmp$ python3 runme.py ⌨️
picoCTF{run_s4n1ty_run} 🔐
AsianHacker-picoctf@webshell:/tmp$ rm runme.py ⌨️
```

## Flag
picoCTF{run_s4n1ty_run}

## Continue
[Continue](./picoGym0405.md)