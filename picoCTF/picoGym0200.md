# picoGym Level 200: login
Source: https://play.picoctf.org/practice/challenge/200

## Goal
My dog-sitter's brother made this website but I can't get in; can you help?<br>
login.mars.picoctf.net

## What I learned
```
btoa(document.querySelector(r[e]).value).replace(/=/g,"");
    base64 to ascii removes all =
username: YWRtaW4 👀
password: cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ 👀
```             

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="styles.css">
        <script src="index.js"></script> 👀
    </head>
    <body>
        <div>
          <h1>Login</h1>
          <form method="POST">
            <label for="username">Username</label>
            <input name="username" type="text"/>
            <label for="username">Password</label>
            <input name="password" type="password"/>
            <input type="submit" value="Submit"/>
          </form>
        </div>
    </body>
</html>

Browser: https://login.mars.picoctf.net/index.js

(async()=>{await new Promise((e=>window.addEventListener("load",e))),document.querySelector("form").addEventListener("submit",(e=>{e.preventDefault();const r={u:"input[name=username]",p:"input[name=password]"},t={};for(const e in r)t[e]=btoa(document.querySelector(r[e]).value).replace(/=/g,"");return"YWRtaW4"!==t.u?alert("Incorrect Username"):"cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ"!==t.p?alert("Incorrect Password"):void alert(`Correct Password! Your flag is ${atob(t.p)}.`)}))})(); 👀

AsianHacker-picoctf@webshell:~$ echo "YWRtaW4=" | base64 -d ⌨️
admin 👀
AsianHacker-picoctf@webshell:~$ echo "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ==" | base64 -d ⌨️
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r} 👀

# Alert
Correct Password! Your flag is picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}. 🔐
```

## Flag
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}

## Continue
[Continue](./picoGym0009.md)