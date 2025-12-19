# git

# Cheats
```
VSC Extension       GitHub Pull Request
VSC Extension       GitHub Desktop
```

# git basic
```
Description: git basic
Create new GitHub w/ ReadMe.md                  Create GitHub w/ empty (best)               Clone a GitHub
                                                                                            Make sure have power to look at email invites
Create a folder and put .gitignore                                                          git clone
git init                                                                                    npm install
git add .           
git commit -m "2nd commit"
git remote add origin git@github.com:trungdullc/app-name.git
git branch -M main
git push -u origin main
git pull                                        Note: all the left side the same
git push -u origin main -f                      git push -u origin main                     git push
```

# Side Quest: Git username & email
```sh
# Check global Git username and email
git config --global user.name
git config --global user.email

# Set username and email
git config --global user.name "Hacker Du"
git config --global user.email "hackerdu@gmail.com"

# GitHub no longer accepts password login for Git (removed password authentication in 2021)
You must authenticate with:
    Option A: Personal Access Token (HTTPS)
        # Check what remote you're using
        git remote -v
        # create a GitHub Personal Access Token
        https://github.com/settings/tokens
        Click "Generate new token (classic)"
        Select scopes:
            repo or (full scopes for convenience)
        Generate token
        Copy it
        # Use token when pushing
        git push origin main
        Username: your-github-username
        Password: <paste your token here>
    Option B: SSH key (recommended)(rsa/ed25519)
        # Check if you already have SSH keys
        ls ~/.ssh
            id_rsa          id_ed25519
            id_rsa.pub      id_ed25519.pub
        # Use ED25519 (recommended):
        ssh-keygen -t ed25519 -C "hackerdu@gmail.com"
        # Use RSA (old school)
        ssh-keygen -t rsa -b 4096 -C "hackerdu@gmail.com"

        # Add your key to the SSH agent
        eval "$(ssh-agent -s)"
        ssh-add ~/.ssh/id_ed25519

        # Add your public key to GitHub
        cat ~/.ssh/id_ed25519.pub

        # Change your remote to SSH
        git remote set-url origin git@github.com:username/repo.git

        # can push with no password
        git push origin main
```

## Back to README.md
[BACK](../README.md)