# showmount

```
Description: NFS (Network File System) is a protocol that allows a computer to share directories and files with others over a network, as if they were local disks

In Capture The Flag (CTF) challenges, NFS is often misconfigured, allowing attackers to:
    Mount NFS shares without authentication
    Access sensitive files
    Create SUID binaries or SSH keys
    Escalate privileges

# Show mountable drives
showmount -e 192.168.0.1

# Mount Drive
mkdir mpt
mount -t nfs -o soft 192.168.0.1:/backup mpt/
```

## Back to README.md
[BACK](/README.md)