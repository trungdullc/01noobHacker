# picoGym Level 265: Enhance!
Source: https://play.picoctf.org/practice/challenge/265

## Goal
Download this image file and find the flag<br>
https://artifacts.picoctf.net/c/102/drawing.flag.svg

## What I learned
```
.svg file is just XML (text)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/102/drawing.flag.svg ⌨️
--2025-09-16 07:13:44--  https://artifacts.picoctf.net/c/102/drawing.flag.svg
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.18, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4149 (4.1K) [application/octet-stream]
Saving to: 'drawing.flag.svg'

drawing.flag.svg                                           100%[======================================================================================================================================>]   4.05K  --.-KB/s    in 0s      

2025-09-16 07:13:44 (137 MB/s) - 'drawing.flag.svg' saved [4149/4149]

AsianHacker-picoctf@webshell:~$ steghide --extract -sf drawing.flag.svg ⌨️
Enter passphrase: 
steghide: the file format of the file "drawing.flag.svg" is not supported.
AsianHacker-picoctf@webshell:~$ strings drawing.flag.svg | grep "pico" ⌨️
AsianHacker-picoctf@webshell:~$ binwalk drawing.flag.svg ⌨️

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             XML document, version: "1.0"

AsianHacker-picoctf@webshell:~$ file drawing.flag.svg ⌨️
drawing.flag.svg: SVG Scalable Vector Graphics image 👀

Method 1: from code
AsianHacker-picoctf@webshell:~$ tail -n 40 drawing.flag.svg ⌨️
         y="132.08501"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3748">p 👀</tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08942"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3754">i 👀</tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09383"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3756">c 👀</tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09824"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3758">o 👀</tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10265"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3760">C 👀</tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10706"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3762">T 👀</tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11147"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3764">F { 3 n h 4 n 👀</tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11588"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3752">c 3 d _ d 0 a 7 5 7 b f } 👀</tspan></text>
  </g>
</svg>

Method 2: Modify font size and position to see better

Method 3: grep tspan since each has unique id
AsianHacker-picoctf@webshell:~$ cat drawing.flag.svg | grep "</tspan" ⌨️
         id="tspan3748">p 👀</tspan><tspan
         id="tspan3754">i 👀</tspan><tspan
         id="tspan3756">c 👀</tspan><tspan
         id="tspan3758">o 👀</tspan><tspan
         id="tspan3760">C 👀</tspan><tspan
         id="tspan3762">T 👀</tspan><tspan
         id="tspan3764">F { 3 n h 4 n 👀</tspan><tspan
         id="tspan3752">c 3 d _ d 0 a 7 5 7 b f }👀</tspan></text>
```

## Flag
picoCTF{3nh4nc3d_d0a757bf}

## Continue
[Continue](./picoGym0290.md)