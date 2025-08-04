# Natas Level 0 Inspect & html comments in source code

## Previous Flag
<b>natas0</b>

## Goal
Start here:<br>
Username: natas0<br>
Password: natas0<br>
URL: http://natas0.natas.labs.overthewire.org<br>

You can find the password for the next level <b>on this page<b>

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
# Install Apache
sudo apt install apache2 apache2-utils

# Add a password
sudo htpasswd -c /etc/apache2/.htpasswd natas1

# Edit site config
sudo nano /etc/apache2/sites-available/000-default.conf

# Add inside <VirtualHost *:80>
<Directory "/var/www/html/natas1">
    AuthType Basic
    AuthName "Restricted Area"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>

# Create /var/www/html/natas1/index.html with test content
<h1>Welcome to Natas1</h1>

# Restart Apache
sudo systemctl restart apache2

Visit: http://localhost/natas1
```

## Example: 🐳 Docker Setup (Nginx + Basic Auth)
```
File structure
natas-nginx/
├── Dockerfile
├── nginx.conf
├── .htpasswd
└── html/
    └── index.html

Dockerfile
    FROM nginx:latest

    # Copy config and web files
    COPY nginx.conf /etc/nginx/nginx.conf
    COPY .htpasswd /etc/nginx/.htpasswd
    COPY html /usr/share/nginx/html

nginx.conf
    events {}

    http {
        server {
            listen 80;
            server_name localhost;

            location / {
                auth_basic "Restricted Area";
                auth_basic_user_file /etc/nginx/.htpasswd;
                root /usr/share/nginx/html;
                index index.html;
            }
        }
    }

html/index.html
    <!DOCTYPE html>
    <html>
    <head><title>Natas1 - Nginx</title></head>
    <body><h1>Secret: Welcome to Natas-style login</h1></body>
    </html>

Generate .htpasswd w/ htpasswd from Apache utils
    htpasswd -cb .htpasswd natas1 mysecretpassword

Or use OpenSSL alternative if htpasswd isn't available
    printf "natas1:$(openssl passwd -apr1 mysecretpassword)\n" > .htpasswd

Build & Run the container
    docker build -t natas-nginx .
    docker run -d -p 8081:80 --name natas-nginx-test natas-nginx
    Open: http://localhost:8081
    Login with: natas1 : mysecretpassword
```

## Example: 🐳 Docker Setup (Nginx + Enhanced Auth w/ Password hashing (Apache MD5 - $apr1$) & SSL support (self-signed certificate))
```
File Structure
    natas-nginx-ssl/
    ├── Dockerfile
    ├── nginx.conf
    ├── .htpasswd
    ├── certs/
    │   ├── selfsigned.crt
    │   └── selfsigned.key
    └── html/
        └── index.html

Dockerfile
    FROM nginx:latest

    # Copy config, SSL certs, password file, and web files
    COPY nginx.conf /etc/nginx/nginx.conf
    COPY .htpasswd /etc/nginx/.htpasswd
    COPY certs /etc/nginx/certs
    COPY html /usr/share/nginx/html

nginx.conf (with HTTPS + auth)
    events {}

    http {
        server {
            listen 443 ssl;
            server_name localhost;

            ssl_certificate     /etc/nginx/certs/selfsigned.crt;
            ssl_certificate_key /etc/nginx/certs/selfsigned.key;

            location / {
                auth_basic "Restricted Area";
                auth_basic_user_file /etc/nginx/.htpasswd;
                root /usr/share/nginx/html;
                index index.html;
            }
        }
    }

html/index.html
    <!DOCTYPE html>
    <html>
    <head><title>Natas Secure</title></head>
    <body><h1>Welcome to the secure Natas login</h1></body>
    </html>

# -c flag is only used for the first user to create file
.htpasswd (Create securely)
    htpasswd -c .htpasswd natas1
    htpasswd .htpasswd natas2
    htpasswd .htpasswd admin
# Each line is like: natas1:$apr1$P...hashedpass...
# Manual: openssl passwd -apr1

Generate Self-Signed SSL Cert
    mkdir certs
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout certs/selfsigned.key \
    -out certs/selfsigned.crt \
    -subj "/CN=localhost"

Build and Run (Self-signed certificate on port 8443)
    docker build -t natas-nginx-ssl .
    docker run -d -p 8443:443 --name natas-ssl natas-nginx-ssl
    Go to: https://localhost:8443
    Chrome/Firefox will warn about self-signed cert
    Login with any of your .htpasswd users.
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