# picoGym Level 271: Fresh Java
Source: https://play.picoctf.org/practice/challenge/271

## Goal
Can you get the flag?<br>
Reverse engineer this Java program.<br>
https://artifacts.picoctf.net/c/199/KeygenMe.class

## What I learned
```
Reverse Engineering

JADX: https://github.com/skylot/jadx
Java Decompiler: http://www.javadecompilers.com/ 
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ vi KeygenMe.java ⌨️
AsianHacker-picoctf@webshell:~$ cat KeygenMe.java ⌨️
import java.util.Scanner;

public class KeygenMe {
   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      System.out.println("Enter key:");
      String var2 = var1.nextLine();
      if (var2.length() != 34) {
         System.out.println("Invalid key");
      } else if (var2.charAt(33) != '}') {
         System.out.println("Invalid key");
      } else if (var2.charAt(32) != 'd') {
         System.out.println("Invalid key");
      } else if (var2.charAt(31) != '0') {
         System.out.println("Invalid key");
      } else if (var2.charAt(30) != 'a') {
         System.out.println("Invalid key");
      } else if (var2.charAt(29) != '1') {
         System.out.println("Invalid key");
      } else if (var2.charAt(28) != 'e') {
         System.out.println("Invalid key");
      } else if (var2.charAt(27) != 'f') {
         System.out.println("Invalid key");
      } else if (var2.charAt(26) != 'b') {
         System.out.println("Invalid key");
      } else if (var2.charAt(25) != '2') {
         System.out.println("Invalid key");
      } else if (var2.charAt(24) != '_') {
         System.out.println("Invalid key");
      } else if (var2.charAt(23) != 'd') {
         System.out.println("Invalid key");
      } else if (var2.charAt(22) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(21) != 'r') {
         System.out.println("Invalid key");
      } else if (var2.charAt(20) != '1') {
         System.out.println("Invalid key");
      } else if (var2.charAt(19) != 'u') {
         System.out.println("Invalid key");
      } else if (var2.charAt(18) != 'q') {
         System.out.println("Invalid key");
      } else if (var2.charAt(17) != '3') {
         System.out.println("Invalid key");
      } else if (var2.charAt(16) != 'r') {
         System.out.println("Invalid key");
      } else if (var2.charAt(15) != '_') {
         System.out.println("Invalid key");
      } else if (var2.charAt(14) != 'g') {
         System.out.println("Invalid key");
      } else if (var2.charAt(13) != 'n') {
         System.out.println("Invalid key");
      } else if (var2.charAt(12) != '1') {
         System.out.println("Invalid key");
      } else if (var2.charAt(11) != 'l') {
         System.out.println("Invalid key");
      } else if (var2.charAt(10) != '0') {
         System.out.println("Invalid key");
      } else if (var2.charAt(9) != '0') {
         System.out.println("Invalid key");
      } else if (var2.charAt(8) != '7') {
         System.out.println("Invalid key");
      } else if (var2.charAt(7) != '{') {
         System.out.println("Invalid key");
      } else if (var2.charAt(6) != 'F') {
         System.out.println("Invalid key");
      } else if (var2.charAt(5) != 'T') {
         System.out.println("Invalid key");
      } else if (var2.charAt(4) != 'C') {
         System.out.println("Invalid key");
      } else if (var2.charAt(3) != 'o') {
         System.out.println("Invalid key");
      } else if (var2.charAt(2) != 'c') {
         System.out.println("Invalid key");
      } else if (var2.charAt(1) != 'i') {
         System.out.println("Invalid key");
      } else if (var2.charAt(0) != 'p') {
         System.out.println("Invalid key");
      } else {
         System.out.println("Valid key");
      }
   }
}
AsianHacker-picoctf@webshell:~$ ls -la KeygenMe.java ⌨️
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 3314 Sep 30 00:08 KeygenMe.java
AsianHacker-picoctf@webshell:~$ chmod u+x KeygenMe.java ⌨️

Method 1: ChatGPT or NotePad++ w/ RE
AsianHacker-picoctf@webshell:~$ javac KeygenMe.java ⌨️
AsianHacker-picoctf@webshell:~$ java KeygenMe ⌨️
Enter key:
picoCTF{700l1ng_r3qu1r3d_2bfe1a0d} ⌨️🔐
Valid key
```

## Flag
picoCTF{700l1ng_r3qu1r3d_2bfe1a0d}

## Continue
[Continue](./picoGym0381.md)