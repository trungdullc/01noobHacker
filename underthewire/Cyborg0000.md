# Cyborg Level 0 SSH Login w/ ssh or PSRemoting

## Previous Flag
```
N/A
```

## Goal
Obtain initial credentials via #StartHere channel on [Slack](https://communityinviter.com/apps/underthewire/under-the-wire). Once you are in the channel, scroll to top to see credentials.<br>
Password: cyborg1 ❤️<br><br>

Be able to log onto UnderTheWire SSH server: cyborg.underthewire.tech. Given port <b>22</b>.  Password stored <br>
You have successfully connected to game server when your path changes to PS C:\Users\Cyborg1\desktop>

## What I learned
```
ssh cyborg1@cyborg.underthewire.tech -p 22

Microsoft Learn Documentation: https://learn.microsoft.com/en-us/docs/ ⭐⭐⭐⭐⭐
```

## Side Quest: joining SLACK
```
hello,
you have to connect to the server with SSH (use putty or mobaxterm for example):
host : century.underthewire.tech
port : 22
For the credentials they are at the top of this chat
Username                  Password
---------                 ---------
century1                  century1
cyborg1                   cyborg1 🔐
groot1                    groot1
oracle1                   oracle1
trebek1                   trebek1
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg1@cyborg.underthewire.tech -p 22 ⌨️
The authenticity of host 'cyborg.underthewire.tech (192.99.167.156)' can't be established.
This host key is known by the following other names/addresses:
    C:\Users\trung.DESKTOP-G7C81CH/.ssh/known_hosts:11: century.underthewire.tech
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added 'cyborg.underthewire.tech' (ECDSA) to the list of known hosts.
cyborg1@cyborg.underthewire.tech's password: ⌨️ cyborg1

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg1\desktop> whoami ⌨️
underthewire\cyborg1
```

## Flag
cyborg1

## Continue
[Continue](./Cyborg0001.md)