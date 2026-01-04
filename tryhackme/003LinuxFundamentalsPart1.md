# Linux Fundamentals Part 1
```bash
# Start Machine
    Add 1 hour
    Terminate

AttackBox:
tryhackme@linux1:~$ ifconfig ⌨️
inet 10.0.3.5
tryhackme@linux1:~$ echo "Hi Hackers" ⌨️
Hi Hackers
tryhackme@linux1:~$ whoami ⌨️
tryhackme
```

# Task 5: Interacting with the Filesystem!
```bash
tryhackme@linux1:~$ ls ⌨️                             # listing
access.log folder1 folder2 folder3 folder4
tryhackme@linux1:~$ cd folder2 ⌨️                     # change directory
tryhackme@linux1:~/folder2$ ls ⌨️
tryhackme@linux1:~/folder2$ cd .. ⌨️
tryhackme@linux1:~$ cat access.log | head -n 5 ⌨️     # concatenating
tryhackme@linux1:~$ pwd ⌨️                            # print working directory
/home/tryhackme/
```

# Task 6: Searching for Files
```bash
# We know filename but not location
tryhackme@linux1:~$ find -name passwords.txt ⌨️
./folder4/passwords.txt
# word count
tryhackme@linux1:~$ wc -l /folder4/passwords.txt ⌨️
# We know extension only
tryhackme@linux1:~$ find -name *.txt ⌨️

Q1: Use grep on "access.log" to find the flag that has a prefix of "THM". What is the flag?
tryhackme@linux1:~$ grep "THM*" access.log 
13.127.130.212 - - [04/May/2021:08:35:26 +0000] "GET THM{ACCESS} lang=en HTTP/1.1" 404 360 "-"
```

# Task 7: An Introduction to Shell Operators
```bash
&:      This operator allows you to run commands in the background of your terminal.
        $ cp largefile.txt &
&&:     This operator allows you to combine multiple commands together in one line of your terminal.
>:      This operator is a redirector - meaning that we can take the output from a command (such as using cat to output a file) and direct it elsewhere.
>>:     This operator does the same function of the > operator but appends the output rather than replacing (meaning nothing is overwritten).

tryhackme@linux1:~$ sleep 60 & ⌨️
[9] 1337
# Check specific process in bg
tryhackme@linux1:~$ bg %9 ⌨️
[9]+ sleep 60 &
tryhackme@linux1:~$ fg %9 ⌨️
sleep 60
```