# picoGym Level 473: Guess My Cheese (Part 1)
Source: https://play.picoctf.org/practice/challenge/473

## Goal
Try to decrypt the secret cheese password to prove you're not the imposter!<br>
Connect to the program on our server: <br>
nc verbal-sleep.picoctf.net 60014

## What I learned
```
ChatGPT: An Affine Cipher is a type of monoalphabetic substitution cipher in classical cryptography.
It’s based on simple math using modular arithmetic. Think of it as a combination of a multiplicative cipher and an additive (Caesar) cipher.

Note: Dynamic answer each time
Note: Can decode message if know A and B
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc verbal-sleep.picoctf.net 60014 ⌨️

*******************************************
***             Part 1                  ***
***    The Mystery of the CLONED RAT    ***
*******************************************

The super evil Dr. Lacktoes Inn Tolerant told me he kidnapped my best friend, Squeexy, and replaced him with an evil clone! You look JUST LIKE SQUEEXY, but I'm not sure if you're him or THE CLONE. I've devised a plan to find out if YOU'RE the REAL SQUEEXY! If you're Squeexy, I'll give you the key to the cloning room so you can maul the imposter...

Here's my secret cheese -- if you're Squeexy, you'll be able to guess it:  GXSZZQITNLZ 👀
Hint: The cheeses are top secret and limited edition, so they might look different from cheeses you're used to!
Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
e ⌨️

What cheese would you like to encrypt? CHEDDAR ⌨️
Here's your encrypted cheese:  ORKZZSX 👀
Not sure why you want it though...*squeak* - oh well!

I don't wanna talk to you too much if you're some suspicious character and not my BFF Squeexy!
You have 2 more chances to prove yourself to me!

Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
e ⌨️

What cheese would you like to encrypt? FETA ⌨️
Here's your encrypted cheese:  VKTS 👀
Not sure why you want it though...*squeak* - oh well!

I don't wanna talk to you too much if you're some suspicious character and not my BFF Squeexy!
You have 1 more chances to prove yourself to me!

Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
g ⌨️


   _   _
  (q\_/p)
   /. .\.-.....-.     ___,
  =\_t_/=     /  `\  (
    )\ ))__ __\   |___)
   (/-(/`  `nn---'

SQUEAK SQUEAK SQUEAK

         _   _
        (q\_/p)
         /. .\        
  ,__   =\_t_/=   
     )   /   \      
    (   ((   ))   
     \  /\) (/\    
      `-\  Y  /    
         nn^nn        
                          

Is that you, Squeexy? Are you ready to GUESS...MY...CHEEEEEEESE?
Remember, this is my encrypted cheese:  GXSZZQITNLZ 👀
So...what's my cheese?
GRADDOSTJXD ⌨️                           

         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))    /O_.-'  O |  
     \  /\) (/\    | o   o  o|   
      `-\  Y  /    |o   o O.-`  
         nn^nn     | O _.-'      
                   '--`         

munch...

         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))      ).-'  O |  
     \  /\) (/\      )   o  o|   
      `-\  Y  /    |o   o O.-`  
         nn^nn     | O _.-'      
                   '--`         

munch...

         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|   
    (   ((   ))        )'  O |  
     \  /\) (/\          )  o|   
      `-\  Y  /         ) O.-`  
         nn^nn        ) _.-'      
                   '--`         

MUNCH.............

YUM! MMMMmmmmMMMMmmmMMM!!! Yes...yesssss! That's my cheese!
Here's the password to the cloning room:  picoCTF{ChEeSy86ec32f4} 🔐

Method 1:
https://www.dcode.fr/cipher-identifier
Results:
  Affine Cipher	👀
  Mono-alphabetic Substitution	
  Cipher Disk/Wheel

Affine Decoder
Affine ciphertext
  GXSZZQITNLZ
  ORKZZSX
  VKTS
Automatic Brute Force Decryption

Result:
A=11,B=18	GRADDOSTJXD 👀 Note: Can also decode w/ this and just the encrypted msg
CHEDDAR
FETA

A=5,B=5	VONEEXLIMWE
HSBEENO
YBIN
```

## Flag
picoCTF{ChEeSy86ec32f4}

## Continue
[Continue](./picoGym0474.md)