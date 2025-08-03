# Bandit Level 28 → Level 29 Git history

## Previous Flag
<b>4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7</b>

## Goal
Use previous password to log in SSH with user <b>bandit29</b> on port <b>2220</b>. There is a git repository at <b>ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220</b>. The password for the user <b>bandit29-git is the same</b> as for the user bandit29.  Clone the repository and find the password for the next level.

## What I learned
```
add .git to .gitignore                                  Don't upload .git to GitHub/GitLab
Important: You can't see GitHub's .gitignore but when you clone it you can see it

git branch                                              List (-a), create, or delete branches
git checkout <branch_name>                              Switch branches
git switch <branch_name>                                Switch branches
git merge                                               Join two or more branches, must be in master/main

git branch -d dev                                       delete local branch
git branch -D dev                                       force delete local branch
git push origin --delete dev                            delete remote branch

git log --oneline                                       history
git checkout <hash>                                     use files at that point in time
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit29@bandit.labs.overthewire.org -p 2220 ⌨️
bandit29@bandit:~$ mktemp -d ⌨️
/tmp/tmp.H7LypBNxoa
bandit29@bandit:~$ cd /tmp/tmp.H7LypBNxoa ⌨️
bandit29@bandit:/tmp/tmp.H7LypBNxoa$ git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo ⌨️
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Could not create directory '/home/bandit29/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit29/.ssh/known_hosts).

bandit29-git@localhost's password: ⌨️
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/tmp.H7LypBNxoa$ ls ⌨️
repo
bandit29@bandit:/tmp/tmp.H7LypBNxoa$ cd repo/ ⌨️
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ ls ⌨️
README.md
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ cat README.md ⌨️ 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!> 👀
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ man git-branch ⌨️ ⭐⭐⭐
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git help branch ⌨️ ⭐⭐⭐
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git branch ⌨️                      # local branch
* master
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git branch -r ⌨️                   # remote branch
  origin/HEAD -> origin/master
  origin/dev
  origin/master
  origin/sploits-dev
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git branch -a ⌨️ ⭐⭐⭐⭐⭐      # all branches
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev                                                          # Note: remote vs local 🐱‍💻
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git checkout dev ⌨️ ⭐⭐⭐⭐⭐
branch 'dev' set up to track 'origin/dev'.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ ls -la ⌨️
total 20
drwxrwxr-x 4 bandit29 bandit29 4096 Aug  3 03:22 .
drwx------ 3 bandit29 bandit29 4096 Aug  3 03:15 ..
drwxrwxr-x 2 bandit29 bandit29 4096 Aug  3 03:22 code
drwxrwxr-x 8 bandit29 bandit29 4096 Aug  3 03:22 .git
-rw-rw-r-- 1 bandit29 bandit29  134 Aug  3 03:22 README.md
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ cat README.md ⌨️
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL 🔐
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git branch -a ⌨️
* dev                                                     # Note: currently in dev branch not master
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev

# Switch to master branch to merge
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git switch master ⌨️ ⭐⭐⭐⭐⭐
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git merge dev ⌨️ ⭐⭐⭐⭐⭐
Updating ef0ecc7..4a754d1
Fast-forward
 README.md         | 2 +-
 code/gif2ascii.py | 1 +
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 code/gif2ascii.py
 bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git push origin master ⌨️
 bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git branch -d dev ⌨️ ⭐⭐⭐        # deleted local branch
Deleted branch dev (was 4a754d1).

# Note: git branch -D dev (force delete if not fully merge with master/main) ⭐⭐⭐ 
# Need also rm remote: git push origin --delete dev ⭐⭐⭐⭐⭐

bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git log --oneline ⌨️ ❤️
4a754d1 (HEAD -> master, origin/dev) add data needed for development
db8b78e add gif2ascii
ef0ecc7 (origin/master, origin/HEAD) fix username
57d742e initial commit of README.md
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ git checkout 57d742e ⌨️ ❤️
Note: switching to '57d742e'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 57d742e initial commit of README.md
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ ls ⌨️
README.md
bandit29@bandit:/tmp/tmp.H7LypBNxoa/repo$ cat README.md ⌨️ 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit29
- password: <no passwords in production!>
```

## Flag
<b>qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL</b>

## Continue
[Continue](/overthewire/Bandit2930.md)