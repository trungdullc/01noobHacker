try:
    import pyperclip
except ImportError:
    pass                                    # Optional: Make sure in code to do try/except

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'      # Every possible symbol that can be encrypted/decrypted

class CaesarCipher:
    def __init__(self):
        self.mode = ""
        self.key = ""
        self.message = ""
        self.translated = ''                 # Stores encrypted/decrypted form of the message

        print("""Caesar Cipher
The Caesar cipher encrypts letters by shifting them over by a
key number. For example, a key of 2 means the letter A is
encrypted into C, the letter B encrypted into D, and so on.\n""")

    def is_encypt_decrypt(self):
        """Ask if want encrypt or decrypt and store mode"""
        while True:
            print('Do you want to (e)ncrypt or (d)ecrypt?')
            response = input('> ').lower()

            if response.startswith('e'):
                self.mode = 'encrypt'
                break
            elif response.startswith('d'):
                self.mode = 'decrypt'
                break
            print('Please enter the letter e or d.')

    def set_key(self):
        """Let the user enter the key to use and store key"""
        while True:
            max_key = len(SYMBOLS) - 1

            print('Please enter the key (0 to {}) to use.'.format(max_key))
            response = input('> ').upper()
            
            if not response.isdecimal():
                continue                    # Note: continue will skip the rest and while True starts all over

            if 0 <= int(response) < len(SYMBOLS):
                self.key = int(response)
                break

    def set_message(self):
        """Let the user enter the message to encrypt/decrypt and store message"""
        print('Enter the message to {}.'.format(self.mode))
        self.message = input('> ')

        # Caesar cipher only works on uppercase letters:
        self.message = self.message.upper()

    def encrypt_decrypt(self):
        """Encrypt/decrypt each symbol in the message"""

        for symbol in self.message:
            if symbol in SYMBOLS:               # Note: Only convert in SYMBOLS no numbers or special characters
                num = SYMBOLS.find(symbol)      # Get the number of the symbol
                if self.mode == 'encrypt':
                    num += self.key
                elif self.mode == 'decrypt':
                    num -= self.key

                # Main Logic ❤️❤️❤️❤️❤️
                # Handle the wrap-around if num is larger than the length of SYMBOLS or less than 0
                if num >= len(SYMBOLS):
                    num -= len(SYMBOLS)
                elif num < 0:
                    num += len(SYMBOLS)

                # Add encrypted/decrypted number's symbol to translated
                self.translated += SYMBOLS[num]
            else:
                # Just add the symbol without encrypting/decrypting
                self.translated += symbol

    def copy_to_clipboard(self):
        """Copy translated to clipboard"""

        # Remember: This was optional on top to copy data into clipboard using pyperclip module
        try:
            pyperclip.copy(self.translated)
            print('Full {}ed text copied to clipboard.'.format(self.mode))
        except:
            pass