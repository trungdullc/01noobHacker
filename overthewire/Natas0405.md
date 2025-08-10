# Natas Level 4 → Level 5 cookies

## Previous Flag
<b>0n35PkggAPm2zbEpOU802c0x0Msn1ToK</b>

## Goal
Username: natas5<br>
URL: http://natas5.natas.labs.overthewire.org<br>

Access disallowed. You are not logged in

## What I learned
```
HTTP is stateless (no info about session/previous requests is saved on receivers/servers side)
client/browser saves session states stored in cookies and sends them with new requests
Cookies stored on client side, meaning client can manipulate

Types of cookies:
    Authentication cookies	    Keep users logged in by storing session/login credentials
    Tracking cookies	        Track user behavior across websites (often for ads/analytics)
    Session cookies	            Temporary; deleted when the browser closes
    Persistent cookies	        Stored on disk; survive browser restarts; expire after a set time
    Secure cookies	            Sent only over HTTPS connections
    HttpOnly cookies	        Not accessible via JavaScript (helps prevent XSS)
    Third-party cookies	        Set by domains other than the one you’re visiting
    First-party cookies	        Set by the same domain you're visiting
    SameSite cookies	        Restrict cross-site request behavior (Strict, Lax, None)
```

## Side Quest
```
# Server-side Cookie Check (Most Common)
    <?php
    if ($_COOKIE['loggedin'] === '1') {
        echo "Access granted. The password is ...";
    } else {
        echo "Access denied.";
    }
    ?>

# Client-side JavaScript Check (To easy to hack)
    const cookies = document.cookie;
    if (cookies.includes("loggedin=1")) {
        document.body.innerHTML = "Access granted. The password is ...";
    }
```

## Solution
```
F12 → Application
Storage → Cookies

Name            Value
loggedin        0

# Change value to 1 by Right Click → Edit "Value"
Name            Value
loggedin        1 ⌨️

F5

Access granted. The password for natas6 is 0RoJwHdSKWFTYR5WuiAewauSuNaBXned 🔐
```

## Flag
<b>0RoJwHdSKWFTYR5WuiAewauSuNaBXned</b>

## Continue
[Continue](./Natas0506.md)