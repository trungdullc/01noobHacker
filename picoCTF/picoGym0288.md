# picoGym Level 288: Power Cookie
Source: https://play.picoctf.org/practice/challenge/288

## Goal
Can you get the flag?<br>
Go to this website and see what you can discover<br>
http://saturn.picoctf.net:63754/

## What I learned
```
Cookies
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ curl -I http://saturn.picoctf.net:63754/ ⌨️
HTTP/1.1 200 OK
Server: nginx
Date: Fri, 22 Aug 2025 21:14:35 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Vary: Accept-Encoding

# View Page Source
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Secure Log In</title>
  </head>
  <body>
    <script src="guest.js"></script> 👀

    <h1>Online Gradebook</h1>
    <button type="button" onclick="continueAsGuest();">Continue as guest</button>
  </body>
</html>

Browser: http://saturn.picoctf.net:55534/guest.js ⌨️
function continueAsGuest()
{
  window.location.href = '/check.php'; 👀
  document.cookie = "isAdmin=0"; 👀👀👀👀👀
}

# JS Fx save cookies to isAdmin
Inspect → Application → Cookies
Name        Value
PHPSESSID   iqvkoo2sogr6l1v99iufmhhm9g

Continue as Guest

We apologize, but we have no guest services at the moment.

Browser: http://saturn.picoctf.net:63754/check.php ⌨️
Name        Value
isAdmin     0 👀
PHPSESSID   iqvkoo2sogr6l1v99iufmhhm9g

# O means False change to 1 and reload page
picoCTF{gr4d3_A_c00k13_5d2505be} 🔐
```

## Flag
picoCTF{gr4d3_A_c00k13_5d2505be} 

## Continue
[Continue](./picoGym0270.md)