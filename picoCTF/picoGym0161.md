# picoGym Level 161: Scavenger Hunt
Source: https://play.picoctf.org/practice/challenge/161

## Goal
There is some interesting information hidden around this site http://mercury.picoctf.net:27278/.<br>
Can you find it?

## What I learned
```
Apache / Web hidden files
  .htaccess                     Per-directory config (rewrites, access rules)
  .htpasswd                     Stores HTTP Basic Auth usernames/password hashes
  .htgroup                      Defines user groups for auth
  .user.ini                     PHP per-directory config override (similar to .htaccess but for PHP)
  .env                          Environment variables (often leaks DB creds, API keys)
  .DS_Store                     MacOS metadata file; may reveal filenames
  .git/ (directory)             Whole Git repo (commit history, code)
  .svn/                         Subversion repo metadata
  .hg/                          Mercurial repo metadata
  .bash_history                 Sometimes left behind if admins made mistakes
  phpinfo.php                   (not hidden but commonly left for debugging)
  config.php, db.php            Credentials for database
  backup.zip, site.bak, old/    Common accidental leftovers
```

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<!doctype html>
<html>
  <head>
    <title>Scavenger Hunt</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="mycss.css👀">
    <script type="application/javascript" src="myjs.js👀"></script>
  </head>
  <body>
    <div class="container">
      <header>
		<h1>Just some boring HTML</h1>
      </header>
      <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen">How</button>
      <button class="tablink" onclick="openTab('tababout', this, '#222')">What</button>
      <div id="tabintro" class="tabcontent">
		<h3>How</h3>
		<p>How do you like my website?</p>
      </div>
      <div id="tababout" class="tabcontent">
		<h3>What</h3>
		<p>I used these to make this site: <br/>
		  HTML <br/>
		  CSS <br/>
		  JS (JavaScript)
		</p>
	<!-- Here's the first part of the flag: picoCTF{t -->👀 
      </div>
    </div>
  </body>
</html>

Browser: http://mercury.picoctf.net:27278/mycss.css
div.container {
    width: 100%;
}

header {
    background-color: black;
    padding: 1em;
    color: white;
    clear: left;
    text-align: center;
}

body {
    font-family: Roboto;
}

h1 {
    color: white;
}

p {
    font-family: "Open Sans";
}

.tablink {
    background-color: #555;
    color: white;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    font-size: 17px;
    width: 50%;
}

.tablink:hover {
    background-color: #777;
}

.tabcontent {
    color: #111;
    display: none;
    padding: 50px;
    text-align: center;
}

#tabintro { background-color: #ccc; }
#tababout { background-color: #ccc; }

/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */👀

Browser: http://mercury.picoctf.net:27278/myjs.js
function openTab(tabName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
	tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
	tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(tabName).style.display = "block";
    if(elmnt.style != null) {
	elmnt.style.backgroundColor = color;
    }
}

window.onload = function() {
    openTab('tabintro', this, '#222');
}

/* How can I keep Google from indexing my website? */ 👀

Browser: http://mercury.picoctf.net:27278/robots.txt
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c 👀
# I think this is an apache server... can you Access the next flag?

Browser: http://mercury.picoctf.net:27278/.htaccess
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.

Browser: http://mercury.picoctf.net:27278/.DS_Store
Congrats! You completed the scavenger hunt. Part 5: _a69684fd}

# Rebuild Flag
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_a69684fd} 🔐
```

## Flag
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_a69684fd}

## Continue
[Continue](./picoGym0488.md)