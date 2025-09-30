# picoGym Level 472: Flag Hunters
Source: https://play.picoctf.org/practice/challenge/472

## Goal
Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default.<br>
Can you get it to print it? There might be something in it for you.<br>
The program's source code can be downloaded here.<br>
https://challenge-files.picoctf.net/c_verbal_sleep/f9515a5a3a8eda47118d8907e6f91bc4cd5b0159b4a2f1fb2e17dbf4872f6011/lyric-reader.py<br>
Connect to the program with netcat:<br>
$ nc verbal-sleep.picoctf.net 57753

## What I learned
```
Reverse Engineering: Python3
Step 1: Write comments in other peoples code to understand it
```

## Side Quest
```
AsianHacker-picoctf@webshell:~$ vi tiny_interpreter.py ⌨️
AsianHacker-picoctf@webshell:~$ cat tiny_interpreter.py ⌨️
# tiny_interpreter.py
"""
Simple interpreter that demonstrates labels, GOTO, CALL, and RETURN.
Syntax:
  [LABEL]          -> defines a label
  PRINT text       -> prints text
  GOTO LABEL       -> unconditional jump
  CALL LABEL       -> push return address, jump to LABEL
  RETURN           -> pop return address and jump back
  END              -> stop execution
"""

program_text = """
[START]
PRINT Welcome to the tiny song.
CALL VERSE1
PRINT Back in START after VERSE1.
END

[VERSE1]
PRINT This is VERSE1, now going to REFRAIN.
CALL REFRAIN
PRINT Returning from REFRAIN to VERSE1.
RETURN

[REFRAIN]
PRINT REFRAIN: sing along!
RETURN
"""

def parse_labels(lines):
    labels = {}
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith('[') and line.endswith(']'):
            labels[line[1:-1]] = i + 1  # next line is where code starts
    return labels

def run(program_text):
    lines = [l.rstrip() for l in program_text.splitlines() if l.strip() != '']
    labels = parse_labels(lines)
    pc = 0                     # program counter (index into lines)
    call_stack = []            # for CALL/RETURN
    while pc < len(lines):
        raw = lines[pc].strip()
        # skip labels on execution (they are markers)
        if raw.startswith('[') and raw.endswith(']'):
            pc += 1
            continue
        parts = raw.split(None, 1)
        instr = parts[0]
        arg = parts[1] if len(parts) > 1 else ''
        if instr == 'PRINT':
            print(arg)
            pc += 1
        elif instr == 'GOTO':
            label = arg
            if label not in labels:
                raise ValueError('Unknown label: ' + label)
            pc = labels[label]
        elif instr == 'CALL':
            label = arg
            if label not in labels:
                raise ValueError('Unknown label: ' + label)
            call_stack.append(pc + 1)  # return address: next instruction
            pc = labels[label]
        elif instr == 'RETURN':
            if not call_stack:
                raise RuntimeError('Return with empty call stack')
            pc = call_stack.pop()
        elif instr == 'END':
            break
        else:
            raise RuntimeError('Unknown instruction: ' + instr)

if __name__ == '__main__':
    run(program_text)

AsianHacker-picoctf@webshell:~$ python3 tiny_interpreter.py ⌨️
Welcome to the tiny song.
This is VERSE1, now going to REFRAIN.
REFRAIN: sing along!
Returning from REFRAIN to VERSE1.
Back in START after VERSE1.
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_verbal_sleep/f9515a5a3a8eda47118d8907e6f91bc4cd5b0159b4a2f1fb2e17dbf4872f6011/lyric-reader.py ⌨️
--2025-09-24 21:16:44--  https://challenge-files.picoctf.net/c_verbal_sleep/f9515a5a3a8eda47118d8907e6f91bc4cd5b0159b4a2f1fb2e17dbf4872f6011/lyric-reader.py
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.18, 3.160.5.64, 3.160.5.40, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3381 (3.3K) [application/octet-stream]
Saving to: 'lyric-reader.py'

lyric-reader.py                                            100%[======================================================================================================================================>]   3.30K  --.-KB/s    in 0s      

2025-09-24 21:16:45 (539 MB/s) - 'lyric-reader.py' saved [3381/3381]

AsianHacker-picoctf@webshell:~$ cat lyric-reader.py ⌨️
import re
import time

# Read in flag from file
flag = open('flag.txt', 'r').read()

# f-string style
# secret_intro = f"""Pico warriors rising, puzzles laid bare,
# Solving each challenge with precision and flair.
# With unity and skill, flags we deliver,
# The ether’s ours to conquer, {flag}
# """

secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n' 👀


song_flag_hunters = secret_intro +\  👀
'''

[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
CROWD (Singalong here!);
RETURN

[VERSE1]
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

REFRAIN;

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

REFRAIN;

Binary sorcerers, let’s tear it apart,
Disassemble the code to reveal the dark heart.
From opcode to logic, tracing each line,
Emulate and break it, this key will be mine.
Debugging the maze, and I see through the deceit,
Patch it up right, and watch the lock release.

REFRAIN;

Ciphertext tumbling, breaking the spin,
Feistel or AES, we’re destined to win.
Frequency, padding, primes on the run,
Vigenère, RSA, cracking them for fun.
Shift the letters, matrices fall,
Decrypt that flag and hear the ether call.

REFRAIN;

SQL injection, XSS flow,
Map the backend out, let the database show.
Inspecting each cookie, fiddler in the fight,
Capturing requests, push the payload just right.
HTML's secrets, backdoors unlocked,
In the world wide labyrinth, we’re never lost.

REFRAIN;

Stack's overflowing, breaking the chain,
ROP gadget wizardry, ride it to fame.
Heap spray in silence, memory's plight,
Race the condition, crash it just right.
Shellcode ready, smashing the frame,
Control the instruction, flags call my name.

REFRAIN;

END;
'''

MAX_LINES = 100

def reader(song, startLabel):
  lip = 0
  start = 0
  refrain = 0
  refrain_return = 0
  finished = False

  # Get list of lyric lines
  song_lines = song.splitlines()
  
  # Find startLabel, refrain and refrain return
  for i in range(0, len(song_lines)):
    if song_lines[i] == startLabel:
      start = i + 1
    elif song_lines[i] == '[REFRAIN]':
      refrain = i + 1
    elif song_lines[i] == 'RETURN':
      refrain_return = i

  # Print lyrics
  line_count = 0
  lip = start
  while not finished and line_count < MAX_LINES:
    line_count += 1
    for line in song_lines[lip].split(';'):
      if line == '' and song_lines[lip] != '':
        continue
      if line == 'REFRAIN':
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
        lip = refrain
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
      elif line == 'END':
        finished = True
      else:
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1

reader(song_flag_hunters, '[VERSE1]')

AsianHacker-picoctf@webshell:~$ nc verbal-sleep.picoctf.net 57753 ⌨️
Command line wizards, we’re starting it right,
Spawning shells in the terminal, hacking all night.
Scripts and searches, grep through the void,
Every keystroke, we're a cypher's envoy.
Brute force the lock or craft that regex,
Flag on the horizon, what challenge is next?

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: some_string;RETURN 0 ⌨️

Echoes in memory, packets in trace,
Digging through the remnants to uncover with haste.
Hex and headers, carving out clues,
Resurrect the hidden, it's forensics we choose.
Disk dumps and packet dumps, follow the trail,
Buried deep in the noise, but we will prevail.

We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: some_string 👀
Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0ed60683} 🔐


[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We’re chasing that victory, and we’ll never quit.
Crowd: some_string 👀
Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, picoCTF{70637h3r_f0r3v3r_0ed60683} 🔐
^C
```

## Flag
picoCTF{70637h3r_f0r3v3r_0ed60683}

## Continue
[Continue](./picoGym0104.md)