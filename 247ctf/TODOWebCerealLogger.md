# Web: Cereal Logger

## Previous Flag
```
247CTF{61f66e2b26507d2498f78b4a77665cb8}
```

## Goal
Using a specially crafted cookie, you can write data to /dev/null. Can you abuse the write and read the flag?

## What I learned
```
Serialization is the process of converting a data structure or object into a format that can be stored or transmitted and then reconstructed later.

Think of it like turning your object in memory into a sequence of bytes or text so it can travel over a network, be saved to a file, or shared between programs — and later be deserialized back into the original object.

```

## Solution
```
START CHALLENGE

https://7c1e98ccb854270e.247ctf.com/

<?php

  class insert_log
  {
      public $new_data = "Valid access logged!";
      public function __destruct()
      {
          $this->pdo = new SQLite3("/tmp/log.db");
          $this->pdo->exec("INSERT INTO log (message) VALUES ('".$this->new_data."');");
      }
  }

  if (isset($_COOKIE["247"]) && explode(".", $_COOKIE["247"])[1].rand(0, 247247247) == "0") {
      file_put_contents("/dev/null", unserialize(base64_decode(explode(".", $_COOKIE["247"])[0])));
  } else {
      echo highlight_file(__FILE__, true);
  }

# https://www.programiz.com/php/online-compiler/
main.php
<?php
$a = "0e1337";
$b = "0e";

// Loose Comparision
if ($a == "0") {
    echo "A Pass\n";
}
else {
    echo "A Fail\n";
}

if ($b == "0") {
    echo "B Pass\n";
}
else {
    echo "B Fail\n";
}

?>

Output:
A Pass
B Fail

=== Code Execution Successful ===

This one going take longer
```

## Flag

## Continue
[Continue](../247ctf/WebCerealLogger.md)