# OpenVAS

```
Source: https://openvas.org/
Description: Comprehensive vulnerability scanner for identifying network, application, and device security issues
It's part of the Greenbone Vulnerability Management (GVM) framework

# Check GVM/OpenVAS Version
gvm-check-setup

# Start GVM/OpenVAS Services
sudo gvm-start
    Starts necessary services like:
        gvmd (Greenbone Vulnerability Manager)
        ospd-openvas (scanner)
        gsad (Greenbone Security Assistant, web UI)

# Stop GVM/OpenVAS Services
sudo gvm-stop

# Set Up Admin User
sudo gvmd --create-user=admin
sudo gvmd --user=admin --new-password=yourpassword

# Update Vulnerability Feeds
sudo greenbone-feed-sync --type SCAP                sudo gvm-feed-update
sudo greenbone-feed-sync --type CERT
sudo greenbone-feed-sync --type GVMD_DATA

# List Existing Targets
gvm-cli --gmp-username admin --gmp-password yourpassword socket --xml '<get_targets/>'

# Create a New Target (via GMP/XML)
gvm-cli --gmp-username admin --gmp-password yourpassword socket --xml '<create_target><name>TestTarget</name><hosts>192.168.1.100</hosts></create_target>'

# Start a Scan Task
gvm-cli --gmp-username admin --gmp-password yourpassword socket --xml '<start_task task_id="TASK_ID"/>'

# Access the Web UI
https://localhost:9392

# Check Logs and Status
sudo journalctl -xe | grep gvmd
sudo tail -f /var/log/gvm/gvmd.log
```

# Example Workflow
```
sudo gvm-start
Update feeds: sudo gvm-feed-update
Create targets/tasks (web UI or gvm-cli)
Launch scan
View results on web UI (https://localhost:9392)
```

## Back to README.md
[BACK](../README.md)