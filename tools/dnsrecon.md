# dnsrecon

```
Description: DNS enumeration tool 

It helps you find:
    Subdomains
    Zone transfers
    DNS records (A, MX, NS, TXT)
    Cache snooping
    Brute-force subdomains
    Reverse lookups

Command             Description
-d <domain>         Target domain (required)
-t <type>	        Type of enumeration (see below)
-a	                Perform all basic record enumerations + bruteforce
-n <nameserver>	    Use a specific DNS server
-b <file>	        Use a custom wordlist for bruteforcing
-r <start-end>	    Reverse lookup a range of IPs
-x <xmlfile>	    Output results to XML

-t Type	            Action
std	                Standard record lookup (A, NS, MX, etc.)
brt	                Bruteforce subdomains
srv	                Find SRV records
axfr	            Test for zone transfer
goo	                Perform Google scraping (deprecated/limited)
rdfind	            Reverse lookup from a range of IPs
tld	                Check TLDs for potential subdomains

# Installation
sudo apt install dnsrecon        # Debian/Ubuntu
pip install dnsrecon             # (if using Python version)
```

# Commands
```
dnsrecon -h

# Basic
dnsrecon -d example.com

# Standard DNS record lookup
dnsrecon -d example.com -t std

# Zone transfer test
dnsrecon -d example.com -t axfr

# Subdomain bruteforce
dnsrecon -d example.com -t brt -D /usr/share/wordlists/dns/namelist.txt

# All-in-one scan
dnsrecon -d example.com -a
```

## Back to README.md
[BACK](../README.md)