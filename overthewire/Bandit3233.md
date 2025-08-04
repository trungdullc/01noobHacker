# Bandit Level 32 → Level 33 Congrats Finish Bandit

## Previous Flag
<b>tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0</b>

## Goal
Use previous password to log in SSH with user <b>bandit32</b> on port <b>2220</b> to test if password correct. At this moment, level 34 does not exist yet.

## What I learned
```
Nothing
```

## Side Quest
```
# Setup a Local SSH Server on your server machine (local VM or Linux box)
sudo apt update && sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh

# Verify it’s working from local machine        # Verify it’s working from another machine
ssh localhost                                   ssh user@hostname_or_ip

# Add a Custom Welcome Message
sudo vi /etc/motd
    .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
    Welcome to your custom wargame challenge!
    Find the password hidden in this shell.
    .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.

# Create the user and disable normal login shell
sudo useradd -m challengeuser -s /home/challengeuser/uppershell
sudo passwd challengeuser

# Optional Delete user
sudo userdel challengeuser

# Optional append user to sudo group
sudo usermod -aG sudo challengeuser
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit33@bandit.labs.overthewire.org -p 2220 ⌨️
```

## Flag
N/A

## Continue
[Continue](/overthewire/Bandit3334.md)