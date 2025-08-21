# picoGym Level 0082: 1_wanna_b3_a_r0ck5tar
Source: https://play.picoctf.org/practice/challenge/82

## Goal
The Rockstar language has changed since this problem was released! Use this Wayback Machine URL to use an <b>older version of Rockstar</b>, here:
https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online<br><br>
I wrote you another song. Put the flag in the picoCTF{} flag format

## What I learned
```
Google: online rockstar compiler (not to be used - translated differently)
  https://codewithrockstar.com/online.html

RockStar Doc: https://codewithrockstar.com/docs/
Python transpliler: https://github.com/yyyyyyyan/rockstar-py
  transpiler (“source-to-source compiler”) program takes code written in one programming language and converts it into another language (TypeScript)

Removing if else forces to run w/o conditionals

Another Solution using Transpiler: https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/1_wanna_b3_a_r0ck5tar.md#1_wanna_b3_a_r0ck5tar 🧠
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://jupiter.challenges.picoctf.org/static/b99c57e4274172bf3c93534b6d59632d/lyrics.txt ⌨️
--2025-08-20 17:44:28--  https://jupiter.challenges.picoctf.org/static/b99c57e4274172bf3c93534b6d59632d/lyrics.txt
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 877 [application/octet-stream]
Saving to: 'lyrics.txt'

lyrics.txt                                                 100%[======================================================================================================================================>]     877  --.-KB/s    in 0s      

2025-08-20 17:44:29 (280 MB/s) - 'lyrics.txt' saved [877/877]

AsianHacker-picoctf@webshell:/tmp$ cat lyrics.txt ⌨️
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"                
Listen to the rhythm
If the rhythm without Music is nothing
Tommy is rockin guitar
Shout Tommy!                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!                 
Tommy is playing rock           
Scream Tommy!       
They are dazzled audiences                  
Shout it!
Rock is electric heaven                     
Scream it!
Tommy is jukebox god            
Say it!                                     
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"                 
Break it down

# Remove the If and Else lines and input whatever you want in input
Keep on rocking!
66
79
78
74
79
86
73

# CyberChef
https://cyberchef.org/#recipe=From_Decimal('Space',false)&input=NjYgNzkgNzggNzQgNzkgODYgNzM
Output: BONJOVI ⌨️

# Modifiy Flag
picoCTF{BONJOVI} 🔐
```

## Flag
picoCTF{BONJOVI}

## Continue
[Continue](./picoGym0436.md)