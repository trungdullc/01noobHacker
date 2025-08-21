# picoGym Level 0378: Specialer
Source: https://play.picoctf.org/practice/challenge/378

## Goal
Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we <b>took out spell checker</b> because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.<br>
ssh -p 64868 ctf-player@saturn.picoctf.net<br>
The password is <b>483e80d4</b>

## What I learned
```
tab + tab is life saver
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ ssh -p 64868 ctf-player@saturn.picoctf.net ⌨️
The authenticity of host '[saturn.picoctf.net]:64868 ([13.59.203.175]:64868)' can't be established.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes ⌨️
Warning: Permanently added '[saturn.picoctf.net]:64868' (ED25519) to the list of known hosts.
ctf-player@saturn.picoctf.net's password: ⌨️
Specialer$ ls ⌨️
-bash: ls: command not found
Specialer$ ! ls ⌨️
-bash: ls: command not found
Specialer$ ((ls)) ⌨️
Specialer$ find . ⌨️
-bash: find: command not found
Specialer$ clear & find . ⌨️
[1] 36
-bash: clear: command not found
-bash: find: command not found
[1]+  Exit 127                clear 
Specialer$ clear & find .; ⌨️
[1] 38
-bash: clear: command not found
-bash: find: command not found
[1]+  Exit 127                clear
Specialer$ ((! /bin/*)) ⌨️
-bash: ((: ! /bin/*: syntax error: operand expected (error token is "/bin/*")
Specialer$ ((/bin/*)) ⌨️
-bash: ((: /bin/*: syntax error: operand expected (error token is "/bin/*")

# Tab (2x) to see all commands in /bin ❤️❤️❤️❤️❤️
Specialer$ ⌨️                                                    # ⌨️ Tab (2x)
!          [[         bg         caller     compgen    coproc     do         else       exec       fc         function   history    kill       mapfile    pwd        return     shopt      then       true       umask      wait
./         ]]         bind       case       complete   declare    done       enable     exit       fg         getopts    if         let        popd       read       select     source     time       type       unalias    while
:          alias      break      cd         compopt    dirs       echo       esac       export     fi         hash       in         local      printf     readarray  set        suspend    times      typeset    unset      {
[          bash       builtin    command    continue   disown     elif       eval       false      for        help       jobs       logout     pushd      readonly   shift      test       trap       ulimit     until      }
Specialer$ cd ⌨️                                                 # ⌨️ Tab (2x)
.hushlogin  .profile    abra/       ala/        sim/ 
Specialer$ cat abra/cada ⌨️                                      # ⌨️ Tab (2x)
cadabra.txt   cadaniel.txt
Specialer$ cat abra/cadabra.txt ⌨️ 
-bash: cat: command not found
Specialer$ echo $(abra/cadabra.txt) ⌨️ 
-bash: abra/cadabra.txt: Permission denied

Specialer$ echo $(<abra/cadabra.txt) ⌨️ 
Nothing up my sleeve!
Specialer$ echo $(<abra/cadaniel.txt) ⌨️ 
Yes, I did it! I really did it! I'm a true wizard!
Specialer$ pwd ⌨️ 
/home/ctf-player
Specialer$ cd ala/ ⌨️                                            # ⌨️ Tab (2x)
kazam.txt  mode.txt   
Specialer$ echo $(<ala/kazam.txt) ⌨️
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_d5ef8b71} 🔐
```

## Flag
picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_d5ef8b71}

## Continue
[Continue](./picoGym0251.md)