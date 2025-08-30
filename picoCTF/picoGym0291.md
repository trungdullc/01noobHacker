# picoGym Level 291: Roboto Sans
Source: https://play.picoctf.org/practice/challenge/291

## Goal
The flag is somewhere on this web application not necessarily on the website. Find it.<br>
Check this out<br>
http://saturn.picoctf.net:64227/

## What I learned
```
/wp-admin/ is default route to access WordPress admin panel
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ curl -I http://saturn.picoctf.net:64227/ ⌨️
HTTP/1.1 200 OK
Server: nginx/1.21.6
Date: Fri, 22 Aug 2025 20:56:07 GMT
Content-Type: text/html
Content-Length: 15920
Last-Modified: Thu, 16 Mar 2023 01:30:51 GMT
Connection: keep-alive
ETag: "6412714b-3e30"
Accept-Ranges: bytes

Browser: http://saturn.picoctf.net:64227/robots.txt ⌨️
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW 👀
anMvbXlmaWxlLnR4dA== 👀
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/

AsianHacker-picoctf@webshell:~$ echo "anMvbXlmaW" | base64 -d ⌨️
js/myfibase64: invalid input
AsianHacker-picoctf@webshell:~$ echo "anMvbXlmaWxlLnR4dA==" | base64 -d ⌨️
js/myfile.txt 👀

Browser: http://saturn.picoctf.net:64227/js/myfile.txt ⌨️
picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043} 🔐
```

## Flag
picoCTF{Who_D03sN7_L1k5_90B0T5_718c9043}

## Continue
[Continue](./picoGym0288.md)