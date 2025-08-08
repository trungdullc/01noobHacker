# Natas Level 1 → Level 2 File Path Weakness from images/audio

## Previous Flag
<b>TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI</b>

## Goal
Username: natas2<br>
URL: http://natas2.natas.labs.overthewire.org<br>

There is nothing on this page 

## What I learned
```
Find files path for weak spots
```

## Solution
```
F12 → Elements

<div id="content">
There is nothing on this page
<img src="files/pixel.png"> 👀
</div>

http://natas2.natas.labs.overthewire.org/files/ ⌨️
http://natas2.natas.labs.overthewire.org/files/users.txt ⌨️
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH 🔐
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

## Flag
<b>3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH</b>

## Continue
[Continue](/overthewire/Natas0203.md)