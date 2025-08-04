# Natas Level 0 → Level 1 Bypass Right Click w/ F12

## Previous Flag
<b>0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq</b>

## Goal
Username: natas1<br>
URL: http://natas1.natas.labs.overthewire.org<br>

You can find the password for the next level <b>on this page</b>, but <b>right clicking has been blocked!</b>

## What I learned
```
F12 Developer Tools still has access to source code
curl and wget also could work
```

## Solution
```
F12

<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">
<h1>natas1</h1>
<div id="content">
You can find the password for the next level on this page, but right clicking has been blocked!

<!--The password for natas2 is TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI --> 🔐
</div>

<div id="wechallform" class="ui-draggable" style="display: block;"><p>Submit token</p><form id="realwechallform" action="https://www.wechall.net/10-levels-on-Natas.html" enctype="application/x-www-form-urlencoded" method="post"><input type="hidden" name="wfid" value="2"><input type="hidden" name="password_solution" value="0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq"><input type="hidden" name="igotitnow" 👻 value="Register"></form></div></body>
```

## Flag
<b>TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI</b>

## Continue
[Continue](/overthewire/Natas0102.md)