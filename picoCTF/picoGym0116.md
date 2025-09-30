# picoGym Level 116: speeds and feeds
Source: https://play.picoctf.org/practice/challenge/116

## Goal
There is something on my shop network running at nc mercury.picoctf.net 33596, but I can't tell what it is. Can you?

## What I learned
```
Reverse Engineering

ChatGPT:
This is G-code — the programming language used for CNC machines (milling machines, 3D printers, laser cutters, etc.) to move a tool along specified coordinates.
        G0 = rapid positioning (move fast without cutting/extruding)
        G1 = linear interpolation (move in a straight line while cutting/extruding)
        X, Y, Z = coordinate positions
        Z0.1 = usually sets the tool just above the surface (e.g., pen barely touching, laser focal plane, cutter depth)
        G1Z0.1 = lower to cutting/working depth
        G0Z0.1 = retract back up before moving elsewhere
```

## Solution
```
https://webshell.picoctf.org/ 

AsianHacker-picoctf@webshell:~$ nc mercury.picoctf.net 33596 > output.txt ⌨️
AsianHacker-picoctf@webshell:~$ sz output.txt ⌨️

Google: simulate g-code
https://ncviewer.com/
picoCTF{num3r1cal_c0ntr0l_e7749028} 🔐
```

## Flag
picoCTF{num3r1cal_c0ntr0l_e7749028}

## Continue
[Continue](./picoGym0266.md)