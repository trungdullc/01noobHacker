# Useful Scripts

```
#!/bin/bash
# Remember:     chmod +x myscript.sh
# Run:          ./myscript.sh                bash myscript.sh

echo "Hello Hacers!"

# Loop through numbers (1 to 10)
for i in {1..10}; do
  echo "Line $i"
done

# Loop through files in a folder
for file in *.txt; do
  echo "Processing $file"
done

# Read a file line-by-line
while IFS= read -r line; do
  echo "Line: $line"
done < tomcat.txt

# if file exist
if [ -f tomcat.txt ]; then
  echo "File exists"
else
  echo "File not found"
fi

# if user is root
if [ "$USER" = "root" ]; then
  echo "You're root!"
fi

# case statement in BASH
read -p "Enter your choice (start|stop|restart): " action

case "$action" in
  start)
    echo "Starting..."
    ;;
  stop)
    echo "Stopping..."
    ;;
  restart)
    echo "Restarting..."
    ;;
  *)
    echo "Unknown command"
    ;;
esac

# convert each line in text file tomcat.txt to base64 and print output
for cred in $(cat tomcat.txt); do
  echo -n "$cred" | base64
  echo
done

# convert each line in text file tomcat.txt to base64 and print output (1 Liner)
for cred in $(cat tomcat.txt); do echo -n $cred | base64; done

# Print 20th line in file tomcat.txt
sed -n 20p tomcat.txt

# Show lines 5 to 10
sed -n '5,10p' tomcat.txt

# Base64 encode all lines in a file
while IFS= read -r line; do echo -n "$line" | base64; echo; done < tomcat.txt

# Find files modified in last 1 day
find . -type f -mtime -1

# Check if port 22 is open on IP
nc -zv 192.168.1.10 22

# Print only non-empty lines
grep -v '^$' file.txt
```

## Back to README.md
[BACK](../README.md)