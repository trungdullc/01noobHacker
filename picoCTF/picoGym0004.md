# picoGym Level 4: where are the robots
Source: https://play.picoctf.org/practice/challenge/4

## Goal
Can you find the robots?<br>
https://jupiter.challenges.picoctf.org/problem/36474/ or<br>
http://jupiter.challenges.picoctf.org:36474

## What I learned
```
robots.txt tells web crawlers (robots/spiders, like Googlebot, Bingbot) which parts of site they are allowed or not allowed to crawl
```

## Solution
```
https://webshell.picoctf.org/

Browser: http://jupiter.challenges.picoctf.org:36474/ ⌨️
# View Page Source (get a estimate where files are contained)

<!doctype html>
<html>
  <head>
    <title>Welcome</title>
    <link href="https://fonts.googleapis.com/css?family=Monoton|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="style.css👀">
  </head>

  <body>
    <div class="container">
      <header>
	<h1>Welcome</h1>
      </header>
      <div class="content">
	<p>Where are the robots?</p>
      </div>
      <footer></footer>
    </div>
  </body>
</html>

Browser: http://jupiter.challenges.picoctf.org:36474/robots.txt ⌨️
User-agent: *
Disallow: /477ce.html 👀

Browser: http://jupiter.challenges.picoctf.org:36474/477ce.html ⌨️

picoCTF{ca1cu1at1ng_Mach1n3s_477ce} 🔐
```

## Flag
picoCTF{ca1cu1at1ng_Mach1n3s_477ce}

## Continue
[Continue](./picoGym0427.md)