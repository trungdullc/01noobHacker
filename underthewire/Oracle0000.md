# Oracle Level 0 SSH Login w/ ssh or PSRemoting

## Previous Flag
```
N/A
```

## Goal
Obtain initial credentials via #StartHere channel on [Slack](https://communityinviter.com/apps/underthewire/under-the-wire). Once you are in the channel, scroll to top to see credentials.<br>
Password: oracle1 ❤️<br><br>

Be able to log onto UnderTheWire SSH server: oracle.underthewire.tech. Given port <b>22</b>.  Password stored <br>
You have successfully connected to game server when your path changes to PS C:\Users\Oracle1\desktop>

## What I learned
```
ssh oracle1@groot.underthewire.tech -p 22

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
cyborg1                   cyborg1
groot1                    groot1
oracle1                   oracle1 🔐
trebek1                   trebek1
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle1@groot.underthewire.tech -p 22 ⌨️
oracle1@groot.underthewire.tech's password: ⌨️ oracle1

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle1\desktop> whoami ⌨️
underthewire\oracle1
```

## Flag
oracle1

## Continue
[Continue](./Oracle0001.md)