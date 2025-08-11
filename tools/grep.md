# grep

```
Description: search for text in files

# Search for the string "flag" in the file /path/to/file (case-sensitive)
grep flag /path/to/file

# Search for "flag" in /path/to/file, ignoring case (matches "Flag", "FLAG")
grep -i flag /path/to/file

# Recursively search for "flag" in all files under the current directory
grep -R flag .

# Treat a binary file as text and search for "flag" inside it
grep -a flag /path/to/file

# Search for "PNG" in a binary file
grep -oba PNG binaryfile.bin
    show byte offset (-b)
    output as binary-safe (-a)
    print matching byte positions (-o)
```

## Back to README.md
[BACK](../README.md)