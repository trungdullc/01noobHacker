# picoGym Level 427: WebDecode 🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/427

## Goal
Do you know how to use the web inspector?<br>
Start searching here to find the flag<br>
http://titan.picoctf.net:60891/

## What I learned
```
View Page Source
base64
```

## Solution
```
https://webshell.picoctf.org/

Browser: http://titan.picoctf.net:60891/
# Click on About
# Right click View Page Source ⌨️

<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <link href="style.css" rel="stylesheet"/>
  <link href="img/favicon.png" rel="shortcut icon" type="image/x-icon"/>
  <!-- font (google) -->
  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&amp;display=swap" rel="stylesheet"/>
  <title>
   About me
  </title>
 </head>
 <body>
  <header>
   <nav>
    <div class="logo-container">
     <a href="index.html">
      <img alt="logo" src="img/binding_dark.gif"/>
     </a>
    </div>
    <div class="navigation-container">
     <ul>
      <li>
       <a href="index.html">
        Home
       </a>
      </li>
      <li>
       <a href="about.html">
        About
       </a>
      </li>
      <li>
       <a href="contact.html">
        Contact
       </a>
      </li>
     </ul>
    </div>
   </nav>
  </header>
  <section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZjZmNmI3OGF9"> 👀
   <h1>
    Try inspecting the page!! You might find it there
   </h1>
   <!-- .about-container -->
  </section>
  <!-- .about -->
  <section class="why">
   <footer>
    <div class="bottombar">
     Copyright © 2023 Your_Name. All rights reserved.
    </div>
   </footer>
  </section>
 </body>
</html>

https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=Y0dsamIwTlVSbnQzWldKZmMzVmpZek56YzJaMWJHeDVYMlF6WXpCa1pXUmZaalptTm1JM09HRjk
  picoCTF{web_succ3ssfully_d3c0ded_f6f6b78a} 🔐

AsianHacker-picoctf@webshell:~$ echo -n "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZjZmNmI3OGF9" | base64 -d ⌨️
picoCTF{web_succ3ssfully_d3c0ded_f6f6b78a} 🔐

Method 2: curl
AsianHacker-picoctf@webshell:~$ curl -I http://titan.picoctf.net:60891/ ⌨️
HTTP/1.1 200 OK
Server: nginx/1.21.6
Date: Thu, 21 Aug 2025 22:30:37 GMT
Content-Type: text/html
Content-Length: 1435
Last-Modified: Wed, 07 Feb 2024 17:25:48 GMT
Connection: keep-alive
ETag: "65c3bd1c-59b"
Accept-Ranges: bytes

AsianHacker-picoctf@webshell:~$ curl http://titan.picoctf.net:60891/ ⌨️
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <link rel="shortcut icon" href="img/favicon.png" type="image/x-icon">
  <!-- font (google) -->
  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <title>Home</title>
</head>
<body>
<header>
  <nav>
    <div class="logo-container">
      <a href="index.html"><img src="img/binding_dark.gif" alt="logo"></a>
    </div>
    <div class="navigation-container">
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
  </nav>
</header>
  <section class="banner">
    <h1>Ha!!!!!! You looking for a flag?</h1>
    <p>Keep Navigating</p>
  
  </section><!-- .banner -->
  <section class="sec-intro">
    <div class="col">
      <p>Haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</p>
      <p>Keepppppppppppppp Searchinggggggggggggggggggg</p>
      <img src="./img/multipage-html-img1.jpg" alt="person">
      <figcaption>Don't give up!</figcaption>
    </div>
  </section><!-- .sec-intro -->
  
  <footer>
    <div class="bottombar">Copyright © 2023 Your_Name. All rights reserved.</div>
  </footer>
  
</body>
</html>AsianHacker-picoctf@webshell:~$ curl http://titan.picoctf.net:60891/about.html ⌨️
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <link href="style.css" rel="stylesheet"/>
  <link href="img/favicon.png" rel="shortcut icon" type="image/x-icon"/>
  <!-- font (google) -->
  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&amp;display=swap" rel="stylesheet"/>
  <title>
   About me
  </title>
 </head>
 <body>
  <header>
   <nav>
    <div class="logo-container">
     <a href="index.html">
      <img alt="logo" src="img/binding_dark.gif"/>
     </a>
    </div>
    <div class="navigation-container">
     <ul>
      <li>
       <a href="index.html">
        Home
       </a>
      </li>
      <li>
       <a href="about.html">
        About
       </a>
      </li>
      <li>
       <a href="contact.html">
        Contact
       </a>
      </li>
     </ul>
    </div>
   </nav>
  </header>
  <section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZjZmNmI3OGF9"> 👀
   <h1>
    Try inspecting the page!! You might find it there
   </h1>
   <!-- .about-container -->
  </section>
  <!-- .about -->
  <section class="why">
   <footer>
    <div class="bottombar">
     Copyright © 2023 Your_Name. All rights reserved.
    </div>
   </footer>
  </section>
 </body>
</html>
```

## Flag
picoCTF{web_succ3ssfully_d3c0ded_f6f6b78a}

## Continue
[Continue](./picoGym0132.md)