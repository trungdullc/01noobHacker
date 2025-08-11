# Useful shell commands

```
Shell elevation (from non-tty shell; just go down the list)
https://netsec.ws/?p=337

Spawn bash from shell
python3 -c "import pty;pty.spawn('/bin/bash')"

Bash
Show interesting files in home directory (potential flags):
find /home -printf -type f "%f\t%p\t%u\t%g\t%m\n" | column -t

Check versions of running software (searching for “pam” in this case):
dpkg -l | grep -i pam
sudo -l
history

Get Meterpreter shell from backgrounded shell:
post/multi/manage/shell_to_meterpreter

Meterpreter
    getuid
    sysinfo
    hashdump (if privileged)
    shell 
    load (tab to autocomplete and get list: kiwi, incognito, etc.)
    getsystem (priv esc) 

Windows network stuff
arp -a
netstat -an
```

## Back to README.md
[BACK](../README.md)