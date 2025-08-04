# Natas Level 2 → Level 3 robots.txt

## Previous Flag
<b>3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH</b>

## Goal
Username: natas3<br>
URL: http://natas3.natas.labs.overthewire.org<br>

There is nothing on this page

## What I learned
```
robots.txt exists on servers to tell crawlers and other web bots which part on website can be visited
    Sitemap also gives web crawlers info about website
```

## Solution
```
F12

<div id="content">
There is nothing on this page
<!-- No more information leaks!! Not even Google will find it this time... -->
</div>

http://natas3.natas.labs.overthewire.org/robots.txt

User-agent: *
Disallow: /s3cr3t/

Allow: /

http://natas3.natas.labs.overthewire.org/s3cr3t/
http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ 🔐
```

## Flag
<b>QryZXc2e0zahULdHrtHxzyYkj59kUxLQ</b>

## Continue
[Continue](/overthewire/Natas0304.md)