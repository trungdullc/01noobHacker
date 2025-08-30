# picoGym Level 46: logon
Source: https://play.picoctf.org/practice/challenge/46

## Goal
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at?<br>
https://jupiter.challenges.picoctf.org/problem/44573/ or<br>
http://jupiter.challenges.picoctf.org:44573

## What I learned
```
Inspect: Network    See all the libraries and external things index.html brought in
```

## Solution
```
https://webshell.picoctf.org/

Browser: http://jupiter.challenges.picoctf.org:44573 ⌨️
admin ⌨️
admin ⌨️
SUBMIT

Success: You logged in! Not sure you'll be able to see the flag though.
Inspect → Application → Cookies
Name        Value
admin       False 👀
password    admin
username    admin

# Modify False to True
Flag: 
picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc} 🔐
```

## Flag
picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc} 

## Continue
[Continue](./picoGym0066.md)