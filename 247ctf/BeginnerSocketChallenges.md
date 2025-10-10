# Beginner Tutorial: Socket Challenges

## Previous Flag
```
247CTF{bb6d77763cd8ee46e303dc2b7046fd02} 
```

## Goal
At the 247/CTF, challenges are not shared with multiple players and VPNs are not required. Instead, you have the control to start and stop your own unique challenge instance at any time. Once you have launched a challenge, you can access the instance by clicking on the pop up which loads in the bottom right hand corner of every page.<br>

Click the ‘START CHALLENGE’ button to the right of this text description to start a socket challenge. Once the challenge instance is launched, the pop up will contain either a tcp:// or udp:// link to access the socket hosting your challenge. Connect to the socket using a tool such as netcat or telnet and submit the flag!

## What I learned
```
Note: Only works on kali linux
```

## Solution
```
START CHALLENGE
  tcp://88b51447f0776cec.247ctf.com:50308

AsianHacker-picoctf@webshell:~$ telnet 88b51447f0776cec.247ctf.com 50308 ⌨️
Trying 144.76.74.118...
^C ⌨️
AsianHacker-picoctf@webshell:~$ nc 88b51447f0776cec.247ctf.com 50308 ⌨️
^C ⌨️
AsianHacker-picoctf@webshell:~$ nc -T tcp 9a7d5205d67de4f9.247ctf.com 50134 ⌨️
nc: illegal tos value tcp

# Executed on Kali Linux
(asianhacker@kali)-[home/asianhacker]
PS> nc -T tcp 9a7d5205d67de4f9.247ctf.com 50134 ⌨️
247CTF{c439cb0d7bbea834d7b71e4b175d13ae} 🔐

(asianhacker@kali)-[home/asianhacker]
PS> nc 9a7d5205d67de4f9.247ctf.com 50134 ⌨️
247CTF{c439cb0d7bbea834d7b71e4b175d13ae} 🔐
```

## Flag
247CTF{c439cb0d7bbea834d7b71e4b175d13ae}

## Continue
[Continue](../247ctf/BeginnerWatchAndLearn)