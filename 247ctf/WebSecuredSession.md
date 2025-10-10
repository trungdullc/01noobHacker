# Web: Secured Session

## Previous Flag
```
247CTF{6ae15c0aeb45a334b3f01eb0dda5cab1}
```

## Goal
If you can guess our random secret key, we will tell you the flag securely stored in your session.

## What I learned
```
Flag securely stored in your session
```

## Side Quest
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> python ⌨️
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import os ⌨️
>>> print(os.urandom(24)) ⌨️
b'\xea\x1dN\xe23/+ \x1c\x86\xca]h\xca\xd8\xb38v\\\xb5\xb1\xb9\xb0\xff'
>>> print(os.urandom(1)) ⌨️
b'6'
>>> print(os.urandom(2)) ⌨️
b'd]'
>>> print(os.urandom(3)) ⌨️
b'=\xb0\x1c'
>>> print(os.urandom(8)) ⌨️
b'Su\xe2\x92\xaa\xb9\xef.'
>>> exit() ⌨️
```

## Solution
```
START CHALLENGE: https://0cd1cac76406582e.247ctf.com/

import os
from flask import Flask, request, session 👀
from flag import flag

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

def secret_key_to_int(s):
    try:
        secret_key = int(s)
    except ValueError:
        secret_key = 0
    return secret_key

@app.route("/flag") 👀 if go to this route /flag will get else
def index():
    # if go this route it need pass correct argument to be converted to int with above fx else it None
    secret_key = secret_key_to_int(request.args['secret_key']) if 'secret_key' in request.args else None
    session['flag'] = flag
    if secret_key == app.config['SECRET_KEY']:
      return session['flag']
    else:
      return "Incorrect secret key!"

@app.route('/')
def source():
    return "
%s
" % open(__file__).read()

if __name__ == "__main__":
    app.run()

# Important: Must be on https://159f11b8415e7cfb.247ctf.com/flag

# Method 1:
Application > Cookies
Name
session 👀
Value
eyJmbGFnIjp7IiBiIjoiTWpRM1ExUkdlMlJoT0RBM09UVm1PR0UxWTJGaU1tVXdNemRrTnpNNE5UZ3dOMkk1WVRreGZRPT0ifX0.aOfaFw.dnLmq_3AcS4WGVtfuPaAxax2VHg

# Base64 decode than extract human readable and base64 decode again
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=ZXlKbWJHRm5JanA3SWlCaUlqb2lUV3BSTTFFeFVrZGxNbEpvVDBSQk0wOVVWbTFQUjBVeFdUSkdhVTF0VlhkTmVtUnJUbnBOTkU1VVozZE9Na2sxV1ZScmVHWlJQVDBpZlgwLmFPZmFGdy5kbkxtcV8zQWNTNFdHVnRmdVBhQXhheDJWSGc
Output: {"flag":{" b":"MjQ3Q1RGe2RhODA3OTVmOGE1Y2FiMmUwMzdkNzM4NTgwN2I5YTkxfQ=="}}.9ö.ÁÙË..Àq...[_¸ö.Å¬vTx

https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=TWpRM1ExUkdlMlJoT0RBM09UVm1PR0UxWTJGaU1tVXdNemRrTnpNNE5UZ3dOMkk1WVRreGZRPT0

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> python ⌨️
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import base64 ⌨️
>>> print(base64.b64decode("MjQ3Q1RGe2RhODA3OTVmOGE1Y2FiMmUwMzdkNzM4NTgwN2I5YTkxfQ==").decode()) ⌨️
247CTF{da80795f8a5cab2e037d7385807b9a91} 🔐
>>> exit() ⌨️

AsianHacker-picoctf@webshell:~$ echo "MjQ3Q1RGe2RhODA3OTVmOGE1Y2FiMmUwMzdkNzM4NTgwN2I5YTkxfQ==" | base64 -d ⌨️
247CTF{da80795f8a5cab2e037d7385807b9a91} 🔐

# Method 2: Burp Suite
# Couldn't get to work on Microsoft Edge or Google Chrome, Burp Suite
Proxy > Open Browser
Intercepter On

GET /flag HTTP/1.1
Host: 159f11b8415e7cfb.247ctf.com
Cookie: _ga=GA1.2.1929956447.1760023440; _gid=GA1.2.1699286742.1760023440; _ga_WRWK351K37=GS2.1.s1760023440$o1$g1$t1760024745$j60$l0$h0; session=eyJmbGFnIjp7IiBiIjoiTWpRM1ExUkdlMlJoT0RBM09UVm1PR0UxWTJGaU1tVXdNemRrTnpNNE5UZ3dOMkk1WVRreGZRPT0ifX0.aOffdg.P8L7XHrPo52-t3ovEfGzz8nR_ro 👀
Sec-Ch-Ua: "Not=A?Brand";v="24", "Chromium";v="140"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive

Method 3: curl
AsianHacker-picoctf@webshell:~$ curl -i https://159f11b8415e7cfb.247ctf.com/flag ⌨️
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 09 Oct 2025 16:08:25 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 21
Connection: keep-alive
Vary: Cookie
Set-Cookie: session=eyJmbGFnIjp7IiBiIjoiTWpRM1ExUkdlMlJoT0RBM09UVm1PR0UxWTJGaU1tVXdNemRrTnpNNE5UZ3dOMkk1WVRreGZRPT0ifX0.aOfd-Q.ahtcy4H17JhW2SLkNCRLuIG0R2U; 👀 HttpOnly; Path=/
```

## Flag
247CTF{da80795f8a5cab2e037d7385807b9a91}

## Continue
[Continue](../247ctf/WebTrustedClient.md)