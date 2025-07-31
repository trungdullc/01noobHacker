# smbclient

```
Description: CLI tool access Windows shares (SMB/CIFS) from Linux or Unix systems

# Install on Debian/Ubuntu                      # Install on Red Hat/Fedora
sudo apt install smbclient                      sudo dnf install samba-client

# List shares on a remote SMB server
smbclient -L //192.168.1.100 -U username
    -L = list shares
    -N: No password (for guest access)
    -U = specify username

# Connect to a specific shared folder and get an interactive shell
smbclient //192.168.1.100/sharedfolder -U username
smb: \> ls
smb: \> get file.txt
smb: \> put exploit.sh

# Mount a share as a local folder (alternative method)
sudo mount -t cifs //192.168.1.100/share /mnt/smb -o username=youruser
```

# Server
```
# Install Samba (SMB Server)
sudo apt update
sudo apt install samba

# Configure SMB Share
sudo vi /etc/samba/smb.conf
    [shared]
        path = /srv/samba/shared
        browseable = yes
        read only = no
        guest ok = yes

# Create shared directory
sudo mkdir -p /srv/samba/shared
sudo chmod 777 /srv/samba/shared

# Restart Samba
sudo systemctl restart smbd
```

# Optional: Create a Samba User (if not using guest)
```
sudo useradd smbuser
sudo smbpasswd -a smbuser

Update smb.conf
    [secure]
        path = /srv/samba/secure
        valid users = smbuser
        read only = no

sudo systemctl restart smbd
```

## Back to README.md
[BACK](/README.md)