# picoGym Level 406: Bookmarklet 🧠🧠🧠🧠🧠
Source: https://play.picoctf.org/practice/challenge/406

## Goal
Why search for the flag when I can make a bookmarklet to print it for me?<br>
Browse here, and find the flag!<br>
http://titan.picoctf.net:64720/

## What I learned
```
bookmarklet is a bookmark that runs JavaScript instead of loading a webpage

In Browser (web page console, JS)
# clear
    console.clear();                                                    // clear()
# print
    console.log("Hello");
    console.table([{name:"Alice",age:20},{name:"Bob",age:30}]);         // nice table
# alert
    alert("Hi");
# input
    let name = prompt("Your name?");
    console.log(name);


In Terminal (Node.js)
# clear
    console.clear();
# print
    console.log("Hello");
    console.error("Oops!");                                             // prints to stderr
    console.warn("Warning");                                            // prints with yellow warning
# Inspect objects (pretty print)
    console.dir(obj, { depth: null });
# input
    const readline = require("readline");
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    rl.question("Your name? ", answer => { console.log("Hi", answer); rl.close(); });
# Run system commands (not built-in Bash echo)
    const { exec } = require("child_process");
    exec("ls", (err, stdout, stderr) => console.log(stdout));
```

## Solution
```
https://webshell.picoctf.org/

Given bookmarklet:
javascript:(function() {
    var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÒËÉ§©í";
    var key = "picoctf";
    var decryptedFlag = "";
    for (var i = 0; i < encryptedFlag.length; i++) {
        decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
    }
    alert(decryptedFlag);
})();

# Method 1: Web Console
# Inspect → Console
clear() ⌨️
# Copy JS fx and press Enter ⌨️

# Alert (popup)
titan.picoctf.net:64720
picoCTF{p@g3_turn3r_6bbf8953} 🔐

# Method 2: Node.js but modify alert since no popup in CLI
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ vi decrypt.js ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat decrypt.js ⌨️
var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÒËÉ§©í";
var key = "picoctf";
var decryptedFlag = "";

for (var i = 0; i < encryptedFlag.length; i++) {
    decryptedFlag += String.fromCharCode(
        (encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256
    );
}

console.log(decryptedFlag); 👀
AsianHacker-picoctf@webshell:/tmp$ node decrypt.js ⌨️
picoCTF{p@g3_turn3r_6bbf8953} 🔐

Method 3: Bookmark
Bookmarks > Manage Bookmarks > Add Bookmark
Paste in the code and click on the bookmarklet
# Note: Not work on Edge Browser
```

## Flag
picoCTF{p@g3_turn3r_6bbf8953}

## Continue
[Continue](./picoGym0492.md)