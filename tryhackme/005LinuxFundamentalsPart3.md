# Linux Fundamentals Part 3
```bash
# Start Machine (Victim)
    Add 1 hour
    Terminate

tryhackme@linux3:~$ ifconfig ⌨️
inet 10.0.3.5

# Start AttackBox
AttackBox:
root@ip-10.0.3.4:~# ifconfig ⌨️
inet 10.0.3.4
root@ip-10.0.3.4:~# ssh tryhackme@10.0.3.5 ⌨️
The authenticity of host '10.0.3.5 (10.0.3.5)' can't be estabished.
ECDSA key fingerprint is SHA256:0x0w0edamthathardpassFR08jum.
Are you sure you want to continue connecting (yes/no)? yes ⌨️
Warning: Permanently added '10.0.3.5' (ECDSA) to the list of known hosts.
tryhackme@10.0.3.5's password: tryhackme ⌨️
tryhackme@linux3:~$
```

# Task 3: Terminal Text Editors
```bash
tryhackme@linux3:~$ nano myfile ⌨️
    Save/Write Out:     Ctrl + O
    Exit:               Ctrl + X
tryhackme@linux3:~$ vim myfile ⌨️
tryhackme@linux3:~$ nvim myfile ⌨️                    # if neovim allowed
    tryhackme@linux3:~$ sudo nvim ⌨️
    sudo nvim
    :!bash
tryhackme@linux3:~$ gedit myfile ⌨️
tryhackme@linux3:~$ mousepad myfile ⌨️

# Open current folder/directory
Windows (CMD / PowerShell)                           Linux                   macOS
start . ⌨️                                           xdg-open .              open . ⌨️
explorer . 
```

# Task 4: General/Useful Utilities
```bash
# Downloading Files w/ wget
# Review below

# Transfering Files from host w/ SCP
Secure copy (SCP) is cp command + using SSH protocol (authentication + encrpytion)
# Uploading to remote server
tryhackme@linux3:~$ scp important.txt bandit01@192.168.1.30:/home/ /renamed.txt ⌨️
# Downloading from remote server
tryhackme@linux3:~$ scp bandit01@192.168.1.30:/home/renamed.txt renamedagain.txt ⌨️

# Serving Files from your host
tryhackme@linux3:~$ python3 -m http.server 8080 & ⌨️         # python3 runs http.server module
[9] 1337
tryhackme@linux3:~$ fg %9 ⌨️
tryhackme@linux3:~$ ifconfig ⌨️                              # Note: if not use & use tmux
inet 10.0.3.5
# Optional: Bind to specific IP
tryhackme@linux3:~$ python3 -m http.server --bind 10.0.3.5 ⌨️

tryhackme@linux3:~$ wget http://10.0.3.5:8000/renamedagain.txt ⌨️
Browser: http://10.0.3.5:8080/renamedagain.txt ⌨️            # default port: 8000

tryhackme@linux3:~$ cp renamedagain.txt /var/www/html/ ⌨️    # apache2
tryhackme@linux3:~$ sudo systemctl start apache2 ⌨️            
# start, stop, restart, enable, disable, restart, reload, status ⭐⭐⭐⭐⭐

tryhackme@linux3:~$ wget http://10.0.3.5/renamedagain.txt ⌨️
Browser: http://10.0.3.5/renamedagain.txt ⌨️

tryhackme@linux3:~$ cp renamedagain.txt /var/www/html/ ⌨️    # nginx
tryhackme@linux3:~$ sudo systemctl start nginx ⌨️

tryhackme@linux3:~$ wget http://10.0.3.5/renamedagain.txt ⌨️
Browser: http://10.0.3.5/renamedagain.txt ⌨️

# CTF tip
sudo -l ⌨️
(root) /bin/systemctl
    Start malicious services
    Abuse writable unit files
    systemctl is a known privilege escalation vector
```
[Review: wget & curl(Task 2)](./002IntroductoryResearching.md)<br>
[updog > python3 -m http.server](../tools/updog.md)

# Task 5: Processes 101
```bash
# view your processes (static)
tryhackme@linux3:~$ ps ⌨️
# view processes run by other users that not run from a session(static)
tryhackme@linux3:~$ ps aux ⌨️

# view your processes (live)
tryhackme@linux3:~$ top ⌨️            # 10 sec refreshes
tryhackme@linux3:~$ htop ⌨️
    PID     USER        COMMAND
    1       root        systemd     # process copied to child but not share memory like threads
    1337    root        init

# Managing Processes
tryhackme@linux3:~$ kill -l ⌨️                # list all signals
SIGTERM(15):    Kill process, but allow it to do some cleanup tasks beforehand
SIGKILL(9):     Kill process - does not do any cleanup after the fact
SIGSTOP(19):    Stop/suspend a process

tryhackme@linux3:~$ kill 1337 ⌨️              # default SIGTERM
tryhackme@linux3:~$ kill -STOP 1337 ⌨️        # kill -19 1337 (pause)
    tryhackme@linux3:~$ kill -CONT 1337 ⌨️    # kill -18 1337 (continue)
tryhackme@linux3:~$ kill -9 1337 ⌨️           # last resort

# Getting Processes/Services to start on boot
Some applications can be started on the boot of the system (web servers, databaseservers, or file transfer servers)
systemctl command allow us to interact w/ systemd process/daemon
syntax: systemctl [option] [service]

# An introduction to backgrounding and foregrounding in Linux
Process can run in two states: background(bg) & foreground(fg)
# Note: Ctrl + Z:   Force process to go into background ⭐⭐⭐
# May need kill sinces uses up resources/memory
```

# Task 6: Maintaining Your System: Automation
```bash
# Windows: Task Scheduler

# crontabs to interact with cron process 
# Crontab process started during boot, facilitating & managining cron jobs
# crontabs requires 6 specific values
#   MIN:    minute
#   HOUR:   hour
#   DOM:    day of the month
#   MON:    month of year
#   DOW:    day of week
#   CMD:    command to execute 

Google: crontab generator ⌨️
    Results: https://crontab.io/

# edit crontab
tryhackme@linux3:~$ crontab -e ⌨️
    # backup files every 12 hours
    0 */12 * * * cp -R /home/hackeredu/Documents /var/backups/ >/dev/null 2>&1 ⌨️
    # special timer: runs every time computer reboots
    @reboot /var/opt/processes.sh
```

# Task 7: Maintaining Your System: Package Management
```bash
# Introducing Packages & Software Repos
developers wish to submit software to community submitted to "apt" repository
if approved others can download and use
tryhackme@linux3:~$ cd /etc/apt/ ⌨️
tryhackme@linux3/etc/apt:~$ ls ⌨️
apt.conf.d  auth.conf.d  keyrings  preferences.d  sources.list  sources.list.d  trusted.gpg.d
tryhackme@linux3/etc/apt:~$ vi sources.list                 # Note: Shows all sources we pull from
    deb http://security.ubuntu.com/ubuntu bionic-securtty main restricted
    # deb-src http://securtty.ubuntu.cbm/ubuntu bionic-security main restricted
    deb http://security.ubuntu.com/ubuntu bionic-security universe
    # deb-src http://security.ubuntu.com/ubuntu bionic-security universe

# Managing your repositiries (Adding and Removing)
apt (package managment software) contains suite of tools to manage packages
    apt command
tryhackme@linux3/etc/apt:~$ add-apt-repository ⌨️

# Note: can install software using dpkg (Debian package installers) but apt checks for updates

# Add community repositories to your list because OS vendors maintain their own repositories
# Note: When add docker or Sublime Text have to update sources.list bc out of date
# When adding software, integrity of dl guaranteed by GPG (Gnu Privacy Guard) keys
# DL GPG key and use apt-key to trust it
tryhackme@linux3/etc/apt:~$ wget -q0 https://download.sublimetext.com/sublimehq-pub.gpg |
sudo apt-key add ⌨️
# Create file name sublime-text.list in /etc/apt/sources.list.d
tryhackme@linux3/etc/apt:~$ vi sublime-text.list.d ⌨️
deb https://download.sublimetext.com/ apt/stable/
# Update apt to recognize new entry
tryhackme@linux3/etc/apt:~$ apt update ⌨️
# Install software that we trusted
tryhackme@linux3/etc/apt:~$ apt install sublime-txt ⌨️

# Note: apt purge ⌨️ (rm config files also)
# Optional: Removing packages
tryhackme@linux3/etc/apt:~$ sudo add-apt-repository --remove ppa:webupd8team/sublime-text-3 ⌨️
# Optional: Manual deleting packages
tryhackme@linux3/etc/apt:~$ apt remove sublime-txt ⌨️
# Update after remove
tryhackme@linux3/etc/apt:~$ apt update ⌨️
```

# Task 8: Maintaining Your System: Logs
```bash
hackerdu@DESKTOP:~$ cd /var/log/ ⌨️
hackerdu@DESKTOP:/var/log$ ls ⌨️
README            auth.log       dist-upgrade  dmesg.1.gz  dmesg.4.gz  fontconfig.log  landscape  syslog
alternatives.log  bootstrap.log  dmesg         dmesg.2.gz  dpkg.log    journal         lastlog    unattended-upgrades
apt               btmp           dmesg.0       dmesg.3.gz  faillog     kern.log        private    wtmp

# Note: On TryHackMe not my wsl there 3 services running on Ubuntu machine
# Apache2 web server
apache2
# Logs for fail2ban service (monitoringbrute force)
fail2ban.log
fail2ban.log1
fail2ban.log.2.gz
fail2ban.log.3.gz
fail2ban.log.4.gz
# UFW service (firewall)
ufw.log
ufw.log.1
ufw.log.2.gz
ufw.log.3.gz
ufw.log.4.gz

# 2 types of important logs are
access.log
access.log.1
error.log
error.log.1

# Note: Other tools Splunk

Q1: What is the IP address of the user who visited the site?
cd /var/log/apache2/ ⌨️
vi access.log.1 ⌨️

Q2: What file did they access?
GET /catsanddogs.jpg
```