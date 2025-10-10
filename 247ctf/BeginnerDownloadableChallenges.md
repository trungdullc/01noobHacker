# Beginner Tutorial: Downloadable Challenges

## Previous Flag
```
247CTF{64b3c32a6856093faed367149ecaafb7}
```

## Goal
A number of challenges require you to download files in order to be able to solve them. All challenge files are served bundled in a zip archive without a password. While none of our challenges are malicious or intended to cause harm, we still recommend you use a virtual machine when downloading and running applications from websites you don't trust - including this one.<br>

Click on the ‘DOWNLOAD CHALLENGE’ button to the right of this text description to download the challenge and submit the flag!<br>
DOWNLOAD CHALLENGE (Not Work): https://247ctf.com/download/46

## What I learned
```
wget not work w/ Downloading Files on 247CTF
```

## Solution
```
AsianHacker-picoctf@webshell:~$ wget https://247ctf.com/download/46 ⌨️
--2025-10-08 21:54:16--  https://247ctf.com/download/46
Resolving 247ctf.com (247ctf.com)... 144.76.74.118
Connecting to 247ctf.com (247ctf.com)|144.76.74.118|:443... connected.
HTTP request sent, awaiting response... 302 FOUND
Location: https://247ctf.com/ [following]
--2025-10-08 21:54:17--  https://247ctf.com/
Reusing existing connection to 247ctf.com:443.
HTTP request sent, awaiting response... 200 OK
Length: 22303 (22K) [text/html]
Saving to: '46'

46                                                         100%[======================================================================================================================================>]  21.78K  --.-KB/s    in 0.001s  

2025-10-08 21:54:18 (14.9 MB/s) - '46' saved [22303/22303]

AsianHacker-picoctf@webshell:~$ file 46 ⌨️
46: HTML document, ASCII text, with very long lines (1823)
</html>AsianHacker-picoctf@webshell:~$ cat 46 | grep 247CTF ⌨️
  <title>247CTF - The game never stops</title>
  <meta name="description" content="247CTF is a security learning environment where hackers can test their abilities across a number of different Capture The Flag (CTF) challenge categories including web, cryptography, networking, reversing and exploitation." />
  <meta property="og:title" content="247CTF - The game never stops" />
  <meta property="og:description" content="247CTF is a security learning environment where hackers can test their abilities across a number of different Capture The Flag (CTF) challenge categories including web, cryptography, networking, reversing and exploitation." />
  <meta property="og:site_name" content="247CTF" />
  <meta name="twitter:description" content="247CTF is a security learning environment where hackers can test their abilities across a number of different Capture The Flag (CTF) challenge categories including web, cryptography, networking, reversing and exploitation." />
  <meta name="twitter:title" content="247CTF - The game never stops" />
  <meta name="twitter:site" content="@247CTF" />
    <img data-aos="flip-left" class="logo p-1 m-3" src="/static/images/logo.png" alt="247CTF">
      Most competitions are only online for a few days. The 247CTF is a continuous learning environment.
    <a class="clickable" href="https://twitter.com/247CTF"><i class="fab fa-twitter pt-2 mr-3 fs15"></i></a>
    <a class="clickable" href="https://www.youtube.com/247CTF"><i class="fab fa-youtube pt-2 mr-3 fs15"></i></a>
    <a class="clickable" href="https://www.patreon.com/247CTF"><i class="fab fa-patreon pt-2 mr-3 fs15"></i></a>
    <a class="clickable" href="mailto:247CTF@gmail.com?Subject=247CTF"><i class="fas fa-envelope pt-2 mr-3 fs15"></i></a>

# Method 1:
# Note: wget not work
AsianHacker-picoctf@webshell:~$ rz ⌨️
AsianHacker-picoctf@webshell:~$ unzip 9353ba2f7ad8f5d85cbbfebd1471efb758d6911a.zip ⌨️
Archive:  9353ba2f7ad8f5d85cbbfebd1471efb758d6911a.zip
  inflating: flag.txt
AsianHacker-picoctf@webshell:~$ cat flag.txt ⌨️
247CTF{518fe2c33b05618278e59c7f8bf69d5e}
```

## Flag
247CTF{518fe2c33b05618278e59c7f8bf69d5e}

## Continue
[Continue](../247ctf/BeginnerWebChallenges)