# Bandit Level 29 → Level 30 git tag

## Previous Flag
<b>qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL</b>

## Goal
Use previous password to log in SSH with user <b>bandit30</b> on port <b>2220</b>. There is a git repository at <b>ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220</b>. The password for the user <b>bandit30-git is the same</b> as for the user bandit30. Clone the repository and find the password.

## What I learned
```
git tag: used to mark specific points in history (release versions)
  Syntax: git tag -a <tag_name> -m <"tag description/message">
  git tag -a secret -m "fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy" ⌨️❤️
```

## Side Quest
```
Created a repo on GitHub cannot set a custom port and only supports standard ports:
  443 for HTTPS (https://github.com/...)
  22 for SSH (git@github.com:...)

If want custom port for git must self-host git repository (on your own server, Raspberry Pi, VPS)
# Initialize a bare repo
git init --bare /home/git/myrepo.git ⌨️❤️

# Run an SSH server or HTTP server on a custom port
# SSH example on port 2000                                # HTTP example on port 2000
sudo vi /etc/ssh/sshd_config ⌨️                            cd /home/git ⌨️
  # Add or edit                                             python3 -m http.server 2000 ⌨️
  Port 2000                               
sudo systemctl restart ssh ⌨️

# Clone using the port
git clone ssh://user@yourserver:2222/home/git/myrepo.git    git clone http://yourserver:8080/myrepo.git
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit30@bandit.labs.overthewire.org -p 2220 ⌨️
bandit30@bandit:~$ mktemp -d ⌨️
/tmp/tmp.9C5dCCySKt
bandit30@bandit:~$ cd /tmp/tmp.9C5dCCySKt ⌨️
bandit30@bandit:/tmp/tmp.9C5dCCySKt$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo ⌨️
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Could not create directory '/home/bandit30/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).

bandit30-git@localhost's password: ⌨️
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/tmp.9C5dCCySKt$ ls ⌨️
repo
bandit30@bandit:/tmp/tmp.9C5dCCySKt$ cd repo/ ⌨️
bandit30@bandit:/tmp/tmp.9C5dCCySKt/repo$ ls ⌨️
README.md
bandit30@bandit:/tmp/tmp.9C5dCCySKt/repo$ cat README.md ⌨️
just an epmty file... muahaha
bandit30@bandit:/tmp/tmp.9C5dCCySKt/repo$ git log --oneline ⌨️
5dd8d20 (HEAD -> master, origin/master, origin/HEAD) initial commit of README.md
bandit30@bandit:/tmp/tmp.9C5dCCySKt/repo$ git branch -a ⌨️
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
bandit30@bandit:/tmp/tmp.9C5dCCySKt/repo$ git help tag ⌨️
bandit30@bandit:/tmp/tmp.9C5dCCySKt/repo$ git tag --list ⌨️
secret
bandit30@bandit:/tmp/tmp.9C5dCCySKt/repo$ git tag ⌨️
secret
bandit30@bandit:/tmp/tmp.9C5dCCySKt/repo$ git show secret ⌨️
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy 🔐
```

## Flag
<b>fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy</b>

## Continue
[Continue](/overthewire/Bandit3031.md)