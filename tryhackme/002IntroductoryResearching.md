# Introductory Researching
## Task 2: Example Research Question on steganography
```bash
# Note: curl -o index.html https://example.com
# Note (Save using remote filename): curl -O https://example.com/file.zip ❤️
# wget https://example.com/file.zip ❤️❤️❤️❤️❤️

For a CTF challenge you download a JPEG using wget URL or curl -o output_file URL
but you suspect something hidden inside

Google: hiding things inside images site:null-byte.wonderhowto.com
    Results: Steganography

Google: extract hidden data from image
    aperisolve (site)
    file
    strings                                     # hidden plaintext
    exiftool                                    # Metadata hiding
    binwalk                                     # Finds embedded files (ZIP, PNG)
    outguess
    foremost                                    # recovers file based on headers
    zsteg (png/bmp)
    stegsolve (png/bmp)
    steghide extract -sf image.jpg (jpg)

AttackBox:
root@kali:~# ifconfig ⌨️
inet 10.0.3.5
# Optional
root@kali:~# sudo apt update && sudo apt upgrade ⌨️
root@kali:~# sudo apt-get install steghide & ⌨️   # & runs in bg

Google: What hash format are modern Windows login passwords stored in?
    Results: LM hash or NTLM hash.  File can be found in %SystemRoot%/system32/config/SAM and mounted on HKLM/SAM
    NTML Decoder: https://md5decrypt.net/en/Ntlm/

sha256crypt is a password hashing algorithm based on the SHA-256 cryptographic hash function, designed as a more secure alternative to older schemes like md5crypt.
    root@kali:~# hash-identifier ⌨️
    https://www.boxentriq.com/code-breaking/cipher-identifier
    https://www.dcode.fr/cipher-identifier
    https://www.dcode.fr/sha256-hash

Favorite Encrpyt/Decrypt site:
    https://cyberchef.io/
Favorite AI Bot:
    https://www.hacktricks.ai/?reset=true
```

## Task 3: Vulnerability Searching: Reconnaissance
```bash
# CMS (Content Managment Systems)
People used to use Wordpress, FuelCMS, Ghost to setup websites now people using AI (unsecure)

Vulnerability Search
    SHODAN (NOT FREE) https://www.shodan.io/

    nvd: https://nvd.nist.gov/vuln
    cve: https://www.cve.org/
    exploit-db.com: https://www.exploit-db.com/         # made by hackers used by hackers
        https://www.exploit-db.com/searchsploit
        root@kali:~# sudo apt update && sudo apt -y install exploitdb ⌨️
        root@kali:~# searchsploit -h ⌨️
    searchsploit:
        # Optional: Update SearchSploit database
        root@kali:~# searchsploit -u ⌨️
        root@kali:~# searchsploit <search_term> ⌨️
        # Copy exploit into working dir
        root@kali:~# searchsploit -m <exploit_path> ⌨️
        # Move exploit into metasploit's module
        root@kali:~#  mv <exploit_file> ~/.msf4/modules/exploits/<category>/ ⌨️
        # Reload modules including new exploit
        root@kali:~# sudo service postgresql start && msfconsole -q ⌨️
        msf > reload_all ⌨️
        # Use exploit in metasploit
        msf > search <exploit_name> ⌨️
        msf > use <exploit_path> ⌨️
        # Configure required options (target, payload) and execute
        msf > set RHOSTS <target_ip> ⌨️
        msf > set PAYLOAD <payload_name> ⌨️
        msf > exploit ⌨️
    metasploit: 
        root@kali:~# sudo service postgresql start && msfconsole -q ⌨️
        # Use search command
        msf > search -h ⌨️
        msf > search scanner ⌨️
        # Get module details
        msf > info auxiliary/scanner/portscan/tcp ⌨️
        # show exploits
        msf > show exploits ⌨️
        # load and configure modules
        msf > use auxiliary/scanner/portscan/tcp ⌨️
        msf > set RHOSTS <target_ip> ⌨️
        # run module
        msf > run ⌨️

Firefox: Shown website and what software it runs: Welcome to Fuel CMS Version 1.4
# Search for exploits
root@kali:~# searchsploit fuelcms ⌨️

Q1: What is the CVE for the 2020 Cross-Site Scripting (XSS) vulnerability found in WPForms?
Google Result: CVE-2020-10385

Q2: There was a Local Privilege Escalation vulnerability found in the Debian version of Apache Tomcat, back in  2016. What is the CVE for this vulnerability?
Google Result: CVE-2016-1240

Q3: What is the very first CVE found in the VLC media player?
Google Result: CVE-2007-0017

Q4: If I wanted to exploit a 2920 buffer overflow in the sudo program, which CVE would I use?
Google Result: CVE-2019-18634
```

## Task 4: Manual Pages
```bash
root@kali:~# man ssh | grep -e "version" ⌨️
    -V  Display the version number and exit.
root@kali:~# whatis ssh ⌨️
root@kali:~# ssh --help ⌨️
root@kali:~# apropos ssh ⌨️

# update tldr
$ tldr --update ⌨️
# tldr help
$ tldr --help ⌨️

# On Debian, Ubuntu, Pop!_OS, Mint
$ sudo apt update && sudo apt install tldr ⌨️
# On RedHat, Fedora, CentOS, AlmaLinux
$ sudo dnf install tldr ⌨️
# On Arch, Manjaro, EndeavourOS
$ sudo pacman -S tldr ⌨️
# Other package managers (npm, pip3, homebrew)
$ npm install -g tldr ⌨️
$ pip3 install tldr ⌨️
$ brew install tldr ⌨️

Q1: SCP is a tool used to copy files from one computer to another. What switch would you use to copy an entire directory?
hackerdu@DESKTOP:~$ man scp | grep -e "director" ⌨️
    -r      Recursively copy entire directories.  Note that scp follows symbolic links encountered in the tree

Q2: fdisk is a command used to view and alter the partitioning scheme used on your hard drive. What switch would you use to list the current partitions?
hackerdu@DESKTOP:~$ man fdisk | grep -e "list" ⌨️
    -l, --list
        always listed in the order in which they are specified on the command-line, or by the kernel listed in

Q3: nano is an easy- to-use text editor for Linux. There are arguably better editors (Vim, being the obvious choice);
however, nano is a great one to start with. What switch would you use to make a backup when opening a file with nano?
hackerdu@DESKTOP-G7C81CH:~$ man nano | grep -e "backup" ⌨️
    -B, --backup
    -C directory, --backupdir=directory
        Make and keep not just one backup file, but make and keep a uniquely numbered one every time a file is saved --
        when backups are enabled (-B).  The uniquely numbered files are stored in the specified directory.
        prepended to, or saved under a different name if it already has one; and dont make  backup  files.  Restricted

Q4: Netcat is a basic tool used to manually send and receive network requests. What command would you use to start netcat in listen mode, using port 12345?
hackerdu@DESKTOP-G7C81CH:~$ man netcat ⌨️
NC(1)                                               General Commands Manual                                     NC(1)

NAME
       nc — arbitrary TCP and UDP connections and listens

SYNOPSIS
    nc  [-46bCDdFhklNnrStUuvZz]  [-I  length]  [-i  interval]  [-M  ttl]  [-m  minttl]  [-O  length]  [-P  proxy_username]
        [-p  source_port]  [-q  seconds]  [-s  sourceaddr]  [-T  keyword]  [-V   rtable]   [-W   recvlimit]   [-w   timeout]
        [-X proxy_protocol] [-x proxy_address[:port]] [destination] [port]

DESCRIPTION
    The  nc  (or  netcat) utility is used for just about anything under the sun involving TCP, UDP, or Unix-domainsockets.
    It can open TCP connections, send UDP packets, listen on arbitrary TCP and UDP ports, do port scanning, and  deal with
    both  IPv4  and IPv6.  Unlike telnet(1), nc scripts nicely, and separates error messages onto standard error instead of
    sending them to standard output, as telnet(1) does with some.

    Common uses include:
        •   simple TCP proxies
        •   shell-script based HTTP clients and servers
        •   network daemon testing
        •   a SOCKS or HTTP ProxyCommand for ssh(1)
        •   and much, much more

    The options are as follows:
    -l  Listen for an incoming connection rather than initiating a connection to a remote host.   The  destination and
        port  to  listen  on can be specified either as non-optional arguments, or with options -s and -prespectively.
        Cannot be used together with -x or -z.  Additionally, any timeouts specified with the -w option are ignored
    -p source_port
        Specify the source port nc should use, subject to privilege restrictions and availability.

root@kali:~# nc -l -p 12345 ⌨️
```