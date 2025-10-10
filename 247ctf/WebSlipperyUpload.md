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
app.config['UPLOAD_FOLDER'] = '/tmp/uploads/'

@app.route('/')
def source():
    return '
%s
' % open('/app/run.py').read()

def zip_extract(zarchive):
    with zipfile.ZipFile(zarchive, 'r') as z:
        for i in z.infolist():
            with open(os.path.join(app.config['UPLOAD_FOLDER'], i.filename), 'wb') as f:
                f.write(z.open(i.filename, 'r').read())

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

# Creating the exploit zip file
https://github.com/ptoomey3/evilarc
https://github.com/ptoomey3/evilarc/blob/master/evilarc.py

curl -X POST -Fzarchive=@evil.zip https://6bf4d0741bb9c294.247ctf.com/zip_upload
```

## Flag


## Continue
[Continue](../247ctf/WebSlipperyUpload.md)