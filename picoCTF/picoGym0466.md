# picoGym Level 466: Tap into Hash
Source: https://play.picoctf.org/practice/challenge/466

## Goal
Can you make sense of this source code file and write a function that will decode the given encrypted file content?<br>
Find the encrypted file here.<br>
https://challenge-files.picoctf.net/c_verbal_sleep/97b2fa78864cfef5beafa9815bc7b4941f2592d12e39287f7212359ce10f086c/enc_flag<br>
It might be good to analyze source file to get the flag.<br>
https://challenge-files.picoctf.net/c_verbal_sleep/97b2fa78864cfef5beafa9815bc7b4941f2592d12e39287f7212359ce10f086c/block_chain.py

## What I learned
```
Reverse Engineering

Blockchain is a type of data structure that’s most often used in cryptocurrencies (Bitcoin, Ethereum)
A blockchain is literally a chain of "blocks." Each block contains:
    A list of transactions or data
    A timestamp
    A reference (hash) to the previous block
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_verbal_sleep/ 97b2fa78864cfef5beafa9815bc7b4941f2592d12e39287f7212359ce10f086c/enc_flag https://challenge-files.picoctf.net/c_verbal_sleep/ 97b2fa78864cfef5beafa9815bc7b4941f2592d12e39287f7212359ce10f086c/block_chain.py ⌨️
--2025-09-30 23:11:53--  https://challenge-files.picoctf.net/c_verbal_sleep/97b2fa78864cfef5beafa9815bc7b4941f2592d12e39287f7212359ce10f086c/enc_flag
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.40, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1368 (1.3K) [application/octet-stream]
Saving to: 'enc_flag'

enc_flag                                                   100%[======================================================================================================================================>]   1.34K  --.-KB/s    in 0s      

2025-09-30 23:11:53 (1.06 GB/s) - 'enc_flag' saved [1368/1368]

--2025-09-30 23:11:53--  https://challenge-files.picoctf.net/c_verbal_sleep/97b2fa78864cfef5beafa9815bc7b4941f2592d12e39287f7212359ce10f086c/block_chain.py
Reusing existing connection to challenge-files.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 3012 (2.9K) [application/octet-stream]
Saving to: 'block_chain.py'

block_chain.py                                             100%[======================================================================================================================================>]   2.94K  --.-KB/s    in 0s      

2025-09-30 23:11:53 (1.92 GB/s) - 'block_chain.py' saved [3012/3012]

FINISHED --2025-09-30 23:11:53--
Total wall clock time: 0.3s
Downloaded: 2 files, 4.3K in 0s (1.53 GB/s)

AsianHacker-picoctf@webshell:~$ cat block_chain.py ⌨️
import time
import base64
import hashlib
import sys
import secrets


class Block:
    def __init__(self, index, previous_hash, timestamp, encoded_transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.encoded_transactions = encoded_transactions
        self.nonce = nonce

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.encoded_transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()


def proof_of_work(previous_block, encoded_transactions):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0

    block = Block(index, previous_block.calculate_hash(),
                  timestamp, encoded_transactions, nonce)

    while not is_valid_proof(block):
        nonce += 1
        block.nonce = nonce

    return block


def is_valid_proof(block):
    guess_hash = block.calculate_hash()
    return guess_hash[:2] == "00"


def decode_transactions(encoded_transactions):
    return base64.b64decode(encoded_transactions).decode('utf-8')


def get_all_blocks(blockchain):
    return blockchain


def blockchain_to_string(blockchain):
    block_strings = [f"{block.calculate_hash()}" for block in blockchain]
    return '-'.join(block_strings)


def encrypt(plaintext, inner_txt, key):
    midpoint = len(plaintext) // 2

    first_part = plaintext[:midpoint]
    second_part = plaintext[midpoint:]
    modified_plaintext = first_part + inner_txt + second_part
    block_size = 16
    plaintext = pad(modified_plaintext, block_size)
    key_hash = hashlib.sha256(key).digest()

    ciphertext = b''

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        cipher_block = xor_bytes(block, key_hash)
        ciphertext += cipher_block

    return ciphertext


def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data.encode() + padding


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def generate_random_string(length):
    return secrets.token_hex(length // 2)


random_string = generate_random_string(64)


def main(token):
    key = bytes.fromhex(random_string)

    print("Key:", key)

    genesis_block = Block(0, "0", int(time.time()), "EncodedGenesisBlock", 0)
    blockchain = [genesis_block]

    for i in range(1, 5):
        encoded_transactions = base64.b64encode(
            f"Transaction_{i}".encode()).decode('utf-8')
        new_block = proof_of_work(blockchain[-1], encoded_transactions)
        blockchain.append(new_block)

    all_blocks = get_all_blocks(blockchain)

    blockchain_string = blockchain_to_string(all_blocks)
    encrypted_blockchain = encrypt(blockchain_string, token, key)

    print("Encrypted Blockchain:", encrypted_blockchain)

if __name__ == "__main__":
    text = sys.argv[1]
    main(text)

AsianHacker-picoctf@webshell:~$ python3 block_chain.py enc_flag ⌨️
Key: b'!\xb7\xa1`\xfb\xa0\x93\xe5\xfdR\xab0\x1c\xe3\x03SV\xe1\xb5\r\x00Q\xdb\xfd\x19.z%\x97\xcb-\x1a'
Encrypted Blockchain: b'\x1d\xf0\xcf<$%\x07\x9d\x14NW\x17\xbad\xb9\xcf\x18\xf3\xcbm.z\x06\x9bHO\r\x12\xea8\xbf\xcf\x1f\xa1\x9c;|yV\xcfIE\t\x16\xbai\xeb\xccI\xa0\x9f:)$\x05\x9a\x1dO\x0cE\xb9:\xb8\x9fQ\xa6\x9d=|.W\xc8H\x15_\x15\xece\xbd\x9e\x1f\xa4\xccj)zT\xcaHB]C\xeee\xb9\xc2N\xa7\x98=\x7f%W\xcf\x1fC\r\x13\xbcd\xe8\xca\x1d\xae\x9ch,*\x05\xcf\x1bEYC\xe9n\xba\xccD\xbb\x9do/)Q\xcb\x19E\x0bE\xbc>\xbb\x98O\xae\x9el*~V\xcfN\x11\nF\xebo\xec\x99\x19\xa3\xc81~CS\xc2L\x10W\x15\xb9n\xbd\xcb\x1e\xf3\x9f<~/\x00\x9b\x15O_\x16\xbcd\xe8\x9d\x19\xae\xcf<-}\x07\x9e\x1c\x15B\x10\xef8\xb8\xc8J\xa2\x9d<,-\x06\xca\x1b\x13YC\xea>\xef\xc2O\xa7\x98</(W\x9b\x1bB]\x11\xe7>\xb8\xc2\x19\xf5\x94o$)Q\x9f\x1cG\\\x16\xe88\xb9\x9fL\xf2\x989$~\x01\x9b\x19B^\r\xefl\xb4\xcaL\xa0\x9dh\x7f/S\xccHG\x0c\x19\xbcj\xb4\xca\x1f\xa7\x94h,/\x07\xcfK\x15_D\xbe=\xba\xc2D\xa7\xc89y}\x05\xc8N\x16\x0b\x15\xbbd\xbe\x9f\x1e\xa1\x95o,y\x0c\x9c\x1dA\\B\xdbX\x89\xff'

Method 1:
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
import time
import base64
import hashlib
import sys
import secrets

import binascii
import codecs


class Block:
    def __init__(self, index, previous_hash, timestamp, encoded_transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.encoded_transactions = encoded_transactions
        self.nonce = nonce

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.encoded_transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()


def proof_of_work(previous_block, encoded_transactions):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0

    block = Block(index, previous_block.calculate_hash(),
                  timestamp, encoded_transactions, nonce)

    while not is_valid_proof(block):
        nonce += 1
        block.nonce = nonce

    return block


def is_valid_proof(block):
    guess_hash = block.calculate_hash()
    return guess_hash[:2] == "00"


def decode_transactions(encoded_transactions):
    return base64.b64decode(encoded_transactions).decode('utf-8')


def get_all_blocks(blockchain):
    return blockchain


def blockchain_to_string(blockchain):
    block_strings = [f"{block.calculate_hash()}" for block in blockchain]
    return '-'.join(block_strings)


# blockchain_string, token, key
def encrypt(plaintext, inner_txt, key):
    midpoint = len(plaintext) // 2

    first_part = plaintext[:midpoint]
    second_part = plaintext[midpoint:]
    modified_plaintext = first_part + inner_txt + second_part
    print('DEBUG:encrypt: len(first_part)=' + str(len(first_part)) + ', len(inner_txt)=' + str(len(inner_txt)) + ', len(second_part)=' + str(len(second_part)))
    block_size = 16
    print('DEBUG:encrypt: plaintext(before pad)=' + str(plaintext))
    plaintext = pad(modified_plaintext, block_size)
    print('DEBUG:encrypt: plaintext(after pad)=' + str(plaintext))    
    key_hash = hashlib.sha256(key).digest()
    print('DEBUG:encrypt: key=' + str(key) + ', key_hash=' + str(key_hash))

    ciphertext = b''

    for i in range(0, len(plaintext), block_size):
        print('DEBUG:encrypt: i=' + str(i))
        block = plaintext[i:i + block_size]
        cipher_block = xor_bytes(block, key_hash)
        # print(str(len(cipher_block)))
        ciphertext += cipher_block

    return ciphertext

def decrypt(ciphertext, key):
    block_size = 16
    inner_text = b''
    # calculate key_hash
    key_hash = hashlib.sha256(key).digest()    
    # loop over cipher blocks (block_size)
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        plaintext_block = xor_bytes(block, key_hash)
        inner_text += plaintext_block
    # remove trailing padding
    num_pad = ord(inner_text[-1:])
    print('DEBUG:decrypt: num_pad=' +  str(num_pad))
    inner_text = inner_text[:-num_pad]
    # remove the blockchain_string pre and post ambles
    inner_text = inner_text[162:]
    inner_text = inner_text[:-162]
    return inner_text


def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data.encode() + padding

            # block, key_hash
def xor_bytes(a, b):
    print('DEBUG: xor_bytes: len(a)=' + str(len(a)) + ', len(b)=' + str(len(b)))
    print('DEBUG: xor_bytes: a=' + str(a) + ', b=' + str(b))
    xor_ab = bytes(x ^ y for x, y in zip(a, b))
    print('DEBUG: xor_bytes: xor_ab=' + str(xor_ab))
    return xor_ab


def generate_random_string(length):
    return secrets.token_hex(length // 2)


random_string = generate_random_string(64)


def main(token):
    key = bytes.fromhex(random_string)

    print("Key:", key)

    genesis_block = Block(0, "0", int(time.time()), "EncodedGenesisBlock", 0)
    blockchain = [genesis_block]

    for i in range(1, 5):
        encoded_transactions = base64.b64encode(
            f"Transaction_{i}".encode()).decode('utf-8')
        new_block = proof_of_work(blockchain[-1], encoded_transactions)
        blockchain.append(new_block)

    all_blocks = get_all_blocks(blockchain)

    blockchain_string = blockchain_to_string(all_blocks)
    encrypted_blockchain = encrypt(blockchain_string, token, key)

    print("Encrypted Blockchain:", encrypted_blockchain)

    # decrypted_token = decrypt(encrypted_blockchain, key)
    # print("Decrypted Token:", decrypted_token)

def main2(enc_file):
    # open enc_file
    with open(enc_file, 'r') as file:
        # extract "Key: <>"
        key_line = file.readline()
        #print(key_line[7:-2])
        #print(codecs.escape_decode(key_line[7:-2])[0])
        key = codecs.escape_decode(key_line[7:-2])[0]
        #print(hex(key_line[6]))
        #print((key_line[7:-2]).decode('hex'))
        #key = (key_line[5:]).encode()
        #key = binascii.unhexlify(bytes(key_line[7:-1], encoding='utf-8'))
        # extract "Encrypted Blockchain: <>"
        enc_blockchain_line = file.readline()
        encrypted_blockchain = codecs.escape_decode(enc_blockchain_line[24:-2])[0]

        print(key)
        print(enc_blockchain_line)

        decrypted_token = decrypt(encrypted_blockchain, key)
        print("Decrypted Token:", decrypted_token)

if __name__ == "__main__":
    text = sys.argv[1]
    # main(text)
    main2(text)

AsianHacker-picoctf@webshell:~$ python3  pythonScript.py enc_flag ⌨️
b'\xa9\xcco`\xfa\xf9\xb5\xc0\xda\xf6*\xb3\xbe\xa9t\x0fi\xae\x13\x01q-\xae\x9ap\xb7\xa45\x1e{\xaa\xb4'
Encrypted Blockchain: b'\xf7Y\x8db\x8bS\xb2\x80q\xf2\xa0\x87\xd6(\xfc\xe6\xf2\\\x82`\x8c\\\xb4\xd4v\xf0\xf2\xd1\xde/\xfa\xb0\xfb]\xdfg\x8bV\xe2\xd1$\xa5\xa6\xd9\x8c+\xa8\xe7\xa6X\x82d\xda\x01\xb1\x85u\xa4\xa3\xd3\xda}\xff\xbc\xeeZ\x8am\x8d\x01\xb1\x84$\xa1\xf4\x85\x8c,\xfa\xe7\xf0S\x8f4\x8f\x02\xb1\x82w\xf1\xf6\x85\xd7/\xff\xb3\xa6]\xdf`\x8b\x00\xe3\xd1"\xf2\xf6\xd8\xda|\xfd\xb7\xf3Z\xd83\xdc\\\xbe\xd6!\xa2\xae\xd8\x8c{\xfa\xb0\xf2G\x8ae\x8a\x01\xe3\xd7q\xf4\xa3\xd9\x8aq\xfd\xbd\xfb\x08\x8ag\x8dQ\xe3\xd0"\xa4\xf2\x84\xdeq\xac\xb5\xf4\x0e\xca<\xdd\x0b\xc5\xe6U\xbc\xf5\x8d\x81*\xa6\xdb\xf09\xe8=\xe8\r\xd4\xd0G\xf6\xe6\x82\xb6\x16\x95\xd1\xa9\'\x8a\'\x8a]\xe5\xfaL\xb6\xd4\x9b\x83\x03\x97\xfe\x81!\xe5a\x87\\\xbf\xd4*\xa2\xf6\x9c\xdex\xf4\xe5\xf6R\x8em\x87W\xb1\x80 \xf5\xf4\xd6\x8a{\xfd\xe7\xf3\x08\x89d\xdfP\xb2\x82u\xf4\xa0\x80\xc3y\xfd\xb2\xa5[\x83m\x8dQ\xe5\x84+\xfe\xa5\x84\xd7p\xf4\xb6\xf1S\x89m\xddQ\xb0\xd7&\xf2\xf2\xd3\x8b,\xf9\xb5\xfa\x08\xd8f\x8c\\\xe5\xd7"\xf3\xf6\xd4\x8c|\xac\xe5\xa7\x08\x8ag\x8d\x02\xbe\xd1$\xa2\xa3\x80\x8ad\xfd\xb4\xa6]\xdc0\xd8W\xb1\x85q\xa5\xf6\x80\xdbq\xa9\xb5\xf0_\xdee\x8e\x00\xbe\xd3r\xf4\xa2\xd4\x88y\xf4\xb0\xa5_\xdc4\xda\x05\xb7\x80r\xf1\xa3\x84\x8ap\xfb\xb2\xfa\x08\x8c`\x8eR\xe3\x81q\xfe\xae\x84\x88x\xcf\x86'

DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf7Y\x8db\x8bS\xb2\x80q\xf2\xa0\x87\xd6(\xfc\xe6', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'43775742b57f8a1b'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf2\\\x82`\x8c\\\xb4\xd4v\xf0\xf2\xd1\xde/\xfa\xb0', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'1685282fe7e00f74'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xfb]\xdfg\x8bV\xe2\xd1$\xa5\xa6\xd9\x8c+\xa8\xe7', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'87e252dc7b18bbec'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xa6X\x82d\xda\x01\xb1\x85u\xa4\xa3\xd3\xda}\xff\xbc', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'e281de77fc424428'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xeeZ\x8am\x8d\x01\xb1\x84$\xa1\xf4\x85\x8c,\xfa\xe7', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'-0083e767fcdbe7c'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf0S\x8f4\x8f\x02\xb1\x82w\xf1\xf6\x85\xd7/\xff\xb3', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'395a1f70d6ad9f27'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xa6]\xdf`\x8b\x00\xe3\xd1"\xf2\xf6\xd8\xda|\xfd\xb7', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'e7e55dec15a94503'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf3Z\xd83\xdc\\\xbe\xd6!\xa2\xae\xd8\x8c{\xfa\xb0', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'00bfb88d2e99b274'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf2G\x8ae\x8a\x01\xe3\xd7q\xf4\xa3\xd9\x8aq\xfd\xbd', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'1-004eeeb348d809'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xfb\x08\x8ag\x8dQ\xe3\xd0"\xa4\xf2\x84\xdeq\xac\xb5', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'8b0235eb1cee08a1'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf4\x0e\xca<\xdd\x0b\xc5\xe6U\xbc\xf5\x8d\x81*\xa6\xdb', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'7dpicoCTF{block_'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf09\xe8=\xe8\r\xd4\xd0G\xf6\xe6\x82\xb6\x16\x95\xd1', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'3SRhViRbT1qcX_XU'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b"\xa9'\x8a'\x8a]\xe5\xfaL\xb6\xd4\x9b\x83\x03\x97\xfe", b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'jM0r49cH_qCzmJZz'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\x81!\xe5a\x87\\\xbf\xd4*\xa2\xf6\x9c\xdex\xf4\xe5', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'BK_4989f9ea}019a'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf6R\x8em\x87W\xb1\x80 \xf5\xf4\xd6\x8a{\xfd\xe7', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'5848937232c7d20c'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf3\x08\x89d\xdfP\xb2\x82u\xf4\xa0\x80\xc3y\xfd\xb2', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'0b31a440f37a-006'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xa5[\x83m\x8dQ\xe5\x84+\xfe\xa5\x84\xd7p\xf4\xb6', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'f19835c6892e9992'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf1S\x89m\xddQ\xb0\xd7&\xf2\xf2\xd3\x8b,\xf9\xb5', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'2938c56e55e2ee41'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xfa\x08\xd8f\x8c\\\xe5\xd7"\xf3\xf6\xd4\x8c|\xac\xe5', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'9bb328ce14a5b5aa'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xa7\x08\x8ag\x8d\x02\xbe\xd1$\xa2\xa3\x80\x8ad\xfd\xb4', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'db023f8c7e4ad-00'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xa6]\xdc0\xd8W\xb1\x85q\xa5\xf6\x80\xdbq\xa9\xb5', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'e7fef377bbaa58d1'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xf0_\xdee\x8e\x00\xbe\xd3r\xf4\xa2\xd4\x88y\xf4\xb0', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'35d00d8aa355f094'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xa5_\xdc4\xda\x05\xb7\x80r\xf1\xa3\x84\x8ap\xfb\xb2', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'f5fada12a64ed966'
DEBUG: xor_bytes: len(a)=16, len(b)=32
DEBUG: xor_bytes: a=b'\xfa\x08\x8c`\x8eR\xe3\x81q\xfe\xae\x84\x88x\xcf\x86', b=b'\xc3j\xbaU\xbed\x86\xb2\x13\xc7\x97\xe1\xeeI\xcd\x84\xdb\xfb\xaf2\x10k>\x8b\xb3\xfe\xcb3`a\xaa\x82'
DEBUG: xor_bytes: xor_ab=b'9b6506e3b99ef1\x02\x02'
DEBUG:decrypt: num_pad=2
Decrypted Token: b'picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_4989f9ea}' 🔐

Method 2:
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
import hashlib
import re
 
block_size = 16
 
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))
 
def decrypt(ciphertext, key):
    plaintext = b''
    key_hash = hashlib.sha256(key).digest()
 
    for i in range(0, len(ciphertext), block_size):
        # NOTE: Each block encrypted using the same part of the key
        block = ciphertext[i:i + block_size]
        plain_block = xor_bytes(block, key_hash)
        plaintext += plain_block
 
    return plaintext
 
def main():
    with open("enc_flag", "r") as f:
        key, c = f.readlines()
 
    key = eval(key[5:])
    c = eval(c[22:])
 
    decrypted_blockchain = decrypt(c, key)
 
    # The flag is the token in the middle of the plaintext!
    flag = re.search(b'picoCTF{.*}', decrypted_blockchain)
    print(flag.group(0).decode("utf-8"))
 
if __name__ == "__main__":
    main()

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_4989f9ea} 🔐
```

## Flag
picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_4989f9ea}

## Continue
[Continue](./picoGym0368.md)