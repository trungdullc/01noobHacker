# picoGym Level 51: WhitePages
Source: https://play.picoctf.org/practice/challenge/51

## Goal
I stopped using YellowPages and moved onto WhitePages...<br>
but the page they gave me is all blank!<br>
https://jupiter.challenges.picoctf.org/static/fa4a277cfa846e07a5981d8a19288a2e/whitepages.txt

## What I learned
```
standard space (0x20)
Unicode EM SPACE (U+2003 / 0xE2 0x80 0x83)

https://en.wikipedia.org/wiki/Whitespace_character
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/fa4a277cfa846e07a5981d8a19288a2e/whitepages.txt
--2025-09-16 23:16:32--  https://jupiter.challenges.picoctf.org/static/fa4a277cfa846e07a5981d8a19288a2e/whitepages.txt
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2982 (2.9K) [application/octet-stream]
Saving to: 'whitepages.txt'

whitepages.txt                                     100%[=============================================================================================================>]   2.91K  --.-KB/s    in 0s      

2025-09-16 23:16:32 (886 MB/s) - 'whitepages.txt' saved [2982/2982]

AsianHacker-picoctf@webshell:~$ file whitepages.txt ⌨️
whitepages.txt: Unicode text, UTF-8 text, with very long lines (1376), with no line terminators
AsianHacker-picoctf@webshell:~$ binwalk whitepages.txt ⌨️ 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

AsianHacker-picoctf@webshell:~$ exiftool whitepages.txt ⌨️
ExifTool Version Number         : 12.40
File Name                       : whitepages.txt
Directory                       : .
File Size                       : 2.9 KiB
File Modification Date/Time     : 2020:10:26 18:39:56+00:00
File Access Date/Time           : 2025:09:16 23:16:35+00:00
File Inode Change Date/Time     : 2025:09:16 23:16:32+00:00
File Permissions                : -rw-rw-r--
File Type                       : TXT
File Type Extension             : txt
MIME Type                       : text/plain
MIME Encoding                   : utf-8
Byte Order Mark                 : No
Newlines                        : (none)
Line Count                      : 1
Word Count                      : 361

AsianHacker-picoctf@webshell:~$ cat whitepages.txt ⌨️
AsianHacker-picoctf@webshell:~$ strings whitepages.txt ⌨️
AsianHacker-picoctf@webshell:~$ xxd whitepages.txt ⌨️
00000000: e280 83e2 8083 e280 83e2 8083 20e2 8083  ............ ...
00000010: 20e2 8083 e280 83e2 8083 e280 83e2 8083   ...............
00000020: 20e2 8083 e280 8320 e280 83e2 8083 e280   ...... ........
00000030: 83e2 8083 20e2 8083 e280 8320 e280 8320  .... ...... ... 
00000040: 2020 e280 83e2 8083 e280 83e2 8083 e280    ..............
00000050: 8320 20e2 8083 20e2 8083 e280 8320 e280  .  ... ...... ..
00000060: 8320 20e2 8083 e280 83e2 8083 2020 e280  .  .........  ..
00000070: 8320 20e2 8083 2020 2020 e280 8320 e280  .  ...    ... ..
00000080: 83e2 8083 e280 83e2 8083 2020 e280 8320  ..........  ... 
00000090: e280 8320 e280 8320 e280 83e2 8083 e280  ... ... ........
000000a0: 8320 e280 83e2 8083 e280 8320 20e2 8083  . .........  ...
000000b0: e280 83e2 8083 e280 83e2 8083 20e2 8083  ............ ...
000000c0: 20e2 8083 e280 83e2 8083 e280 83e2 8083   ...............
000000d0: 20e2 8083 20e2 8083 e280 83e2 8083 e280   ... ...........
000000e0: 83e2 8083 20e2 8083 e280 8320 e280 83e2  .... ...... ....
000000f0: 8083 e280 83e2 8083 20e2 8083 e280 8320  ........ ...... 
00000100: e280 8320 e280 8320 e280 83e2 8083 2020  ... ... ......  
00000110: e280 8320 e280 83e2 8083 e280 8320 e280  ... ......... ..
00000120: 8320 e280 8320 e280 83e2 8083 e280 8320  . ... ......... 
00000130: e280 8320 e280 83e2 8083 20e2 8083 e280  ... ...... .....
00000140: 83e2 8083 e280 83e2 8083 e280 8320 e280  ............. ..
00000150: 8320 e280 83e2 8083 e280 83e2 8083 e280  . ..............
00000160: 8320 e280 8320 e280 8320 e280 8320 e280  . ... ... ... ..
00000170: 8320 e280 83e2 8083 e280 83e2 8083 20e2  . ............ .
00000180: 8083 e280 8320 e280 83e2 8083 2020 e280  ..... ......  ..
00000190: 83e2 8083 e280 8320 e280 83e2 8083 20e2  ....... ...... .
000001a0: 8083 e280 8320 e280 8320 e280 83e2 8083  ..... ... ......
000001b0: e280 83e2 8083 2020 e280 83e2 8083 20e2  ......  ...... .
000001c0: 8083 e280 83e2 8083 e280 83e2 8083 e280  ................
000001d0: 8320 e280 8320 e280 83e2 8083 20e2 8083  . ... ...... ...
000001e0: e280 8320 e280 83e2 8083 e280 8320 e280  ... ......... ..
000001f0: 8320 e280 8320 e280 83e2 8083 e280 83e2  . ... ..........
00000200: 8083 2020 e280 8320 e280 83e2 8083 2020  ..  ... ......  
00000210: 2020 e280 8320 e280 8320 e280 83e2 8083    ... ... ......
00000220: 20e2 8083 e280 8320 e280 83e2 8083 e280   ...... ........
00000230: 8320 e280 83e2 8083 e280 8320 e280 8320  . ......... ... 
00000240: e280 83e2 8083 2020 e280 83e2 8083 20e2  ......  ...... .
00000250: 8083 e280 83e2 8083 e280 83e2 8083 e280  ................
00000260: 83e2 8083 20e2 8083 e280 8320 20e2 8083  .... ......  ...
00000270: e280 83e2 8083 20e2 8083 e280 83e2 8083  ...... .........
00000280: e280 83e2 8083 e280 8320 e280 83e2 8083  ......... ......
00000290: e280 83e2 8083 20e2 8083 e280 8320 e280  ...... ...... ..
000002a0: 83e2 8083 e280 83e2 8083 e280 8320 e280  ............. ..
000002b0: 8320 e280 83e2 8083 e280 83e2 8083 2020  . ............  
000002c0: e280 8320 e280 83e2 8083 20e2 8083 2020  ... ...... ...  
000002d0: e280 8320 e280 83e2 8083 e280 8320 2020  ... .........   
000002e0: e280 8320 e280 8320 e280 83e2 8083 20e2  ... ... ...... .
000002f0: 8083 e280 8320 e280 83e2 8083 2020 2020  ..... ......    
00000300: e280 8320 e280 8320 e280 8320 e280 8320  ... ... ... ... 
00000310: e280 8320 e280 83e2 8083 2020 20e2 8083  ... ......   ...
00000320: e280 8320 e280 83e2 8083 e280 8320 e280  ... ......... ..
00000330: 83e2 8083 e280 83e2 8083 20e2 8083 e280  .......... .....
00000340: 83e2 8083 e280 83e2 8083 e280 8320 e280  ............. ..
00000350: 8320 e280 83e2 8083 20e2 8083 e280 8320  . ...... ...... 
00000360: e280 83e2 8083 e280 8320 e280 8320 e280  ......... ... ..
00000370: 8320 e280 8320 e280 83e2 8083 e280 83e2  . ... ..........
00000380: 8083 e280 8320 e280 83e2 8083 2020 2020  ..... ......    
00000390: e280 8320 e280 8320 e280 83e2 8083 20e2  ... ... ...... .
000003a0: 8083 e280 8320 e280 8320 e280 8320 e280  ..... ... ... ..
000003b0: 83e2 8083 e280 83e2 8083 e280 83e2 8083  ................
000003c0: 20e2 8083 20e2 8083 e280 83e2 8083 e280   ... ...........
000003d0: 83e2 8083 20e2 8083 e280 8320 e280 83e2  .... ...... ....
000003e0: 8083 e280 83e2 8083 20e2 8083 e280 8320  ........ ...... 
000003f0: e280 83e2 8083 2020 e280 8320 e280 8320  ......  ... ... 
00000400: e280 83e2 8083 2020 e280 83e2 8083 e280  ......  ........
00000410: 83e2 8083 e280 83e2 8083 2020 e280 83e2  ..........  ....
00000420: 8083 e280 83e2 8083 e280 83e2 8083 2020  ..............  
00000430: e280 83e2 8083 e280 83e2 8083 e280 83e2  ................
00000440: 8083 20e2 8083 e280 83e2 8083 e280 83e2  .. .............
00000450: 8083 e280 8320 e280 83e2 8083 e280 8320  ..... ......... 
00000460: 20e2 8083 e280 8320 20e2 8083 2020 2020   ......  ...    
00000470: e280 8320 2020 e280 83e2 8083 20e2 8083  ...   ...... ...
00000480: e280 8320 20e2 8083 e280 83e2 8083 20e2  ...  ......... .
00000490: 8083 e280 8320 20e2 8083 e280 8320 e280  .....  ...... ..
000004a0: 8320 e280 8320 2020 e280 83e2 8083 2020  . ...   ......  
000004b0: e280 83e2 8083 20e2 8083 e280 83e2 8083  ...... .........
000004c0: e280 83e2 8083 e280 8320 e280 83e2 8083  ......... ......
000004d0: e280 83e2 8083 e280 8320 e280 8320 2020  ......... ...   
000004e0: e280 8320 20e2 8083 e280 8320 20e2 8083  ...  ......  ...
000004f0: e280 8320 e280 8320 e280 83e2 8083 20e2  ... ... ...... .
00000500: 8083 2020 e280 83e2 8083 e280 83e2 8083  ..  ............
00000510: 20e2 8083 e280 83e2 8083 e280 83e2 8083   ...............
00000520: e280 8320 e280 8320 e280 83e2 8083 e280  ... ... ........
00000530: 83e2 8083 e280 8320 20e2 8083 20e2 8083  .......  ... ...
00000540: e280 8320 e280 8320 2020 e280 8320 e280  ... ...   ... ..
00000550: 83e2 8083 e280 8320 2020 e280 8320 e280  .......   ... ..
00000560: 83e2 8083 e280 8320 2020 e280 83e2 8083  .......   ......
00000570: 2020 e280 8320 20e2 8083 e280 83e2 8083    ...  .........
00000580: 20e2 8083 e280 8320 2020 e280 8320 e280   ......   ... ..
00000590: 8320 e280 8320 2020 e280 83e2 8083 20e2  . ...   ...... .
000005a0: 8083 e280 8320 20e2 8083 e280 8320 2020  .....  ......   
000005b0: e280 8320 20e2 8083 20e2 8083 e280 83e2  ...  ... .......
000005c0: 8083 e280 83e2 8083 20e2 8083 2020 e280  ........ ...  ..
000005d0: 83e2 8083 e280 83e2 8083 20e2 8083 e280  .......... .....
000005e0: 83e2 8083 e280 83e2 8083 e280 8320 e280  ............. ..
000005f0: 8320 e280 83e2 8083 e280 83e2 8083 e280  . ..............
00000600: 8320 e280 83e2 8083 e280 83e2 8083 e280  . ..............
00000610: 8320 e280 83e2 8083 20e2 8083 e280 83e2  . ...... .......
00000620: 8083 e280 83e2 8083 e280 83e2 8083 2020  ..............  
00000630: e280 83e2 8083 e280 8320 e280 83e2 8083  ......... ......
00000640: 2020 e280 8320 e280 8320 e280 83e2 8083    ... ... ......
00000650: 2020 e280 83e2 8083 20e2 8083 e280 83e2    ...... .......
00000660: 8083 2020 e280 83e2 8083 e280 8320 e280  ..  ......... ..
00000670: 83e2 8083 2020 e280 83e2 8083 2020 e280  ....  ......  ..
00000680: 83e2 8083 e280 83e2 8083 20e2 8083 20e2  .......... ... .
00000690: 8083 e280 83e2 8083 e280 83e2 8083 20e2  .............. .
000006a0: 8083 e280 8320 e280 83e2 8083 e280 83e2  ..... ..........
000006b0: 8083 20e2 8083 e280 8320 e280 8320 2020  .. ...... ...   
000006c0: e280 83e2 8083 e280 83e2 8083 e280 8320  ............... 
000006d0: 20e2 8083 20e2 8083 e280 8320 e280 8320   ... ...... ... 
000006e0: 20e2 8083 e280 83e2 8083 2020 e280 8320   .........  ... 
000006f0: 20e2 8083 2020 2020 e280 8320 e280 83e2   ...    ... ....
00000700: 8083 e280 83e2 8083 2020 e280 8320 e280  ........  ... ..
00000710: 8320 e280 8320 e280 83e2 8083 e280 8320  . ... ......... 
00000720: e280 83e2 8083 e280 8320 20e2 8083 e280  .........  .....
00000730: 8320 2020 20e2 8083 2020 e280 8320 20e2  .    ...  ...  .
00000740: 8083 2020 20e2 8083 e280 8320 20e2 8083  ..   ......  ...
00000750: 2020 2020 e280 8320 2020 e280 8320 e280      ...   ... ..
00000760: 83e2 8083 e280 8320 e280 8320 2020 2020  ....... ...     
00000770: e280 8320 20e2 8083 e280 83e2 8083 e280  ...  ...........
00000780: 8320 e280 8320 20e2 8083 2020 e280 83e2  . ...  ...  ....
00000790: 8083 e280 8320 20e2 8083 2020 e280 83e2  .....  ...  ....
000007a0: 8083 e280 8320 e280 8320 2020 2020 e280  ..... ...     ..
000007b0: 8320 2020 e280 83e2 8083 2020 e280 8320  .   ......  ... 
000007c0: 2020 e280 83e2 8083 e280 83e2 8083 e280    ..............
000007d0: 8320 20e2 8083 e280 83e2 8083 e280 8320  .  ............ 
000007e0: e280 8320 20e2 8083 e280 83e2 8083 2020  ...  .........  
000007f0: e280 8320 20e2 8083 e280 8320 e280 8320  ...  ...... ... 
00000800: e280 8320 2020 e280 83e2 8083 2020 e280  ...   ......  ..
00000810: 8320 e280 8320 2020 2020 e280 8320 20e2  . ...     ...  .
00000820: 8083 e280 83e2 8083 e280 8320 e280 8320  ........... ... 
00000830: 2020 e280 83e2 8083 20e2 8083 e280 8320    ...... ...... 
00000840: 20e2 8083 e280 8320 e280 8320 e280 8320   ...... ... ... 
00000850: e280 8320 2020 2020 e280 8320 20e2 8083  ...     ...  ...
00000860: e280 83e2 8083 2020 e280 8320 2020 e280  ......  ...   ..
00000870: 83e2 8083 20e2 8083 e280 8320 20e2 8083  .... ......  ...
00000880: e280 8320 e280 8320 e280 8320 20e2 8083  ... ... ...  ...
00000890: e280 83e2 8083 e280 8320 e280 8320 2020  ......... ...   
000008a0: e280 8320 e280 83e2 8083 e280 8320 20e2  ... .........  .
000008b0: 8083 e280 8320 e280 8320 e280 8320 20e2  ..... ... ...  .
000008c0: 8083 e280 8320 e280 83e2 8083 e280 8320  ..... ......... 
000008d0: e280 8320 2020 2020 e280 8320 20e2 8083  ...     ...  ...
000008e0: e280 8320 e280 8320 e280 8320 2020 e280  ... ... ...   ..
000008f0: 83e2 8083 e280 8320 e280 8320 2020 e280  ....... ...   ..
00000900: 8320 e280 8320 e280 8320 20e2 8083 e280  . ... ...  .....
00000910: 83e2 8083 e280 8320 e280 8320 20e2 8083  ....... ...  ...
00000920: 2020 e280 83e2 8083 e280 8320 e280 8320    ......... ... 
00000930: 2020 2020 e280 83e2 8083 2020 e280 83e2      ......  ....
00000940: 8083 2020 e280 8320 20e2 8083 e280 8320  ..  ...  ...... 
00000950: e280 8320 e280 83e2 8083 2020 e280 83e2  ... ......  ....
00000960: 8083 20e2 8083 e280 83e2 8083 2020 e280  .. .........  ..
00000970: 8320 e280 83e2 8083 e280 83e2 8083 2020  . ............  
00000980: e280 83e2 8083 20e2 8083 e280 83e2 8083  ...... .........
00000990: 2020 e280 83e2 8083 2020 e280 83e2 8083    ......  ......
000009a0: 2020 e280 83e2 8083 e280 83e2 8083 e280    ..............
000009b0: 83e2 8083 2020 20e2 8083 e280 83e2 8083  ....   .........
000009c0: e280 83e2 8083 2020 e280 83e2 8083 e280  ......  ........
000009d0: 8320 e280 8320 20e2 8083 e280 8320 e280  . ...  ...... ..
000009e0: 83e2 8083 e280 8320 20e2 8083 e280 8320  .......  ...... 
000009f0: 20e2 8083 e280 83e2 8083 2020 20e2 8083   .........   ...
00000a00: e280 8320 e280 8320 20e2 8083 e280 83e2  ... ...  .......
00000a10: 8083 e280 8320 e280 8320 20e2 8083 e280  ..... ...  .....
00000a20: 8320 e280 83e2 8083 e280 8320 20e2 8083  . .........  ...
00000a30: e280 83e2 8083 e280 8320 e280 8320 20e2  ......... ...  .
00000a40: 8083 e280 83e2 8083 20e2 8083 e280 83e2  ........ .......
00000a50: 8083 2020 e280 83e2 8083 20e2 8083 e280  ..  ...... .....
00000a60: 8320 20e2 8083 e280 83e2 8083 e280 8320  .  ............ 
00000a70: e280 83e2 8083 2020 20e2 8083 e280 8320  ......   ...... 
00000a80: e280 8320 20e2 8083 e280 8320 e280 83e2  ...  ...... ....
00000a90: 8083 e280 83e2 8083 2020 20e2 8083 e280  ........   .....
00000aa0: 8320 e280 83e2 8083 2020 e280 8320 20e2  . ......  ...  .
00000ab0: 8083 e280 8320 20e2 8083 e280 83e2 8083  .....  .........
00000ac0: e280 8320 e280 8320 20e2 8083 e280 8320  ... ...  ...... 
00000ad0: 20e2 8083 e280 8320 20e2 8083 e280 8320   ......  ...... 
00000ae0: e280 83e2 8083 e280 8320 20e2 8083 e280  .........  .....
00000af0: 83e2 8083 e280 8320 e280 83e2 8083 2020  ....... ......  
00000b00: e280 8320 e280 83e2 8083 e280 8320 20e2  ... .........  .
00000b10: 8083 e280 83e2 8083 2020 e280 8320 20e2  ........  ...  .
00000b20: 8083 e280 8320 20e2 8083 e280 8320 20e2  .....  ......  .
00000b30: 8083 e280 83e2 8083 e280 8320 e280 8320  ........... ... 
00000b40: 20e2 8083 e280 8320 e280 83e2 8083 e280   ...... ........
00000b50: 83e2 8083 2020 e280 8320 20e2 8083 e280  ....  ...  .....
00000b60: 8320 2020 2020 e280 8320 e280 83e2 8083  .     ... ......
00000b70: e280 83e2 8083 20e2 8083 20e2 8083 e280  ...... ... .....
00000b80: 83e2 8083 e280 83e2 8083 20e2 8083 e280  .......... .....
00000b90: 8320 e280 83e2 8083 e280 83e2 8083 20e2  . ............ .
00000ba0: 8083 e280 8320                           ..... 

# Method 1: Open in Notepad++ and manally replace w/ 0 and 1 then cyberchef from binary
# Ctrl + h ❤️
00001010000010010000100101110000011010010110001101101111010000110101010001000110000010100000101000001001000010010101001101000101010001010010000001010000010101010100001001001100010010010100001100100000010100100100010101000011010011110101001001000100010100110010000000100110001000000100001001000001010000110100101101000111010100100100111101010101010011100100010000100000010100100100010101010000010011110101001001010100000010100000100100001001001101010011000000110000001100000010000001000110011011110111001001100010011001010111001100100000010000010111011001100101001011000010000001010000011010010111010001110100011100110110001001110101011100100110011101101000001011000010000001010000010000010010000000110001001101010011001000110001001100110000101000001001000010010111000001101001011000110110111101000011010101000100011001111011011011100110111101110100010111110110000101101100011011000101111101110011011100000110000101100011011001010111001101011111011000010111001001100101010111110110001101110010011001010110000101110100011001010110010001011111011001010111000101110101011000010110110001011111001100110110010100110010001101000011001000110011001100000011100000110001011001000110011000111001011000010110010001100001011000100011001001100001001110010110010000111001001101100110000101100110011001000110000100110100011000110110011001100001011001000011011001111101000010100000100100001001
https://cyberchef.io/#recipe=From_Binary('Space',8)&input=MDAwMDEwMTAwMDAwMTAwMTAwMDAxMDAxMDExMTAwMDAwMTEwMTAwMTAxMTAwMDExMDExMDExMTEwMTAwMDAxMTAxMDEwMTAwMDEwMDAxMTAwMDAwMTAxMDAwMDAxMDEwMDAwMDEwMDEwMDAwMTAwMTAxMDEwMDExMDEwMDAxMDEwMTAwMDEwMTAwMTAwMDAwMDEwMTAwMDAwMTAxMDEwMTAxMDAwMDEwMDEwMDExMDAwMTAwMTAwMTAxMDAwMDExMDAxMDAwMDAwMTAxMDAxMDAxMDAwMTAxMDEwMDAwMTEwMTAwMTExMTAxMDEwMDEwMDEwMDAxMDAwMTAxMDAxMTAwMTAwMDAwMDAxMDAxMTAwMDEwMDAwMDAxMDAwMDEwMDEwMDAwMDEwMTAwMDAxMTAxMDAxMDExMDEwMDAxMTEwMTAxMDAxMDAxMDAxMTExMDEwMTAxMDEwMTAwMTExMDAxMDAwMTAwMDAxMDAwMDAwMTAxMDAxMDAxMDAwMTAxMDEwMTAwMDAwMTAwMTExMTAxMDEwMDEwMDEwMTAxMDAwMDAwMTAxMDAwMDAxMDAxMDAwMDEwMDEwMDExMDEwMTAwMTEwMDAwMDAxMTAwMDAwMDExMDAwMDAwMTAwMDAwMDEwMDAxMTAwMTEwMTExMTAxMTEwMDEwMDExMDAwMTAwMTEwMDEwMTAxMTEwMDExMDAxMDAwMDAwMTAwMDAwMTAxMTEwMTEwMDExMDAxMDEwMDEwMTEwMDAwMTAwMDAwMDEwMTAwMDAwMTEwMTAwMTAxMTEwMTAwMDExMTAxMDAwMTExMDAxMTAxMTAwMDEwMDExMTAxMDEwMTExMDAxMDAxMTAwMTExMDExMDEwMDAwMDEwMTEwMDAwMTAwMDAwMDEwMTAwMDAwMTAwMDAwMTAwMTAwMDAwMDAxMTAwMDEwMDExMDEwMTAwMTEwMDEwMDAxMTAwMDEwMDExMDAxMTAwMDAxMDEwMDAwMDEwMDEwMDAwMTAwMTAxMTEwMDAwMDExMDEwMDEwMTEwMDAxMTAxMTAxMTExMDEwMDAwMTEwMTAxMDEwMDAxMDAwMTEwMDExMTEwMTEwMTEwMTExMDAxMTAxMTExMDExMTAxMDAwMTAxMTExMTAxMTAwMDAxMDExMDExMDAwMTEwMTEwMDAxMDExMTExMDExMTAwMTEwMTExMDAwMDAxMTAwMDAxMDExMDAwMTEwMTEwMDEwMTAxMTEwMDExMDEwMTExMTEwMTEwMDAwMTAxMTEwMDEwMDExMDAxMDEwMTAxMTExMTAxMTAwMDExMDExMTAwMTAwMTEwMDEwMTAxMTAwMDAxMDExMTAxMDAwMTEwMDEwMTAxMTAwMTAwMDEwMTExMTEwMTEwMDEwMTAxMTEwMDAxMDExMTAxMDEwMTEwMDAwMTAxMTAxMTAwMDEwMTExMTEwMDExMDAxMTAxMTAwMTAxMDAxMTAwMTAwMDExMDEwMDAwMTEwMDEwMDAxMTAwMTEwMDExMDAwMDAwMTExMDAwMDAxMTAwMDEwMTEwMDEwMDAxMTAwMTEwMDAxMTEwMDEwMTEwMDAwMTAxMTAwMTAwMDExMDAwMDEwMTEwMDAxMDAwMTEwMDEwMDExMDAwMDEwMDExMTAwMTAxMTAwMTAwMDAxMTEwMDEwMDExMDExMDAxMTAwMDAxMDExMDAxMTAwMTEwMDEwMDAxMTAwMDAxMDAxMTAxMDAwMTEwMDAxMTAxMTAwMTEwMDExMDAwMDEwMTEwMDEwMDAwMTEwMTEwMDExMTExMDEwMDAwMTAxMDAwMDAxMDAxMDAwMDEwMDE

# Method 2:
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
from string import printable

fn = "whitepages.txt"
with open(fn, "rb") as f:
    b = f.read()

# Build a list of bits from the stream (we'll keep other bytes as separators)
bits = []
i = 0
while i < len(b):
    if b[i] == 0x20:
        bits.append("S")   # normal space token
        i += 1
    elif i+2 < len(b) and b[i] == 0xE2 and b[i+1] == 0x80 and b[i+2] == 0x83:
        bits.append("E")   # em-space token
        i += 3
    else:
        # skip other bytes (newlines etc.)
        i += 1

# compress tokens into a raw bitstring using chosen mapping
def token_to_bitstream(tokens, map_space_to):
    m = {'S': map_space_to, 'E': '1' if map_space_to == '0' else '0'}
    return "".join(m[t] for t in tokens)

def decode_bitstream(s, width=8, order='msb'):
    out = []
    # ignore trailing incomplete byte
    L = (len(s) // width) * width
    for i in range(0, L, width):
        chunk = s[i:i+width]
        if order == 'lsb':
            chunk = chunk[::-1]
        val = int(chunk, 2)
        out.append(chr(val))
    return "".join(out)

# Helper to score readability (fraction printable)
def printable_score(text):
    if not text:
        return 0.0
    good = sum(1 for c in text if c in printable)
    return good / len(text)

candidates = []
for map_space in ('0','1'):
    raw = token_to_bitstream(bits, map_space)
    for width in (8,7):
        for order in ('msb','lsb'):
            decoded = decode_bitstream(raw, width=width, order=order)
            score = printable_score(decoded)
            candidates.append((score, map_space, width, order, decoded))

# sort by best printable score and show top results
candidates.sort(key=lambda x: x[0], reverse=True)
print("Top candidate decodings (score, space_bit, width, order):\n")
for score, map_space, width, order, decoded in candidates[:12]:
    print(f"score={score:.3f}  space={map_space}  width={width}  order={order}")
    # print first 200 chars (safe)
    print(decoded[:200].replace('\n','\\n'))
    print("-"*60)

# If nothing obvious, print the very best entire output
best = candidates[0]
print("\n=== Best full decode (for inspection) ===")
print(f"space={best[1]} width={best[2]} order={best[3]} score={best[0]:.3f}\n")
print(best[4])

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
Top candidate decodings (score, space_bit, width, order):

score=1.000  space=1  width=8  order=msb
\n		picoCTF\n\n		SEE PUBLIC RECORDS & BACKGROUND REPORT\n		5000 Forbes Ave, Pittsburgh, PA 15213\n		picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}\n		
------------------------------------------------------------
score=0.883  space=0  width=7  order=msb
z}^h|Z9^*w/WmvV.W-}>U=YmWM}6u<X+7:f3_^oWK%b[0U,7=}6u/X+5?/[mJgsy}}f!
NfQM}ziwuy4.NbQYD_'_Wo[|v+Nf=>o4>-H/;L#EhiNAGgSIT2AFfT	d65EfS:j\nO$tdkKfs|>:7c'S9twc&xlLz3O2sILz7IA=>o
------------------------------------------------------------
score=0.847  space=0  width=7  order=lsb
/_=-N=*w|zu[75:uZ_>U^M[uY_6W
jv.3f}={uiR#mUv^_6Wz
jV~zm[)sgO__3BX93EY_/d,KwWO:t9#EM}r}u{m7jl93^>{>Z	zTn$bQdK9AqseI&A<13H6V<Q3e.+\(ykli3gL>.vLcreNwl<c2/fly&gI/vIA^>{
------------------------------------------------------------
score=0.760  space=1  width=7  order=lsb
P Bt`R1{BU\n$HJE\n% A*!2$\n& I(ar	QL B\n-\y*e	! I(r)$V0  L='FL:& PS4(0iEgF\:2n
\n`HFL!AiA%cv+f[{.t4cF>g6jY>CNLj7lI)C.LQoT#WmhglL3`AQ	3
1hCMpdfPY6fP	6>!A
------------------------------------------------------------
score=0.745  space=1  width=7  order=msb
!%Fo!U`P(	)Q(RA*B&(2I\nC'THE L !(4Z$O*SHBI\nP'TJ@P$5^r1.2le\nKQhs1.&; X ($	Td1BAKARc7PjD3m\o:lc1>s8,6+M>a9+vIJa:,E{bu0[sd4fAEHfX,FdaY3Ld0M63H6>BA
------------------------------------------------------------
score=0.477  space=0  width=8  order=lsb
¯ooñi9	=Õ¯¯oo5]]ûõU½Ím=ûµ]=
µÝ5ûû½}=-µ
UÝûµ]õ
µÕ¯ooSóóóû	±¹Y1û}YËûõiÑÑ1¹Q±éËûõ}ûsS³s3¯ooñi9	=Õ!	ÑyÉÉ1ñy9Y1y±Y9±YyÑYÙYqQyÉ3Y³Ó³3óãsÙcyÙy¹³ycÙcyÙyÓ9yÙA¯oo
------------------------------------------------------------
score=0.390  space=1  width=8  order=lsb
PÆöÂ*bPPÊ¢¢\nªB2ÂJ¢ÂòJ"ÊdBÂÒâJòªr"J¢\nòJ*P¬böNF¦În¦4\n..ÎF®Næ4\n¬LÌPÆöÂ*bÞvö.ú66úÎÆ¦ÎúN¦úÆN¦.¦&ú¦®6úÌ¦L,LÌ&f&FL&lf&,Æf&l¾P
------------------------------------------------------------
score=0.000  space=0  width=8  order=msb
õöö¼«¹õõöö¬ººß¯ª½³¶¼ß­º¼°­»¬ßÙß½¾¼´¸­°ª±»ß­º¯°­«õööÊÏÏÏß¹ß¾Óß¯Óß¯¾ßÎÊÍÎÌõöö¼«¹      ÌÍËÍÌÏÇÎÆÍÆÆÉËÉõöö
------------------------------------------------------------

=== Best full decode (for inspection) ===
space=1 width=8 order=msb score=1.000


		picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6} 🔐

# Method 3:
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
from pwn import *   # pwntools — provides handy helpers like `unbits`

# Open the binary file that contains hidden data encoded in whitespace.
# Using "rb" so we get raw bytes (important because some whitespace is multi-byte UTF-8).
with open("whitepages.txt", "rb") as bin_file:
    # Read the whole file as a mutable bytearray (you can replace bytes in-place).
    data = bytearray(bin_file.read())

    # Replace the UTF-8 sequence \xe2\x80\x83 (U+2003 EM SPACE) with ASCII byte '0'
    # Note: \xe2\x80\x83 is three bytes in UTF-8; we map that whole sequence to the character '0'.
    data = data.replace(b'\xe2\x80\x83', b'0')

    # Replace the ordinary ASCII space (0x20) with ASCII byte '1'.
    # After these two replacements, bytes that were whitespace become ASCII characters '0' or '1'.
    data = data.replace(b'\x20', b'1')

    # Convert the byte sequence of '0' and '1' bytes to a Python string of characters '0'/'1'.
    # Example: b'01000001' -> "01000001"
    data = data.decode("ascii")

    # `unbits` is a pwntools helper that takes a string of '0'/'1' bits and converts
    # them into bytes (it interprets every 8 bits as one byte). The result is typically
    # bytes or a printable string depending on the hidden payload.
    # Print the decoded payload.
    print(unbits(data))

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
b'\n\t\tpicoCTF\n\n\t\tSEE PUBLIC RECORDS & BACKGROUND REPORT\n\t\t5000 Forbes Ave, Pittsburgh, PA 15213\n\t\tpicoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}\n\t\t'🔐

# Method 4:
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
def convertSpacesToBinary():
    with open('whitepages.txt', 'rb') as f:
        result = f.read()
    result = result.replace(b'\xe2\x80\x83', b'0')  # Unicode EM SPACE -> 0
    result = result.replace(b'\x20', b'1')  # ASCII Space -> 1
    result = result.decode()
    return result

def convertFromBinaryToASCII(binaryValues):
    binary_int = int(binaryValues, 2)
    byte_number = (binary_int.bit_length() + 7) // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode('ascii')
    print(ascii_text)

convertFromBinaryToASCII(convertSpacesToBinary())

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️

                picoCTF

                SEE PUBLIC RECORDS & BACKGROUND REPORT
                5000 Forbes Ave, Pittsburgh, PA 15213
                picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}🔐

# Method 5:
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
# read_whitespace_bits_bytes.py
# Reads file in binary and maps the UTF-8 byte sequence for EM-SPACE -> '0' and ASCII space -> '1'.

from pwn import unbits

with open("whitepages.txt", "rb") as fh:
    b = fh.read()

# replace the 3-byte UTF-8 encoding of U+2003 with ASCII '0', and ASCII space 0x20 with '1'
b = b.replace(b'\xe2\x80\x83', b'0')
b = b.replace(b'\x20', b'1')

# remove all bytes other than '0' or '1' (optional)
b = b.replace(b'\n', b'').replace(b'\r', b'')
# filter strictly to digits (safety)
b = bytes(ch for ch in b if ch in (ord('0'), ord('1')))

bit_string = b.decode('ascii')
print("bits:", bit_string)

# Optional decode
try:
    decoded = unbits(bit_string)
    if isinstance(decoded, (bytes, bytearray)):
        print("decoded:", decoded.decode("utf-8", errors="replace"))
    else:
        print("decoded:", decoded)
except Exception as e:
    print("unbits conversion failed:", e)

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
bits: 00001010000010010000100101110000011010010110001101101111010000110101010001000110000010100000101000001001000010010101001101000101010001010010000001010000010101010100001001001100010010010100001100100000010100100100010101000011010011110101001001000100010100110010000000100110001000000100001001000001010000110100101101000111010100100100111101010101010011100100010000100000010100100100010101010000010011110101001001010100000010100000100100001001001101010011000000110000001100000010000001000110011011110111001001100010011001010111001100100000010000010111011001100101001011000010000001010000011010010111010001110100011100110110001001110101011100100110011101101000001011000010000001010000010000010010000000110001001101010011001000110001001100110000101000001001000010010111000001101001011000110110111101000011010101000100011001111011011011100110111101110100010111110110000101101100011011000101111101110011011100000110000101100011011001010111001101011111011000010111001001100101010111110110001101110010011001010110000101110100011001010110010001011111011001010111000101110101011000010110110001011111001100110110010100110010001101000011001000110011001100000011100000110001011001000110011000111001011000010110010001100001011000100011001001100001001110010110010000111001001101100110000101100110011001000110000100110100011000110110011001100001011001000011011001111101000010100000100100001001
decoded: 
                picoCTF

                SEE PUBLIC RECORDS & BACKGROUND REPORT
                5000 Forbes Ave, Pittsburgh, PA 15213
                picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6} 🔐
```

## Flag
picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}

## Continue
[Continue](./picoGym0103.md)