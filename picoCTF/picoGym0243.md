# picoGym Level 0243: HashingJobApp
Source: https://play.picoctf.org/practice/challenge/243

## Goal
If you want to hash with the best, beat this test!<br>
nc saturn.picoctf.net 57060

## What I learned
```
CyberChef
md5sum
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ tmux new-session \; split-window -h \; attach ⌨️❤️❤️❤️❤️❤️

# Note (switch in webshell): Use ctrl + b + o ⭐⭐⭐⭐⭐                            # Important: echo -n to exclude \n from calculation
AsianHacker-picoctf@webshell:~$ nc saturn.picoctf.net 57060 ⌨️                        │AsianHacker-picoctf@webshell:~$ echo -n "musicals" | md5sum ⌨️
Please md5 hash the text between quotes, excluding the quotes: 'musicals'             │fb93d71bbad4b9be2e167c0914bbd83e  -
Answer:                                                                               │AsianHacker-picoctf@webshell:~$ echo -n "a treehouse" | md5sum ⌨️
fb93d71bbad4b9be2e167c0914bbd83e ⌨️                                                   │98b0ee4dfd8e04322c60bd32481b512e  -
fb93d71bbad4b9be2e167c0914bbd83e                                                      │AsianHacker-picoctf@webshell:~$ echo -n "hairballs" |md5sum ⌨️
Correct.                                                                              │360927e98748b8675251a4a68b637b4b  -
Please md5 hash the text between quotes, excluding the quotes: 'a treehouse'          │AsianHacker-picoctf@webshell:~$ whatis md5sum ⌨️
Answer:                                                                               │md5sum (1)           - compute and check MD5 message digest
98b0ee4dfd8e04322c60bd32481b512e ⌨️                                                   │
98b0ee4dfd8e04322c60bd32481b512e                                                      │
Correct.                                                                              │
Please md5 hash the text between quotes, excluding the quotes: 'hairballs'            │
Answer:                                                                               │
360927e98748b8675251a4a68b637b4b ⌨️                                                   │
360927e98748b8675251a4a68b637b4b                                                      │
Correct.                                                                              │
picoCTF{4ppl1c4710n_r3c31v3d_674c1de2} 🔐                                             │

# Method 2: CyberChef
https://cyberchef.io/#recipe=MD5()&input=bXVzaWNhbHM
https://cyberchef.io/#recipe=MD5()&input=YSB0cmVlaG91c2U
https://cyberchef.io/#recipe=MD5()&input=aGFpcmJhbGxz
```

## Flag
picoCTF{4ppl1c4710n_r3c31v3d_674c1de2}

## Continue
[Continue](./picoGym0245.md)