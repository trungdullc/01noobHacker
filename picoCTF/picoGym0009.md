# picoGym Level 9: picobrowser
Source: https://play.picoctf.org/practice/challenge/9

## Goal
This website can be rendered only by picobrowser, go and catch the flag! <br>
https://jupiter.challenges.picoctf.org/problem/28921/ or<br>
http://jupiter.challenges.picoctf.org:28921

## What I learned
```
http header
```             

## Solution
```
https://webshell.picoctf.org/

Browser: http://jupiter.challenges.picoctf.org:28921
# Click Flag button
You're not picobrowser! Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0

# Burp Suite
Browser: http://jupiter.challenges.picoctf.org:28921/
Proxy → Intercept on
# Click on Flag
# Send Request to Repeater

GET /flag HTTP/1.1
Host: jupiter.challenges.picoctf.org:28921
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: picobrowser 👀
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://jupiter.challenges.picoctf.org:28921/
Accept-Encoding: gzip, deflate, br
Cookie: _ga=GA1.2.647513796.1755785140; _ga_L6FT52K063=GS2.2.s1755785141$o1$g1$t1755785333$j60$l0$h844368113
Connection: keep-alive

Result:
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 2115
Set-Cookie: session=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/

<!DOCTYPE html>
<html lang="en">

<head>
    <title>My New Website</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="/">Home</a>
                    </li>
                    <li role="presentation"><a href="/unimplemented">Sign In</a>
                    </li>
                    <li role="presentation"><a href="/unimplemented">Sign Out</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">My New Website</h3>
        </div>
       <!-- Categories: success (green), info (blue), warning (yellow), danger (red) -->
       <div class="alert alert-success alert-dismissible" role="alert" id="myAlert">
         <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
         <!-- <strong>Title</strong> --> picobrowser!
           </div>
        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{p1c0_s3cr3t_ag3nt_84f9c865}</code></p> 🔐
            <!-- <p><a class="btn btn-lg btn-success" href="admin" role="button">Click here for the flag!</a> -->
            <!-- </p> -->
        </div>
        <footer class="footer">
            <p>&copy; PicoCTF 2019</p>
        </footer>
    </div>
    <script>
    $(document).ready(function(){
        $(".close").click(function(){
            $("myAlert").alert("close");
        });
    });
    </script>
</body>
</html>
```

## Flag
picoCTF{p1c0_s3cr3t_ag3nt_84f9c865}

## Continue
[Continue](./picoGym0124.md)