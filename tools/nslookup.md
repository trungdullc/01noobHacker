# nslookup

```
Description: (Windows) (Name Server Lookup) CLI tool to query DNS records for domains and IP addresses

It helps you:
    Look up IP addresses for domain names (A records)
    Get mail servers (MX records)
    Find name servers (NS records)
    Test DNS resolution issues

Note: nslookup is simple, dig and dnsrecon offer more advanced DNS analysis

nslookup google.com

# Use a specific DNS server
nslookup example.com 8.8.8.8

# Get specific DNS records (interactive mode)
nslookup
> set type=MX
> example.com

# Find authoritative name servers
nslookup -type=ns example.com

# Email-related: nslookup for SPF
nslookup -type=txt domain.com

# Email-related: nslookup for DMARC
nslookup -type=txt _dmarc.domain.com
```

## Back to README.md
[BACK](../README.md)