# Useful git commands

# Important: Set Git Identity before using
```
# Configure Git User Info (Required Once)               git config --global --list ⭐
git config --global user.name "Your Name" ⭐           git config --global user.name
git config --global user.email "you@example.com" ⭐    git config --global user.email

# Authentication to GitHub (GitHub no longer supports password login) w/ SSH or GPG Keys
# Generate SSH key
ssh-keygen -t ed25519 -C "you@example.com" ⭐           ~/.ssh/id_ed25519
ssh-keygen -t rsa -b 4096 -C "you@example.com"          ~/.ssh/id_rsa

# Copy public key into GitHub/GitLab
cat ~/.ssh/id_ed25519.pub ⭐
cat ~/.ssh/id_rsa.pub

# Optional: Tell Git to use SSH by editing .git/config
https://github.com/username/repo.git → git@github.com:username/repo.git
```

# Optional: GPG key
```
# On Ubuntu/Debian                          # On macOS
sudo apt update                             brew install gnupg
sudo apt install gnupg

# Generate a GPG Key
gpg --full-generate-key ⭐
    Key type: 1 (RSA)                           Key type: 9 ECC (sign only)
    Key size: 4096                              Next prompt: Choose 1 for Curve: ed25519
    Expiration: your choice                     Key usage: Default is fine (S for signing)
    Name/email: must match Git/GitHub
    Passphrase: optional but recommended

# List Your GPG Keys
gpg --list-secret-keys --keyid-format=long ⭐
    /home/you/.gnupg/secring.gpg
    ----------------------------------
    sec     rsa4096/ABC123DEF456GHI7 2025-07-30 [SC]
            Your Name <you@example.com>
Take note of that key ID: ABC123DEF456GHI7 ⭐

# Tell Git to Use Your GPG Key
git config --global user.signingkey ABC123DEF456GHI7 ⭐
git config --global commit.gpgsign true ⭐

# Optional (enable GPG for all signed commits)
git config --global gpg.format gpg

# Add GPG Key to GitHub/GitLab
gpg --armor --export ABC123DEF456GHI7 ⭐

# Test It (Sign a Commit)
git commit -S -m "Signed commit"            # Note: If set globally, -S isn't needed
```

# Clone a Remote Repository
```
git clone https://github.com/user/repo.git ⭐⭐⭐⭐⭐
```

# Basic
```
# Initialize a Git Repository (rarely used, better to create README.md .gitignore on GitHub/GitLab)
git init

# Track Files and Commit ⭐⭐⭐⭐⭐
git add filename.txt                # stage a file
git add .                           # stage all files
git commit -m "Initial commit"      # commit with message

# Connect to Remote Repo (GitHub, rarely used if did git clone)
git remote add origin https://github.com/user/repo.git
git push -fu origin main            # first force push

# TEAMWORK: Create a pull request on GitHub
    GitHub → "Compare & pull request" → Fill description → Submit
    Code gets reviewed and approved
    After approval → PR is merged into main

# Pull Latest Changes
git fetch origin main
git pull origin main ⭐⭐⭐⭐⭐
```

# Branches
```
# Basic
git branch                  # list local branches
git branch -a               # all branches (local + remote)
git checkout -b dev         # create and switch to new branch
git branch -d dev           # delete branch (after merge)

# Create and Switch to a New Branch ⭐⭐⭐
git branch feature-xyz      # create branch         # shorthand
git checkout feature-xyz    # switch to it          git checkout -b feature-xyz

# Merge a Branch Back into Main ⭐⭐⭐⭐⭐
git checkout main
git merge feature-xyz
```

# View changes and fix stuff
```
# View Changes and History
git status                      # Important: view staged, modified, untracked ⭐⭐⭐⭐⭐
git diff                        # show unstaged changes
git log                         # Important: view commit history ⭐⭐⭐
git log --oneline --graph       # prettier history
git show <commit_hash>          # show details of a specific commit ⭐⭐

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo commit and changes:
git reset --hard HEAD~1

# Important: Revert a specific commit ⭐⭐⭐⭐
git revert <commit_hash>

# Stash Temporary Work
git stash                       # save uncommitted changes
git stash list                  # see stash stack
git stash pop                   # re-apply latest stash
```

# 🚑 Recover from Mess
```
git reflog                      # see recent HEAD history (use to recover)
git checkout HEAD@{1}           # go back to previous HEAD
```

# Fix Merge Conflicts
```
git status                      # see conflicted files

# Edit the files to fix manually
git add conflicted_file.txt
git commit                      # finalize merge

<<<<<<< HEAD
your changes from current branch
=======
incoming changes from the branch you’re merging
>>>>>>> other-branch

# Set default mergetool         # Note: global      git mergetool --tool-help
git mergetool --tool=vimdiff    git config --global merge.tool vscode

# Use mergetool                 VSC: Accept Current, Accept Incoming, Accept Both
vimdiff FILE.html               code FILE.html

# Mark conflict as resolved
git add FILE.html
git commit
    Merge branch 'feature'
```

# You about git push but some idiot on team changed your files now you behind main ⭐
```
# Stash your work
git stash push -m "my uncommitted changes"
git pull origin main                git pull --rebase origin main

# If there are conflicts
code conflicted_file.txt
git add conflicted_file.txt
git commit                          # or continue merge
git push origin main
```

# Workflow Example
```
git init
git add .
git commit -m "init"
git remote add origin https://github.com/user/repo.git
git push -u origin main

git checkout -b feature-login
# work on it...
git add .
git commit -m "add login"
git checkout main
git merge feature-login
git push
```