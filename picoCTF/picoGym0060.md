# picoGym Level 60: vault-door-3
Source: https://play.picoctf.org/practice/challenge/60

## Goal
This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java<br>
https://jupiter.challenges.picoctf.org/static/943ea40e3f54fca6d2145fa7aadc5e09/VaultDoor3.java

## What I learned
```
When you put a thing back into encoder it may revert back to flag
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/943ea40e3f54fca6d2145fa7aadc5e09/VaultDoor3.java ⌨️
--2025-09-25 21:19:15--  https://jupiter.challenges.picoctf.org/static/943ea40e3f54fca6d2145fa7aadc5e09/VaultDoor3.java
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1474 (1.4K) [application/octet-stream]
Saving to: 'VaultDoor3.java'

VaultDoor3.java                                            100%[======================================================================================================================================>]   1.44K  --.-KB/s    in 0s      

2025-09-25 21:19:15 (486 MB/s) - 'VaultDoor3.java' saved [1474/1474]

AsianHacker-picoctf@webshell:~$ cat VaultDoor3.java ⌨️
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }

        # Output Buffer: debug, Add this line 🧠
        System.out.println(buffer);

        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}

Method 1:
AsianHacker-picoctf@webshell:~$ javac VaultDoor3.java ⌨️
AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  VaultDoor3.class  VaultDoor3.java
AsianHacker-picoctf@webshell:~$ java VaultDoor3 ⌨️ 
Enter vault password: test ⌨️
Exception in thread "main" java.lang.StringIndexOutOfBoundsException: begin 8, end 3, length 4
        at java.base/java.lang.String.checkBoundsBeginEnd(String.java:3319)
        at java.base/java.lang.String.substring(String.java:1874)
        at VaultDoor3.main(VaultDoor3.java:9)
AsianHacker-picoctf@webshell:~$ java VaultDoor3 ⌨️
Enter vault password: abcdefghijk ⌨️
Access denied!
AsianHacker-picoctf@webshell:~$ java VaultDoor3 ⌨️ 
Enter vault password: picoCTF{jU5t_a_sna_3lpm18g947_u_4_m9r54f} ⌨️
jU5t_a_s1mpl3_an4gr4m_4_u_79958f 🔐
Access denied!

# Method 2: rebuild w/ python
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
def checkPassword(password):
    if not len(password) == 32:
        return False
    buffer = [""] * 32

    for i in range(8):
        buffer[i] = password[i]

    for i in range(8, 16):
        buffer[i] = password[23 - i]
    
    for i in range(16, 32, 2):
        buffer[i] = password[46 - i]
    
    for i in range(31, 16, -2):
        buffer[i] = password[i]
    print(''.join(buffer))                  # Combine and print the reconstructed password

checkPassword("jU5t_a_sna_3lpm18g947_u_4_m9r54f")

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
jU5t_a_s1mpl3_an4gr4m_4_u_79958f 🔐

# Method 3: java
AsianHacker-picoctf@webshell:~$ vi Sol.java ⌨️
AsianHacker-picoctf@webshell:~$ cat Sol.java ⌨️
import java.util.*;

class Sol {
    public static void main(String args[]) {
        char[] buffer = "jU5t_a_sna_3lpm18g947_u_4_m9r54f".toCharArray();
        char[] password = new char[100];
        int i;
        for (i=0; i<8; i++) {
            password[i] = buffer[i];
        }
        for (; i<16; i++) {
            password[23-i]=buffer[i];
        }
        for (; i<32; i+=2) {
            password[46-i]=buffer[i];
        }
        for (i=31; i>=17; i-=2) {
            password[i]=buffer[i];
        }
        String s = new String(password);
        System.out.println(s);
    }
}

AsianHacker-picoctf@webshell:~$ javac Sol.java ⌨️ 
AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  Sol.class  Sol.java
AsianHacker-picoctf@webshell:~$ java Sol ⌨️
jU5t_a_s1mpl3_an4gr4m_4_u_79958f 🔐

# Method 4: node
AsianHacker-picoctf@webshell:~$ node ⌨️
Welcome to Node.js v22.14.0.
Type ".help" for more information.
> password = "jU5t_a_sna_3lpm18g947_u_4_m9r54f" ⌨️
'jU5t_a_sna_3lpm18g947_u_4_m9r54f'
> var i; ⌨️
undefined
> var buffer = Array(32); ⌨️
undefined
> for (i=0; i<8; i++) {
... buffer[i] = password.charAt(i);
... } ⌨️
's'
> for (; i<16; i++) {
... buffer[i] = password.charAt(23-i);
... } ⌨️
'n'
> for (; i<32; i+=2) {
... buffer[i] = password.charAt(46-i);
... } ⌨️
'8'
> for (i=31; i>=17; i-=2) {
... buffer[i] = password.charAt(i);
... } ⌨️
'g'
> console.log("picoCTF{" + buffer.join("") + "}"); ⌨️
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f} 🔐
undefined
```

## Flag
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}

## Continue
[Continue](./picoGym0071.md)