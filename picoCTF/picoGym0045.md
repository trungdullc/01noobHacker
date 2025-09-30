# picoGym Level 45: vault-door-6
Source: https://play.picoctf.org/practice/challenge/45

## Goal
This vault uses an XOR encryption scheme. The source code for this vault is here: VaultDoor6.java<br>
https://jupiter.challenges.picoctf.org/static/86e94cc555b2ca7375424c884ef581a6/VaultDoor6.java

## What I learned
```

```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/86e94cc555b2ca7375424c884ef581a6/VaultDoor6.java
--2025-09-26 00:03:07--  https://jupiter.challenges.picoctf.org/static/86e94cc555b2ca7375424c884ef581a6/VaultDoor6.java
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1526 (1.5K) [application/octet-stream]
Saving to: 'VaultDoor6.java'

VaultDoor6.java                                            100%[======================================================================================================================================>]   1.49K  --.-KB/s    in 0s      

2025-09-26 00:03:07 (63.3 MB/s) - 'VaultDoor6.java' saved [1526/1526]

AsianHacker-picoctf@webshell:~$ cat VaultDoor6.java 
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
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

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x66, 0x36, 0x30, 0x67, 0x6c, 0x64, 0x6c,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}

# Method 1: python
AsianHacker-picoctf@webshell:~$ python3 ⌨️
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> myBytes = [
...     0x3b, 0x65, 0x21, 0x0a, 0x38, 0x00, 0x36, 0x1d,
...     0x0a, 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0x0a,
...     0x21, 0x1d, 0x61, 0x3b, 0x0a, 0x2d, 0x65, 0x27,
...     0x0a, 0x66, 0x36, 0x30, 0x67, 0x6c, 0x64, 0x6c
... ] ⌨️
>>> # XOR with 0x55 to reverse the Java check ⌨️
>>> password_bytes = [b ^ 0x55 for b in myBytes] ⌨️
>>> print(password_bytes) ⌨️
[110, 48, 116, 95, 109, 85, 99, 72, 95, 104, 52, 114, 68, 51, 114, 95, 116, 72, 52, 110, 95, 120, 48, 114, 95, 51, 99, 101, 50, 57, 49, 57]
>>> # Convert to string, replacing non-printable bytes with '_' ⌨️
>>> password = ''.join(chr(b) if 32 <= b <= 126 else '_' for b in password_bytes) ⌨️
>>> print(password) ⌨️
n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919 🔐
>>> exit() ⌨️

# Method 2: Flipper Zero and MicroPython
# Need: MicroPython installed
# Optional: qFlipper for screen shots
# DL VaultDoor6.java onto Flipper Zero

import flipperzero as fz
from time import sleep

# XOR'd Flag Bytes
hexBytes = [PUT_THE_BYTES_HERE]

disp_flag = ""
bool_exit = False
p0, p1 = 0, 20

# Button press handler for text scrolling
# Back to exit, Left to scroll left, Right to scroll right
@fz.on_input
def user_input(button, type):
    global bool_exit, p0, p1
    if button == fz.INPUT_BUTTON_BACK and type == fz.INPUT_TYPE_SHORT:
        bool_exit = True
    elif button == fz.INPUT_BUTTON_LEFT and type == fz.INPUT_TYPE_SHORT:
        p0 -= 1; p1 -= 1
    elif button == fz.INPUT_BUTTON_RIGHT and type == fz.INPUT_TYPE_SHORT:
        p0 += 1; p1 += 1

flag = []                           # Init flag var
for i in "picoCTF{": flag.append(i) # Add flag tag

# Decode The XOR Bytes and append to flag string
for i in hexBytes: flag.append(chr(i^0x55))

flag.append("}") # Close the flag string

# Flag is too long for screen, need to scroll it across
while not bool_exit:
    # Limit how much of the flag is shown on the screen
    for i in range(p0,p1):
        try: disp_flag += flag[i]
        except: disp_flag += " "
    fz.canvas_clear()                                  # Clear the display
    fz.canvas_set_text(15, 10, "picoCTF Vault Door 6") # Place the title
    fz.canvas_set_text(10, 20, disp_flag)              # Place the viewable flag text
    fz.canvas_update()                                 # Update the display
    disp_flag = ""                                     # Reset the flag var
    sleep(0.1)                                         # Short delay

# Run script on Flipper Zero
# qFlipper to drag and drop solution file into SD Card/apps_assets/upython/
# Start uPython tool, press ok button to open a file
# Find the solution file in the list and hit ok again to run it
# Apps > Tools > uPython > Open > Vault_6_Solve.py
```

## Flag
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919}

## Continue
[Continue](./picoGym0400.md)