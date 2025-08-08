# Natas Level 7 → Level 8 Reverse an encryption bin2hex(strrev(base64_encode($secret)))

## Previous Flag
<b>xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q</b>

## Goal
Username: natas8<br>
URL: http://natas8.natas.labs.overthewire.org<br>

Input secret: <br>
View sourcecode

## What I learned
```
base64_encode($secret)          Converts string into Base64 format
strrev(...)                     Reverses Base64-encoded string
bin2hex(...)                    Converts it into hexadecimal

Learn how to use CyberChef (Drag)
https://gchq.github.io/CyberChef/

PHP Sandbox:
    https://3v4l.org/#vnull
```

## Solution
```
Click view source Code
http://natas8.natas.labs.overthewire.org/index-source.html

<div id="content">

<?
$encodedSecret = "3d3d516343746d4d6d6c315669563362"; 👀

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret))); 👀
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>

<form method=post>
Input secret: <input name=secret><br>
<input type=submit name=submit>
</form>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>

https://gchq.github.io/CyberChef/ ⌨️
# Convert Hex to bin (Drag: From Hex)
==QcCtmMml1ViV3b

# Need reverse (Drag: Reverse)
b3ViV1lmMmtCcQ==

# Convert to base64 (Drag: From Base64)
oubWYf2kBq 👀

@trungdullc ➜ /workspaces/01noobHacker (main) $ vi decode.php ⌨️
@trungdullc ➜ /workspaces/01noobHacker (main) $ cat decode.php ⌨️
<?php
$encoded = "3d3d516343746d4d6d6c315669563362";

// Step 1: hex → binary
$step1 = hex2bin($encoded);

// Step 2: reverse string
$step2 = strrev($step1);

// Step 3: base64 decode
$originalSecret = base64_decode($step2);

echo "Decoded secret: $originalSecret\n";
?>
@trungdullc ➜ /workspaces/01noobHacker (main) $ php decode.php ⌨️
Xdebug: [Step Debug] Could not connect to debugging client. Tried: localhost:9003 (through xdebug.client_host/xdebug.client_port).
Decoded secret: oubWYf2kBq 👀
@trungdullc ➜ /workspaces/01noobHacker (main) $ rm decode.php ⌨️
@trungdullc ➜ /workspaces/01noobHacker (main) $ php -r '$e="3d3d516343746d4d6d6c315669563362";echo base64_decode(strrev(hex2bin($e)))."\n";' ⌨️⭐⭐⭐⭐⭐
Xdebug: [Step Debug] Could not connect to debugging client. Tried: localhost:9003 (through xdebug.client_host/xdebug.client_port).
oubWYf2kBq 👀

# PHP Sandbox (php that makes most sense to me)
https://3v4l.org/#vnull ⌨️
<?php
function decodeSecret($secret){
  return base64_decode(strrev(hex2bin($secret)));
  }
  
print "The secret is: "; 
print decodeSecret("3d3d516343746d4d6d6c315669563362");
print "\n";
?>

Result for 8.2.20:
The secret is: oubWYf2kBq 👀

Input secret: oubWYf2kBq
Access granted. The password for natas9 is ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t 🔐
```

## Flag
<b>ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t</b>

## Continue
[Continue](/overthewire/Natas0809.md)