"""
sPoNgEcAsE

Translates English messages into sPOnGEcAsE.

Level: Beginner
What I learned:
    TODO later
"""

import random

try:
    import pyperclip
except ImportError:
    pass

def englishToSpongecase(message):
    """Return the spongecase form of the given string."""
    spongecase = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongecase += character
            continue

        if useUpper:
            spongecase += character.upper()
        else:
            spongecase += character.lower()

        # Flip the case, 90% of the time
        if random.randint(1, 100) <= 90:
            useUpper = not useUpper             # Flip the case
    return spongecase

def main():
    """Run the Spongecase program."""
    print('''sPoNgEtExT

eNtEr YoUr MeSsAgE:''')
    spongecase = englishToSpongecase(input('> '))
    print(f"\n{spongecase}")

    try:
        pyperclip.copy(spongecase)
        print('(cOpIed SpOnGeCasE to ClIpbOaRd.)')
    except:
        pass

if __name__ == '__main__':
    main()