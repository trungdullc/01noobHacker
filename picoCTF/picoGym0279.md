# picoGym Level 279: Lookey here
Source: https://play.picoctf.org/practice/challenge/279

## Goal
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.<br>
Download the data here.<br>
https://artifacts.picoctf.net/c/125/anthem.flag.txt

## What I learned
```
grep
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/125/anthem.flag.txt ⌨️
--2025-09-17 18:53:48--  https://artifacts.picoctf.net/c/125/anthem.flag.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.77, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 108668 (106K) [application/octet-stream]
Saving to: 'anthem.flag.txt'

anthem.flag.txt                                            100%[======================================================================================================================================>] 106.12K  --.-KB/s    in 0.05s   

2025-09-17 18:53:48 (2.14 MB/s) - 'anthem.flag.txt' saved [108668/108668]

AsianHacker-picoctf@webshell:~$ file anthem.flag.txt ⌨️
anthem.flag.txt: Unicode text, UTF-8 text
AsianHacker-picoctf@webshell:~$ cat anthem.flag.txt | grep "picoCTF" ⌨️
      we think that the men of picoCTF{gr3p_15_@w3s0m3_58f5c024} 🔐
```

## Flag
picoCTF{gr3p_15_@w3s0m3_58f5c024}

## Continue
[Continue](./picoGym0305.md)