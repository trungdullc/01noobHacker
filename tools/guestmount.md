# guestmount

```
Description: Mount virtual machine disk images (QCOW2, VMDK, or VDI files) on your local filesystem
It's part of libguestfs suite, accessing and modifying VM disk images without launching VM

Syntax: guestmount -a <disk.img> -m <mountpoint> <local_dir>
    -a: specifies the image file
    -m: specifies the partition to mount (e.g., /dev/sda1)
    <local_dir>: where to mount the contents on your system

# Install
# Debian/Ubuntu                                 # Fedora/RHEL/CentOS
sudo apt install libguestfs-tools               sudo dnf install libguestfs-tools      

# Mount VHD from Remote SMB Share
guestmount --add /mnt/backups/WindowsImageBackup/<file>.vhd --inspector --ro /mnt/vhd

# List Partitions in a Disk Image
virt-filesystems -a disk.qcow2 --long --parts --blkdevs --filesystems

# Mount a VM Disk Partition
guestmount -a disk.qcow2 -m /dev/sda1 --ro /mnt/vm
    Use --rw instead of --ro if you want write access (risky)
    
# Mount a Logical Volume or LVM
guestmount -a disk.qcow2 -m /dev/centos/root --ro /mnt/vm

# Mount a Logical Volume or LVM w/ full LVM detection
guestmount -a disk.qcow2 -m /dev/VolGroup00/LogVol00 --ro /mnt/vm

# Unmount the Image
guestunmount /mnt/vm

# Access Files After Mount
ls /mnt/vm/etc
cat /mnt/vm/etc/passwd
cp /mnt/vm/var/log/messages .
```

## Back to README.md
[BACK](../README.md)