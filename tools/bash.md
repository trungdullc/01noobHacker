# Basic Linux Commands

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
                                        
# Set TEMP variables
```
IP=8.8.8.8                              $env:IP = "8.8.8.8"             set temporarly variable in shell environment

env                                     Get-ChildItem Env:              printenv
```

## Help
```
whatis <COMMAND>                        Get-Command <COMMAND>           short description if available, Note: Don't use commas
⭐man <COMMAND>                        Get-Help <COMMAND> -Full
<COMMAND> --help        <COMMAND> -h    <cmd> /? 
apropos <COMMAND>                       Get-Help *<keyword>*
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
⭐ls -lah                               `Get-ChildItem -Force                       list all human readable files
cd <DIRECTORY>
cd                                      Set-Location                                change directory to HOME
cd ~                                                                                change directory to Home
cd -                                                                                change to previous selected directory
cd ../..                                                                            go back 2 parent directories
⭐pwd                                   Get-Location                                show current directory
realpath FILE/DIR                       Resolve-Path FILE/DIR
mkdir <DIRECTORY>                       New-Item -ItemType Directory DIR            create a folder
⭐mktemp -d
rm FILE                                 Remove-Item FILE
rm FILE1 FILE2                                                                      remove FILE1 & FILE2
rm FILE?.txt                                                                        remove FILE0.txt to FILE9.txt
rm FILE*                                                                            remove all files that start with FILE
rm FILE.                                                                            remove file named FILE.
rm -rf <DIRECTORY>                                                                  remove non empty folder recursively
cp FILE1 FILE2                          Copy-Item FILE1 FILE2                       copy FILE1 to FILE2
cp -r DIR1 DIR2
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
whereis <APP>                                       Get-Command app                         show all possible locations for program
⭐locate <FILE>                                     Get-ChildItem -Recurse -Filter FILE     shows all possible locations for file
find . -name "*.txt"                                Get-ChildItem -Recurse -Include *.txt   Find all .txt files from current dir
find / -perm -4000 -type f 2>/dev/null                                                      Find SUID binaries
find /var -type f -size +1M                                                                 Find files over 1MB
find . -mtime -4                                                                            Find all files modified in last 4 days
# Note: Below search inside files, awk is grep w/ column awareness, sed is Stream EDitor
⭐ grep -E "PATTERN1 | PATTERN2" FILE1 FILE2        Select-String -Pattern "pattern" FILE   search in files for PATTERN
⭐ grep -ir "PATTERN" DIR                                       search for pattern recursively & case insensitive in directory
grep "PATTERN" FILE                                                                         ❤️❤️❤️❤️❤️
grep -rl "FILENAME" DIR                             Get-ChildItem -Recurse | Select-String "PATTERN" ❤️❤️❤️❤️❤️
awk '{print $1, $3}' file.txt                       `Import-Csv file                        Print 1st and 3rd columns
awk -F: '{print $1}' /etc/passwd                                                            Use ':' as delimiter
awk '$3 > 1000' /etc/passwd                                                                 Print lines where 3rd field > 1000
sed 's/old/new/' file.txt                           (Get-Content file) -replace "old","new"
                                                                        /s: Substitute/Replace first 'old' with 'new' per line
sed 's/old/new/g' file.txt                                              /g: Replace all 'old' with 'new'
sed '/pattern/d' file.txt                                               /d: Delete lines matching pattern
sed -n '2,4p' file.txt                                                  p: Print only lines 2 to 4
```
[find](tools/find.md)<br>
[grep]()

## File Transfer over Network
```
⭐ssh -p <PORT> user@host                   Connect to SSH server on custom port
⭐scp -P <PORT> file user@host:/path        Copy file to remote host on custom port
⭐scp -P <PORT> user@host:/path/file .      Copy file from remote host on custom port
⭐telnet <HOST> <PORT>                      Connect to remote host via Telnet on specified port
⭐ftp <HOST>                                File Transfer Protocol client (unencrypted)
⭐sftp -P <PORT> user@host                  Secure FTP over SSH (interactive)
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
⭐kill -9 PID                                                       SIGKILL (forced kill)
killall PROC                        Stop-Process -Name PROC         kill all processes named PROC

sleep 100                                                           pause: ctrl + z
sleep 200 &
bg                                                                  resumes sleep in background
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
Note: Used w/ ls -la & creating scripts running with shebang #!/bin/bash
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

## CTF
[picoGym0450: openssl & sha256sum](../picoCTF/picoGym0450.md)

## Back to README.md
[BACK](../README.md)