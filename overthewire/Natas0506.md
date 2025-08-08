# Natas Level 5 → Level 6 include & require

## Previous Flag
<b>0RoJwHdSKWFTYR5WuiAewauSuNaBXned</b>

## Goal
Username: natas6<br>
URL: http://natas6.natas.labs.overthewire.org<br>

Input secret: <br>
View sourcecode

## What I learned
```
php is a scripting language usually used on server side
It's possible to include code from other files into a file by using include or require
```

## Side Quest
```
# Create a directory
mkdir natas && cd natas

vi index.php
    <?php
    include "includes/secret.inc";

    if (array_key_exists("submit", $_POST)) {
        if ($secret == $_POST['secret']) {
            echo "Access granted. The password for natas7 is <b>$real_password</b>";
        } else {
            echo "Wrong secret";
        }
    }
    ?>

    <form method="post">
        Input secret: <input name="secret"><br>
        <input type="submit" name="submit">
    </form>

vi includes/secret.inc
    <?php
        $secret = "letmein123";
        $real_password = "Natas7RealPasswordGoesHere";
    ?>

# Start PHP's built-in web server
php -S localhost:8080

Browser: http://localhost:8080
```

## Solution
```
Click view sourcecode link (because we can't see server php code)
http://natas6.natas.labs.overthewire.org/index-source.html

<?
include "includes/secret.inc"; 👀
    if(array_key_exists("submit", $_POST)) { 
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>

<form method=post>
Input secret: <input name=secret><br> 👀
<input type=submit name=submit>
</form>

http://natas6.natas.labs.overthewire.org/includes/secret.inc ⌨️
<?
$secret = "FOEIUWGHFEEUHOFUOIU"; 👀
?>

Access granted. The password for natas7 is bmg8SvU1LizuWjx3y7xkNERkHxGre0GS 🔐
```

## Flag
<b>bmg8SvU1LizuWjx3y7xkNERkHxGre0GS</b>

## Continue
[Continue](/overthewire/Natas0607.md)