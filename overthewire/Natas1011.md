# Natas Level 10 → Level 11 Reverse an encryption

## Previous Flag
<b>UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk</b>

## Goal
Username: natas11<br>
URL: http://natas11.natas.labs.overthewire.org<br>

Cookies are protected with XOR encryption<br>
Background color: #ffffff<br>
View sourcecode

## What I learned
```
D = Data, K = Key, C = Ciphertext
D ^ K = C
D ^ C = K
Just need 2 of the 3 and XOR it to get the last
```

## Solution
```
Click View source code
http://natas11.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas11", "pass": "<censored>" };</script></head>
<?

$defaultdata = array("showpassword"=>"no", "bgcolor"=>"#ffffff"); 👀

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true); 👀
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}
saveData($data);
?>

<h1>natas11</h1>
<div id="content">
<body style="background: <?=$data['bgcolor']?>;">
Cookies are protected with XOR encryption<br/><br/>

<?
if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored><br>";
}

?>

<form>
Background color: <input name=bgcolor value="<?=$data['bgcolor']?>">
<input type=submit value="Set color">
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

F12 → Application
Storage → Cookies
Name        Value
data        HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GdGdfVXRnTRg%3D (URL Encoding)

CyberChef (URL Decode) or click Show URL-decode on developer tools
https://gchq.github.io/CyberChef/
HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GdGdfVXRnTRg=

PHP Sandbox:
    https://3v4l.org/#vnull
<?php
echo json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"))
?>

{"showpassword":"no","bgcolor":"#ffffff"}

curl -u natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk \
     -b "data=HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=" \
     http://natas11.natas.labs.overthewire.org/
```

## Flag

## Continue
[Continue](/overthewire/Natas1112.md)