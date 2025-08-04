# Natas Level 0 Inspect & html comments

## Previous Flag
<b>natas0</b>

## Goal
```
Start here:
Username: natas0
Password: natas0
URL:      http://natas0.natas.labs.overthewire.org
```
![alt text](/static/nataslogin.png "Natas Login")

## What I learned
```
Natas teaches the basics of serverside web-security
All passwords are also stored in /etc/natas_webpass/

Each lvl has its own website http://natasX.natas.labs.overthewire.org (X = lvl number)
There is no SSH login like in bandit.

curl or wget to DL website source code
Apache/Nginx handles HTTP Basic Authentication
```

## Side Quest Apache: HTTP Basic Auth Setup
```
# Enable mod_auth_basic (usually enabled by default)
sudo a2enmod auth_basic
sudo systemctl restart apache2

# Create a password file
sudo htpasswd -c /etc/apache2/.htpasswd natas1
# Enter and confirm password when prompted

# Configure your site’s .htaccess
# Place in /var/www/html/natas1/.htaccess or inside Apache site config:
    AuthType Basic
    AuthName "Restricted Area"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
# Or inside a <Directory> block in /etc/apache2/sites-available/000-default.conf:
    <Directory /var/www/html/natas1>
        AuthType Basic
        AuthName "Restricted Area"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user
    </Directory>
# Restart Apache
sudo systemctl restart apache2
```

## Side Quest Nginx: HTTP Basic Auth Setup
```
# Install htpasswd tool
sudo apt install apache2-utils
# Create password file
sudo htpasswd -c /etc/nginx/.htpasswd natas1
# Edit Nginx config
# In your site’s block (e.g., /etc/nginx/sites-available/default):
    location /natas1/ {
        auth_basic "Restricted Area";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
# Reload Nginx
sudo nginx -t
sudo systemctl reload nginx
```

## Example: 🐳 Docker Setup (Apache + Basic Auth)
```
File Structure:
    natas-apache/
    ├── Dockerfile
    ├── .htpasswd
    ├── index.html
    └── apache.conf

Dockerfile
    FROM httpd:2.4

    # Copy custom config and files
    COPY apache.conf /usr/local/apache2/conf/httpd.conf
    COPY .htpasswd /usr/local/apache2/.htpasswd
    COPY index.html /usr/local/apache2/htdocs/index.html

apache.conf (Basic Auth setup)
    ServerName localhost

    Listen 80

    LoadModule auth_basic_module modules/mod_auth_basic.so
    LoadModule authn_file_module modules/mod_authn_file.so

    DocumentRoot "/usr/local/apache2/htdocs"
    <Directory "/usr/local/apache2/htdocs">
        AuthType Basic
        AuthName "Natas Login"
        AuthUserFile "/usr/local/apache2/.htpasswd"
        Require valid-user
    </Directory>

index.html
<!DOCTYPE html>
    <html>
    <head><title>Natas1</title></head>
    <body><h1>Secret Zone</h1></body>
    </html>

Create .htpasswd
    htpasswd -cb .htpasswd natas1 mysecretpassword

Build and run:
    docker build -t natas-apache .
    docker run -d -p 8080:80 --name natas-test natas-apache
    Visit: http://localhost:8080 — login with natas1 : mysecretpassword
```

## Example: Local Dev Setup (Apache)
```

```

## Solution
```
Inspect or F12
<div id="content">
You can find the password for the next level on this page.

<!--The password for natas1 is 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq --> 🔐
</div>
```

## Flag
<b>0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq</b>

## Continue
[Continue](/overthewire/Natas0001.md)