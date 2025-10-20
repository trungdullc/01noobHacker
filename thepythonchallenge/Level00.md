# Level 00

## Previous Flag
```
N/A
```

## Goal
Picture of 2^38<br>
Hint: try to change the URL address.

## What I learned
```
2**38 is used in python as power/exponent
Sames as left shift by 1
for loops
range

Note: no double type in python only float
Solutions: https://www.hackingnote.com/en/python-challenge-solutions/ (check here if got time, got other ways to solve)
```

## Side Quest
```
AsianHacker-picoctf@webshell:~$ python3 -q
>>> answer = 1
>>> 
>>> def power(exponent) -> float:
...    global answer                                # Note: This is needed in python
...    for i in range(exponent):
...       answer *= 2
...    return answer
... 
>>> power(38)
274877906944
>>> quit()

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py 
#!/usr/bin/python3

answer = 1

def power(exponent) -> float:
    global answer
    for i in range(exponent):
        answer *= 2
    return answer

print(power(38))
AsianHacker-picoctf@webshell:/tmp$ chmod u+x pythonScript.py 
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py 
274877906944

AsianHacker-picoctf@webshell:/tmp$ vi bashScript.bash
AsianHacker-picoctf@webshell:/tmp$ cat bashScript.bash 
#!/bin/bash

answer=1
exponent=38

for ((i=0; i<exponent; i++)); do
  answer=$((answer * 2))
done

echo "$answer"
AsianHacker-picoctf@webshell:/tmp$ chmod u+x bashScript.bash 
AsianHacker-picoctf@webshell:/tmp$ ./bashScript.bash 
274877906944
AsianHacker-picoctf@webshell:/tmp$ bash bashScript.bash 
274877906944

PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> $exponent = 38
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> $answer = 1
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> for ($i = 0; $i -lt $exponent; $i++) {
>>     $answer *= 2
>> }
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Write-Output $answer
274877906944
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/def/0.html ⌨️

Think: Hint to change to next URL address go to 1.html
Browser: http://www.pythonchallenge.com/pc/def/1.html ⌨️
2**38 is much much larger.

Think: this means solve 2**38 and append to url
AsianHacker-picoctf@webshell:~$ python3 -c "print(2**38)" ⌨️
274877906944 👀
AsianHacker-picoctf@webshell:/tmp$ python3 -q
>>> type(pow(2, 38))
<class 'int'>

Browser: http://www.pythonchallenge.com/pc/def/274877906944.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/def/274877906944.html 

## Continue
[Continue](./Level01.md)