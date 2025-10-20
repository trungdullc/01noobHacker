# Misc: The Flag Lottery

## Previous Flag
```
247CTF{38f5daf742a4b3d74b3a7575bf4d7d1e}
```

## Goal
Can you guess the secret number to win the lottery? The prize is a flag!

## What I learned
```
Incorrectly initialized random
secret.seed(int(time.time()))           # weakness
    time.time() returns the current UNIX timestamp — basically the number of seconds since 1970.

secret = random.Random() → Creates a new Random object
secret.seed(int(time.time())) → Seeds the PRNG with the current Unix timestamp, in seconds
winning_choice = str(secret.random()) → Generates a random number between 0 and 1

Note: The solution requires python 2. On python 3 precision of random differs a bit and won't produce the same results

Plan: 
    Locally figure estimate of UNIX timestamp give or take 3 sec
    Apply it w/ nc or telnet remotely
```

## Solution
```
DOWNLOAD CHALLENGE

AsianHacker-picoctf@webshell:~$ rz
AsianHacker-picoctf@webshell:~$ ls                                                
1e264d3cbd544dba7028b8afc881e8729048ff3f.zip  README.txt
AsianHacker-picoctf@webshell:~$ unzip 1e264d3cbd544dba7028b8afc881e8729048ff3f.zip 
Archive:  1e264d3cbd544dba7028b8afc881e8729048ff3f.zip
  inflating: the_flag_lottery.py     
AsianHacker-picoctf@webshell:~$ rm 1e264d3cbd544dba7028b8afc881e8729048ff3f.zip 
AsianHacker-picoctf@webshell:~$ cat the_flag_lottery.py 
import SocketServer, threading, random, time

class ThreadedLotteryServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class LotteryHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        secret = random.Random()
        secret.seed(int(time.time())) 
        winning_choice = str(secret.random())
        self.request.sendall("Can you guess the number to win the flag lottery?\n")
        your_choice = self.request.recv(1024).strip()
        if winning_choice == your_choice:
            self.request.sendall("Congratulations you won the lottery! Have a flag!\n")
            self.request.sendall("%s\n" % open('flag.txt').readline().rstrip())
        else:
            self.request.sendall("Nope! The winning number was %s, better luck next time!\n" % winning_choice)
        return

if __name__ == '__main__':
    SocketServer.TCPServer.allow_reuse_address = True
    server = ThreadedLotteryServer(("0.0.0.0", 5000), LotteryHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    server.serve_forever()

START CHALLENGE

AsianHacker-picoctf@webshell:~$ cat exploit.py 
#!/usr/bin/python3

import random
import time

# Approximate server time
current_time = int(time.time())

# Try a window of ±5 seconds (adjust if necessary)
for t in range(current_time - 3, current_time + 3):
    secret = random.Random()
    secret.seed(t)
    print(f"Time={t}, winning_choice={secret.random()}")

AsianHacker-picoctf@webshell:~$ ./exploit.py 
Time=1760162866, winning_choice=0.7957017519521817
Time=1760162867, winning_choice=0.8041981949616958
Time=1760162868, winning_choice=0.5949630613533147
Time=1760162869, winning_choice=0.5632611386732354
Time=1760162870, winning_choice=0.3800409216148698
Time=1760162871, winning_choice=0.7545289978375337
AsianHacker-picoctf@webshell:~$ nc c1662b52335f382b.247ctf.com 50484
0.7545289978375337
0.3800409216148698
0.5632611386732354
0.5949630613533147
0.8041981949616958
0.7957017519521817

Not Work
```

## Flag


## Continue
[Continue](../247ctf/MiscTheFlagLottery.md)