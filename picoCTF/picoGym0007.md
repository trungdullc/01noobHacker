# picoGym Level 7: vault-door-training
Source: https://play.picoctf.org/practice/challenge/7

## Goal
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project.<br>
The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open.<br> Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer!<br>
You will need to read the source code for each level to figure out what the password is for that vault door.<br>
As a warmup, we have created a replica vault in our training facility.<br>
The source code for the training vault is here: VaultDoorTraining.java<br>
https://jupiter.challenges.picoctf.org/static/a4a1ca9c54d8fac9404f9cbc50d9751a/VaultDoorTraining.java

## What I learned
```
Reverse Engineering: Java
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/a4a1ca9c54d8fac9404f9cbc50d9751a/VaultDoorTraining.java
--2025-09-24 21:53:17--  https://jupiter.challenges.picoctf.org/static/a4a1ca9c54d8fac9404f9cbc50d9751a/VaultDoorTraining.java
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 943 [application/octet-stream]
Saving to: 'VaultDoorTraining.java'

VaultDoorTraining.java                                     100%[======================================================================================================================================>]     943  --.-KB/s    in 0s      

2025-09-24 21:53:17 (321 MB/s) - 'VaultDoorTraining.java' saved [943/943]

AsianHacker-picoctf@webshell:~$ cat VaultDoorTraining.java 
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) { 👀
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
   }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18"); 🔐
    }
}
```

## Flag
picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}

## Continue
[Continue](./picoGym0012.md)