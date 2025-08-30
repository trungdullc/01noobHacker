# picoGym Level 278: Local Authority
Source: https://play.picoctf.org/practice/challenge/278

## Goal
Can you get the flag?<br>
Go to this website and see what you can discover.<br>
http://saturn.picoctf.net:50058/

## What I learned
```
Don't store passwords in JS code
```

## Solution
```
https://webshell.picoctf.org/

# SQL Injection (Failed)
;ls;
ls

Illegal character in username or password.

# Default user/pass (Failed)
admin
admin

Log In Failed

Browser: http://saturn.picoctf.net:50058/index.php (Nothing)
Browser: http://saturn.picoctf.net:50058/login.php

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Login Page</title>
  </head>
  <body>
    <script src="secure.js👀"></script>
    
    <p id='msg'></p>
    
    <form hidden action="admin.php👀" method="post" id="hiddenAdminForm">
      <input type="text" name="hash" required id="adminFormHash">
    </form>
    
    <script type="text/javascript">
      function filter(string) {
        filterPassed = true;
        for (let i =0; i < string.length; i++){
          cc = string.charCodeAt(i);
          
          if ( (cc >= 48 && cc <= 57) ||
               (cc >= 65 && cc <= 90) ||
               (cc >= 97 && cc <= 122) )
          {
            filterPassed = true;     
          }
          else
          {
            return false;
          }
        }
        
        return true;
      }
    
      window.username = "";
      window.password = "";
      
      usernameFilterPassed = filter(window.username);
      passwordFilterPassed = filter(window.password);
      
      if ( usernameFilterPassed && passwordFilterPassed ) {
      
        loggedIn = checkPassword(window.username, window.password);
        
        if(loggedIn)
        {
          document.getElementById('msg').innerHTML = "Log In Successful";
          document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881";
          document.getElementById('hiddenAdminForm').submit();
        }
        else
        {
          document.getElementById('msg').innerHTML = "Log In Failed";
        }
      }
      else {
        document.getElementById('msg').innerHTML = "Illegal character in username or password."
      }
    </script>
    
  </body>
</html>

Browser: http://saturn.picoctf.net:50058/admin.php (Failed)
Not Authorized
Browser: http://saturn.picoctf.net:50058/secure.js
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' ) 👀
  {
    return true;
  }
  else
  {
    return false;
  }
}

# Found
admin
strongPassword098765

# Redirected: http://saturn.picoctf.net:50058/admin.php
picoCTF{j5_15_7r4n5p4r3n7_05df90c8} 🔐
```

## Flag
picoCTF{j5_15_7r4n5p4r3n7_05df90c8}

## Continue
[Continue](./picoGym0018.md)