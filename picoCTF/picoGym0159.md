# picoGym Level 159: Dachshund Attacks
Source: https://play.picoctf.org/practice/challenge/159

## Goal
What if d is too small? Connect with<br>
nc mercury.picoctf.net 58978

## What I learned
```
Dachshunds (small German dog)
RSA Attack
Hinting: Wiener's attack is a cryptographic attack on RSA encryption that exploits small private keys, allowing an attacker to recover the private key using continued fractions
https://en.wikipedia.org/wiki/Wiener%27s_attack

RsaCtfTool (Didn't Work)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc mercury.picoctf.net 58978 ⌨️
Welcome to my RSA challenge!
e: 41913282002523483329093687969351788033266647845311075926138287046557388458914924455174725300162174250383534917266884744188980883890066661102828543333126490117093487877176886758808794418202985507851027697683897960449646943987512648457030787039025626321460826862853934899532317399640222254540933876864726274489
n: 93883008965586135555662559364865131148309336865336746100034713448788785748812468140332802018763335785711861902818075029346796064727601739623155797625114999328869855195267754060057019368294955297117938743778900414241306337211136525532145237170650443430634424765445251261763166972906885680400599379906660606619
c: 55868306557023949554261967989201891298679700272506892016617386686426995120825855584791870356348453282176130001501114254122751788709986452392283814095938474171328930358268191775121446114952019645724613789450360792166899770820178427884692462659569011999828959970182635577949456690725309606035112305278821638877

ChatGPT: what cipher and how to solve
You’re looking at an RSA challenge. The three values shown are the RSA public exponent e, the modulus n, and the ciphertext c. To recover the plaintext (the flag) you must decrypt the RSA ciphertext — which in practice means finding the private key (or otherwise factoring n)

Google: rsa wiener attack github
https://github.com/pablocelayes/rsa-wiener-attack

Method 1:
https://www.dcode.fr/rsa-cipher ⌨️
Results:
Plaintext as Integer Value: 198614235373674103788888306985643587194108045477674049828655868730909536893 👀
Plaintext as Hexadecimal Format: 70 69 63 6F 43 54 46 7B 70 72 6F 76 69 6E 67 5F 77 69 65 6E 65 72 5F 36 39 30 37 33 36 32 7D 👀❤️❤️❤️

AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
# the decrypted integer you got
m = 198614235373674103788888306985643587194108045477674049828655868730909536893

# convert to hex string (could have skip this step since site did it)
hex_str = hex(m)[2:]   # strip "0x"
print("Hex:", hex_str)

# convert hex string to bytes
msg_bytes = bytes.fromhex(hex_str)
print("Bytes:", msg_bytes)

# decode to ascii/utf-8
print("Flag:", msg_bytes.decode())
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️ 
Hex: 7069636f4354467b70726f76696e675f7769656e65725f363930373336327d
Bytes: b'picoCTF{proving_wiener_6907362}'
Flag: picoCTF{proving_wiener_6907362} 🔐

# Note: One Liner
AsianHacker-picoctf@webshell:~$ python -c "m=198614235373674103788888306985643587194108045477674049828655868730909536893;print(bytes.fromhex(hex(m)[2:]).decode())" ⌨️
picoCTF{proving_wiener_6907362} 🔐

# Get hex value from python then put in cyberchef (useless, gotten hex from dcode site)
https://cyberchef.io/#recipe=From_Hex('Auto')&input=NzAgNjkgNjMgNkYgNDMgNTQgNDYgN0IgNzAgNzIgNkYgNzYgNjkgNkUgNjcgNUYgNzcgNjkgNjUgNkUgNjUgNzIgNUYgMzYgMzkgMzAgMzcgMzMgMzYgMzIgN0Q
picoCTF{proving_wiener_6907362} 🔐

# Method 2: find d w/ owiener 1.0.9
https://pypi.org/project/owiener/
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
Traceback (most recent call last):
  File "/tmp/pyhtonScript.py", line 1, in <module>
    import owiener
ModuleNotFoundError: No module named 'owiener'
AsianHacker-picoctf@webshell:/tmp$ pip3 install owiener ⌨️❤️❤️❤️❤️❤️
Defaulting to user installation because normal site-packages is not writeable
Collecting owiener
  Downloading owiener-1.0.9-py3-none-any.whl.metadata (4.6 kB)
Downloading owiener-1.0.9-py3-none-any.whl (6.7 kB)
WARNING: Error parsing dependencies of send2trash: Expected matching RIGHT_PARENTHESIS for LEFT_PARENTHESIS, after version specifier
    sys-platform (=="darwin") ; extra == 'objc'
                 ~^
Installing collected packages: owiener
Successfully installed owiener-1.0.9

[notice] A new release of pip is available: 25.0.1 -> 25.2
[notice] To update, run: python3 -m pip install --upgrade pip
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
import owiener

def main() -> None:
    e = 41913282002523483329093687969351788033266647845311075926138287046557388458914924455174725300162174250383534917266884744188980883890066661102828543333126490117093487877176886758808794418202985507851027697683897960449646943987512648457030787039025626321460826862853934899532317399640222254540933876864726274489
    n = 93883008965586135555662559364865131148309336865336746100034713448788785748812468140332802018763335785711861902818075029346796064727601739623155797625114999328869855195267754060057019368294955297117938743778900414241306337211136525532145237170650443430634424765445251261763166972906885680400599379906660606619
    c = 55868306557023949554261967989201891298679700272506892016617386686426995120825855584791870356348453282176130001501114254122751788709986452392283814095938474171328930358268191775121446114952019645724613789450360792166899770820178427884692462659569011999828959970182635577949456690725309606035112305278821638877
    d = owiener.attack(e, n)

    if d is None:
        print("Failed")

    else :
        print("Hacked d = {}".format(d))

    decrypted_msg = pow(c, d, n)

    print("Decrypted message: ", decrypted_msg)

    # convert to hex string (remove "0x" prefix)
    hex_str = hex(decrypted_msg)[2:]

    print("Hex:", hex_str)

    # Convert hex string → bytes → ASCII
    ascii_text = bytes.fromhex(hex_str).decode()

    print(ascii_text)

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:/tmp$ python3 pythonScript.py 
Hacked d = 5662560980762399288156855382816307027558981075717534854290056746276461204849
Decrypted message:  198614235373674103788888306985643587194108045477674049828655868730909536893
Hex: 7069636f4354467b70726f76696e675f7769656e65725f363930373336327d
picoCTF{proving_wiener_6907362} 🔐

# Method 3: Modify another programmers work
https://github.com/pablocelayes/rsa-wiener-attack/tree/master
Youtube Solution: https://www.youtube.com/watch?v=8zvtBabPc5s (Watch when got time)
```

## Flag
picoCTF{proving_wiener_6907362}

## Continue
[Continue](./picoGym0412.md)