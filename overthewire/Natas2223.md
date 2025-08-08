# Natas Level 22 → Level 23 PHP Loose Comparison Vulnerability

## Previous Flag
<b>dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs</b>

## Goal
Username: natas23<br>
URL: http://natas23.natas.labs.overthewire.org<br>

Password:<br>
Login

## What I learned
```
strstr() PHP Documentation: https://www.php.net/manual/en/function.strstr.php
strstr() in PHP     Find 1st occurrence of substring (needle) inside another string (haystack) and returns search+ anything after
PHP loose comparisons using == instead of === (also in JS, Perl)

@trungdullc ➜ /workspaces/01noobHacker (main) $ php --help
@trungdullc ➜ /workspaces/01noobHacker (main) $ php -d xdebug.mode=off -a
Interactive shell
php > echo strstr("iloveyou2", "iloveyou");
iloveyou2
php > echo strstr("whatmakesayiloveyou2", "iloveyou");
iloveyou2
php > if ((int) $_REQUEST["passwd"] > 10) { echo "true"; } else { echo "false"; }
false
php > exit
```

## Solution
```
View source code
http://natas23.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas23", "pass": "<censored>" };</script></head>
<body>
<h1>natas23</h1>
<div id="content">

Password:
<form name="input" method="get">
    <input type="text" name="passwd" size=20>
    <input type="submit" value="Login">
</form>

<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){ 👀
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
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

# Need value above 10 and contain iloveyou
Password: 911iloveyouhoney ⌨️
Login

The credentials for the next level are:
Username: natas24 Password: MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd 🔐
```

## Flag
<b>MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd</b>

## Continue
[Continue](/overthewire/Natas2324.md)