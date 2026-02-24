"""
Vigenère Cipher

The Vigenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.

Level: Beginner
What I learned:
    TODO later
"""

try:
    import pyperclip
except ImportError:
    pass

from vigenere import Vigenere

def main():
    vigenere = Vigenere()

    # Let the user specify if they are encrypting or decrypting:
    while True:             # Keep asking until the user enters e or d
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()

        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # Let the user specify the key to use
    while True:             # Keep asking until the user enters a valid key
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        response = input('> ').upper()
        if response.isalpha():
            myKey = response
            break

    # Let the user specify the message to encrypt/decrypt
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # Perform the encryption/decryption
    if myMode == 'encrypt':
        translated = vigenere.encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = vigenere.decryptMessage(myMessage, myKey)

    print('%sed message:' % (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass                        # Do nothing if pyperclip wasn't installed

if __name__ == '__main__':
    main()