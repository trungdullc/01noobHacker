# picoGym Level 134: Shop
Source: https://play.picoctf.org/practice/challenge/134

## Goal
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source.<br>
https://mercury.picoctf.net/static/73724c199e55e6c056bb00e7bbfdfb38/source<br>
The shop is open for business at nc mercury.picoctf.net 10337.

## What I learned
```
Reverse Engineering
A common vulnerability in these kinds of puzzles is tricking the software by buying or selling a negative number of items.

Optional: Ghidra Decompiler
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/73724c199e55e6c056bb00e7bbfdfb38/source ⌨️
--2025-09-29 22:05:38--  https://mercury.picoctf.net/static/73724c199e55e6c056bb00e7bbfdfb38/source
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1984519 (1.9M) [application/octet-stream]
Saving to: 'source'

source                                                     100%[======================================================================================================================================>]   1.89M  1.84MB/s    in 1.0s    

2025-09-29 22:05:39 (1.84 MB/s) - 'source' saved [1984519/1984519]

AsianHacker-picoctf@webshell:~$ file source ⌨️
source: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, Go BuildID=VzqWa9zw0T7uu0fIpzlr/GX_jOPrDyG7EJ49Mafov/8nLti5urveRPmDg4XzP1/dGBVjid622Z_AGO6iyBH, with debug_info, not stripped
AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  source
AsianHacker-picoctf@webshell:~$ ls -la source ⌨️ 
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 1984519 Mar 17  2021 source
AsianHacker-picoctf@webshell:~$ chmod u+x source ⌨️

AsianHacker-picoctf@webshell:~$ nc mercury.picoctf.net 10337 ⌨️
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
1 ⌨️
How many do you want to buy?
-22 ⌨️
You have 370 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      30
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
2 ⌨️
How many do you want to buy?
1 ⌨️
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 51 100 97 51 52 97 56 102 125] 👀

https://cyberchef.io/#recipe=From_Decimal('Space',false)&input=MTEyIDEwNSA5OSAxMTEgNjcgODQgNzAgMTIzIDk4IDUyIDEwMCA5NSA5OCAxMTQgMTExIDEwMyAxMTQgOTcgMTA5IDEwOSAxMDEgMTE0IDk1IDUxIDEwMCA5NyA1MSA1MiA5NyA1NiAxMDIgMTI1
```

## Flag
picoCTF{b4d_brogrammer_3da34a8f}

## Continue
[Continue](./picoGym0116.md)