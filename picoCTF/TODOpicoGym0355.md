# picoGym Level 355: Java Code Analysis!?!
Source: https://play.picoctf.org/practice/challenge/355

## Goal
BookShelf Pico, my premium online book-reading service.<br>
I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!<br>
Additional details will be available after launching your challenge instance.<br>
Here are the credentials to get you started:<br>
Username: "user"<br>
Password: "user"<br>
Source code can be downloaded here<br>
https://artifacts.picoctf.net/c/479/bookshelf-pico.zip
Website can be accessed here!<br>
http://saturn.picoctf.net:57163/

## What I learned
```
Youtube Source: https://www.youtube.com/watch?v=AT61XquM3mI
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/479/bookshelf-pico.zip
--2025-08-22 23:31:05--  https://artifacts.picoctf.net/c/479/bookshelf-pico.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5701821 (5.4M) [application/octet-stream]
Saving to: 'bookshelf-pico.zip'

bookshelf-pico.zip                                         100%[======================================================================================================================================>]   5.44M  1.83MB/s    in 3.0s    

2025-08-22 23:31:08 (1.83 MB/s) - 'bookshelf-pico.zip' saved [5701821/5701821]

AsianHacker-picoctf@webshell:/tmp$ unzip bookshelf-pico.zip 
AsianHacker-picoctf@webshell:/tmp$ rm bookshelf-pico.zip 
AsianHacker-picoctf@webshell:/tmp$ ls -la
total 28
drwxrwxrwt 1 root                root                 177 Aug 22 23:32 .
drwxr-xr-x 1 root                root                  70 Aug 22 23:30 ..
drwx------ 3 root                root                  41 Mar  5 02:13 .wine-0
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 4582 Dec  9  2022 README.md
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 1492 Jun  7  2022 build.gradle
drwxrwxr-x 3 AsianHacker-picoctf AsianHacker-picoctf   29 Jun  7  2022 gradle
-rwxrwxr-x 1 AsianHacker-picoctf AsianHacker-picoctf 5766 Jun  7  2022 gradlew
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 2763 Jun  7  2022 gradlew.bat
drwxr-xr-x 2 root                root                   6 Mar  5 02:09 hsperfdata_root
drwxr-xr-x 3 root                root                  45 Mar  5 02:13 node-compile-cache
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf   43 Jun  7  2022 settings.gradle
drwxrwxr-x 4 AsianHacker-picoctf AsianHacker-picoctf   42 Jun  7  2022 src
drwxrwxr-x 4 AsianHacker-picoctf AsianHacker-picoctf   49 Nov 26  2022 userdata
AsianHacker-picoctf@webshell:/tmp$ cat README.md 

# Login
Email: user
Password: user

# Click on Flag Book
# Inspect → Network
# Look at http://saturn.picoctf.net:57163/ xhr → Headers for JWT (Java Web Token)
Authorization                           Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiRnJlZSIsImlzcyI6ImJvb2tzaGVsZiIsImV4cCI6MTc1NjUxMDkwMywiaWF0IjoxNzU1OTA2MTAzLCJ1c2VySWQiOjEsImVtYWlsIjoidXNlciJ9.0hWH-mraS8u-3uGBVKm7vJ4MrYrNqZLwFo20LmAtxpw

# Decode JWT Online
https://cyberchef.io/#recipe=JWT_Decode()&input=ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SnliMnhsSWpvaVJuSmxaU0lzSW1semN5STZJbUp2YjJ0emFHVnNaaUlzSW1WNGNDSTZNVGMxTmpVeE1Ea3dNeXdpYVdGMElqb3hOelUxT1RBMk1UQXpMQ0oxYzJWeVNXUWlPakVzSW1WdFlXbHNJam9pZFhObGNpSjkuMGhXSC1tcmFTOHUtM3VHQlZLbTd2SjRNcllyTnFaTHdGbzIwTG1BdHhwdw
{
    "role": "Free",
    "iss": "bookshelf",
    "exp": 1756510903,
    "iat": 1755906103,
    "userId": 1,
    "email": "user"
}


```

## Flag


## Continue
[Continue](./picoGym0355.md)