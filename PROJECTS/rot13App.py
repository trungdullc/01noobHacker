"""
ROT13 Cipher
The simplest shift cipher for encrypting and decrypting text

Level: Beginner
What I learned:
    Set letters in own str and mod it by 26 to rotate within self using .find()
"""

try:
    import pyperclip
except ImportError:
    pass                                            # Optional, NameError

UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def main():
    print('ROT13 Cipher\n')

    while True:                                         # Main program loop
        print('Enter a message to encrypt/decrypt (or QUIT):')
        message = input('> ')

        if message.upper().startswith("Q"):
            break                                       # Break out of the main program loop

        # Rotate the letters in message by 13 characters
        translated = ''

        for character in message:
            if character.isupper():
                # Concatenate uppercase translated character ❤️
                transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
                translated += UPPER_LETTERS[transCharIndex]
            elif character.islower():
                # Concatenate lowercase translated character ❤️
                transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
                translated += LOWER_LETTERS[transCharIndex]
            else:
                # Concatenate the character untranslated
                translated += character

        # Display the translation
        print('The translated message is:')
        print(translated)
        print()

        try:
            # Copy the translation to the clipboard
            pyperclip.copy(translated)
            print('(Copied to clipboard.)')
        except:
            pass

if __name__ == "__main__":
    main()