# picoGym Level 69: Client-side-again
Source: https://play.picoctf.org/practice/challenge/69

## Goal
Can you break into this super secure portal?<br>
https://jupiter.challenges.picoctf.org/problem/56816/ or<br>
http://jupiter.challenges.picoctf.org:56816

## What I learned
```
JavaScript Beautifier: http://www.jsnice.org/

Obfuscation is making data hard to read or interpret without actually encrypting it. Common forms:

Encoding (like Base64)
    Converts binary data into ASCII characters
    Example: M → TQ== in Base64
    Double Base64 (Base64 encoded twice) is just a simple obfuscation: first encode, then encode again
Bit Flipping / Manual Tampering
    Changing certain bits to modify the data
    Often used in CTFs to test your ability to reverse obfuscation
Hex / URL Encoding
    Characters are replaced with codes like %20 for space or 0x41 for A
Custom schemes
    Sometimes CTFs use their own “scrambled” mapping to make it harder to read
```             

## Side Quest
```
# Docker
docker ps ⌨️
docker stop newContainer ⌨️
docker rm newContainer ⌨️
docker run --rm -p 80:80 -v C:\Users\Hacker\Downloads\temp:/usr/local/apache2/htdocs/ httpd ⌨️

Browser: localhost:80 ⌨️

cd .\Downloads\temp\ ⌨️
code . ⌨️
    Right Click: Format All Document
```

## Solution
```
https://webshell.picoctf.org/

Browser: http://jupiter.challenges.picoctf.org:56816 ⌨️
# View Page Source
<html>
<head>
<title>Secure Login Portal V2.0</title>
</head>
<body background="barbed_wire.jpeg" >
<!-- standard MD5 implementation -->
<script type="text/javascript" src="md5.js"></script>

<script type="text/javascript"> 👀
  var _0x5a46=['37115}','_again_3','this','Password\x20Verified','Incorrect\x20password','getElementById','value','substring','picoCTF{','not_this'];(function(_0x4bd822,_0x2bd6f7){var _0xb4bdb3=function(_0x1d68f6){while(--_0x1d68f6){_0x4bd822['push'](_0x4bd822['shift']());}};_0xb4bdb3(++_0x2bd6f7);}(_0x5a46,0x1b3));var _0x4b5b=function(_0x2d8f05,_0x4b81bb){_0x2d8f05=_0x2d8f05-0x0;var _0x4d74cb=_0x5a46[_0x2d8f05];return _0x4d74cb;};function verify(){checkpass=document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];split=0x4;if(checkpass[_0x4b5b('0x2')](0x0,split*0x2)==_0x4b5b('0x3')){if(checkpass[_0x4b5b('0x2')](0x7,0x9)=='{n'){if(checkpass[_0x4b5b('0x2')](split*0x2,split*0x2*0x2)==_0x4b5b('0x4')){if(checkpass[_0x4b5b('0x2')](0x3,0x6)=='oCT'){if(checkpass[_0x4b5b('0x2')](split*0x3*0x2,split*0x4*0x2)==_0x4b5b('0x5')){if(checkpass['substring'](0x6,0xb)=='F{not'){if(checkpass[_0x4b5b('0x2')](split*0x2*0x2,split*0x3*0x2)==_0x4b5b('0x6')){if(checkpass[_0x4b5b('0x2')](0xc,0x10)==_0x4b5b('0x7')){alert(_0x4b5b('0x8'));}}}}}}}}else{alert(_0x4b5b('0x9'));}}
</script>
<div style="position:relative; padding:5px;top:50px; left:38%; width:350px; height:140px; background-color:gray">
<div style="text-align:center">
<p>New and Improved Login</p>

<p>Enter valid credentials to proceed</p>
<form action="index.html" method="post">
<input type="password" id="pass" size="8" />
<br/>
<input type="submit" value="verify" onclick="verify(); return false;" />
</form>
</div>
</div>
</body>
</html>

# Web Console
_0x4b5b ⌨️
ƒ (_0x2d8f05,_0x4b81bb){_0x2d8f05=_0x2d8f05-0x0;var _0x4d74cb=_0x5a46[_0x2d8f05];return _0x4d74cb;}
_0x4b5b("0x0") ⌨️
'getElementById'
_0x4b5b("0x1") ⌨️
'value'
_0x4b5b("0x2") ⌨️
'substring'
_0x4b5b("0x3") ⌨️
'picoCTF{'
_0x4b5b("0x4") ⌨️
'not_this'
_0x4b5b("0x5") ⌨️
'37115}'
_0x4b5b("0x6") ⌨️
'_again_3'
_0x4b5b("0x7") ⌨️
'this'
_0x4b5b("0x8") ⌨️
'Password Verified'
_0x4b5b("0x9") ⌨️
'Incorrect password'

console.log(_0x4b5b('0x3') + _0x4b5b('0x4') + _0x4b5b('0x6') + _0x4b5b('0x5')); ⌨️
picoCTF{not_this_again_337115} 🔐
```

## Flag
picoCTF{not_this_again_337115}

## Continue
[Continue](./picoGym0109.md)