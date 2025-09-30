# picoGym Level 294: Safe Opener
Source: https://play.picoctf.org/practice/challenge/294

## Goal
Can you open this safe?<br>
I forgot the key to my safe but this program is supposed to help me with retrieving the lost key.<br>
https://artifacts.picoctf.net/c/83/SafeOpener.java<br>
Can you help me unlock my safe?<br>
Put the password you recover into the picoCTF flag format like: picoCTF{password}<br>

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/83/SafeOpener.java
--2025-09-26 20:58:05--  https://artifacts.picoctf.net/c/83/SafeOpener.java
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.18, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1258 (1.2K) [application/octet-stream]
Saving to: 'SafeOpener.java'

SafeOpener.java                                            100%[======================================================================================================================================>]   1.23K  --.-KB/s    in 0s      

2025-09-26 20:58:05 (1014 MB/s) - 'SafeOpener.java' saved [1258/1258]

AsianHacker-picoctf@webshell:~$ cat SafeOpener.java 
import java.io.*;
import java.util.*;  
public class SafeOpener {
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;
        

        while (i < 3) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();

            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
              
            isOpen = openSafe(encodedkey); 👀
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }
    
    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"; 👀
        
        if (password.equals(encodedkey)) { 👀
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
}

# Method 1:
AsianHacker-picoctf@webshell:~$ echo "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d ⌨️
pl3as3_l3t_m3_1nt0_th3_saf3 🔐

# Method 2:
AsianHacker-picoctf@webshell:~$ javac SafeOpener.java ⌨️
AsianHacker-picoctf@webshell:~$ java SafeOpener ⌨️
Enter password for the safe: cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz ⌨️
Y0d3ellYTXpYMnd6ZEY5dE0xOHhiblF3WDNSb00xOXpZV1l6
Password is incorrect

You have  2 attempt(s) left
Enter password for the safe: pl3as3_l3t_m3_1nt0_th3_saf3 🔐
cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz
Sesame open
```

## Flag
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}

## Continue
[Continue](./picoGym0375.md)