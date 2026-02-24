"""
Duckling Screensaver
A screensaver of many many ducklings

>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^

Level: Intermediate
What I learned:
    None is Python3 version of C null or C++ nullptr
 """

import random, sys, time
from duckling import Duckling, WIDTH, DUCKLING_WIDTH, DENSITY, PAUSE

def main():
    print('Duckling Screensaver')
    print('Press Ctrl-C to quit...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:                                                 # Main program loop
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # See if we should create a duckling in this lane
            if (ducklingObj == None and random.random() <= DENSITY):
                    # Place a duckling in this lane
                    ducklingObj = Duckling()
                    ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                # Draw a duckling if there is one in this lane
                print(ducklingObj.getNextBodyPart(), end='')
                # Delete the duckling if we've finished drawing it
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                # Draw five spaces since there is no duckling here
                print(' ' * DUCKLING_WIDTH, end='')

        print()
        sys.stdout.flush()                  # Make sure text appears on the screen
        time.sleep(PAUSE)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()