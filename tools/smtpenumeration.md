# SMTP Enumeration

```
SMTP operates as an application-layer protocol that facilitates email transmission between mail servers
    Port 25: Server-to-server email transfer (not for client submission)
    Port 465: SMTP with implicit SSL (less common)
    Port 587: Modern standard for sending email from clients (uses STARTTLS for encryption)

POP3 (Post Office Protocol version 3)
    Port 110: POP3 (unencrypted or with STARTTLS)
    Port 995: POP3 over SSL/TLS (secure)

IMAP (Internet Message Access Protocol)
    Port 143: IMAP (unencrypted or with STARTTLS)
    Port 993: IMAP over SSL/TLS (secure)

Mail Transfer Agent (MTA): Transfers email between servers
Mail Delivery Agent (MDA): Delivers email to recipient mailboxes
Mail User Agent (MUA): End-user email client software
```

# Common SMTP Vulnerabilities
```
Open Relays: Misconfigured SMTP servers that allow unauthorized email transmission can be exploited for spam distribution and phishing campaigns

Information Disclosure: Verbose banners often reveal server software versions, making vulnerability identification easier for attackers

Authentication Weaknesses: Servers lacking proper authentication mechanisms or using weak credentials become easy targets for unauthorized access

User Enumeration: Improperly configured servers may allow attackers to verify email addresses using VRFY and EXPN commands
```

# Banner Grabbing Techniques
```
Banner grabbing reveals crucial information about target SMTP servers, including software versions and configurations

telnet 8.8.8.8 25               nc 8.8.8.8 25               nmap -sV -p 25 8.8.8.8
```

# User Enumeration Methods
```
# VRFY Command: VRFY command verifies if specific users exist on the server
VRFY admin@example.com

# EXPN Command: EXPN command reveals mailing list members
EXPN staff@example.com
```

# Automated Enumeration Tools
```
# Metasploit SMTP Enumeration                       # Nmap SMTP Enumeration Script
use auxiliary/scanner/smtp/smtp_enum                nmap --script smtp-enum-users -p 25 target_ip
set RHOSTS target_ip
set USER_FILE /path/to/usernames.txt                # SMTP User Enum Tool
run                                                 

# SMTP User Enum Tool
smtp-user-enum -M VRFY -U /path/to/userlist.txt -t target_ip
```

# Advanced Enumeration Techniques
```
Timing-Based Enumeration: Attackers measure server response times to differentiate between valid and invalid users:
    Valid users: Slower response (150ms)
    Invalid users: Faster response (100ms)

Response Code Analysis: Different SMTP response codes can indicate user validity:
    250 OK: Valid user
    550 No such user: Invalid user
```

# SMTP Relay Attack Testing
```
# Detecting Open Relays
nmap -p 25 --script smtp-open-relay target_ip

Risks of Open Relays:
    Spam propagation
    IP blacklisting
    Phishing and malware distribution
```

# Brute Force Attack Testing
```
# hydra
hydra -l user -P /path/to/passwords.txt smtp://target_ip -V

# medusa
medusa -h target_ip -u user -P /path/to/passwords.txt -M smtp

# Metasploit Brute Force Module
use auxiliary/scanner/smtp/smtp_login
set RHOSTS target_ip
set USER_FILE /path/to/usernames.txt
set PASS_FILE /path/to/passwords.txt
run
```

# Securing SMTP Servers
```
Essential Security Measures
    Disable Open Relay: Require authentication for email transmission
    Remove Verbose Banners: Limit information disclosure
    Implement Strong Authentication: Use SASL mechanisms
    Enable TLS Encryption: Protect data in transit
    Disable VRFY/EXPN: Prevent user enumeration

# Advanced Security Configurations: SPF Record Implementation
example.com. IN TXT "v=spf1 mx ip4:192.168.1.100 -all"

# Advanced Security Configurations: DKIM Configuration
DKIM-Signature: v=1; a=rsa-sha256; d=example.com; s=key;

# Advanced Security Configurations: DMARC Policy
_dmarc.example.com. IN TXT "v=DMARC1; p=reject; rua=mailto:dmarc-reports@example.com"
```

# Practical Testing Lab Setup using Metasploitable 2 VM
```
# Banner Grabbing
Terminal window
telnet 192.168.1.61 25
netcat 192.168.1.61 25
nmap -sV -p 25 192.168.1.61

# User Enumeration
# Telnet method
telnet 192.168.1.61 25
VRFY msfadmin

# Metasploit method
msfconsole
search smtp user
use auxiliary/scanner/smtp/smtp_enum
set RHOST 192.168.1.61
exploit
```

# Mitigation Strategies
```
Immediate Actions:
    Disable unnecessary SMTP commands
    Implement proper authentication
    Configure TLS encryption
    Set up monitoring and logging

Long-term Security:
    Regular vulnerability assessments
    Security patch management
    Employee security training
    Incident response planning
```

# Best Practices for Penetration Testers
```
Always obtain proper authorization before testing
Document all findings thoroughly
Provide clear remediation steps
Test in isolated environments when possible
Follow responsible disclosure practices
```

## Back to README.md
[BACK](/README.md)