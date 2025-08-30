# picoGym Level 426: Unminify
Source: https://play.picoctf.org/practice/challenge/426

## Goal
I don't like scrolling down to read the code of my website, so I've squished it. As a bonus, my pages load faster!<br>
Browse here, and find the flag!<br>
http://titan.picoctf.net:54378/

## What I learned
```
Add 'view-source:' before URL

# If R-Click Disabled use below
Try CTRL+U / ⌘+U in your browser to view the page source
curl <URL>
F12
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ curl -I http://titan.picoctf.net:54378/ ⌨️
HTTP/1.1 200 OK
Server: nginx/1.21.6
Date: Fri, 22 Aug 2025 03:37:23 GMT
Content-Type: text/html
Content-Length: 1352
Last-Modified: Wed, 07 Feb 2024 17:58:49 GMT
Connection: keep-alive
ETag: "65c3c4d9-548"
Expires: Sat, 23 Aug 2025 03:37:23 GMT
Cache-Control: max-age=86400
Cache-Control: public, max-age=86400
Accept-Ranges: bytes

AsianHacker-picoctf@webshell:~$ curl http://titan.picoctf.net:54378/ | grep -E "picoCTF{" ⌨️
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1352  100  1352    0     0  20981      0 --:--:-- --:--:-- --:--:-- 20800
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>picoCTF - picoGym | Unminify Challenge</title><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png"><style>body{font-family:"Lucida Console",Monaco,monospace}h1,p{color:#000}</style></head><body class="picoctf{}" style="margin:0"><div class="picoctf{}" style="margin:0;padding:0;background-color:#757575;display:auto;height:40%"><a class="picoctf{}" href="/"><img src="picoctf-logo-horizontal-white.svg" alt="picoCTF logo" style="display:inline-block;width:160px;height:90px;padding-left:30px"></a></div><center><br class="picoctf{}"><br class="picoctf{}"><div class="picoctf{}" style="padding-top:30px;border-radius:3%;box-shadow:0 5px 10px #0000004d;width:50%;align-self:center"><img class="picoctf{}" src="hero.svg" alt="flag art" style="width:150px;height:150px"><div class="picoctf{}" style="width:85%"><h2 class="picoctf{}">Welcome to my flag distribution website!</h2><div class="picoctf{}" style="width:70%"><p class="picoctf{}">If you're reading this, your browser has succesfully received the flag.</p><p class="picoCTF{pr3tty_c0d3_51d374f0}🔐"></p><p class="picoctf{}">I just deliver flags, I don't know how to read them...</p></div></div><br class="picoctf{}"></div></center></body></html>

Method 2: Find Command
View Page Source
Ctrl + F
```

## Flag
picoCTF{pr3tty_c0d3_51d374f0}

## Continue
[Continue](./picoGym0161.md)