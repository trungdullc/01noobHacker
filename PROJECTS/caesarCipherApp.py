"""
Caesar Cipher
The Caesar cipher is a shift cipher that uses addition and subtraction to encrypt and decrypt letters
ROT-13 is popular in Capture the Flag (CTF)

Level: Beginner
What I learned:
    pyperclip module used to copy things to clipboard useful for hackers when in remote access and copying illegal security keys or passwords
"""

import sys
from caesarCipher import CaesarCipher

def main():
    caesarCipher = CaesarCipher()

    caesarCipher.is_encypt_decrypt()
    caesarCipher.set_key()
    caesarCipher.set_message()
    caesarCipher.encrypt_decrypt()

    print(caesarCipher.translated)                          # Display encrypted/decrypted string to the screen

    caesarCipher.copy_to_clipboard()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:                               # ❤️ When Ctrl-C is pressed, end the program
        print('\nThanks for running my app')
        sys.exit()