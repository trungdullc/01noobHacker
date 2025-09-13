# picoGym Level 367: ReadMyCert
Source: https://play.picoctf.org/practice/challenge/367

## Goal
How about we take you on an adventure on exploring certificate signing requests<br>
Take a look at this CSR file here<br>
https://artifacts.picoctf.net/c/420/readmycert.csr

## What I learned
```
Most csr encrypted in base64
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/420/readmycert.csr ⌨️
--2025-09-08 22:48:06--  https://artifacts.picoctf.net/c/420/readmycert.csr
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 997 [application/octet-stream]
Saving to: 'readmycert.csr'

readmycert.csr                                             100%[======================================================================================================================================>]     997  --.-KB/s    in 0s      

2025-09-08 22:48:06 (287 MB/s) - 'readmycert.csr' saved [997/997]

AsianHacker-picoctf@webshell:/tmp$ file readmycert.csr ⌨️
readmycert.csr: PEM certificate request
AsianHacker-picoctf@webshell:/tmp$ cat readmycert.csr ⌨️
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF9hNzE2
M2JlOH0xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAL6KBBqiFmUHDwT3NtVw+Ozveo9uAZ+c47X5n+MEsWPowsNIz9fG
kpLf9rgu9kR4ZR1H5IEddOGEsTA9qRUc1mwBuZeld5o9ltDU+6YzCKANDnwS61sB
w4FV54LTy33T1+1bc11o++3LM34pFCGWI3lwoj8GWDRJdxvvp5Iwh5kz4ki6Mwp/
HAKyyG9i9KMOXAm/Zw0FkL1UZppHa00cbdCieen7lZgeVpFlIs3uo8tL6fGmpYww
Ard6ZFzL1zCwgZukSHsul20gi9Ba4Uz3R4f6zA/PL0S7haAif96yyi/REREKUZGt
76Gt8zv2xVAqhZYYpFqOmv1ycRmZSyF8GWkCAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAI4mtS0h
2HQseRJfnySGJdsnquMyLSV1EdvAfb2qTosXuQH0vunk5NbnR9yjXKej0I2Uu6DW
f9UehV+QsgW1tmZKpjGXj602nESDBVwiyNw84AXaW74+vH1lVKu9YFf08GI40Fee
jYYjQLz6DatXL0Qsuyjjo/MF1W1z/N7ErLvox7tj+dIOfEs14LYx61JrwwcAw8Ak
1lo4gwusg/+aEpAhDcw62Bjh2iGfwydHV7vh04vWBzPoSz5xyrNG+w8kALKKRUTh
Z9wKzilfeMGpobC7at6ys5cMdrC3ePVxn0XWTQEWfjQwtr+UtOoOWlP8eJEstWQU
qbdZveR4nsgbnkU=
-----END CERTIFICATE REQUEST-----

# Method 1: OpenSSL tool ability to handle various cryptographic operations
AsianHacker-picoctf@webshell:/tmp$ openssl req -in readmycert.csr -text -noout ⌨️
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN = picoCTF{read_mycert_a7163be8} 🔐, name = ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:be:8a:04:1a:a2:16:65:07:0f:04:f7:36:d5:70:
                    f8:ec:ef:7a:8f:6e:01:9f:9c:e3:b5:f9:9f:e3:04:
                    b1:63:e8:c2:c3:48:cf:d7:c6:92:92:df:f6:b8:2e:
                    f6:44:78:65:1d:47:e4:81:1d:74:e1:84:b1:30:3d:
                    a9:15:1c:d6:6c:01:b9:97:a5:77:9a:3d:96:d0:d4:
                    fb:a6:33:08:a0:0d:0e:7c:12:eb:5b:01:c3:81:55:
                    e7:82:d3:cb:7d:d3:d7:ed:5b:73:5d:68:fb:ed:cb:
                    33:7e:29:14:21:96:23:79:70:a2:3f:06:58:34:49:
                    77:1b:ef:a7:92:30:87:99:33:e2:48:ba:33:0a:7f:
                    1c:02:b2:c8:6f:62:f4:a3:0e:5c:09:bf:67:0d:05:
                    90:bd:54:66:9a:47:6b:4d:1c:6d:d0:a2:79:e9:fb:
                    95:98:1e:56:91:65:22:cd:ee:a3:cb:4b:e9:f1:a6:
                    a5:8c:30:02:b7:7a:64:5c:cb:d7:30:b0:81:9b:a4:
                    48:7b:2e:97:6d:20:8b:d0:5a:e1:4c:f7:47:87:fa:
                    cc:0f:cf:2f:44:bb:85:a0:22:7f:de:b2:ca:2f:d1:
                    11:11:0a:51:91:ad:ef:a1:ad:f3:3b:f6:c5:50:2a:
                    85:96:18:a4:5a:8e:9a:fd:72:71:19:99:4b:21:7c:
                    19:69
                Exponent: 65537 (0x10001)
        Attributes:
            Requested Extensions:
                X509v3 Extended Key Usage: 
                    TLS Web Client Authentication
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        8e:26:b5:2d:21:d8:74:2c:79:12:5f:9f:24:86:25:db:27:aa:
        e3:32:2d:25:75:11:db:c0:7d:bd:aa:4e:8b:17:b9:01:f4:be:
        e9:e4:e4:d6:e7:47:dc:a3:5c:a7:a3:d0:8d:94:bb:a0:d6:7f:
        d5:1e:85:5f:90:b2:05:b5:b6:66:4a:a6:31:97:8f:ad:36:9c:
        44:83:05:5c:22:c8:dc:3c:e0:05:da:5b:be:3e:bc:7d:65:54:
        ab:bd:60:57:f4:f0:62:38:d0:57:9e:8d:86:23:40:bc:fa:0d:
        ab:57:2f:44:2c:bb:28:e3:a3:f3:05:d5:6d:73:fc:de:c4:ac:
        bb:e8:c7:bb:63:f9:d2:0e:7c:4b:35:e0:b6:31:eb:52:6b:c3:
        07:00:c3:c0:24:d6:5a:38:83:0b:ac:83:ff:9a:12:90:21:0d:
        cc:3a:d8:18:e1:da:21:9f:c3:27:47:57:bb:e1:d3:8b:d6:07:
        33:e8:4b:3e:71:ca:b3:46:fb:0f:24:00:b2:8a:45:44:e1:67:
        dc:0a:ce:29:5f:78:c1:a9:a1:b0:bb:6a:de:b2:b3:97:0c:76:
        b0:b7:78:f5:71:9f:45:d6:4d:01:16:7e:34:30:b6:bf:94:b4:
        ea:0e:5a:53:fc:78:91:2c:b5:64:14:a9:b7:59:bd:e4:78:9e:
        c8:1b:9e:45
    
Method 2: Decrypt base64
AsianHacker-picoctf@webshell:/tmp$ echo -n "MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF9hNzE2
> M2JlOH0xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
> ADCCAQoCggEBAL6KBBqiFmUHDwT3NtVw+Ozveo9uAZ+c47X5n+MEsWPowsNIz9fG
> kpLf9rgu9kR4ZR1H5IEddOGEsTA9qRUc1mwBuZeld5o9ltDU+6YzCKANDnwS61sB
> w4FV54LTy33T1+1bc11o++3LM34pFCGWI3lwoj8GWDRJdxvvp5Iwh5kz4ki6Mwp/
> HAKyyG9i9KMOXAm/Zw0FkL1UZppHa00cbdCieen7lZgeVpFlIs3uo8tL6fGmpYww
> Ard6ZFzL1zCwgZukSHsul20gi9Ba4Uz3R4f6zA/PL0S7haAif96yyi/REREKUZGt
> 76Gt8zv2xVAqhZYYpFqOmv1ycRmZSyF8GWkCAwEAAaAmMCQGCSqGSIb3DQEJDjEX
> MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAI4mtS0h
> 2HQseRJfnySGJdsnquMyLSV1EdvAfb2qTosXuQH0vunk5NbnR9yjXKej0I2Uu6DW
> f9UehV+QsgW1tmZKpjGXj602nESDBVwiyNw84AXaW74+vH1lVKu9YFf08GI40Fee
> jYYjQLz6DatXL0Qsuyjjo/MF1W1z/N7ErLvox7tj+dIOfEs14LYx61JrwwcAw8Ak
> 1lo4gwusg/+aEpAhDcw62Bjh2iGfwydHV7vh04vWBzPoSz5xyrNG+w8kALKKRUTh
> Z9wKzilfeMGpobC7at6ys5cMdrC3ePVxn0XWTQEWfjQwtr+UtOoOWlP8eJEstWQU
> qbdZveR4nsgbnkU=" | base64 -d ⌨️
000<1&0$U
         picoCTF{read_mycert_a7163be8}10U) 🔐
0       *H                                      ctfPlayer0"0
|[ÁU}[s]h3~)!#yp?X4Iw03H3
TfGkMmТyVe"K񦥌0zd\0H{.m ZLG/D"޲/
Q;P*Zrq100U%0$ *H
             0
+0      *H
W/D,(msĬǻc|K51Rk$Z8Ѝ_fJ16D\"<[>}eT`Wb8W#@
:!'GWӋ3K>qʳF$EDg   !
)_xj޲
     vxqEM~40ZSx,dYx

Method 4: CyberChef
https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=TUlJQ3B6Q0NBWThDQVFBd1BERW1NQ1FHQTFVRUF3d2RjR2xqYjBOVVJudHlaV0ZrWDIxNVkyVnlkRjloTnpFMgpNMkpsT0gweEVqQVFCZ05WQkNrTUNXTjBabEJzWVhsbGNqQ0NBU0l3RFFZSktvWklodmNOQVFFQkJRQURnZ0VQCkFEQ0NBUW9DZ2dFQkFMNktCQnFpRm1VSER3VDNOdFZ3K096dmVvOXVBWitjNDdYNW4rTUVzV1Bvd3NOSXo5ZkcKa3BMZjlyZ3U5a1I0WlIxSDVJRWRkT0dFc1RBOXFSVWMxbXdCdVplbGQ1bzlsdERVKzZZekNLQU5EbndTNjFzQgp3NEZWNTRMVHkzM1QxKzFiYzExbysrM0xNMzRwRkNHV0kzbHdvajhHV0RSSmR4dnZwNUl3aDVrejRraTZNd3AvCkhBS3l5RzlpOUtNT1hBbS9adzBGa0wxVVpwcEhhMDBjYmRDaWVlbjdsWmdlVnBGbElzM3VvOHRMNmZHbXBZd3cKQXJkNlpGekwxekN3Z1p1a1NIc3VsMjBnaTlCYTRVejNSNGY2ekEvUEwwUzdoYUFpZjk2eXlpL1JFUkVLVVpHdAo3Nkd0OHp2MnhWQXFoWllZcEZxT212MXljUm1aU3lGOEdXa0NBd0VBQWFBbU1DUUdDU3FHU0liM0RRRUpEakVYCk1CVXdFd1lEVlIwbEJBd3dDZ1lJS3dZQkJRVUhBd0l3RFFZSktvWklodmNOQVFFTEJRQURnZ0VCQUk0bXRTMGgKMkhRc2VSSmZueVNHSmRzbnF1TXlMU1YxRWR2QWZiMnFUb3NYdVFIMHZ1bms1TmJuUjl5alhLZWowSTJVdTZEVwpmOVVlaFYrUXNnVzF0bVpLcGpHWGo2MDJuRVNEQlZ3aXlOdzg0QVhhVzc0K3ZIMWxWS3U5WUZmMDhHSTQwRmVlCmpZWWpRTHo2RGF0WEwwUXN1eWpqby9NRjFXMXovTjdFckx2b3g3dGorZElPZkVzMTRMWXg2MUpyd3djQXc4QWsKMWxvNGd3dXNnLythRXBBaERjdzYyQmpoMmlHZnd5ZEhWN3ZoMDR2V0J6UG9TejV4eXJORyt3OGtBTEtLUlVUaApaOXdLemlsZmVNR3BvYkM3YXQ2eXM1Y01kckMzZVBWeG4wWFdUUUVXZmpRd3RyK1V0T29PV2xQOGVKRXN0V1FVCnFiZFp2ZVI0bnNnYm5rVT0 ⌨️
```

## Flag
picoCTF{read_mycert_a7163be8}

## Continue
[Continue](./picoGym0261.md)