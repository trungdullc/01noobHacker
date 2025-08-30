# picoGym Level 349: findme
Source: https://play.picoctf.org/practice/challenge/349

## Goal
Help us test the form by submiting the username as test and password as test!<br>
The website running here.<br>
http://saturn.picoctf.net:60009/

## What I learned
```
HTTP/1.1 302 Found
Page Redirect 
```             

## Solution
```
https://webshell.picoctf.org/

test ⌨️
test! ⌨️

# Burp Suite
# Request
POST /login HTTP/1.1
Host: saturn.picoctf.net:60009
Content-Length: 30
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://saturn.picoctf.net:60009
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://saturn.picoctf.net:60009/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=test&password=test%21

# Send to Repeater and get Response
HTTP/1.1 302 Found
X-Powered-By: Express
Location: /next-page/id=cGljb0NURntwcm94aWVzX2Fs
Vary: Accept
Content-Type: text/html; charset=utf-8
Content-Length: 120
Date: Sat, 23 Aug 2025 02:30:57 GMT
Connection: keep-alive
Keep-Alive: timeout=5

<p>Found. Redirecting to <a href="/next-page/id=cGljb0NURntwcm94aWVzX2Fs">/next-page/id=cGljb0NURntwcm94aWVzX2Fs</a></p> 👀

# Follow Redirect
# Response
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 264
ETag: W/"108-p43QX15azZA05imtghrPlRHx7LY"
Date: Sat, 23 Aug 2025 02:26:52 GMT
Connection: keep-alive
Keep-Alive: timeout=5

<!DOCTYPE html>
<head>
    <title>flag</title>
</head>
<body>
    <script>
        setTimeout(function () {
           // after 2 seconds
           window.location = "/next-page/id=bF90aGVfd2F5XzI1YmJhZTlhfQ=="; 👀
        }, 0.5)
      </script>
    <p></p>
</body>

# Base64 decode and combine flag
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=Y0dsamIwTlVSbnR3Y205NGFXVnpYMkZz
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=YkY5MGFHVmZkMkY1WHpJMVltSmhaVGxoZlE9PQ

AsianHacker-picoctf@webshell:~$ echo "cGljb0NURntwcm94aWVzX2Fs" | base64 -d ⌨️
picoCTF{proxies_al 👀
AsianHacker-picoctf@webshell:~$ echo "bF90aGVfd2F5XzI1YmJhZTlhfQ==" | base64 -d ⌨️
l_the_way_25bbae9a} 👀

# Build flag
picoCTF{proxies_all_the_way_25bbae9a} 🔐
```

## Flag
picoCTF{proxies_all_the_way_25bbae9a}

## Continue
[Continue](./picoGym0376.md)