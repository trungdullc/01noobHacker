# picoGym Level 71: vault-door-4
Source: https://play.picoctf.org/practice/challenge/71

## Goal
This vault uses ASCII encoding for the password. The source code for this vault is here: VaultDoor4.java<br>
https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java

## What I learned
```
CyberChef
Reverse Engineering
JavaScript
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java ⌨️
--2025-09-25 21:59:58--  https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1497 (1.5K) [application/octet-stream]
Saving to: 'VaultDoor4.java'

VaultDoor4.java                                            100%[======================================================================================================================================>]   1.46K  --.-KB/s    in 0s      

2025-09-25 21:59:58 (847 MB/s) - 'VaultDoor4.java' saved [1497/1497]

AsianHacker-picoctf@webshell:~$ cat VaultDoor4.java ⌨️
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
            '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

# Method 1: ChatGPT
# Convert each value to ASCII

Decimal:
    106 → 'j'
    85 → 'U'
    53 → '5'
    116 → 't'
    95 → '_'
    52 → '4'
    95 → '_'
    98 → 'b'

Hex:
    0x55 → 'U'
    0x6e → 'n'
    0x43 → 'C'
    0x68 → 'h'
    0x5f → '_'
    0x30 → '0'
    0x66 → 'f'
    0x5f → '_'

Octal:
    0142 → 98 → 'b'
    0131 → 89 → 'Y'
    0164 → 116 → 't'
    063 → 51 → '3'
    0163 → 115 → 's'
    0137 → 95 → '_'
    0143 → 99 → 'c'
    061 → 49 → '1'

Character literals:
    '9' → '9'
    '4' → '4'
    'f' → 'f'
    '7' → '7'
    '4' → '4'
    '5' → '5'
    '8' → '8'
    'e' → 'e'

# Method 2: python3
# Note: Can't have 0142 must be 0o142
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
def crackPassword():
    myBytes = [
        106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
        0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
        0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o143, 0o61 ,
        '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e']

    # Convert all integer values to characters
    decoded_chars = [chr(val) if isinstance(val, int) else val for val in myBytes]

    return decoded_chars

def getFlag(decoded_chars):
    return "picoCTF{" + "".join(decoded_chars) + "}"

print(getFlag(crackPassword()))

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e} 🔐

# Method 3: Modify Java
AsianHacker-picoctf@webshell:~$ cat VaultDoor4.java ⌨️
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
            '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
        };

        // Debug 🧠
        String password_decrypted = new String(myBytes);
        System.out.println(password_decrypted);

        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

AsianHacker-picoctf@webshell:~$ javac VaultDoor4.java ⌨️
AsianHacker-picoctf@webshell:~$ java VaultDoor4 ⌨️
Enter vault password: abcdefghijklmnopqrstuv ⌨️
jU5t_4_bUnCh_0f_bYt3s_c194f7458e 🔐
Access denied!

# Method 3: JavaScript
const base = String.fromCharCode(
  106, 85, 53, 116, 95, 52, 95, 98,
  0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
  0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o143
); ⌨️

undefined
const suffix = ['9','4','f','7','4','5','8','e'].join(""); ⌨️
undefined
console.log(base + suffix); ⌨️
VM2053:1 jU5t_4_bUnCh_0f_bYt3s_c94f7458e 🔐

# Method 4: CyberChef
https://cyberchef.io/#recipe=From_Decimal('Space',false)&input=MTA2LCA4NSwgNTMsIDExNiwgOTUsIDUyLCA5NSwgOTg
https://cyberchef.io/#recipe=From_Hex('Auto')&input=MHg1NSwgMHg2ZSwgMHg0MywgMHg2OCwgMHg1ZiwgMHgzMCwgMHg2NiwgMHg1Zg
https://cyberchef.io/#recipe=From_Octal('Space')&input=MDE0MiwgMDEzMSwgMDE2NCwgMDYzLCAwMTYzLCAwMTM3LCAwMTQz

# Append this to above '9','4','f','7','4','5','8','e'
```

## Flag
picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}

## Continue
[Continue](./picoGym0077.md)