# Leviathan Level 0

## Previous Flag
<b>leviathan0</b>

## Goal
Use previous password to log in SSH with user <b>leviathan0</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org

## What I learned
```
Leviathan teaches basic Linux command-line skills, file permissions, and simple binaries
Basic nix commands refers to fundamental Unix or Linux (Unix-like) shell commands
    *nix shorthand includes Unix, Linux, and BSD systems
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh leviathan0@leviathan.labs.overthewire.org -p 2223 ⌨️
                   _            _       _   _                 
                  | | _____   _(_) __ _| |_| |__   __ _ _ __  
                  | |/ _ \ \ / / |/ _` | __| '_ \ / _` | '_ \ 
                  | |  __/\ V /| | (_| | |_| | | | (_| | | | |
                  |_|\___| \_/ |_|\__,_|\__|_| |_|\__,_|_| |_|
                                                              

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

leviathan0@leviathan.labs.overthewire.org's password: ⌨️
leviathan0@leviathan:~$ ls
leviathan0@leviathan:~$ cd /etc/leviathan_pass/
leviathan0@leviathan:/etc/leviathan_pass$ ls
leviathan0  leviathan1  leviathan2  leviathan3  leviathan4  leviathan5  leviathan6  leviathan7
leviathan0@leviathan:/etc/leviathan_pass$ cat leviathan0
leviathan0
leviathan0@leviathan:/etc/leviathan_pass$ cat leviathan1
cat: leviathan1: Permission denied
leviathan0@leviathan:/etc/leviathan_pass$ cd
```

## Flag


## Continue
[Continue](/overthewire/Leviathan0001.md)