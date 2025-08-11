# gobuster

```
Source: https://github.com/OJ/gobuster
Description: CLI brute-force URLs, directories, DNS subdomains, or S3 buckets on a target web server or domain

Flag	                        Purpose
--insecuressl	                Allows gobuster to scan HTTPS sites with untrusted SSL certs
-x	                            File extensions to check
-t	                            Number of threads (20 is default for speed)

HTTP
    # Basic
    gobuster dir -u http://192.168.0.X -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

    # Fast Scan (Small List)
    gobuster dir -e -u http://192.168.0.1 -w /usr/share/wordlists/dirb/big.txt -t 20

    # Fast Scan (Big List)
    gobuster dir -e -u http://192.168.0.1 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 20

    # Slow Scan (Check File Extensions)
    gobuster dir -e -u http://192.168.0.1 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html,cgi,sh,bak,aspx -t 20

HTTPS (set --insecuressl flag)
    gobuster dir -u https://192.168.0.1 -w /usr/share/wordlists/dirb/common.txt --insecuressl -t 20

SMBCLIENT
    Fix NT_STATUS_CONNECTION_DISCONNECTED errors in new Kali installations:
        add client min protocol = NT1 to your \etc\samba\smb.conf file
    # List Shares (As Guest)
    smbclient -U guest -L 192.168.0.1

    # Connect to A Share (As User Hacker)
    smbclient \\\\192.168.0.1\\Users -U c.smith

    # Download All Files From A Directory Recursively
    smbclient \\\\192.168.0.1\\Data -U Hacker -c 'prompt OFF;recurse ON;cd '\Users\Hacker\';lcd '/tmp/Hacker';mget *'

Alternate File Streams
    # List Streams
    smbclient \\\\192.168.0.1\\Data -U Hacker -c 'allinfo "\Users\Hacker\file.txt"'

    # Download Stream By Name (:SECRET)
    smbclient \\\\192.168.0.1\\Data -U Hacker
    get "\Users\Hacker\file.txt:SECRET:$DATA"
```

## Back to README.md
[BACK](../README.md)