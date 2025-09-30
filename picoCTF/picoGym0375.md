# picoGym Level 375: Safe Opener 2
Source: https://play.picoctf.org/practice/challenge/375

## Goal
What can you do with this file?<br>
I forgot the key to my safe but this file is supposed to help me with retrieving the lost key.<br>
https://artifacts.picoctf.net/c/291/SafeOpener.class<br>
Can you help me unlock my safe?

## What I learned
```
Reverse Engineering

strings
    -t x        print offset of each found string, in hexadecimal (x)

xxd -s 0x31d -l 64 SafeOpener.class
    -s 0x31d → start at offset 0x31d
    -l 64 → show 64 bytes from there

hexdump -C -s 0x31d -n 64 SafeOpener.class
    -C → nice canonical hex + ASCII view.
    -s → skip bytes before the offset.
    -n → number of bytes to display.

Java Decompiler:
    jadx (gui): https://github.com/skylot/jadx ⭐⭐⭐⭐⭐
        defpackage > SafeOpener
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/291/SafeOpener.class ⌨️
--2025-09-26 21:08:15--  https://artifacts.picoctf.net/c/291/SafeOpener.class
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2036 (2.0K) [application/octet-stream]
Saving to: 'SafeOpener.class'

SafeOpener.class                                           100%[======================================================================================================================================>]   1.99K  --.-KB/s    in 0s      

2025-09-26 21:08:15 (1.75 GB/s) - 'SafeOpener.class' saved [2036/2036]

AsianHacker-picoctf@webshell:~$ file SafeOpener.class ⌨️
SafeOpener.class: compiled Java class data, version 52.0 (Java 1.8)
AsianHacker-picoctf@webshell:~$ cat SafeOpener.class ⌨️
4
CDE     FG
H
I
JL      FN
OP
Q
RS
.T
OU
VW
X
Y
[
]
R`ab<init>()VCodeLineNumberTableLocalVariableTablethis
                                                      LSafeOpener;main([Ljava/lang/String;)VisOpenZargs[Ljava/lang/StringkeyboardLjava/io/BufferedReader;encodercEncoder
                                                                                                                                                                        InnerClassesLjava/util/Base64$Encoder;
StackMapTable*Dcdang/String;keyiI
ExceptionsopenSafe(Ljava/lang/String;)password
SourceFileSafeOpener.java
                         java/io/BufferedReaderjava/io/InputStreamReaderf
                                                                         gh
                                                                           i
                                                                            jk
                                                                              lm
                                                                                noEnter password for the safe: p
                                                                                                                qr
                                                                                                                  std
                                                                                                                     uv
                                                                                                                       wx
                                                                                                                         yr
                                                                                                                           >?java/lang/StringBuilder
You have  
          z{
            z| attempt(s) left
                              }t,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_198203f7} 🔐
                                                                             ~
                                                                              Sesame openPassword is incorrect

SafeOpenerjava/lang/Objectjava/util/Base64$Encoderjava/lang/Stringjava/io/IOExceptionjava/lang/SysteminLjava/io/InputStream;(Ljava/io/InputStream;)V(Ljava/io/Reader;)Vjava/util/Base64
getEncoder()Ljava/util/Base64$Encoder;outLjava/io/PrintStream;java/io/PrintStreamprint(Ljava/lang/String;)readLine()Ljava/lang/StringgetBytes()[BencodeToString([B)Ljava/lang/String;printlnappend-(Ljava/lang/String;)Ljava/lang/StringBuilder;(I)Ljava/lang/StringBuildertoStringequals(Ljava/lang/Object;)Z! /*!"
                                                                          #$    %& <xYYL:6T

+
&.4>EKPqtw"HK,'(!)*f+,b-1_23[43 X567 89:;;V<=   >? uL*+
                 "#&'"@323;AB0
.J/   

AsianHacker-picoctf@webshell:~$ strings -t x SafeOpener.class | grep picoCTF ⌨️
    31d ,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_198203f7} 🔐

# Optional:
AsianHacker-picoctf@webshell:~$ xxd -s 0x31d -l 64 SafeOpener.class ⌨️
0000031d: 2c70 6963 6f43 5446 7b53 4166 335f 3070  ,picoCTF{SAf3_0p
0000032d: 336e 3372 725f 7930 755f 736f 6c76 3364  3n3rr_y0u_solv3d
0000033d: 5f69 745f 3139 3832 3033 6637 7d0c 007e  _it_198203f7}..~ 🔐
0000034d: 007f 0100 0b53 6573 616d 6520 6f70 656e  .....Sesame open

AsianHacker-picoctf@webshell:~$ hexdump -C -s 0x31d -n 64 SafeOpener.class ⌨️
0000031d  2c 70 69 63 6f 43 54 46  7b 53 41 66 33 5f 30 70  |,picoCTF{SAf3_0p|
0000032d  33 6e 33 72 72 5f 79 30  75 5f 73 6f 6c 76 33 64  |3n3rr_y0u_solv3d|
0000033d  5f 69 74 5f 31 39 38 32  30 33 66 37 7d 0c 00 7e  |_it_198203f7}..~| 🔐
0000034d  00 7f 01 00 0b 53 65 73  61 6d 65 20 6f 70 65 6e  |.....Sesame open|
0000035d
```

## Flag
picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_198203f7}

## Continue
[Continue](./picoGym0313.md)