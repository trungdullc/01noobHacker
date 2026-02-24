"""
Caesar Cipher Cracker
This programs hacks messages encrypted with the Caesar cipher by doing a brute force attack against every possible key.

Note: Message need be in uppercase to work because lowercase gets ignored
Level: Beginner
What I Learned:
    Nothing, just review
    builtins.str.find() returns index starting from 0 to location
"""

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('Caesar Cipher Cracker')

    print('Enter the encrypted Caesar cipher message to hack')
    message = input('> ')

    for index in range(len(SYMBOLS)):                   # Loop through every possible key
        translated = ''

        for symbol in message:                          # Decrypt each symbol in the message
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)              # Get the number of the symbol
                num -= index                            # Decrypt the number

                if num < 0:                             # Handle the wrap-around if num is less than 0
                    num = num + len(SYMBOLS)

                translated += SYMBOLS[num]              # Add decrypted number's symbol to translated
            else:
                translated += symbol                    # Just add the symbol without decrypting

        # Display key being tested along with decrypted text
        print('Key #{}: {}'.format(index, translated))

if __name__ == "__main__":
    main()