# Natas Level 15 → Level 16 Restricted Blind SQL Injection

## Previous Flag
<b>hPkjKYviLQctEW33QmuXL6eDVfMW4sGo</b>

## Goal
Username: natas16<br>
URL: http://natas16.natas.labs.overthewire.org<br>

For security reasons, we now filter even more on certain characters<br>
Find words containing:<br>
Output:

## What I learned
```
bypass w/ grep since less restricted than sql
```

## Solution
```
Click View source code
http://natas16.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas16", "pass": "<censored>" };</script></head>
<body>
<h1>natas16</h1>
<div id="content">

For security reasons, we now filter even more on certain characters<br/><br/>
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
    if(preg_match('/[;|&`\'"]/',$key)) { 👀
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
?>
</pre>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

@trungdullc ➜ /workspaces/01noobHacker (main) $ python scripts/blindsqlinjectionfilter.py ⌨️
E
Eq
Eqj
EqjH
EqjHJ
EqjHJb
EqjHJbo
EqjHJbo7
EqjHJbo7L
EqjHJbo7LF
EqjHJbo7LFN
EqjHJbo7LFNb
EqjHJbo7LFNb8
EqjHJbo7LFNb8v
EqjHJbo7LFNb8vw
EqjHJbo7LFNb8vwh
EqjHJbo7LFNb8vwhH
EqjHJbo7LFNb8vwhHb
EqjHJbo7LFNb8vwhHb9
EqjHJbo7LFNb8vwhHb9s
EqjHJbo7LFNb8vwhHb9s7
EqjHJbo7LFNb8vwhHb9s75
EqjHJbo7LFNb8vwhHb9s75h
EqjHJbo7LFNb8vwhHb9s75ho
EqjHJbo7LFNb8vwhHb9s75hok
EqjHJbo7LFNb8vwhHb9s75hokh
EqjHJbo7LFNb8vwhHb9s75hokh5
EqjHJbo7LFNb8vwhHb9s75hokh5T
EqjHJbo7LFNb8vwhHb9s75hokh5TF
EqjHJbo7LFNb8vwhHb9s75hokh5TF0
EqjHJbo7LFNb8vwhHb9s75hokh5TF0O
EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC
EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC 🔐
```

## Flag
<b>EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC</b>

## Continue
[Continue](/overthewire/Natas1617.md)