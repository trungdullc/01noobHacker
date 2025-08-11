# openssl

```
Description: Toolkit for the TLS/SSL protocols and a general-purpose cryptography library
It’s commonly used for:
    Generating private keys and public key certificates
    Creating Certificate Signing Requests (CSRs)
    Encrypting and decrypting files
    Testing SSL/TLS on servers (e.g., websites)
    Converting certificate formats (PEM, DER, PKCS#12)

openssl version

# Generate a Private Key
openssl genpkey -algorithm RSA -out private.key -aes256
openssl genrsa -out private.key 2048                            # legacy
    -aes256 encrypts private key with a passphrase

# Generate a Certificate Signing Request (CSR)
openssl req -new -key private.key -out request.csr

# Self-Sign a Certificate
openssl req -x509 -days 365 -key private.key -in request.csr -out cert.pem

# View Certificate Details
openssl x509 -in cert.pem -noout -text

# Convert Between Certificate Formats PEM to DER
openssl x509 -in cert.pem -outform der -out cert.der

# Convert Between Certificate Formats DER to PEM
openssl x509 -in cert.der -inform der -out cert.pem

# Convert Between Certificate Formats  PFX (PKCS#12) to PEM
openssl pkcs12 -in cert.pfx -out cert.pem -nodes

# Encrypt a file using AES
openssl enc -aes-256-cbc -salt -in file.txt -out file.enc

# Decrypt
openssl enc -d -aes-256-cbc -in file.enc -out file.txt

# Test SSL/TLS on a Remote Server
openssl s_client -connect google.com:443

# Check a Private Key
openssl rsa -check -in private.key

# Check CSR Details
openssl req -text -noout -verify -in request.csr
```

## Back to README.md
[BACK](../README.md)