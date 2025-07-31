# sed

```
Description: Stream EDitor for text manipulation, searching, finding and replacing, inserting, and deleting lines in a file or stream

Syntax: sed [options] 'command' filename

echo "hello world" | sed 's/world/universe/'

# Replaces first occurrence of "old" with "new" on each line
sed 's/old/new/' file.txt

# Replaces all occurrences on each line (g = global)
sed 's/old/new/g' file.txt

# In-place replacement (modifies file directly)
sed -i 's/old/new/g' file.txt

# Case-Insensitive Replace
sed 's/hello/hi/I' file.txt

# Print Specific Lines
sed -n '5p' file.txt                                # Print only line 5
sed -n '3,6p' file.txt                              # Print lines 3 to 6

# Delete Lines
sed '2d' file.txt                                   # Delete line 2
sed '3,5d' file.txt                                 # Delete lines 3 to 5
sed '/pattern/d' file.txt                           # Delete lines matching a pattern

# Insert or Append Text
sed '2i\This is inserted above line 2' file.txt     # Insert before line 2
sed '3a\This is appended after line 3' file.txt     # Append after line 3

# Replace Only on Specific Line(s)
sed '5s/error/success/' file.txt                    # Replace "error" with "success" only on line 5

# Multiple sed Commands
sed -e 's/foo/bar/' -e 's/hello/world/' file.txt

# Save Output to a New File
sed 's/foo/bar/g' input.txt > output.txt

# Remove Blank Lines
sed '/^$/d' file.txt

# Replace Tabs with Commas
sed 's/\t/,/g' file.txt

# Using Variables in sed
search="old"
replace="new"
sed "s/$search/$replace/g" file.txt
```

## Back to README.md
[BACK](/README.md)