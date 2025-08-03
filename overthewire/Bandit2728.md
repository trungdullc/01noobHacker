# Bandit Level 27 → Level 28 Git introduction and basics

## Previous Flag
<b>Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN</b>

## Goal
Use previous password to log in SSH with user <b>bandit28</b> on port <b>2220</b>. There is a git repository at <b>ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220</b>. The password for the user <b>bandit28-git is the same</b> as for the user bandit28. <b>Clone the repository</b> and find the password for the next level.

## What I learned
```
git show            to see difference
git checkout        go back to version to see changes
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit28@bandit.labs.overthewire.org -p 2220 ⌨️
bandit28@bandit:~$ mktemp -d ⌨️
/tmp/tmp.cAOcHS6eu3
bandit28@bandit:~$ cd /tmp/tmp.cAOcHS6eu3 ⌨️
bandit28@bandit:/tmp/tmp.cAOcHS6eu3$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).

bandit28-git@localhost's password: ⌨️
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.cAOcHS6eu3$ ls ⌨️
repo
bandit28@bandit:/tmp/tmp.cAOcHS6eu3$ cd repo/ ⌨️
bandit28@bandit:/tmp/tmp.cAOcHS6eu3/repo$ ls ⌨️
README.md
bandit28@bandit:/tmp/tmp.cAOcHS6eu3/repo$ cat README.md ⌨️ 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
bandit28@bandit:/tmp/tmp.cAOcHS6eu3/repo$ git log ⌨️
commit 494cf8c7bef69317392930b84777b0da35cb1b3f (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Mon Jul 28 19:03:49 2025 +0000

    fix info leak

commit f257900db7c134cb5224c91013817e76d18457e0 👀
Author: Morla Porla <morla@overthewire.org>
Date:   Mon Jul 28 19:03:49 2025 +0000

    add missing data

commit 76a999f68286e42e0f98210ec45e66f4d35612b1
Author: Ben Dover <noone@overthewire.org>
Date:   Mon Jul 28 19:03:49 2025 +0000

    initial commit of README.md

bandit28@bandit:/tmp/tmp.cAOcHS6eu3/repo$ git show f257900db ⌨️
commit f257900db7c134cb5224c91013817e76d18457e0
Author: Morla Porla <morla@overthewire.org>
Date:   Mon Jul 28 19:03:49 2025 +0000

    add missing data

diff --git a/README.md b/README.md
index 7ba2d2f..d4e3b74 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: <TBD>
+- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7 🔐

bandit28@bandit:/tmp/tmp.cAOcHS6eu3/repo$ git log --oneline ⌨️
494cf8c (HEAD -> master, origin/master, origin/HEAD) fix info leak
f257900 add missing data
76a999f initial commit of README.md
bandit28@bandit:/tmp/tmp.cAOcHS6eu3/repo$ git checkout f257900 ⌨️
Note: switching to 'f257900'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at f257900 add missing data
bandit28@bandit:/tmp/tmp.cAOcHS6eu3/repo$ ls ⌨️
README.md
bandit28@bandit:/tmp/tmp.cAOcHS6eu3/repo$ cat README.md ⌨️ 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7 🔐
```

## Flag
<b>4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7</b>

## Continue
[Continue](/overthewire/Bandit2829.md)