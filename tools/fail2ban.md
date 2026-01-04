# fail2ban (TODO)
```
Source: https://github.com/fail2ban/fail2ban
Description: Fail2Ban is an intrusion prevention software framework. Written in the Python programming language, it is designed to prevent brute-force attacks. It is able to run on POSIX systems that have an interface to a packet-control system or firewall installed locally, such as iptables or TCP Wrapper.

What Fail2Ban does
    Watches log files
    Detects repeated failures
    Adds firewall rules (iptables/nftables)
    Temporarily or permanently bans IPs

fail2ban-client -h
fail2ban-client version

# Need enable fail2ban as an automatic service
cd /etc/init.d
vi init.d
    cp files/debian-initd /etc/init.d/fail2ban
    update-rc.d fail2ban defaults
    service fail2ban start
```

## Back to README.md
[BACK](../README.md)
