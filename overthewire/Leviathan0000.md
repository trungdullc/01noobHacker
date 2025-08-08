# Leviathan Level 0 Backup and Privilege Escalation

## Previous Flag
<b>leviathan0</b>

## Goal
Use previous password to log in SSH with user <b>leviathan0</b> and port <b>2223</b> accessed on leviathan.labs.overthewire.org
Du Hint:

## What I learned
```
Leviathan teaches basic Linux command-line skills, file permissions, and simple binaries
Basic nix commands refers to fundamental Unix or Linux (Unix-like) shell commands
    *nix shorthand includes Unix, Linux, and BSD systems

Backups is a way attackers do privilege escalation
Privilege escalation is when an attacker gains higher or unauthorized levels of access to a system, often moving from a low-privileged user (like www-data) to a root/admin user
```

## Solution
```
# Note: Had to switch over
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh leviathan0@leviathan.labs.overthewire.org -p 2223 ⌨️
# Note: Had to switch locally GitHub Codespace trying charge me
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads> ssh leviathan0@leviathan.labs.overthewire.org -p 2223 ⌨️
                   _            _       _   _                 
                  | | _____   _(_) __ _| |_| |__   __ _ _ __  
                  | |/ _ \ \ / / |/ _` | __| '_ \ / _` | '_ \ 
                  | |  __/\ V /| | (_| | |_| | | | (_| | | | |
                  |_|\___| \_/ |_|\__,_|\__|_| |_|\__,_|_| |_|
                                                              

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

leviathan0@leviathan.labs.overthewire.org's password: ⌨️
leviathan0@leviathan:~$ ls ⌨️
leviathan0@leviathan:~$ cd /etc/leviathan_pass/ ⌨️
leviathan0@leviathan:/etc/leviathan_pass$ ls ⌨️
leviathan0  leviathan1  leviathan2  leviathan3  leviathan4  leviathan5  leviathan6  leviathan7
leviathan0@leviathan:/etc/leviathan_pass$ cat leviathan0 ⌨️
leviathan0
leviathan0@leviathan:/etc/leviathan_pass$ cat leviathan1 ⌨️
cat: leviathan1: Permission denied
leviathan0@leviathan:/etc/leviathan_pass$ cd ⌨️
leviathan0@leviathan:~$ ls -la ⌨️
total 24
drwxr-xr-x   3 root       root       4096 Jul 28 19:05 .
drwxr-xr-x 150 root       root       4096 Jul 28 19:06 ..
drwxr-x---   2 leviathan1 leviathan0 4096 Jul 28 19:05 .backup 👀     
-rw-r--r--   1 root       root        220 Mar 31  2024 .bash_logout
-rw-r--r--   1 root       root       3851 Jul 28 18:47 .bashrc     
-rw-r--r--   1 root       root        807 Mar 31  2024 .profile
leviathan0@leviathan:~$ cd .backup/ ⌨️
leviathan0@leviathan:~/.backup$ ls -la ⌨️
total 140
drwxr-x--- 2 leviathan1 leviathan0   4096 Jul 28 19:05 .
drwxr-xr-x 3 root       root         4096 Jul 28 19:05 ..
-rw-r----- 1 leviathan1 leviathan0 133259 Jul 28 19:05 bookmarks.html
leviathan0@leviathan:~/.backup$ head -n 10 bookmarks.html ⌨️ 
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1 LAST_MODIFIED="1160271046">Bookmarks</H1>

<DL><p>
    <DT><H3 LAST_MODIFIED="1160249304" PERSONAL_TOOLBAR_FOLDER="true" ID="rdf:#$FvPhC3">Bookmarks Toolbar Folder</H3>
leviathan0@leviathan:~/.backup$ cat bookmarks.html | grep -ie "leviathan"
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is 3QJ3TgzHDq"🔐 ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

## Flag
<b>3QJ3TgzHDq</b>

## Continue
[Continue](/overthewire/Leviathan0001.md)