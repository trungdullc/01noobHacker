# picoGym Level 12: vault-door-1
Source: https://play.picoctf.org/practice/challenge/12

## Goal
This vault uses some complicated arrays! I hope you can make sense of it, special agent.<br>
The source code for this vault is here: VaultDoor1.java<br>
https://jupiter.challenges.picoctf.org/static/29b91e638ccbd76aaa8c0462d1c64d8d/VaultDoor1.java

## What I learned
```
Notepad ++
    Ctrl + H
VSC
    Ctrl + F
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/29b91e638ccbd76aaa8c0462d1c64d8d/VaultDoor1.java ⌨️
--2025-09-25 00:16:51--  https://jupiter.challenges.picoctf.org/static/29b91e638ccbd76aaa8c0462d1c64d8d/VaultDoor1.java
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2264 (2.2K) [application/octet-stream]
Saving to: 'VaultDoor1.java'

VaultDoor1.java                                            100%[======================================================================================================================================>]   2.21K  --.-KB/s    in 0s      

2025-09-25 00:16:51 (918 MB/s) - 'VaultDoor1.java' saved [2264/2264]

AsianHacker-picoctf@webshell:~$ cat VaultDoor1.java ⌨️
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
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

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '3' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == 'f' &&
               password.charAt(30) == 'b' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '6' &&
               password.charAt(26) == 'f' &&
               password.charAt(31) == '0';
    }
}

# Method 1: Notepad++ and RE
# Copy password.charAt() into Notepad++
Edit > Line Operation > Sort Lines as Asending Integers

password.charAt(0)  == 'd' &&
password.charAt(1)  == '3' &&
password.charAt(2)  == '5' &&
password.charAt(3)  == 'c' &&
password.charAt(4)  == 'r' &&
password.charAt(5)  == '4' &&
password.charAt(6)  == 'm' &&
password.charAt(7)  == 'b' &&
password.charAt(8)  == 'l' &&
password.charAt(9)  == '3' &&
password.charAt(10) == '_' &&
password.charAt(11) == 't' &&
password.charAt(12) == 'H' &&
password.charAt(13) == '3' &&
password.charAt(14) == '_' &&
password.charAt(15) == 'c' &&
password.charAt(16) == 'H' &&
password.charAt(17) == '4' &&
password.charAt(18) == 'r' &&
password.charAt(19) == '4' &&
password.charAt(20) == 'c' &&
password.charAt(21) == 'T' &&
password.charAt(22) == '3' &&
password.charAt(23) == 'r' &&
password.charAt(24) == '5' &&
password.charAt(25) == '_' &&
password.charAt(26) == 'f' &&
password.charAt(27) == 'f' &&
password.charAt(28) == '6' &&
password.charAt(29) == '3' &&
password.charAt(30) == 'b' &&
password.charAt(31) == '0'

Notepad++: Control + H > Regular Expression ❤️
Find what: .* ' ⌨️
Replace with:
Replace all

Find what: '.* ⌨️
Replace with:
Replace all

Search Mode: Extended
Find what: \r ⌨️
Replace with:
Replace all

d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0

# Method 2: VSC
AsianHacker-picoctf@webshell:~$ vi main.java ⌨️
AsianHacker-picoctf@webshell:~$ cat main.java ⌨️
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        char[] password = new char[32];

        // Use Ctrl + F to replace ❤️
        // Note: click v to toggle replace
        // Note: there RE next to it
        password[0]  = 'd';
        password[1]  = '3';
        password[2]  = '5';
        password[3]  = 'c';
        password[4]  = 'r';
        password[5]  = '4';
        password[6]  = 'm';
        password[7]  = 'b';
        password[8]  = 'l';
        password[9]  = '3';
        password[10] = '_';
        password[11] = 't';
        password[12] = 'H';
        password[13] = '3';
        password[14] = '_';
        password[15] = 'c';
        password[16] = 'H';
        password[17] = '4';
        password[18] = 'r';
        password[19] = '4';
        password[20] = 'c';
        password[21] = 'T';
        password[22] = '3';
        password[23] = 'r';
        password[24] = '5';
        password[25] = '_';
        password[26] = 'f';
        password[27] = 'f';
        password[28] = '6';
        password[29] = '3';
        password[30] = 'b';
        password[31] = '0';

        System.out.println(password);
    }
}
AsianHacker-picoctf@webshell:~$ javac main.java ⌨️
AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  VaultDoor1.class  main.java
AsianHacker-picoctf@webshell:~$ java VaultDoor1 ⌨️ 
d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0 🔐
```

## Flag
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}

## Continue
[Continue](./picoGym0060.md)