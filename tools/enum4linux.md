# enum4linux
```
Source: https://github.com/CiscoCXSecurity/enum4linux
Description:  Enumeration script for Windows systems that queries SMB (Samba) services for detailed information — like users, shares, policies, domains

sudo apt install enum4linux                             git clone https://github.com/CiscoCXSecurity/enum4linux
                                                        cd enum4linux
                                                        chmod +x enum4linux.pl

Option	                    Description
-U	                        Enumerate users
-S	                        Enumerate shares
-P	                        Enumerate password policy
-G	                        Get group memberships
-a	                        Run all options (recommended for CTFs) ⭐

# Runs all default scans (users, shares, passwords, policies)
enum4linux 8.8.8.8
```

## Back to README.md
[BACK](/README.md)