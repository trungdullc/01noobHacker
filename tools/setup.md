# Setup Usages with variable
```
# Create a working directory to store results of your scans
mkdir ~/CTF/$IP

# Update Git Repos (recursive)
find . -maxdepth 3 -name .git -type d | rev | cut -c 6- | rev | xargs -I {} git -C {} pull
```

## Back to README.md
[BACK](/README.md)