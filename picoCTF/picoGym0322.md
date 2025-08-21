# picoGym Level 0322: Big Zip
Source: https://play.picoctf.org/practice/challenge/322

## Goal
Unzip this archive and find the flag

## What I learned
```
grep -r
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/503/big-zip-files.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ file big-zip-files.zip ⌨️
big-zip-files.zip: Zip archive data, at least v1.0 to extract, compression method=store
AsianHacker-picoctf@webshell:/tmp$ unzip big-zip-files.zip ⌨️
AsianHacker-picoctf@webshell:/tmp$ grep -r "picoCTF" big-zip-files ⌨️
big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc} 🔐
AsianHacker-picoctf@webshell:/tmp$ rm -rf big-zip* ⌨️
```

## Flag
picoCTF{gr3p_15_m4g1c_ef8790dc}

## Continue
[Continue](./picoGym0301.md)