# picoGym Level 451: Binary Instrumentation 1
Source: https://play.picoctf.org/practice/challenge/451

## Goal
I have been learning to use the Windows API to do cool stuff! Can you wake up my program to get the flag?<br>
Download the exe here. Unzip the archive with the password picoctf<br>
https://challenge-files.picoctf.net/c_verbal_sleep/c71239e2890bd0008ff9c1da986438d276e7a96ba123cb3bc7b04d5a3de27fe7/bininst1.zip

## What I learned
```
Reverse Engineering

Frida: a dynamic instrumentation toolkit
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_verbal_sleep/ c71239e2890bd0008ff9c1da986438d276e7a96ba123cb3bc7b04d5a3de27fe7/bininst1.zip ⌨️
--2025-09-30 06:20:32--  https://challenge-files.picoctf.net/c_verbal_sleep/c71239e2890bd0008ff9c1da986438d276e7a96ba123cb3bc7b04d5a3de27fe7/bininst1.zip
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.64, 3.160.5.95, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 18230 (18K) [application/octet-stream]
Saving to: 'bininst1.zip'

bininst1.zip                                               100%[======================================================================================================================================>]  17.80K  --.-KB/s    in 0.007s  

2025-09-30 06:20:32 (2.46 MB/s) - 'bininst1.zip' saved [18230/18230]

AsianHacker-picoctf@webshell:~$ unzip bininst1.zip ⌨️
Archive:  bininst1.zip
[bininst1.zip] bininst1.exe password: ⌨️
  inflating: bininst1.exe            
AsianHacker-picoctf@webshell:~$ file bininst1.exe ⌨️
bininst1.exe: PE32+ executable (console) x86-64, for MS Windows
AsianHacker-picoctf@webshell:~$ strings -n 8 bininst1.exe ⌨️
!This program cannot be run in DOS mode.
HcD$0HcL$0
D$0HcD$0H;
AsianHacker-picoctf@webshell:~$ rm bininst1.zip ⌨️

# Method 1: frida
$ pip install frida-tools ⌨️
$ .\bininst1.exe ⌨️

# Modify Handler: Edit the generated Sleep.js file to reduce the sleep duration
$ frida-trace -i Sleep .\bininst1.exe ⌨️

defineHandler({
onEnter(log, args, state) {
log('Sleep() - Original dwMilliseconds = ' + args[0]);
args[0] = ptr("0x02"); // Set sleep duration to 2ms
log('Sleep() - Modified dwMilliseconds = ' + args[0]);
},
onLeave(log, retval, state) {}
});

# Or replace sleep script
$ cat killsleep.js ⌨️
var sleep=Module.findExportByName("kernel32.dll","Sleep")

Interceptor.replace(sleep, new NatieCallback(function(ms) {
    return  // don't sleep
}, "void", ["uint32]))

$ frida -f .\bininst1.exe -l .\killsleep.js ⌨️
flag is: cGljb0NURnt3NGtlX20zX3VwX3cxdGhfZnIxZGFfZjI3YWNjMzh9

AsianHacker-picoctf@webshell:~$ echo "cGljb0NURnt3NGtlX20zX3VwX3cxdGhfZnIxZGFfZjI3YWNjMzh9" | base64 -d
picoCTF{w4ke_m3_up_w1th_fr1da_f27acc38}
```

## Flag
picoCTF{w4ke_m3_up_w1th_fr1da_f27acc38} 🔐

## Continue
[Continue](./picoGym0452.md)