# picoGym Level 152: Some Assembly Required 1
Source: https://play.picoctf.org/practice/challenge/152

## Goal
http://mercury.picoctf.net:26318/index.html

## What I learned
```
obfuscated JavaScript file

Use tools like strings, xxd, or wasm2wat to analyze WebAssembly
WebAssembly (Wasm) is a binary instruction format designed to run code at near-native speed inside web browsers and other environments
```

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<html>
<head>
	<meta charset="UTF-8">
	<script src="G82XCw5CX3.js"></script> 👀
</head>
<body>
	<h4>Enter flag:</h4>
	<input type="text" id="input"/>
	<button onclick="onButtonPress()">Submit</button>
	<p id="result"></p>
</body>
</html>

Browser: http://mercury.picoctf.net:26318/G82XCw5CX3.js ⌨️
const _0x402c=['value','2wfTpTR','instantiate','275341bEPcme','innerHTML','1195047NznhZg','1qfevql','input','1699808QuoWhA','Correct!','check_flag','Incorrect!','./JIFxzHyW8W'👀,'23SMpAuA','802698XOMSrr','charCodeAt','474547vVoGDO','getElementById','instance','copy_char','43591XxcWUl','504454llVtzW','arrayBuffer','2NIQmVj','result'];const _0x4e0e=function(_0x553839,_0x53c021){_0x553839=_0x553839-0x1d6;let _0x402c6f=_0x402c[_0x553839];return _0x402c6f;};(function(_0x76dd13,_0x3dfcae){const _0x371ac6=_0x4e0e;while(!![]){try{const _0x478583=-parseInt(_0x371ac6(0x1eb))+parseInt(_0x371ac6(0x1ed))+-parseInt(_0x371ac6(0x1db))*-parseInt(_0x371ac6(0x1d9))+-parseInt(_0x371ac6(0x1e2))*-parseInt(_0x371ac6(0x1e3))+-parseInt(_0x371ac6(0x1de))*parseInt(_0x371ac6(0x1e0))+parseInt(_0x371ac6(0x1d8))*parseInt(_0x371ac6(0x1ea))+-parseInt(_0x371ac6(0x1e5));if(_0x478583===_0x3dfcae)break;else _0x76dd13['push'](_0x76dd13['shift']());}catch(_0x41d31a){_0x76dd13['push'](_0x76dd13['shift']());}}}(_0x402c,0x994c3));let exports;(async()=>{const _0x48c3be=_0x4e0e;let _0x5f0229=await fetch(_0x48c3be(0x1e9)),_0x1d99e9=await WebAssembly[_0x48c3be(0x1df)](await _0x5f0229[_0x48c3be(0x1da)]()),_0x1f8628=_0x1d99e9[_0x48c3be(0x1d6)];exports=_0x1f8628['exports'];})();function onButtonPress(){const _0xa80748=_0x4e0e;let _0x3761f8=document['getElementById'](_0xa80748(0x1e4))[_0xa80748(0x1dd)];for(let _0x16c626=0x0;_0x16c626<_0x3761f8['length'];_0x16c626++){exports[_0xa80748(0x1d7)](_0x3761f8[_0xa80748(0x1ec)](_0x16c626),_0x16c626);}exports['copy_char'](0x0,_0x3761f8['length']),exports[_0xa80748(0x1e7)]()==0x1?document[_0xa80748(0x1ee)](_0xa80748(0x1dc))[_0xa80748(0x1e1)]=_0xa80748(0x1e6):document[_0xa80748(0x1ee)](_0xa80748(0x1dc))[_0xa80748(0x1e1)]=_0xa80748(0x1e8);}

# Find JS Beautify Online or use VSC
const _0x402c = ['value', '2wfTpTR', 'instantiate', '275341bEPcme', 'innerHTML', '1195047NznhZg', '1qfevql', 'input', '1699808QuoWhA', 'Correct!', 'check_flag', 'Incorrect!', './JIFxzHyW8W'👀, '23SMpAuA', '802698XOMSrr', 'charCodeAt', '474547vVoGDO', 'getElementById', 'instance', 'copy_char', '43591XxcWUl', '504454llVtzW', 'arrayBuffer', '2NIQmVj', 'result'];
const _0x4e0e = function(_0x553839, _0x53c021) {
    _0x553839 = _0x553839 - 0x1d6;
    let _0x402c6f = _0x402c[_0x553839];
    return _0x402c6f;
};
(function(_0x76dd13, _0x3dfcae) {
    const _0x371ac6 = _0x4e0e;
    while (!![]) {
        try {
            const _0x478583 = -parseInt(_0x371ac6(0x1eb)) + parseInt(_0x371ac6(0x1ed)) + -parseInt(_0x371ac6(0x1db)) * -parseInt(_0x371ac6(0x1d9)) + -parseInt(_0x371ac6(0x1e2)) * -parseInt(_0x371ac6(0x1e3)) + -parseInt(_0x371ac6(0x1de)) * parseInt(_0x371ac6(0x1e0)) + parseInt(_0x371ac6(0x1d8)) * parseInt(_0x371ac6(0x1ea)) + -parseInt(_0x371ac6(0x1e5));
            if (_0x478583 === _0x3dfcae) break;
            else _0x76dd13['push'](_0x76dd13['shift']());
        } catch (_0x41d31a) {
            _0x76dd13['push'](_0x76dd13['shift']());
        }
    }
}(_0x402c, 0x994c3));
let exports;
(async () => {
    const _0x48c3be = _0x4e0e;
    let _0x5f0229 = await fetch(_0x48c3be(0x1e9)),
        _0x1d99e9 = await WebAssembly[_0x48c3be(0x1df)](await _0x5f0229[_0x48c3be(0x1da)]()),
        _0x1f8628 = _0x1d99e9[_0x48c3be(0x1d6)];
    exports = _0x1f8628['exports'];
})();

function onButtonPress() {
    const _0xa80748 = _0x4e0e;
    let _0x3761f8 = document['getElementById'](_0xa80748(0x1e4))[_0xa80748(0x1dd)];
    for (let _0x16c626 = 0x0; _0x16c626 < _0x3761f8['length']; _0x16c626++) {
        exports[_0xa80748(0x1d7)](_0x3761f8[_0xa80748(0x1ec)](_0x16c626), _0x16c626);
    }
    exports['copy_char'](0x0, _0x3761f8['length']), exports[_0xa80748(0x1e7)]() == 0x1 ? document[_0xa80748(0x1ee)](_0xa80748(0x1dc))[_0xa80748(0x1e1)] = _0xa80748(0x1e6) : document[_0xa80748(0x1ee)](_0xa80748(0x1dc))[_0xa80748(0x1e1)] = _0xa80748(0x1e8);
}

Method Cheat: Assume ./ is path
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ curl http://mercury.picoctf.net:26318/JIFxzHyW8W -o output.bin ⌨️
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   824  100   824    0     0  25813      0 --:--:-- --:--:-- --:--:-- 26580
AsianHacker-picoctf@webshell:/tmp$ file output.bin ⌨️
output.bin: WebAssembly (wasm) binary module version 0x1 (MVP)
AsianHacker-picoctf@webshell:/tmp$ cat output.bin ⌨️
asm````pA
         A
         A
         A

A
A
 A
  A

   memory__wasm_call_ctorsstrcmp
check_flaginput copy_char
                         __dso_handle
__global_base
__memory_base__heap_base
             __table_base

*#!A !  k!  6  6 (!  6 (!  6
                            @@ (!A j!           6 -!
  
:
  (
   !
    A!
       
        
6       j!
  
  -!  :
 -
 -!A!  q!@ 
  !A!  q! -
!A!  q!  k!  6

               -
                !A!  q!
!  q! !!A!" ! "q!# #
 -
  !$A!% $ %q!& -
!'A!( ' (q!) & )k!*  *6
                        (!+ +
                             L
                              A!A!A!  ! ! !  G!A!  sA!          q!
 

?#!A!  k!  6
               (
                ! !  :

                      2A
                       +picoCTF{8857462f9e30faae4d037e5e25fee1ce} 🔐
AsianHacker-picoctf@webshell:/tmp$ strings output.bin ⌨️
memory
__wasm_call_ctors
strcmp
check_flag
input
        copy_char
__dso_handle
__data_end
__global_base
__heap_base
__memory_base
__table_base
j!       
  F!!A
!" ! "q!# #
!% $ %q!& 
!( ' (q!) & )k!* 
!+ +
        q!
+picoCTF{8857462f9e30faae4d037e5e25fee1ce} 🔐

AsianHacker-picoctf@webshell:/tmp$ xxd output.bin | tail ⌨️
000002a0: 0021 0520 0420 0547 2106 417f 2107 2006  .!. . .G!.A.!. .
000002b0: 2007 7321 0841 0121 0920 0820 0971 210a   .s!.A.!. . .q!.
000002c0: 200a 0f0b 3f01 057f 2380 8080 8000 2102   ...?...#.....!.
000002d0: 4110 2103 2002 2003 6b21 0420 0420 0036  A.!. . .k!. . .6
000002e0: 020c 2004 2001 3602 0820 0428 020c 2105  .. . .6.. .(..!.
000002f0: 2004 2802 0821 0620 0620 053a 00b0 8880   .(..!. . .:....
00000300: 8000 0f0b 0b32 0100 4180 080b 2b70 6963  .....2..A...+pic
00000310: 6f43 5446 7b38 3835 3734 3632 6639 6533  oCTF{8857462f9e3
00000320: 3066 6161 6534 6430 3337 6535 6532 3566  0faae4d037e5e25f
00000330: 6565 3163 657d 0000                      ee1ce}.. 🔐
```

## Flag
picoCTF{8857462f9e30faae4d037e5e25fee1ce}

## Continue
[Continue](./picoGym0131.md)