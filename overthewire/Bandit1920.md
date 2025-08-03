# Bandit Level 19 → Level 20 Suid and linux permissions

## Previous Flag
<b>0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO</b>

## Goal
Use previous password to log in SSH with user <b>bandit20</b> on port <b>2220</b>.  There is a <b>setuid binary in the home directory</b> that does the following: it makes a connection to localhost on the <b>port you specify as a commandline argument</b>. It then reads a line of text from the connection and <b>compares it to the password in the previous level (bandit20)</b>. If the password is correct, it will <b>transmit password for next level (bandit21)</b>.

NOTE: Try connecting to your own network daemon to see if it works as you think

## What I learned
```
nc (netcat) can mimic servers
tmux
Horizontally: ctrl+b then "         Vertically: ctrl+b then %
Navigate: ctrl+b then ← / →
Close Panel: ctrl+d or exit
suconnect is a binary executable (c/c++ program) that contains next password
nc -lnvp 8080
  -l: listen mode
  -n: don’t resolve DNS (faster)
  -v: verbose
  -p 8080: listen on port 8080
```

## Side Quest
```
# server.py that mimics nc
import socket

PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("127.0.0.1", PORT))
    server.listen(1)
    print(f"Listening on port {PORT}...")
    conn, addr = server.accept()
    
    with conn:
        print("Connected by", addr)
        
        # Step 1: Read Bandit20 password
        data = conn.recv(1024).decode().strip()
        print(f"Received: {data}")
        
        # Step 2: Send same password back
        conn.sendall((data + "\n").encode())

        # Step 3: Wait for suconnect to send Bandit21 password
        response = conn.recv(1024).decode().strip()
        print(f"Bandit21 password: {response}")

bandit20@bandit:~$ ./suconnect 8080   # Do 2nd      │ bandit20@bandit:~$ python3 server.py # Do 1st

#!/bin/bash
# suconnect.sh
PORT=8080
CORRECT_PASS="0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO"
NEXT_PASS="EeoULMCra2q0dSkYj561DX7s1CpBuOBt"

# Use exec to reuse same connection for in/out
while true; do
  echo "[*] Waiting on $PORT..."
  nc -lnp $PORT | {
    read INPUT
    echo "[>] Got: $INPUT" >&2
    if [[ "$INPUT" == "$CORRECT_PASS" ]]; then
      echo "[+] Valid password. Sending Bandit21 password..." >&2
      echo "$NEXT_PASS"
    else
      echo "Wrong!"
    fi
  }
done

chmod +x suconnect.sh
./suconnect 8080                                  | ./suconnect.sh

// suconnect.cpp
// Program that acts more like overthewire with dummy server and suconnect listening for response
#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: ./suconnect <port>" << std::endl;
        return 1;
    }

    int port = std::stoi(argv[1]);
    const char* password = "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO";  // Bandit20 password

    // 1. Create socket
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        perror("socket");
        return 1;
    }

    // 2. Server address
    sockaddr_in server{};
    server.sin_family = AF_INET;
    server.sin_port = htons(port);
    inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

    // 3. Connect
    if (connect(sock, (sockaddr*)&server, sizeof(server)) < 0) {
        perror("connect");
        close(sock);
        return 1;
    }

    // 4. Send the password
    send(sock, password, strlen(password), 0);

    // 5. Read response
    char buffer[1024] = {0};
    ssize_t bytes = recv(sock, buffer, sizeof(buffer) - 1, 0);
    if (bytes < 0) {
        perror("recv");
        close(sock);
        return 1;
    }

    buffer[bytes] = '\0';  // Null-terminate
    std::cout << "Read: " << buffer << std::endl;

    // 6. Compare
    if (strcmp(buffer, password) == 0) {
        std::cout << "Password matches, sending next password" << std::endl;
        std::cout << "EeoULMCra2q0dSkYj561DX7s1CpBuOBt" << std::endl;
    } else {
        std::cout << "Wrong! Please enter the correct current password." << std::endl;
    }

    close(sock);
    return 0;
}

g++ suconnect.cpp -o suconnect
./suconnect 8080                                    | nc -lnvp 8080
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit20@bandit.labs.overthewire.org -p 2220 ⌨️
bandit20@bandit:~$ ls -lah suconnect ⌨️
-rwsr-x--- 1 bandit21 bandit20 16K Jul 28 19:03 suconnect
bandit20@bandit:~$ whatis ssh nc cat bash screen tmux ⌨️
ssh (1)              - OpenSSH remote login client
nc (1)               - arbitrary TCP and UDP connections and listens
cat (1)              - concatenate files and print on the standard output
bash (1)             - GNU Bourne-Again SHell
screen (1)           - screen manager with VT100/ANSI terminal emulation
tmux (1)             - terminal multiplexer
bandit20@bandit:~$ tmux ⌨️

bandit20@bandit:~$ ./suconnect 8080 ⌨️   # Do 2nd   │bandit20@bandit:~$ nc -lnvp 8080 ⌨️ # Do 1st
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO              │Listening on 0.0.0.0 8080
Password matches, sending next password             │Connection received on 127.0.0.1 37322
bandit20@bandit:~$                                  │0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO ⌨️  # Do 3rd
                                                    │EeoULMCra2q0dSkYj561DX7s1CpBuOBt 🔐
                                                    │bandit20@bandit:~$ exit ⌨️

bandit20@bandit:~$ echo -n '0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO' | nc -l -p 8080 & ⌨️
[1] 718506
bandit20@bandit:~$ id ⌨️
uid=11020(bandit20) gid=11020(bandit20) groups=11020(bandit20)
[1]+  Done                    echo -n '0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO' | nc -l -p 8080
bandit20@bandit:~$ ps aux ⌨️
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
bandit20  617776  0.0  0.1   9068  5760 pts/7    Ss   21:23   0:00 -bash
bandit20  785242  0.0  0.1  10884  4480 pts/7    R+   21:26   0:00 ps aux
bandit20 1754240  0.0  0.1  13280  4896 ?        Ss   14:16   0:00 tmux
bandit20 1754241  0.0  0.1   8772  5376 pts/35   Ss   14:16   0:00 -bash
bandit20 1754329  0.0  0.1   8772  5376 pts/60   Ss   14:16   0:00 -bash
bandit20 1762783  0.0  0.0   3436  1792 pts/35   S+   14:19   0:00 nc -l 30020
bandit20 2521237  0.0  0.1   9292  4992 ?        Ss   Jul31   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --
bandit20 2530870  0.0  0.0      0     0 ?        Zs   20:46   0:00 [bash] <defunct>
bandit20@bandit:~$ ./suconnect 8080 ⌨️               # Note: Forgot -l so need do right away
Could not connect
bandit20@bandit:~$ echo -n '0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO' | nc -l -p 8080 & ⌨️
[1] 918058
bandit20@bandit:~$ ./suconnect 8080 ⌨️
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
EeoULMCra2q0dSkYj561DX7s1CpBuOBt 🔐
[1]+  Done                    echo -n '0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO' | nc -l -p 8080
```

## Flag
<b>EeoULMCra2q0dSkYj561DX7s1CpBuOBt</b>

## Continue
[Continue](/overthewire/Bandit2021.md)