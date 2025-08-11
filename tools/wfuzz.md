# wfuzz

```
Source: https://github.com/xmendez/wfuzz
Description: Web App Enumeration

pip install wfuzz

# Run Wfuzz from a docker image
docker run -v $(pwd)/wordlist:/wordlist/ -it ghcr.io/xmendez/wfuzz wfuzz

# Enumerate directories with a wordlist
wfuzz -u http://10.10.10.X/FUZZ/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Enumerate login POST data from a password list
wfuzz -z file,wordlist/others/common_pass.txt -d "uname=FUZZ&pass=FUZZ"  --hc 302 
```

## Back to README.md
[BACK](../README.md)