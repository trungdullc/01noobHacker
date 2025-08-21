# picoGym Level 0320: First Find
Source: https://play.picoctf.org/practice/challenge/320

## Goal
Unzip this archive and find the file named <b>uber-secret.txt</b>

## What I learned
```
man find
OPTIONS
-L              Follow symbolic links
-O1             (Default) filter based on file name first
-O2             File name first, then file-type
-O3             Automatically re-order search based on efficient use of resources and likelihood of success
-maxdepth X     Search this directory along with all sub-directories to a level of X
-iname          Search while ignoring text case.
-not            Only produce results that don’t match the test case
-type f         Look for files ❤️❤️❤️❤️❤️
-type d         Look for directories

find . -name FILE.txt
find /home -name *.jpg
find . -type f -empty                           # Look for empty file in current directory
find -O3 -L /var/www/ -name "*.html"
# Find all .db files (ignoring text case) that have been changed in preceding 6 days by a user called randomperson
find /home -user randomperson-mtime 6 -iname ".db"
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/502/files.zip ⌨️
--2025-08-17 03:25:23--  https://artifacts.picoctf.net/c/502/files.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.128, 3.160.22.16, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3995553 (3.8M) [application/octet-stream]
Saving to: 'files.zip'

files.zip                                                  100%[======================================================================================================================================>]   3.81M  1.82MB/s    in 2.1s    

2025-08-17 03:25:25 (1.82 MB/s) - 'files.zip' saved [3995553/3995553]

AsianHacker-picoctf@webshell:/tmp$ file files.zip ⌨️
files.zip: Zip archive data, at least v1.0 to extract, compression method=store
AsianHacker-picoctf@webshell:/tmp$ unzip files.zip ⌨️
Archive:  files.zip
   creating: files/
   creating: files/satisfactory_books/
   creating: files/satisfactory_books/more_books/
  inflating: files/satisfactory_books/more_books/37121.txt.utf-8  
  inflating: files/satisfactory_books/23765.txt.utf-8  
  inflating: files/satisfactory_books/16021.txt.utf-8  
  inflating: files/13771.txt.utf-8   
   creating: files/adequate_books/
   creating: files/adequate_books/more_books/
   creating: files/adequate_books/more_books/.secret/
   creating: files/adequate_books/more_books/.secret/deeper_secrets/
   creating: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
 extracting: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt  
  inflating: files/adequate_books/more_books/1023.txt.utf-8  
  inflating: files/adequate_books/46804-0.txt  
  inflating: files/adequate_books/44578.txt.utf-8  
   creating: files/acceptable_books/
   creating: files/acceptable_books/more_books/
  inflating: files/acceptable_books/more_books/40723.txt.utf-8  
  inflating: files/acceptable_books/17880.txt.utf-8  
  inflating: files/acceptable_books/17879.txt.utf-8  
  inflating: files/14789.txt.utf-8   
AsianHacker-picoctf@webshell:/tmp$ ls -la ⌨️
total 3904
drwxrwxrwt 1 root                root                     48 Aug 17 03:25 .
drwxr-xr-x 1 root                root                     70 Aug 17 02:57 ..
drwx------ 3 root                root                     41 Mar  5 02:13 .wine-0
drwxrwxr-x 5 AsianHacker-picoctf AsianHacker-picoctf     148 May 13  2022 files 👀
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 3995553 Aug  4  2023 files.zip
drwxr-xr-x 2 root                root                      6 Mar  5 02:09 hsperfdata_root
drwxr-xr-x 3 root                root                     45 Mar  5 02:13 node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ cd files ⌨️
AsianHacker-picoctf@webshell:/tmp/files$ ls -la ⌨️
total 1924
drwxrwxr-x 5 AsianHacker-picoctf AsianHacker-picoctf     148 May 13  2022 .
drwxrwxrwt 1 root                root                     48 Aug 17 03:25 ..
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 1003806 May  7  2022 13771.txt.utf-8
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf  960595 May  7  2022 14789.txt.utf-8
drwxrwxr-x 3 AsianHacker-picoctf AsianHacker-picoctf      86 May 13  2022 acceptable_books
drwxrwxr-x 3 AsianHacker-picoctf AsianHacker-picoctf      82 May 13  2022 adequate_books
drwxrwxr-x 3 AsianHacker-picoctf AsianHacker-picoctf      86 May 13  2022 satisfactory_books
AsianHacker-picoctf@webshell:/tmp/files$ whatis zip ⌨️
zip (1)              - package and compress (archive) files
AsianHacker-picoctf@webshell:/tmp/files$ whatis find ⌨️
find (1)             - search for files in a directory hierarchy
find (1posix)        - find files
AsianHacker-picoctf@webshell:/tmp/files$ man find ⌨️
AsianHacker-picoctf@webshell:/tmp/files$ find . -name uber-secret.txt ⌨️
./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt 👀
AsianHacker-picoctf@webshell:/tmp/files$ find . -type f -name uber-secret.txt ⌨️
./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt 👀
AsianHacker-picoctf@webshell:/tmp/files$ cat adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt ⌨️
picoCTF{f1nd_15_f457_ab443fd1} 🔐
AsianHacker-picoctf@webshell:/tmp/files$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
files  files.zip  hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ rm -rf files* ⌨️
```

## Flag
picoCTF{f1nd_15_f457_ab443fd1}

## Continue
[Continue](./picoGym0322.md)