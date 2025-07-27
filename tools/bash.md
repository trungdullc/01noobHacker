# Basic Linux Commands

# Set TEMP variables
```
IP=8.8.8.8                              set temporarly variable in shell environment

env                                     printenv
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
```

## Networking
```
⭐ping <HOST>                           ping host 8.8.8.8 or google.com
whois <DOMAIN>                          reconnaissance & threat intelligence
dig <DOMAIN>                            returns DNS for domain
dig -x <DOMAIN>                         return reserve lookup host
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
```

## Processes
```
⭐ps aux                            output all process show user column & background/demon (static)
top                                 real time monitoring (dynamic)
htop                                advanced real time monitoring (dynamic)
kill PID                            kill process w/ Process ID (PID)
killall PROC                        kill all processes named PROC
```

# System Info (once got reverse shell on victim)
```
⭐whoami                            $USER
hostname
date
uptime                              shows uptime
w                                   shows who online
cat /proc/cpuinfo
cat /proc/meminfo
free                                show memory and swap usage
du                                  show directory space usage
du -sh                              display readable size in GB
df                                  show disk usage
uname -a                            show kernel config
```

## Compressing
```
tar cf FILE.tar FILE1 FILE2         compress

```