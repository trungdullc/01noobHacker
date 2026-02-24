"""
DNA
A simple animation of a DNA double-helix. Press Ctrl-C to stop

Level: Beginner
What I learned:
    Showed how .format() could be useful
"""

import random, sys, time

PAUSE = 0.15                        # (!) Try changing this to 0.5 or 0.0

# These are the individual rows of the DNA animation
ROWS = [
    #123456789 <- Use this to measure the number of spaces
    '         ##',                  # Index 0 has no {}
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',                     # Index 9 has no {}
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']

def main():
    try:
        print('DNA Animation')
        print('Press Ctrl-C to quit...')
        time.sleep(2)

        row_index = 0

        while True:                                 # Main program loop
            # Increment rowIndex to draw next row
            row_index += 1

            if row_index == len(ROWS):
                row_index = 0                       # RESET

            # Row indexes 0 and 9 don't have nucleotides:
            if row_index == 0 or row_index == 9:
                print(ROWS[row_index])
                continue

            # Select random nucleotide pairs, guanine-cytosine or adenine-thymine
            random_selection = random.randint(1, 4)

            if random_selection == 1:
                left_nucleotide, right_nucleotide = 'A', 'T'
            elif random_selection == 2:
                left_nucleotide, right_nucleotide = 'T', 'A'
            elif random_selection == 3:
                left_nucleotide, right_nucleotide = 'C', 'G'
            elif random_selection == 4:
                left_nucleotide, right_nucleotide = 'G', 'C'

            # Print the row
            print(ROWS[row_index].format(left_nucleotide, right_nucleotide))    # ❤️ Note: don't need f string with {left_nucleotide}
            time.sleep(PAUSE)                       # Add a slight pause
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
