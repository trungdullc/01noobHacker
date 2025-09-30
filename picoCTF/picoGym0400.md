# picoGym Level 400: Picker I
Source: https://play.picoctf.org/practice/challenge/400

## Goal
This service can provide you with a random number, but can it do anything else?<br>
Connect to the program with netcat:<br>
nc saturn.picoctf.net 49267 <br>
The program's source code can be downloaded here.<br>
https://artifacts.picoctf.net/c/514/picker-I.py

## What I learned
```
Reverse Engineering
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/514/picker-I.py ⌨️
--2025-09-26 03:29:47--  https://artifacts.picoctf.net/c/514/picker-I.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3429 (3.3K) [application/octet-stream]
Saving to: 'picker-I.py'

picker-I.py                                                100%[======================================================================================================================================>]   3.35K  --.-KB/s    in 0s      

2025-09-26 03:29:47 (2.53 GB/s) - 'picker-I.py' saved [3429/3429]

AsianHacker-picoctf@webshell:~$ cat picker-I.py ⌨️
import sys

def getRandomNumber(): 
  print(4)  # Chosen by fair die roll 👀
            # Guaranteed to be random
            # (See XKCD)

def exit():
  sys.exit(0) 👀
  
def esoteric1():
  esoteric = \
  '''
  int query_apm_bios(void)
{
        struct biosregs ireg, oreg;

        /* APM BIOS installation check */
        initregs(&ireg);
        ireg.ah = 0x53;
        intcall(0x15, &ireg, &oreg);

        if (oreg.flags & X86_EFLAGS_CF)
                return -1;              /* No APM BIOS */

        if (oreg.bx != 0x504d)          /* "PM" signature */
                return -1;

        if (!(oreg.cx & 0x02))          /* 32 bits supported? */
                return -1;

        /* Disconnect first, just in case */
        ireg.al = 0x04;
        intcall(0x15, &ireg, NULL);

        /* 32-bit connect */
        ireg.al = 0x03;
        intcall(0x15, &ireg, &oreg);

        boot_params.apm_bios_info.cseg        = oreg.ax;
        boot_params.apm_bios_info.offset      = oreg.ebx;
        boot_params.apm_bios_info.cseg_16     = oreg.cx;
        boot_params.apm_bios_info.dseg        = oreg.dx;
        boot_params.apm_bios_info.cseg_len    = oreg.si;
        boot_params.apm_bios_info.cseg_16_len = oreg.hsi;
        boot_params.apm_bios_info.dseg_len    = oreg.di;

        if (oreg.flags & X86_EFLAGS_CF)
                return -1;

        /* Redo the installation check as the 32-bit connect;
           some BIOSes return different flags this way... */

        ireg.al = 0x00;
        intcall(0x15, &ireg, &oreg);

        if ((oreg.eflags & X86_EFLAGS_CF) || oreg.bx != 0x504d) {
                /* Failure with 32-bit connect, try to disconnect and ignore */
                ireg.al = 0x04;
                intcall(0x15, &ireg, NULL);
                return -1;
        }

        boot_params.apm_bios_info.version = oreg.ax;
        boot_params.apm_bios_info.flags   = oreg.cx;
        return 0;
}
  '''
  print(esoteric)

def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag) 👀❤️
    
def esoteric2():
  esoteric = \
  '''
#include "boot.h"

#define MAX_8042_LOOPS  100000
#define MAX_8042_FF     32

static int empty_8042(void)
{
        u8 status;
        int loops = MAX_8042_LOOPS;
        int ffs   = MAX_8042_FF;

        while (loops--) {
                io_delay();

                status = inb(0x64);
                if (status == 0xff) {
                        /* FF is a plausible, but very unlikely status */
                        if (!--ffs)
                                return -1; /* Assume no KBC present */
                }
                if (status & 1) {
                        /* Read and discard input data */
                        io_delay();
                        (void)inb(0x60);
                } else if (!(status & 2)) {
                        /* Buffers empty, finished! */
                        return 0;
                }
        }

        return -1;
}

/* Returns nonzero if the A20 line is enabled.  The memory address
   used as a test is the int $0x80 vector, which should be safe. */

#define A20_TEST_ADDR   (4*0x80)
#define A20_TEST_SHORT  32
#define A20_TEST_LONG   2097152 /* 2^21 */

static int a20_test(int loops)
{
        int ok = 0;
        int saved, ctr;

        set_fs(0x0000);
        set_gs(0xffff);

        saved = ctr = rdfs32(A20_TEST_ADDR);

        while (loops--) {
                wrfs32(++ctr, A20_TEST_ADDR);
                io_delay();     /* Serialize and make delay constant */
                ok = rdgs32(A20_TEST_ADDR+0x10) ^ ctr;
                if (ok)
                        break;
        }

        wrfs32(saved, A20_TEST_ADDR);
        return ok;
}

/* Quick test to see if A20 is already enabled */
static int a20_test_short(void)
{
        return a20_test(A20_TEST_SHORT);
}
  '''
  print(esoteric)

while(True):
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()') 👀
  except Exception as e:
    print(e)
    break

AsianHacker-picoctf@webshell:~$ nc saturn.picoctf.net 49267
Try entering "getRandomNumber" without the double quotes...
==> getRandomNumber ⌨️
4
Try entering "getRandomNumber" without the double quotes...
==> win ⌨️
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x36 0x65 0x30 0x34 0x34 0x34 0x30 0x64 0x7d 
Try entering "getRandomNumber" without the double quotes...
==> exit ⌨️

# Decode
https://cyberchef.io/#recipe=From_Hex('Auto')&input=MHg3MCAweDY5IDB4NjMgMHg2ZiAweDQzIDB4NTQgMHg0NiAweDdiIDB4MzQgMHg1ZiAweDY0IDB4MzEgMHgzNCAweDZkIDB4MzAgMHg2ZSAweDY0IDB4NWYgMHgzMSAweDZlIDB4NWYgMHgzNyAweDY4IDB4MzMgMHg1ZiAweDcyIDB4MzAgMHg3NSAweDY3IDB4NjggMHg1ZiAweDM2IDB4NjUgMHgzMCAweDM0IDB4MzQgMHgzNCAweDMwIDB4NjQgMHg3ZCA

AsianHacker-picoctf@webshell:~$ printf '\x70\x69\x63\x6f\x43\x54\x46\x7b\x34\x5f\x64\x31\x34\x6d\x30\x6e\x64\x5f\x31\x6e\x5f\x37\x68\x33\x5f\x72\x30\x75\x67\x68\x5f\x36\x65\x30\x34\x34\x34\x30\x64\x7d\n' ⌨️
picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d} 🔐
AsianHacker-picoctf@webshell:~$ echo 70 69 63 6f 43 54 46 7b 34 5f 64 31 34 6d 30 6e 64 5f 31 6e 5f 37 68 33 5f 72 30 75 67 68 5f 36 65 30 34 34 34 30 64 7d | xxd -r -p ⌨️
picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d} 🔐
AsianHacker-picoctf@webshell:~$ python3 -c "print(bytes.fromhex('70 69 63 6f 43 54 46 7b 34 5f 64 31 34 6d 30 6e 64 5f 31 6e 5f 37 68 33 5f 72 30 75 67 68 5f 36 65 30 34 34 34 30 64 7d').decode())" ⌨️
picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d} 🔐

AsianHacker-picoctf@webshell:~$ python3 ⌨️
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> output = "0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x36 0x65 0x30 0x34 0x34 0x34 0x30 0x64 0x7d" ⌨️
>>> print("".join([chr(int(o, 16)) for o in output.split()])) ⌨️
picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d} 🔐
```

## Flag
picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d}

## Continue
[Continue](./picoGym0401.md)