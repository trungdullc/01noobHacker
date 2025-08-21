# picoGym Level 0442: Binary Search
Source: https://play.picoctf.org/practice/challenge/442

## Goal
Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.
Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!<br>
ssh -p 56697 ctf-player@atlas.picoctf.net<br>
Using the password <b>6abf4a82</b>. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!

## What I learned
```
Setup shell to go directly into bash script and exit when done
    Modifying SSH configuration with ForceCommand in sshd_config
    Setting user's shell to a script in /etc/passwd
    Using wrappers or specific configuration files/.bash_profile or /.ssh/rc

binary-search.sh
#!/usr/bin/env bash
exec /opt/game/binary-search                    # exec replaces the shell; no shell remains

# Make it executable and not writable by any user
sudo chown root:root /opt/game/binary-search /opt/game/binary-search.sh
sudo chmod 755 /opt/game/binary-search /opt/game/binary-search.sh

# Method 1: ForceCommand in sshd_config (clean + hard to bypass)
# /etc/ssh/sshd_config
Match User ctf-player
    ForceCommand /opt/game/binary-search.sh 👀
    PermitTTY yes 👀                                # if game needs interactive input
    AllowTcpForwarding no
    X11Forwarding no
    PermitTunnel no

sudo systemctl reload sshd                          # ssh
# Now any SSH login as ctf-player runs /opt/game/binary-search.sh

# Method 2: Use profile scripts (Weaker, easier to bypass)
echo 'exec /opt/game/binary-search' >> ~ctf-player/.bash_profile
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh -p 56697 ctf-player@atlas.picoctf.net ⌨️
The authenticity of host '[atlas.picoctf.net]:56697 ([18.217.83.136]:56697)' can't be established.
ED25519 key fingerprint is SHA256:M8hXanE8l/Yzfs8iuxNsuFL4vCzCKEIlM/3hpO13tfQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[atlas.picoctf.net]:56697' (ED25519) to the list of known hosts.
ctf-player@atlas.picoctf.net's password: ⌨️
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500 ⌨️
Lower! Try again.
Enter your guess: 250 ⌨️
Higher! Try again.
Enter your guess: 350 ⌨️
Higher! Try again.
Enter your guess: 400 ⌨️
Lower! Try again.
Enter your guess: 375 ⌨️
Higher! Try again.
Enter your guess: 382 ⌨️
Higher! Try again.
Enter your guess: 390 ⌨️
Lower! Try again.
Enter your guess: 384 ⌨️
Higher! Try again.
Enter your guess: 386 ⌨️
Higher! Try again.
Enter your guess: 388 ⌨️
Congratulations! You guessed the correct number: 388 
Here's your flag: picoCTF{g00d_gu355_bee04a2a} 🔐
Connection to atlas.picoctf.net closed.
```

## Flag
picoCTF{g00d_gu355_bee04a2a}

## Continue
[Continue](./picoGym0037.md)