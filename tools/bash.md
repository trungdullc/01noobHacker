# Basic Linux Commands

# Set TEMP variables
```
IP=8.8.8.8                              set temporarly variable in shell environment

env                                     printenv
```

## Help
```
whatis <COMMAND>                        short description if available, Note: Don't use commas
⭐man <COMMAND>
<COMMAND> --help                        <COMMAND> -h
apropos <COMMAND>
```

## TEMP Power
```
⭐sudo <COMMAND>                        Run a command as root
sudo -u <USERNAME> <COMMAND>            Run command as another user	sudo
⭐sudo su                               Open a root shell (becomes root)
⭐sudo su <USERNAME>                    Switch to a user as root
⭐⭐sudo!!                              Noob move, lazy retype command w/ sudo in front
```

## FILES & NAVIGATING
```
⭐file FILE1                            see file type
⭐ls -lah                               list all human readable files
cd <DIRECTORY>
cd                                      change directory to HOME
cd ~                                    change directory to Home
cd -                                    change to previous selected directory
cd ../..                                go back 2 parent directories
⭐pwd                                   show current directory
mkdir <DIRECTORY>                       create a folder
rm FILE1 FILE2                          remove FILE1 & FILE2
rm FILE?.txt                            remove FILE0.txt to FILE9.txt
rm FILE*                                remove all files that start with FILE
rm FILE.                                remove file named FILE.
rm -rf <DIRECTORY>                      remove non empty folder recursively
cp FILE1 FILE2                          copy FILE1 to FILE2
cp -r DIR1 DIR2
mv FILE1 FILE2                          rename FILE1 to FILE2
mv FILE1 DIR/FILE2                      move FILE1 to FILE2 into directory DIR
touch FILE                              create empty file or update file
notepad FILE                            * if have notepad set in linux
vi FILE                                 can also use vim if installed
nano FILE
cat FILE                                output contents of file
cat > FILE                              write stdinput to file
cat >> FILE                             append stdinput to file
tail -f FILE                            output content of file
tail -n 10 FILE                         output last 10 lines of file
head -n 10 FILE                         output first 10 lines of file
wc FILE                                 (l)ines (w)ords bytes
wc -c FILE                              Bytes (characters)
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
cat WORDS.txt | sort -r                             reverse sort
sort WORDS.txt | uniq -c                            count each uniq line, Note: must use sort before unique
sort WORDS.txt | uniq -u                            show unique words only no duplicates
cut -c1-4 FILE.txt                                  First 4 characters of each line
cut -d',' -f1,2 FILE.csv                            Extract 1st & 2nd field in comma-separated file, Delimiter is ,
cut -d':' -f1 /etc/passwd	                        Get usernames from passwd file, Delimiter is :
cut -f2                                             Get 2nd field (tab-delimited by default)
```

## Search
```
whereis <APP>                                       show all possible locations for program
⭐locate <FILE>                                     shows all possible locations for file
find . -name "*.txt"                                Find all .txt files from current dir
find / -perm -4000 -type f 2>/dev/null              # Find SUID binaries
find /var -type f -size +1M                         Find files over 1MB
find . -mtime -4                                    Find all files modified in last 4 days
# Note: Below search inside files, awk is grep w/ column awareness, sed is Stream EDitor
⭐ grep -E "PATTERN1 | PATTERN2" FILE1 FILE2        search in files for PATTERN
⭐ grep -ir "PATTERN" DIR                           search for pattern recursively & case insensitive in directory
awk '{print $1, $3}' file.txt                       Print 1st and 3rd columns
awk -F: '{print $1}' /etc/passwd                    Use ':' as delimiter
awk '$3 > 1000' /etc/passwd                         Print lines where 3rd field > 1000
sed 's/old/new/' file.txt                           /s: Substitute/Replace first 'old' with 'new' per line
sed 's/old/new/g' file.txt                          /g: Replace all 'old' with 'new'
sed '/pattern/d' file.txt                           /d: Delete lines matching pattern
sed -n '2,4p' file.txt                              p: Print only lines 2 to 4
```
[find](tools/find.md)<br>
[grep]()

## Networking
```
⭐arp -a                                ARP (Address Resolution Protocol) table
⭐ping <HOST>                           ping host 8.8.8.8 or google.com
⭐whois <DOMAIN>                        reconnaissance & threat intelligence
⭐dig <DOMAIN>                          returns DNS for domain
⭐dig -x <DOMAIN>                       return reserve lookup host
⭐wget FILE                             download file (exploit/script) for CTF
wget -c FILE                            continue topped download
wget -r URL                             recursively download files from url
wget --user-agent="EvilBot" URL         Spoof user agent (evade basic detection)
curl URL -O                             transfer data to/from server: DL from URL -O save file w/ original name
curl -o about.html URL                  -o save file to custom name about.html
# simulate login (pentesting: web forms, brute-force attacks, or fuzzing)
curl -X POST -d "username=admin&password=1234" http://target.com/login
# API testing, Recon, or scripting authenticated requests
curl -H "Authorization: Bearer eyJ...abc" https://api.example.com/user/profile

ip a                                    Show IP addresses
ifconfig                                ipconfig
netstat -tuln                           Show all network connections
ss -tuln                                Check Open Ports
```
[Resource Saver](https://chromewebstore.google.com/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb?hl=en-US&pli=1): DL <b>all resources</b> from website<br>
[certutil](certutil.md): Transfering Files<br>
[wget](tools/wget.md)

## Processes
```
⭐ps aux                            output all process show user column & background/demon (static)
top                                 real time monitoring (dynamic)
htop                                advanced real time monitoring (dynamic)
kill PID                            kill process w/ Process ID (PID)
⭐kill -9 PID                       SIGKILL (forced kill)
killall PROC                        kill all processes named PROC

sleep 100                           pause: ctrl + z
sleep 200 &
bg                                  resumes sleep in background
fg                                  brings sleep to foreground
fg %2                               brings 2nd job to foreground
⭐jobs                              view background jobs
```

# System Info (once got reverse shell on victim)
```
⭐whoami                            $USER
hostname                            $HOSTNAME
id                                  show current User and Groups
date
uptime                              shows uptime
w                                   shows who online
cat /proc/cpuinfo
cat /proc/meminfo
free                                show memory and swap usage
du                                  show directory space usage
du -sh                              display readable size in human-readable format (KB/MB/GB/TB)
df                                  show disk usage
⭐lscpu                             CPU info
lsblk                               Disk info
uname -a                            show kernel config
```
[guestmount](tools/guestmount.md)<br>
[showmount](tools/showmount.md)<br>
[snmp](tools/snmp.md)


## Compressing
```
gzip FILE1                              single file compression
gunzip FILE1.gz                         gzip -d FILE1.gz
bzip2 FILE1                             single file compression
bunzip2 FILE1.bz2                       bzip2 -d FILE1.bz2
tar cf ARCHIVE.tar FILE1 FILE2          archive, not compress
tar xf ARCHIVE.tar                      extract
zip FILES.zip FILE1 FILE2
unzip FILES.zip
7z a ARCHIVE.7z FILE1 FILE2
7z x ARCHIVE.7z
rar a ARCHIVE.rar FILE1 FILE2
unrar x ARCHIVE.rar
⭐apack ARCHIVE.zip FILE1 FILE2         Auto-detects compression by extension
⭐aunpack ARCHIVE.zip                   Auto-detect and extract
```

## Permissions
```
Note: Used w/ ls -la & creating scripts running with shebang #!/bin/bash
4   (R)ead          2   (W)rite         1   e(X)ecute
-rwxrwxrwx          chmod 777 FILE      chmod ugo+rwx FILE
-rwxr-xr-x          chmod 755 FILE      chmod u=rwx,g=rx,o=rx FILE
rw-r--r--           chmod 644 FILE      chmod u=rw,g=r,o=r FILE
rm write from group & others            chmod go-w FILE

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
apt update                                  Update package index (Debian/Ubuntu)
apt install <PACKAGE>                       Install a package
apt remove <PACKAGE>                        Remove a package
dnf install <PACKAGE>                       Install on Fedora/RHEL
dnf remove <PACKAGE>                        Remove from Fedora/RHEL
```

## Back to README.md
[BACK](/README.md)