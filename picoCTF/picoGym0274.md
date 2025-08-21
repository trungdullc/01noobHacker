# picoGym Level 274: Includes
Source: https://play.picoctf.org/practice/challenge/274

## Goal
Can you get the flag?<br>
Go to this website and see what you can discover.<br>
http://saturn.picoctf.net:51037/

## What I learned
```
HTML source code (Ctrl+U in browser)
Network requests (browser dev tools → Network tab)
JavaScript files (hidden logic, flags sometimes inside)
CSS file (hidden comment)
Cookies and storage (Inspect → Application tab)
```

## Side Quest
```
# serve index.html
<!DOCTYPE html>
<html>
<head>
  <title>Hacker's CTF Challenge</title>
</head>
<body>
  <h1>Hello from my container!</h1>
</body>
</html>

# Start simple web server
# server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080  # container's internal port
server = HTTPServer(("", PORT), SimpleHTTPRequestHandler)
print(f"Serving on port {PORT}")
server.serve_forever()

# Write Dockerfile
# Start from a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY index.html server.py ./

# Expose container port
EXPOSE 8080

# Run the server
CMD ["python", "server.py"]

# # Start from a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY index.html server.py ./

# Expose container port
EXPOSE 8080

# Run server
CMD ["python", "server.py"]



# Build the image
docker build -t pico-web .

# Run on a random port
docker run -d -p 0:8080 pico-web
  0       random available port on the host
  8080    container port

# Find the assigned port since random
docker ps
CONTAINER ID   IMAGE      COMMAND          PORTS                         NAMES
abcd1234       pico-web   "python server…"  0.0.0.0:58988👀->8080/tcp   nostalgic_fermi

# Client: Connect in browser
http://localhost:58988

# Name resolution via /etc/hosts or DNS
Linux / macOS:
  /etc/hosts
Windows:
  C:\Windows\System32\drivers\etc\hosts
```

## Solution
```
https://webshell.picoctf.org/

Burp Suite: Intercept On
# Note: Not pick up popup Request (Close Burp Suite)

# View Page Source
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css👀">
    <title>On Includes</title>
  </head>
  <body>
    <script src="script.js👀"></script>
  
    <h1>On Includes</h1>
    <p>Many programming languages and other computer files have a directive, 
       often called include (sometimes copy or import), that causes the 
       contents of a second file to be inserted into the original file. These 
       included files are called copybooks or header files. They are often used
       to define the physical layout of program data, pieces of procedural code
       and/or forward declarations while promoting encapsulation and the reuse
       of code.</p>
    <br>
    <p> Source: Wikipedia on Include directive </p>
    <button type="button" onclick="greetings();">Say hello</button>
  </body>
</html>

Browser: http://saturn.picoctf.net:51037/script.js
function greetings() {
  alert("This code is in a separate file!");
}
//  f7w_2of2_df589022} 👀

Browser: http://saturn.picoctf.net:51037/style.css
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */ 👀

# Modify flag
picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}🔐
```

## Flag
picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}

## Continue
[Continue](./picoGym0275.md)