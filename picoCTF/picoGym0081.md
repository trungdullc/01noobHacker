# picoGym Level 81: like1000
Source: https://play.picoctf.org/practice/challenge/81

## Goal
This .tar file got tarred a lot.<br>
https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar

## What I learned
```
bash
python
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:/tmp$ wget https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar ⌨️
--2025-09-17 21:47:23--  https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10250240 (9.8M) [application/octet-stream]
Saving to: '1000.tar'

1000.tar                                           100%[=============================================================================================================>]   9.78M  1.82MB/s    in 5.4s    

2025-09-17 21:47:28 (1.82 MB/s) - '1000.tar' saved [10250240/10250240]

# Method 1: bash
AsianHacker-picoctf@webshell:/tmp$ tar -xf 1000.tar ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
1000.tar  999.tar 👀  dds1-alpine.flag.img  filler.txt  hsperfdata_root  node-compile-cache

# AsianHacker-picoctf@webshell:/tmp$ while ls *.tar 1> /dev/null 2>&1; do for f in *.tar; do tar -xf "$f" && rm "$f"; done; done ⌨️
AsianHacker-picoctf@webshell:/tmp$ vi bash_script.sh ⌨️
AsianHacker-picoctf@webshell:/tmp$ chmod +x bash_script.sh ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat bash_script.sh ⌨️
#!/bin/bash

# Loop until no more tar files are left
while ls *.tar 1> /dev/null 2>&1; do
    for f in *.tar; do
        echo "Extracting $f..."
        tar -xf "$f"
        rm "$f"  # optional: delete the tar after extracting
    done
done
AsianHacker-picoctf@webshell:/tmp$ ./bash_script.sh ⌨️
AsianHacker-picoctf@webshell:/tmp$ ls ⌨️
filler.txt  flag.png 👀  hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ cat filler.txt ⌨️
alkfdslkjf;lkjfdsa;lkjfdsa
AsianHacker-picoctf@webshell:/tmp$ sz flag.png ⌨️
picoCTF{l0t5_0f_TAR5} 🔐

# Method 2: python
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
import tarfile          # built-in Python module to read, create, and extract .tar, .tar.gz, .tar.bz2
import glob             # file pattern matching module
import os               # operating system interface module

def extract_recursive():
    iteration = 0
    while True:
        tar_files = sorted(glob.glob("*.tar"), reverse=True)
        if not tar_files:
            print("No more .tar files found. Done!")
            break

        iteration += 1
        print(f"\nIteration {iteration}, found {len(tar_files)} tar file(s)...")

        for filename in tar_files:
            print(f"Extracting {filename}...")
            try:
                with tarfile.open(filename) as tar:
                    tar.extractall()
                os.remove(filename)           # remove tar after extracting
            except Exception as e:
                print(f"Failed to extract {filename}: {e}")

if __name__ == "__main__":
    extract_recursive()

AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py ⌨️
```

## Flag
picoCTF{l0t5_0f_TAR5}

## Continue
[Continue](./picoGym0311.md)