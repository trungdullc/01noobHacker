# find

## Finding by Name and Pattern
```
# Basic name search (case-sensitive)
find /path/to/search -name "filename.txt"

# Case-insensitive search
find /path/to/search -iname "README*"

# Using wildcards (MUST use quotes)
find . -name "*.log"                        # All log files
find . -name "config.*"                     # Files starting with config
find . -name "*backup*"                     # Files containing 'backup'

# Multiple extensions
find . -name "*.jpg" -o -name "*.png" -o -name "*.gif"

# Find files NOT matching pattern
find . -type f ! -name "*.txt"
```

## Finding by File Type
```
# Find only files
find /var/log -type f

# Find only directories
find /home -type d -name "*project*"

# Find symbolic links
find /usr/bin -type l

# Find broken symbolic links
find /usr/local -type l ! -exec test -e {} \; -print

# Find block devices
find /dev -type b

# Find character devices
find /dev -type c
```

## Finding by Size
```
# Find files larger than 100MB
find /home -size +100M

# Find files smaller than 1KB
find /tmp -size -1k

# Find files exactly 50MB
find . -size 50M

# Find empty files
find /var/log -type f -empty

# Find empty directories
find /tmp -type d -empty

# Size ranges
find . -size +10M -size -100M               # Between 10MB and 100MB
```

## Finding by Time and Date
```
# Files modified in last 24 hours
find /home/user -mtime -1

# Files modified more than 7 days ago
find /tmp -mtime +7

# Files accessed in last 2 hours
find /var/log -amin -120

# Files changed in last 30 minutes
find . -cmin -30

# Files modified between specific dates
find . -newermt "2024-01-01" ! -newermt "2024-12-31"

# Files modified today
find /home -daystart -mtime -1
```

## Finding by Permissions and Ownership
```
# Find writable directories (security check)
find / -writable -type d 2>/dev/null

# Find executable files
find /usr/local/bin -type f -executable

# Find SUID files (important for security audits)
find / -perm -4000 -type f 2>/dev/null

# Find SGID files
find / -perm -2000 -type f 2>/dev/null

# Find files with specific permissions
find . -perm 755                    # Exactly 755
find . -perm -755                   # At least 755
find . -perm /755                   # Any of 755 bits set

# Find files owned by specific user
find /home -user john

# Find files owned by specific group
find /var/www -group www-data

# Find files with no owner (orphaned files)
find / -nouser 2>/dev/null

# Find files with no group
find / -nogroup 2>/dev/null
```

## Advance: Combining Multiple Criteria
```
# Find large log files modified recently
find /var/log -name "*.log" -size +10M -mtime -7

# Find shell scripts owned by root
find /usr/local -name "*.sh" -user root -type f

# Find configuration files modified in last week
find /etc -name "*.conf" -mtime -7 -type f

# Find temporary files older than 1 day
find /tmp -name "*.tmp" -mtime +1 -delete
```

## Advanced: Using Logical Operators
```
# AND operator (default)
find . -name "*.txt" -size +1M

# OR operator
find . \( -name "*.jpg" -o -name "*.png" -o -name "*.gif" \)

# NOT operator
find . -type f ! -name "*.bak"

# Complex logic
find . \( -name "*.log" -o -name "*.txt" \) -a -mtime -7
```

## Advanced: Execute Commands on Found Files
```
# Make shell scripts executable
find . -name "*.sh" -exec chmod +x {} \;

# Delete temporary files safely
find /tmp -name "*.tmp" -mtime +7 -exec rm -f {} \;

# Copy configuration files to backup
find /etc -name "*.conf" -exec cp {} /backup/config/ \;

# Show detailed info for large files
find . -size +100M -exec ls -lh {} \;

# Count lines in all Python files
find . -name "*.py" -exec wc -l {} +

# Use with confirmation
find . -name "*.log" -ok rm {} \;
```

## Advanced: Advanced Output and Processing
```
# Print with null separator (safer for xargs)
find . -name "*.txt" -print0 | xargs -0 grep "pattern"

# Custom format output
find . -type f -printf "%p %s %TY-%Tm-%Td\n"

# Find and process with xargs
find . -name "*.c" -print0 | xargs -0 grep -l "main"

# Pipe to while loop
find . -name "*.log" | while read file; do
    echo "Processing $file"
    # Process each file
done
```

## Optimization: Limit Search Scope
```
# Limit search depth
find . -maxdepth 3 -name "*.txt"

# Stay on same filesystem
find / -xdev -name "core" 2>/dev/null

# Skip certain directories
find / -path /proc -prune -o -name "*.conf" -print
find / -path /sys -prune -o -path /proc -prune -o -name "*.log" -print
```

## Optimization: Optimize for Speed
```
# Use specific paths instead of /
find /home/user/documents -name "*.pdf"  # Better than find / -name "*.pdf"

# Put most restrictive criteria first
find . -name "*.txt" -size +1M           # Name check is faster than size

# Use -quit to stop after first match
find . -name "config.txt" -quit
```

## Real-World Use Cases: System Administration
```
# Find large files consuming disk space
find / -type f -size +100M 2>/dev/null | head -20

# Find recently modified system files
find /etc -mtime -1 -type f

# Security audit - find SUID/SGID files
find / \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null

# Find world-writable files (security risk)
find / -perm -002 -type f 2>/dev/null

# Clean up old log files
find /var/log -name "*.log" -mtime +30 -exec gzip {} \;
```

## Real-World Use Cases: Development Tasks
```
# Find source code files
find . \( -name "*.c" -o -name "*.h" -o -name "*.cpp" \) -type f

# Find and count lines of code
find . -name "*.py" -exec wc -l {} + | tail -1

# Find TODO comments in code
find . -name "*.js" -exec grep -Hn "TODO" {} \;

# Find large binary files in project
find . -type f -size +10M ! -path "./.git/*"

# Clean up build artifacts
find . -name "*.o" -o -name "*.pyc" -o -name "__pycache__" -exec rm -rf {} +
```

## Real-World Use Cases: File Management
```
# Find duplicate files by name
find . -name "*.txt" | sort | uniq -d

# Organize files by extension
find /downloads -name "*.pdf" -exec mv {} /documents/pdfs/ \;

# Find old downloads to clean up
find ~/Downloads -mtime +30 -type f

# Backup important files
find /home/user/documents -name "*.doc*" -exec cp {} /backup/ \;
```

## Common Solutions: Handling Special Characters
```
# Files with spaces
find . -name "* *" -type f
find . -print0 | xargs -0 ls -l        # Safe with spaces

# Files with quotes or special chars
find . -name $'*\n*'                   # Files with newlines in name
find . -name "*[<>]*"                  # Files with < or > in name
```

## Common Solutions: Permission Issues
```
# Suppress permission denied errors
find / -name "*.conf" 2>/dev/null

# Only search readable directories
find / -readable -name "*.txt" 2>/dev/null

# Run with sudo for system-wide searches
sudo find / -name "*.log" -size +100M
```

## Common Solutions: Symbolic Links
```
# Follow symbolic links
find -L . -name "*.txt"

# Don't follow symbolic links (default)
find -P . -name "*.txt"

# Find symbolic links themselves
find . -type l -ls
```

## Quick Reference Card
```
Task	                        Command
Find by name	                find . -name "filename"
Case insensitive	            find . -iname "pattern"
Find directories only	        find . -type d
Find files only	                find . -type f
Find by size	                find . -size +100M
Find by time	                find . -mtime -7
Find and delete	                find . -name "*.tmp" -delete
Find and execute	            find . -name "*.sh" -exec chmod +x {} \;
Multiple conditions	            find . -name "*.log" -size +1M -mtime -1
Exclude pattern	                find . -type f ! -name "*.bak"
```

# Q: How do I find all files with a specific name?
```
find / -name "filename" 2>/dev/null
# Use -iname for case-insensitive search
find / -iname "readme.txt" 2>/dev/null
```

# Q: How to find files containing specific text?
```
find . -type f -exec grep -l "search text" {} \;
# Or combine with grep
find . -name "*.txt" | xargs grep "search text"
```

# Q: How do I find the largest files on my system?
```
find / -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -10
# Or simpler version
find / -type f -size +100M 2>/dev/null | head -10
```

# Q: How to find files modified in the last hour?
```
find . -mmin -60                # Modified in last 60 minutes
find . -cmin -60                # Changed in last 60 minutes
find . -amin -60                # Accessed in last 60 minutes
```

# Q: How do I delete all files with a specific extension?
```
# Safe way - list first
find . -name "*.tmp" -type f
# Then delete
find . -name "*.tmp" -type f -delete
# Or with confirmation
find . -name "*.tmp" -type f -ok rm {} \;
```

# Q: How to find and move files to another directory?
```
find . -name "*.pdf" -exec mv {} /destination/folder/ \;
# For files with spaces in names
find . -name "*.pdf" -print0 | xargs -0 -I {} mv {} /destination/folder/
```

# Q: How do I find empty files and directories?
```
find . -type f -empty       # Empty files
find . -type d -empty       # Empty directories
find . -empty               # Both empty files and directories
```

# Q: How to find files but exclude certain directories?
```
find / -path /proc -prune -o -path /sys -prune -o -name "*.log" -print
# Or exclude multiple patterns
find . \( -path ./node_modules -o -path ./.git \) -prune -o -name "*.js" -print
```

# Q: How do I find files larger than a specific size?
```
find . -size +100M                  # Larger than 100 MB
find . -size +1G                    # Larger than 1 GB
find . -size +500k                  # Larger than 500 KB
find . -size +100c                  # Larger than 100 bytes
```

# Q: How to find files within a size range?
```
find . -size +10M -size -100M       # Between 10MB and 100MB
find . -size +1k -size -1M          # Between 1KB and 1MB
```

# Q: How do I find what’s taking up disk space?
```
# Find largest directories
find . -type d -exec du -sh {} \; | sort -hr | head -10
# Find largest files
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -10
```

# Q: How to find files modified between specific dates?
```
# Files modified after Jan 1, 2024
find . -newermt "2024-01-01"
# Files modified between two dates
find . -newermt "2024-01-01" ! -newermt "2024-12-31"
```

# Q: How do I find files not accessed in 30 days?
```
find /home -atime +30               # Not accessed in 30+ days
find /tmp -atime +7 -delete         # Delete files not accessed in 7+ days
```

# Q: How to find files modified today?
```
find . -daystart -mtime -1          # Modified today
find . -newer /tmp/timestamp        # Modified after timestamp file
```

# Q: How do I find files with specific permissions?
```
find . -perm 755            # Exactly 755
find . -perm -644           # At least 644 (owner read/write, others read)
find . -perm /222           # Anyone can write
```

# Q: How to find files owned by a specific user?
```
find /home -user john       # Files owned by user 'john'
find / -uid 1000            # Files owned by UID 1000
find / -nouser              # Files with no owner (orphaned)
```

# Q: How do I find world-writable files (security risk)?
```
find / -perm -002 -type f 2>/dev/null       # World-writable files
find / -perm -022 -type d 2>/dev/null       # World-writable directories
```

# Q: How to find SUID and SGID files?
```
find / -perm -4000 -type f 2>/dev/null                          # SUID files
find / -perm -2000 -type f 2>/dev/null                          # SGID files
find / \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null     # Both
```

# Q: How do I use find with other commands safely?
```
# Safe with filenames containing spaces
find . -name "*.txt" -print0 | xargs -0 grep "pattern"
# Process each file in a loop
find . -name "*.log" | while IFS= read -r file; do
    echo "Processing: $file"
done
```

# Q: How to find files and perform multiple actions?
```
find . -name "*.sh" -exec chmod +x {} \; -exec echo "Made {} executable" \;
# Or use a script
find . -name "*.txt" -exec bash -c 'wc -l "$1"; cp "$1" /backup/' _ {} \;
```

# Q: How do I find files excluding certain file types?
```
find . -type f ! -name "*.tmp" ! -name "*.bak"
find . -type f ! \( -name "*.o" -o -name "*.so" \)
```

# Q: How to find recently installed packages’ files?
```
# On Debian/Ubuntu
find /usr -newermt "1 day ago" -type f
# Find files installed by specific package
dpkg -L package_name | while read file; do test -f "$file" && echo "$file"; done
```

# Q: Why is find command slow and how to speed it up?
```
# Use more specific paths
find /home/user instead of find /

# Limit depth
find . -maxdepth 3 -name "*.txt"

# Put most selective criteria first
find . -name "specific_name" -size +100M    # name first is faster

# Exclude large directories
find / -path /proc -prune -o -path /sys -prune -o -name "*.conf" -print
```

# Q: How do I handle “Permission denied” errors?
```
find / -name "*.conf" 2>/dev/null           # Suppress errors
find / -readable -name "*.conf"             # Only search readable
sudo find / -name "*.conf"                  # Run with elevated privileges
```

# Q: How to find files across multiple filesystems?
```
find / -name "*.log"                        # Crosses filesystem boundaries
find / -xdev -name "*.log"                  # Stays on same filesystem
find /home /var -name "*.conf"              # Search multiple specific paths
```

# Q: How do I use wildcards correctly with find?
```
find . -name "*.txt"                        # Correct - quoted
find . -name *.txt                          # Wrong - shell expands first
find . -name "*[0-9]*"                      # Files with numbers
find . -name "*backup*"                     # Files containing 'backup'
```

# Q: How to find files with multiple extensions?
```
find . \( -name "*.jpg" -o -name "*.png" -o -name "*.gif" \)
find . -regex ".*\.\(jpg\|png\|gif\)$"
```

# Q: How do I find files NOT matching a pattern?
```
find . -type f ! -name "*.txt"              # All non-txt files
find . -type f ! -name "*.bak" ! -name "*.tmp"  # Exclude multiple
```

## Back to README.md
[BACK](../README.md)
