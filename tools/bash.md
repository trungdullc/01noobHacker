# Basic Linux Commands
# Note: No spaces in bash

# Install WSL (Windows Subsystem for Linux) on Windows
wsl --install ❤️❤️❤️❤️❤️
wsl

wsl --list --online
        The following is a list of valid distributions:
            NAME            FRIENDLY NAME
            Ubuntu          Ubuntu
            Debian          Debian GNU/Linux
            kali-linux      Kali Linux Rolling
wsl --install -d kali-linux
wsl -d kali-linux
sudo apt update && sudo apt upgrade -y

# clear
```
clear
ctrl + L
```

## alias
```
alias ping="ping -c 5"

AsianHacker-picoctf@webshell:~$ alias -p                            # Get-Alias
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
```

# Set TEMP variables
```
IP=8.8.8.8                              $env:IP = "8.8.8.8"             set temporarly variable in shell environment
env                                     Get-ChildItem Env:              printenv

# shell variables ont env variables
# env only shows environment variables
AsianHacker-picoctf@webshell:~$ myString="Some string"
AsianHacker-picoctf@webshell:~$ length=7
AsianHacker-picoctf@webshell:~$ export myString length ❤️❤️❤️❤️❤️
AsianHacker-picoctf@webshell:~$ env | grep -E '^(myString|length)='
length=7
myString=Some string
```

# Built-in variables
```
AsianHacker-picoctf@webshell:~$ echo "Last program's return value: $?"
Last program's return value: 0
AsianHacker-picoctf@webshell:~$ echo "Script's PID: $$"
Script's PID: 23
AsianHacker-picoctf@webshell:~$ echo "Number of args passed to script: $#"
Number of args passed to script: 0
AsianHacker-picoctf@webshell:~$ echo "All arguments passed to script: $@"
All arguments passed to script: 
AsianHacker-picoctf@webshell:~$ echo "Script's args seperated into diff variables: $1 $2..."
Script's args seperated into diff variables:  ...
```

## $(...) same as backticks ❤️❤️❤️❤️❤️
```
AsianHacker-picoctf@webshell:~$ echo "There are $(ls | wc -l) items here."
There are 5 items here.
AsianHacker-picoctf@webshell:~$ echo "There are `ls | wc -l` items here."
There are 5 items here.
```

## Help
```
AsianHacker-picoctf@webshell:~$ help
    help help
    help for
    help return
    help source
    help .
whatis <COMMAND>                        Get-Command <COMMAND>           short description if available, Note: Don't use commas
⭐man <COMMAND>                        Get-Help <COMMAND> -Full
<COMMAND> --help        <COMMAND> -h    <cmd> /? 
apropos <COMMAND>                       Get-Help *<keyword>*
AsianHacker-picoctf@webshell:~$ apropos info | grep "^info.*("
info (1ssl)          - OpenSSL application commands
infocmp (1)          - compare or print out terminfo descriptions
infotocap (1)        - convert a terminfo description into a termcap description
```

## Math Evaluation echo $((...))
```
AsianHacker-picoctf@webshell:~$ echo $(( 10 ** 3))
1000
AsianHacker-picoctf@webshell:~$ echo $(( 10 ^ 3))                   # 10 XOR 3
9
```

## Evaluation $()
```
AsianHacker-picoctf@webshell:~$ NAME1=$(whoami)
AsianHacker-picoctf@webshell:~$ NAME2=$(sudo whoami)
-bash: sudo: command not found
AsianHacker-picoctf@webshell:~$ echo "$NAME1"
AsianHacker-picoctf

AsianHacker-picoctf@webshell:~$ echo -e "cat\ndog\nbunny\nEOF" > file999.txt
AsianHacker-picoctf@webshell:~$ Contents=$(cat file999.txt)
AsianHacker-picoctf@webshell:~$ echo "$Contents"
cat
dog
bunny
EOF
AsianHacker-picoctf@webshell:~$ echo -e "START OF FILE\n$Contents\nEND OF FILE"
START OF FILE
cat
dog
bunny
EOF
END OF FILE
```

## Parameter Expansion ${...}
```
AsianHacker-picoctf@webshell:~$ echo "${myString}"
Some string
AsianHacker-picoctf@webshell:~$ echo "$myString"
Some string
AsianHacker-picoctf@webshell:~$ echo '$myString' ⚠️ Don't use ''
$myString ⚠️⚠️⚠️⚠️⚠️
AsianHacker-picoctf@webshell:~$ echo `$myString` ⚠️ Don't use ``
-bash: Some: command not found
```

## Indirect Expansion ${!...}
```
AsianHacker-picoctf@webshell:~$ other_variable="myString"
AsianHacker-picoctf@webshell:~$ echo ${!other_variable}
Some string
```

## Brace Expansion {..}
```
AsianHacker-picoctf@webshell:~$ echo {1..5}
1 2 3 4 5
AsianHacker-picoctf@webshell:~$ echo {a..c}
a b c
AsianHacker-picoctf@webshell:~$ echo {a..c} {1..5}
a b c 1 2 3 4 5
```

## String substitution (1st occurance)
```
AsianHacker-picoctf@webshell:~$ echo "${myString/Some/Hacker1}"
Hacker1 string
AsianHacker-picoctf@webshell:~$ echo $myString
Some string
AsianHacker-picoctf@webshell:~$ echo "${#myString}"                         # strlen
11
AsianHacker-picoctf@webshell:~$ echo "${myString:0:length}"
Some st
AsianHacker-picoctf@webshell:~$ echo "${myString: -5}"
tring
```

## array/list
```
AsianHacker-picoctf@webshell:~$ myArray=(one two three four five)
AsianHacker-picoctf@webshell:~$ echo "$myArray"
one
AsianHacker-picoctf@webshell:~$ echo "${myArray[0]}"
one
AsianHacker-picoctf@webshell:~$ echo "${myArray[@]}"
one two three four five
AsianHacker-picoctf@webshell:~$ echo "${#myArray[@]}"
5
AsianHacker-picoctf@webshell:~$ echo "${#myArray[1]}"
3
AsianHacker-picoctf@webshell:~$ echo "${myArray[@]:3:2}"
four five

# Print all elements w/ \n
AsianHacker-picoctf@webshell:~$ for item in "${myArray[@]}"; do
> echo "$item"
> done
one
two
three
four
five
```

## input (Note: Not need declare)
```
AsianHacker-picoctf@webshell:~$ echo "What is your name"
What is your name
AsianHacker-picoctf@webshell:~$ read name
Hacker X
AsianHacker-picoctf@webshell:~$ echo "Hello, $name!"
Hello, Hacker X!
```

## if[[]]; then
```
AsianHacker-picoctf@webshell:~$ if [[ "$name" != "$USER" ]]; then
> echo "Your name isn't your username"
> elif [[ "$name" == "Hacker X" ]]; then
> echo "Hi Hacker"
> else
> echo "Your name is your username"
> fi
Your name isn't your username

AsianHacker-picoctf@webshell:~$ if [[ "$name" == "Hacker X" ]] || [ "$age" == 30 ]]; then
> echo "This will run if either is True"
> fi
This will run if either is True

# Check if a string is empty or not set -z and -n to check if string is NOT empty ❤️❤️❤️
# Note: Spaces before and after matter ❤️
AsianHacker-picoctf@webshell:~$ if [[ -z "$name" ]]; then
> echo "name is unset"
> fi

AsianHacker-picoctf@webshell:~$ a=2
AsianHacker-picoctf@webshell:~$ b=5
AsianHacker-picoctf@webshell:~$ if [[ "$a" -lt "$b" ]]; then echo "$a is less than $b"; fi
2 is less than 5
    # Other comparison operators for numbers
    -ne     not equal
    -lt     less than
    -gt     greather than
    -le     less than or equal to
    -ge     greather than or equal to
```

## RegEx operator ~=
```
AsianHacker-picoctf@webshell:~$ email=me@example.com
AsianHacker-picoctf@webshell:~$ if [[ "$email" =~ [a-z]+@[a-z]{2,}\.(com|net|org) ]]; then
> echo "Valid email!"
> fi
Valid email!
```

## conditional execution, not ||
```
AsianHacker-picoctf@webshell:~$ echo "Always executed" || echo "Only"
Always executed
AsianHacker-picoctf@webshell:~$ echo "Always executed" && echo "Only"
Always executed
Only
AsianHacker-picoctf@webshell:~$ echo "Always executed" "Only"
Always executed Only
```

## Use subshells to work across directories
```
AsianHacker-picoctf@webshell:~$ (echo "First, I'm here $PWD") && (cd /tmp; echo "Then, I'm here: $PWD")
First, I'm here /home/AsianHacker-picoctf
Then, I'm here: /tmp
AsianHacker-picoctf@webshell:~$ pwd
/home/AsianHacker-picoctf
```

## Base case statements == Java/C++ switch
```
AsianHacker-picoctf@webshell:~$ case "$myString" in
> "Some string") echo "Some";;
> "hi") echo "Hello";;
> *) echo "This not null";;
> esac
Some

AsianHacker-picoctf@webshell:~$ myNumber=1337
AsianHacker-picoctf@webshell:~$ case "$myNumber" in
> 0) echo "This is 0";;
> 1) echo "This is 1";;
> *) echo "This not null";;
> esac
This not null
```

## for
```
AsianHacker-picoctf@webshell:~$ for ((i=1; i<=3; i++))
> do
> echo $i
> done
1
2
3

# -n no new line
AsianHacker-picoctf@webshell:~$ for ((i=1; i<=3; i++)); do echo -n "$i "; done
1 2 3

AsianHacker-picoctf@webshell:~$ for variable in {1..3}
> do
> echo "$variable"
> done
1
2
3

AsianHacker-picoctf@webshell:~$ for variable in {1..3}; do echo -n "$variable "; done
1 2 3 

AsianHacker-picoctf@webshell:~$ echo -e "dog\ncat\npig" > file1
AsianHacker-picoctf@webshell:~$ echo -e "red\nblue\ngreen" > file2
AsianHacker-picoctf@webshell:~$ for variable in file1 file2
> do
> cat "$variable"
> done
dog
cat
pig
red
blue
green

AsianHacker-picoctf@webshell:~$ for output in $(ls)
> do
> cat "$output"
> done

AsianHacker-picoctf@webshell:~$ for output in /tmp 
> do
> cat "$output"
> done
cat: /tmp: Is a directory
```

## while
```
AsianHacker-picoctf@webshell:~$ while true; do
> echo "loop body"
> break
> done
loop body

AsianHacker-picoctf@webshell:~$ while [[ $myString == "Some string" ]]; do                              
> echo "loop body"
> break
> done
loop body
AsianHacker-picoctf@webshell:~$ while [[ $myString == "Some string" ]]; do echo "loop body"; break; done
loop body

# POSIX sythax uses [] and = (confusing)
AsianHacker-picoctf@webshell:~$ while [ "$myString" = "Some string" ]; do
>   echo "loop body"
>   break
> done
loop body
```

## TEMP Power
```
⭐sudo <COMMAND>                        Run PS as Administrator                     Run a command as root
sudo -u <USERNAME> <COMMAND>            Run command as another user	sudo
⭐sudo su                               Start-Process PowerShell -Credential user   Open a root shell (becomes root)
⭐sudo su <USERNAME>                    Start-Process PowerShell -Verb RunAs        Switch to a user as root
⭐⭐sudo!!                                                                          Noob move, lazy retype command w/ sudo in front
```

## FILES & NAVIGATING
```
⭐file FILE1                            `Get-Item FILE                              see file type
ls -l                                                                               list every file and dir on seperate lines
ls -t                                                                               sort dir by last-modified date (descending)
ls -R                                                                               recursively ls this dir and all of its subdirectory
⭐ls -lah                               `Get-ChildItem -Force                       list all human readable files
cd <DIRECTORY>
cd                                      Set-Location                                change directory to HOME
cd ~                                                                                change directory to HOME
cd ~/Docutments/..                                                                  cd to HOME
cd -                                                                                change to previous selected directory
cd ../..                                                                            go back 2 parent directories
⭐pwd                                   Get-Location                                show current directory
realpath FILE/DIR                       Resolve-Path FILE/DIR
mkdir <DIRECTORY>                       New-Item -ItemType Directory DIR            create a folder
mkdir -p myNewDir/with/intermediate                                                 create subfolders
⭐mktemp -d
rm FILE                                 Remove-Item FILE
rm FILE1 FILE2                                                                      remove FILE1 & FILE2
rm FILE?.txt                                                                        remove FILE0.txt to FILE9.txt
rm FILE*                                                                            remove all files that start with FILE
rm FILE.                                                                            remove file named FILE.
rm -rf <DIRECTORY>                                                                  remove non empty folder recursively
cp FILE1 FILE2                          Copy-Item FILE1 FILE2                       copy FILE1 to FILE2
cp -r SOURCE DEST
mv FILE1 FILE2                          Move-Item FILE1 FILE2                       rename FILE1 to FILE2
mv FILE1 DIR/FILE2                                                                  move FILE1 to FILE2 into directory DIR
touch FILE                              New-Item FILE                               create empty file or update file
notepad FILE                                                                        * if have notepad set in linux
vi FILE                                                                             can also use vim if installed
nano FILE
cat FILE                                Get-Content FILE                            output contents of file
cat > FILE                                                                          write stdinput to file
cat >> FILE                                                                         append stdinput to file
cat ~/FILE                                                                          ❤️❤️❤️❤️❤️
tail -f FILE                            Get-Content FILE -Wait                      output content of file
tail -n 10 FILE                                                                     output last 10 lines of file
head -n 10 FILE                         Get-Content FILE -TotalCount 10             output first 10 lines of file
wc FILE                                 `(Get-Content FILE                          (l)ines (w)ords bytes
wc -c FILE                                                                          Bytes (characters)
```
[Magic Numbers](https://en.wikipedia.org/wiki/List_of_file_signatures): Starting values that identify a file format<br>
[stat](tools/stat.md): Output file info<br>
[strings](tools/strings.md): Output sequence of human readable characters from a file

## Comparing Files
```
diff FILE1 FILE2                                    shows line by line differences
sdiff FILE1 FILE2                                   shows side by side file comparison
```

## Sorting and Extracting
```
uniq -d WORDS.txt
cat WORDS.txt | sort -r                             reverse sort
sort WORDS.txt | uniq -c                            count each uniq line, Note: must use sort before unique
sort WORDS.txt | uniq -u                            show unique words only no duplicates
cut -c1-4 FILE.txt                                  First 4 characters of each line
cut -d"," -f 1 FILE.txt                             Print only 1st column before , character
cut -d',' -f1,2 FILE.csv                            Extract 1st & 2nd field in comma-separated file, Delimiter is ,
cut -d':' -f1 /etc/passwd	                        Get usernames from passwd file, Delimiter is :
cut -f2                                             Get 2nd field (tab-delimited by default)
```

## Search
```
whereis <APP>                                       Get-Command app                         show all possible locations for program
⭐locate <FILE>                                     Get-ChildItem -Recurse -Filter FILE     shows all possible locations for file
find . -name "*.txt"                                Get-ChildItem -Recurse -Include *.txt   Find all .txt files from current dir
find / -perm -4000 -type f 2>/dev/null                                                      Find SUID binaries /dev/null 2>&1
find /var -type f -size +1M                                                                 Find files over 1MB
find . -mtime -4                                                                            Find all files modified in last 4 days
# Note: Below search inside files, awk is grep w/ column awareness, sed is Stream EDitor
⭐ grep -E "PATTERN1 | PATTERN2" FILE1 FILE2        Select-String -Pattern "pattern" FILE   search in files for PATTERN
⭐ grep -ir "PATTERN" DIR                                       search for pattern recursively & case insensitive in directory
grep "PATTERN" FILE                                                                         ❤️❤️❤️❤️❤️
grep -rl "FILENAME" DIR                             Get-ChildItem -Recurse | Select-String "PATTERN" ❤️❤️❤️❤️❤️
grep "^foo.*bar$" file.txt                          Print lines which begin w/ foo and end w/ bar but ignore binary files
grep "^foo.*bar$" file.txt | grep -v "not"                                                  -v: inverse match same as !=
grep -c "^foo.*bar$" file.txt                                                               -c: print number of lines that match RE
grep -r "^foo.*bar$" someDir/                                                               -r: recursively
grep -n "^foo.*bar$" file.txt                                                               -n: give line numbers
fgrep "foobar" file.txt                                                                     search string w/o RE, grep -F
awk '{print $1, $3}' file.txt                       `Import-Csv file                        Print 1st and 3rd columns
awk -F: '{print $1}' /etc/passwd                                                            Use ':' as delimiter
awk '$3 > 1000' /etc/passwd                                                                 Print lines where 3rd field > 1000
sed 's/old/new/' file.txt                           (Get-Content file) -replace "old","new"
                                                                        /s: Substitute/Replace first 'old' with 'new' per line
sed 's/old/new/g' file.txt                                              /g: Replace all 'old' with 'new'
sed -i "s/bad/better/g" file.txt                                        -i: ignore case sub bad w/ better globally
sed '/pattern/d' file.txt                                               /d: Delete lines matching pattern
sed -n '2,4p' file.txt                                                  p: Print only lines 2 to 4
```
[find](../tools/find.md)<br>
[grep](../tools/grep.md)

## File Transfer over Network
```
⭐ssh -p <PORT> user@host                   Connect to SSH server on custom port
⭐scp -P <PORT> file user@host:/path        Copy file to remote host on custom port (remote cp)
⭐scp -P <PORT> user@host:/path/file .      Copy file from remote host on custom port
⭐telnet <HOST> <PORT>                      Connect to remote host via Telnet on specified port
⭐ftp <HOST>                                File Transfer Protocol client (unencrypted)
⭐sftp -P <PORT> user@host                  Secure FTP over SSH (interactive scp)
⭐rsync -e "ssh -p <PORT>" src dest         Remote sync files w/ SSH for large or incremental transfers
⭐nc                                        Raw TCP/UDP used to transfer files in tricky environments
⭐⭐⭐sz FILE                              Download from remote server
⭐⭐⭐⭐⭐rz -y                           Upload to remote server ❤️❤️❤️❤️❤️
```
cd /path/to/files<br>
python3 -m http.server 8000

## Networking
```
⭐arp -a                                                                        ARP (Address Resolution Protocol) table
⭐ping <HOST>                           Test-Connection host                    ping host 8.8.8.8 or google.com
⭐whois <DOMAIN>                        Resolve-DnsName domain                  reconnaissance & threat intelligence
⭐dig <DOMAIN>                          Resolve-DnsName domain                  returns DNS for domain
⭐dig -x <DOMAIN>                       return reserve lookup host
⭐wget FILE                             Invoke-WebRequest URL -OutFile file     download file (exploit/script) for CTF
wget -c FILE                                                                    continue topped download
wget -r URL                                                                     recursively download files from url
wget --user-agent="EvilBot" URL                                                 Spoof user agent (evade basic detection)
curl URL -O                             Invoke-WebRequest URL
                                                transfer data to/from server: DL from URL -O save file w/ original name
curl -o about.html URL                          -o save file to custom name about.html
# simulate login (pentesting: web forms, brute-force attacks, or fuzzing)
curl -X POST -d "username=admin&password=1234" http://target.com/login
# API testing, Recon, or scripting authenticated requests
curl -H "Authorization: Bearer eyJ...abc" https://api.example.com/user/profile

ip a                                    Get-NetIPAddress                        Show IP addresses
ifconfig                                ipconfig
netstat -tuln                           Get-NetTCPConnection                    Show all network connections
ss -tuln                                Get-NetUDPEndpoint                      Check Open Ports
```
[Resource Saver](https://chromewebstore.google.com/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb?hl=en-US&pli=1): DL <b>all resources</b> from website<br>
[certutil](certutil.md): Transfering Files<br>
[wget](tools/wget.md)

## Processes
```
⭐ps aux                            Get-Process                     output all process show user column & background/demon (static)
top                                                                 real time monitoring (dynamic)
htop                                                                advanced real time monitoring (dynamic)
kill PID                            Stop-Process -Id PID            kill process w/ Process ID (PID)
kill %2                                                             Kill job number 2
⭐kill -9 PID                                                       SIGKILL (forced kill)
killall PROC                        Stop-Process -Name PROC         kill all processes named PROC

sleep 100                                                           pause: ctrl + z
sleep 200 &
# Ctrl + c: kill process, Ctrl + z: pause
⭐bg                                                                resumes sleep in background
fg                                                                  brings sleep to foreground
fg %2                                                               brings 2nd job to foreground
⭐jobs                              Get-Job                         view background jobs
```

# System Info (once got reverse shell on victim)
```
⭐whoami                            $env:USERNAME                                               $USER
hostname                            hostname                                                    $HOSTNAME
id                                  whoami /all                                                 show current User and Groups
date
uptime                              (Get-CimInstance Win32_OperatingSystem).LastBootUpTime      shows uptime
w                                   query user                                                  shows who online
cat /proc/cpuinfo                   Get-CimInstance Win32_Processor
cat /proc/meminfo                   Get-CimInstance Win32_PhysicalMemory
free                                Get-Counter '\Memory\Available MBytes'                      show memory and swap usage
du                                                                                              show directory space usage
du -sh                                                          display readable size in human-readable format (KB/MB/GB/TB)
df                                  Get-PSDrive                                                 show disk usage
⭐lscpu                                                                                         CPU info
lsblk                               Get-Disk                                                    Disk info
uname -a                            systeminfo                                                  show kernel config
⭐mmls disk.img                                                                                 Autopsy(GUI)
⭐fls -o <START#> disk.img                                                                      Autopsy(GUI)
⭐fls -o <START#> disk.img <MEMORY#>                                                            Autopsy(GUI)
⭐icat -o <START#> disk.img <MEMORY#>                                                           Autopsy(GUI)
```
[guestmount](tools/guestmount.md)<br>
[showmount](tools/showmount.md)<br>
[snmp](tools/snmp.md)


## Compressing
```
gzip FILE1                                                                  single file compression
gunzip FILE1.gz                     gzip -d FILE1.gz ❤️❤️❤️❤️❤️
bzip2 FILE1                                                                 single file compression
bunzip2 FILE1.bz2                   bzip2 -d FILE1.bz2 ❤️❤️❤️❤️❤️
tar cf ARCHIVE.tar FILE1 FILE2          tar.exe -xf file.tar                archive, not compress
tar xf ARCHIVE.tar                                                          extract
                                                                                        zip --encrypt -r my_protected_info.zip my_info/
zip FILES.zip FILE1 FILE2               Compress-Archive FILE1 FILE2
unzip FILES.zip                         Expand-Archive FILES.zip            ❤️❤️❤️❤️❤️
7z a ARCHIVE.7z FILE1 FILE2                                                 7ZIP (GUI)
7z x ARCHIVE.7z
rar a ARCHIVE.rar FILE1 FILE2                                               WinRar (GUI)
unrar x ARCHIVE.rar
⭐apack ARCHIVE.zip FILE1 FILE2         Auto-detects compression by extension
⭐aunpack ARCHIVE.zip                   Auto-detect and extract
```
zcat FILE1.gz                           Read w/o extract 

## Permissions
```
Note: Used w/ ls -la & creating scripts running with shebang #!/bin/bash or #!/usr/bin/env bash
4   (R)ead          2   (W)rite         1   e(X)ecute
-rwxrwxrwx          chmod 777 FILE      chmod ugo+rwx FILE
-rwxr-xr-x          chmod 755 FILE      chmod u=rwx,g=rx,o=rx FILE
rw-r--r--           chmod 644 FILE      chmod u=rw,g=r,o=r FILE
rm write from group & others            chmod go-w FILE
                    chmod -R 777 DIR ❤️❤️❤️❤️❤️

chown Hacker FILE                       change owner of FILE
chown HACKER:DEV FILE                   change owner & group of FILE

chgrp DEV FILE                          change group of FILE
```

## Privilege
```
sudo useradd hacker                         sudo userdel -r hacker
sudo passwd hacker
sudo usermod -aG sudo hacker                sudo gpasswd -d hacker sudo
sudo usermod -G group1,group2 hacker        # Modifying User's groups
```

## Package Managment
```
apt-cache search <PACKAGE>                  ❤️❤️❤️❤️❤️
apt search <PACKAGE>                        Newer than apt-cache, also formatted
apt show <PACKAGE>
apt update                                  Update package index (Debian/Ubuntu)
sudo apt install <PACKAGE>                  Install a package ❤️❤️❤️❤️❤️
sudo apt remove <PACKAGE>                   Remove a package
dnf install <PACKAGE>                       Install on Fedora/RHEL
dnf remove <PACKAGE>                        Remove from Fedora/RHEL
```

## Scripting
```
trap "rm $TEMP_FILE; exit" SIGHUP SIGINT SIGTERM            # execute command when trap signal activates
```

## Functions
```
# Note: Bash fx just calls
# Return values can be obtained w/ $?
# ${0}, ${1}, ${2} are arguments
# return (and $?) are limited to 0–255, so return 911 becomes 911 % 256 = 143 ❤️
AsianHacker-picoctf@webshell:~$ function foo() {
> echo "Arguments work just like script arguments: $@"
> echo "And: $1, $2"
> echo "This is a fx"
> returnValue=911
> return $returnValue
> }
AsianHacker-picoctf@webshell:~$ foo hacker du
Arguments work just like script arguments: hacker du
And: hacker, du
This is a fx
AsianHacker-picoctf@webshell:~$ echo $?
143

# Another way to declare fx w/o using function keyword
AsianHacker-picoctf@webshell:~$ bar() {
> echo "Another way to declare fx"
> return 0
> }
AsianHacker-picoctf@webshell:~$ bar
Another way to declare fx
```

## Du Investigation
```
AsianHacker-picoctf@webshell:~$ env
SHELL=/bin/bash
LESS=R
NVM_INC=/usr/local/nvm/versions/node/v22.14.0/include/node
PWD=/home/AsianHacker-picoctf
LOGNAME=AsianHacker-picoctf
HOME=/home/AsianHacker-picoctf
PATH=/home/AsianHacker-picoctf/.local/bin:/usr/local/nvm/versions/node/v22.14.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/go/bin
NVM_BIN=/usr/local/nvm/versions/node/v22.14.0/bin
MAIL=/var/mail/AsianHacker-picoctf
_=/usr/bin/env
```

## CTF
[picoGym0450: openssl & sha256sum](../picoCTF/picoGym0450.md)

## Back to README.md
[BACK](../README.md)