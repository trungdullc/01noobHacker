# volatility

```
Source: https://github.com/volatilityfoundation/volatility
Description: Advanced memory forensics framework

# Identifying the Memory Dump Profile
volatility -f Path_To_File imageinfo
```

# Process Analysis
```
# List All Processes
volatility -f Path_To_File --profile=Profile_Name pslist

# Detect Hidden Processes
volatility -f Path_To_File --profile=Profile_Name psxview

# View Process Tree
volatility -f Path_To_File --profile=Profile_Name pstreeView Process Tree
```

# Command History Analysis
```
# List Executed Commands
volatility -f Path_To_File --profile=Profile_Name cmdscan

# View Executed Command Output
volatility -f Path_To_File --profile=Profile_Name consoles
```

# Data Extraction
```
# Retrieve Clipboard Content
volatility -f Path_To_File --profile=Profile_Name clipboard

# View Environment Variables
volatility -f Path_To_File --profile=Profile_Name envars
```

# File System Analysis
```
# Scan for Files
volatility -f Path_To_File --profile=Profile_Name filescan | grep Documents

# Dump Files
volatility -f Path_To_File --profile=Profile_Name dumpfiles -Q 0x0000000017663e7 -D .
```

# Memory Analysis
```
# Dump Memory of Specific Processes
volatility -f Path_To_File --profile=Profile_Name memdump -p 231 -D .

# View Process Commands
volatility -f Path_To_File --profile=Profile_Name cmdline -p 123,234
```

# Registry Analysis
```
# List Registry Hives
volatility -f Path_To_File --profile=Profile_Name hivelist

# Extract Registry Keys
volatility -f Path_To_File --profile=Profile_Name printkey -K "Software\Microsoft\Windows\CurrentVersion\Run"
```

# Timeline Analysis
```
# Explore Deleted and Modified Files
volatility -f Path_To_File --profile=Profile_Name mftparser

# Retrieve Last Shutdown Time
volatility -f Path_To_File --profile=Profile_Name shutdowntime
```

# Visual Evidence
```
# Capture Screenshots
volatility -f Path_To_File --profile=Profile_Name screenshot -D .
```

# String Searching
```
# Search for Interesting Strings
strings Challenge.raw | grep "Mega"
strings Challenge.raw | grep "Pastebin"
strings Challenge.raw | grep "Passwords"
strings Challenge.raw | grep "Flag{"
```

# Leveraging External Plugins
```
git clone https://github.com/superponible/volatility-plugins

firefoxhistory.py:          Extract Firefox browsing history, cookies, and downloads
chromehistory.py:           Extract Chrome browsing history, visits, search terms, and downloads
prefetch.py:                Scan memory for prefetch files and extract timestamps
idxparser.py:               Scan memory for Java IDX files and extract details
```

## Back to README.md
[BACK](../README.md)