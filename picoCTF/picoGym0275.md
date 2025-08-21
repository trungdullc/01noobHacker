# picoGym Level 275: Inspect HTML
Source: https://play.picoctf.org/practice/challenge/275

## Goal
Can you get the flag?<br>
Go to this website and see what you can discover.<br>
http://saturn.picoctf.net:58988/

## What I learned
```
HTML source code (Ctrl+U in browser)
Network requests (browser dev tools → Network tab)
JavaScript files (hidden logic, flags sometimes inside)
CSS file (hidden comment)
Cookies and storage (Inspect → Application tab)
```

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>On Histiaeus</title>
  </head>
  <body>
    <h1>On Histiaeus</h1>
    <p>However, according to Herodotus, Histiaeus was unhappy having to stay in
       Susa, and made plans to return to his position as King of Miletus by 
       instigating a revolt in Ionia. In 499 BC, he shaved the head of his 
       most trusted slave, tattooed a message on his head, and then waited for 
       his hair to grow back. The slave was then sent to Aristagoras, who was 
       instructed to shave the slave's head again and read the message, which 
       told him to revolt against the Persians.</p>
    <br>
    <p> Source: Wikipedia on Histiaeus </p>
	<!--picoCTF{1n5p3t0r_0f_h7ml_fd5d57bd}--> 🔐
  </body>
</html>
```

## Flag
picoCTF{1n5p3t0r_0f_h7ml_fd5d57bd}

## Continue
[Continue](./picoGym0469.md)