# Restricted Environments (rbash)

```
# No ls dir find or grep
echo *                                          	Lists files in current dir
echo /home/*                                        Lists user folders
for f in *; do echo "$f"; done	                    Lists files one per line
while read f; do echo "$f"; done < <(ls)	        Use if ls exists but want scriptable output

# Read any file with mapfile
mapfile -t  < /etc/passwd
printf "$s\n" "${anything[@]}"

/etc/passwd                                         List of users
/etc/shadow	                                        Password hashes (if readable)
/proc/version	                                    Kernel version
/proc/cpuinfo	                                    CPU info
/proc/meminfo	                                    Memory info
/proc/self/environ	                                Current environment variables
/dev/null, /dev/zero, /dev/random	                Special devices (useful in scripting)

# read as input
echo "What's your name, age, city?"
read name age city
echo "$name is $age years old from $city"

# read as silent input
read -sp "Enter password: " password
echo
echo "Password length: ${#password}"

# read from file
while read line; do
  echo "Line: $line"
done < myfile.txt
```

## Back to README.md
[BACK](../README.md)