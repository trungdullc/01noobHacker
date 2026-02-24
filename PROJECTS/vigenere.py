# Every possible symbol that can be encrypted/decrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Vigenere:
    def __init__(self):
            print('''Vigenère Cipher
The Viegenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.''')
            
    def encryptMessage(self, message, key):
        """Encrypt the message using the key."""
        return self.translateMessage(message, key, 'encrypt')


    def decryptMessage(self, message, key):
        """Decrypt the message using the key."""
        return self.translateMessage(message, key, 'decrypt')


    def translateMessage(self, message, key, mode):
        """Encrypt or decrypt the message using the key."""
        translated = []  # Stores the encrypted/decrypted message string.

        keyIndex = 0
        key = key.upper()

        for symbol in message:  # Loop through each character in message.
            num = LETTERS.find(symbol.upper())
            if num != -1:  # -1 means symbol.upper() was not in LETTERS.
                if mode == 'encrypt':
                    # Add if encrypting:
                    num += LETTERS.find(key[keyIndex])
                elif mode == 'decrypt':
                    # Subtract if decrypting:
                    num -= LETTERS.find(key[keyIndex])

                num %= len(LETTERS)  # Handle the potential wrap-around.

                # Add the encrypted/decrypted symbol to translated.
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())

                keyIndex += 1  # Move to the next letter in the key.
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                # Just add the symbol without encrypting/decrypting:
                translated.append(symbol)

        return ''.join(translated)