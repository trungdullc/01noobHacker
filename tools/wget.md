# wget

```
Description: Download files, other ways: curl, certutil

# Start with serving files from current directory over HTTP
python3 -m http.server 8000

# Recursively download an entire website (mirror it) starting from homepage
wget -rc http://example.com

# Recursively crawl a website AND ignore site's robots.txt restrictions
wget -r -e robots=off http://example.com

# Recursively download ONLY files ending in `.pdf` from site
wget -rcA .pdf http://example.com

# Download lse.sh script from GitHub and save it as "lse.sh"
# Make the script executable
wget "https://raw.githubusercontent.com/diego-treitos/linux-smart-enumeration/master/lse.sh" -O lse.sh
chmod +x lse.sh

# Run lse.sh script with level 2 enumeration
./lse.sh -l2
```

## Back to README.md
[BACK](../README.md)