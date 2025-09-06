# picoGym Level 131: Some Assembly Required 2
Source: https://play.picoctf.org/practice/challenge/131

## Goal
http://mercury.picoctf.net:23889/index.html

## What I learned
```
Debug Web Assembly: https://developer.chrome.com/docs/devtools/wasm/

Youtube Solution: https://www.youtube.com/watch?v=2TCZEkW0bjc
```

## Solution
```
https://webshell.picoctf.org/

# View Page Source
<html>
<head>
	<meta charset="UTF-8">
	<script src="Y8splx37qY.js"></script> 👀
</head>
<body>
	<h4>Enter flag:</h4>
	<input type="text" id="input"/>
	<button onclick="onButtonPress()">Submit</button>
	<p id="result"></p>
</body>
</html>

# Browser: http://mercury.picoctf.net:23889/Y8splx37qY.js ⌨️
const _0x6d8f=['copy_char','value','207aLjBod','1301420SaUSqf','233ZRpipt','2224QffgXU','check_flag','408533hsoVYx','instance','278338GVFUrH','Correct!','549933ZVjkwI','innerHTML','charCodeAt','./aD8SvhyVkb','result','977AzKzwq','Incorrect!','exports','length','getElementById','1jIrMBu','input','615361geljRK'];const _0x5c00=function(_0x58505a,_0x4d6e6c){_0x58505a=_0x58505a-0xc3;let _0x6d8fc4=_0x6d8f[_0x58505a];return _0x6d8fc4;};(function(_0x12fd07,_0x4e9d05){const _0x4f7b75=_0x5c00;while(!![]){try{const _0x1bb902=-parseInt(_0x4f7b75(0xc8))*-parseInt(_0x4f7b75(0xc9))+-parseInt(_0x4f7b75(0xcd))+parseInt(_0x4f7b75(0xcf))+parseInt(_0x4f7b75(0xc3))+-parseInt(_0x4f7b75(0xc6))*parseInt(_0x4f7b75(0xd4))+parseInt(_0x4f7b75(0xcb))+-parseInt(_0x4f7b75(0xd9))*parseInt(_0x4f7b75(0xc7));if(_0x1bb902===_0x4e9d05)break;else _0x12fd07['push'](_0x12fd07['shift']());}catch(_0x4f8a){_0x12fd07['push'](_0x12fd07['shift']());}}}(_0x6d8f,0x4bb06));let exports;(async()=>{const _0x835967=_0x5c00;let _0x1adb5f=await fetch(_0x835967(0xd2)),_0x355961=await WebAssembly['instantiate'](await _0x1adb5f['arrayBuffer']()),_0x5c0ffa=_0x355961[_0x835967(0xcc)];exports=_0x5c0ffa[_0x835967(0xd6)];})();function onButtonPress(){const _0x50ea62=_0x5c00;let _0x5f4170=document[_0x50ea62(0xd8)](_0x50ea62(0xda))[_0x50ea62(0xc5)];for(let _0x19d3ca=0x0;_0x19d3ca<_0x5f4170['length'];_0x19d3ca++){exports[_0x50ea62(0xc4)](_0x5f4170[_0x50ea62(0xd1)](_0x19d3ca),_0x19d3ca);}exports['copy_char'](0x0,_0x5f4170[_0x50ea62(0xd7)]),exports[_0x50ea62(0xca)]()==0x1?document['getElementById'](_0x50ea62(0xd3))[_0x50ea62(0xd0)]=_0x50ea62(0xce):document[_0x50ea62(0xd8)](_0x50ea62(0xd3))['innerHTML']=_0x50ea62(0xd5);}

# Beautify JS Code
const _0x6d8f = ['copy_char', 'value', '207aLjBod', '1301420SaUSqf', '233ZRpipt', '2224QffgXU', 'check_flag', '408533hsoVYx', 'instance', '278338GVFUrH', 'Correct!', '549933ZVjkwI', 'innerHTML', 'charCodeAt', './aD8SvhyVkb', 'result', '977AzKzwq', 'Incorrect!', 'exports', 'length', 'getElementById', '1jIrMBu', 'input', '615361geljRK'];
const _0x5c00 = function(_0x58505a, _0x4d6e6c) {
    _0x58505a = _0x58505a - 0xc3;
    let _0x6d8fc4 = _0x6d8f[_0x58505a];
    return _0x6d8fc4;
};
(function(_0x12fd07, _0x4e9d05) {
    const _0x4f7b75 = _0x5c00;
    while (!![]) {
        try {
            const _0x1bb902 = -parseInt(_0x4f7b75(0xc8)) * -parseInt(_0x4f7b75(0xc9)) + -parseInt(_0x4f7b75(0xcd)) + parseInt(_0x4f7b75(0xcf)) + parseInt(_0x4f7b75(0xc3)) + -parseInt(_0x4f7b75(0xc6)) * parseInt(_0x4f7b75(0xd4)) + parseInt(_0x4f7b75(0xcb)) + -parseInt(_0x4f7b75(0xd9)) * parseInt(_0x4f7b75(0xc7));
            if (_0x1bb902 === _0x4e9d05) break;
            else _0x12fd07['push'](_0x12fd07['shift']());
        } catch (_0x4f8a) {
            _0x12fd07['push'](_0x12fd07['shift']());
        }
    }
}(_0x6d8f, 0x4bb06));
let exports;
(async () => {
    const _0x835967 = _0x5c00;
    let _0x1adb5f = await fetch(_0x835967(0xd2)),
        _0x355961 = await WebAssembly['instantiate'](await _0x1adb5f['arrayBuffer']()),
        _0x5c0ffa = _0x355961[_0x835967(0xcc)];
    exports = _0x5c0ffa[_0x835967(0xd6)];
})();

function onButtonPress() {
    const _0x50ea62 = _0x5c00;
    let _0x5f4170 = document[_0x50ea62(0xd8)](_0x50ea62(0xda))[_0x50ea62(0xc5)];
    for (let _0x19d3ca = 0x0; _0x19d3ca < _0x5f4170['length']; _0x19d3ca++) {
        exports[_0x50ea62(0xc4)](_0x5f4170[_0x50ea62(0xd1)](_0x19d3ca), _0x19d3ca);
    }
    exports['copy_char'](0x0, _0x5f4170[_0x50ea62(0xd7)]), exports[_0x50ea62(0xca)]() == 0x1 ? document['getElementById'](_0x50ea62(0xd3))[_0x50ea62(0xd0)] = _0x50ea62(0xce) : document[_0x50ea62(0xd8)](_0x50ea62(0xd3))['innerHTML'] = _0x50ea62(0xd5);
}

# ChatGPT to deobfuscate
let exports;

(async () => {
    // Load the wasm file
    let response = await fetch("./aD8SvhyVkb"); 👀
    let wasmModule = await WebAssembly.instantiate(await response.arrayBuffer());
    exports = wasmModule.instance.exports;
})();

function onButtonPress() {
    // Grab user input from <input id="input">
    let userInput = document.getElementById("input").value;

    // Copy each character into wasm memory
    for (let i = 0; i < userInput.length; i++) {
        exports.copy_char(userInput.charCodeAt(i), i);
    }

    // Null-terminate string in wasm memory
    exports.copy_char(0, userInput.length);

    // Call wasm flag check
    if (exports.check_flag() == 1) {
        document.getElementById("result").innerHTML = "Correct!";
    } else {
        document.getElementById("result").innerHTML = "Incorrect!";
    }
}

# curl or wget followed by sz
AsianHacker-picoctf@webshell:~$ curl http://mercury.picoctf.net:23889/aD8SvhyVkb --output output.bin ⌨️
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   864  100   864    0     0   9461      0 --:--:-- --:--:-- --:--:--  9494
AsianHacker-picoctf@webshell:~$ file output.bin ⌨️
output.bin: WebAssembly (wasm) binary module version 0x1 (MVP)
# Note: .wasm file should of renamed .bin
AsianHacker-picoctf@webshell:~$ strings output.bin ⌨️
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
+xakgK\Nsl<8?nmi:<i;0j9:;?nm8i=0??:=njn=9u 👀

# Download wasm from remote
AsianHacker-picoctf@webshell:~$ sz output.bin ⌨️

# Disassemble .wasm file into human-readable WebAssembly Text format .wat
wasm2wat output.bin -o output.wat ⌨️

# Other Method Online: https://www.wa2.io/wat
(module
  (type (;0;) (func))
  (type (;1;) (func (param i32 i32) (result i32)))
  (type (;2;) (func (result i32)))
  (type (;3;) (func (param i32 i32)))
  (func (;0;) (type 0))
  (func (;1;) (type 1) (param i32 i32) (result i32)
    (local i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32)
    global.get 0
    local.set 2
    i32.const 32
    local.set 3
    local.get 2
    local.get 3
    i32.sub
    local.set 4
    local.get 4
    local.get 0
    i32.store offset=24
    local.get 4
    local.get 1
    i32.store offset=20
    local.get 4
    i32.load offset=24
    local.set 5
    local.get 4
    local.get 5
    i32.store offset=16
    local.get 4
    i32.load offset=20
    local.set 6
    local.get 4
    local.get 6
    i32.store offset=12
    block ;; label = @1
      loop ;; label = @2
        local.get 4
        i32.load offset=16
        local.set 7
        i32.const 1
        local.set 8
        local.get 7
        local.get 8
        i32.add
        local.set 9
        local.get 4
        local.get 9
        i32.store offset=16
        local.get 7
        i32.load8_u
        local.set 10
        local.get 4
        local.get 10
        i32.store8 offset=11
        local.get 4
        i32.load offset=12
        local.set 11
        i32.const 1
        local.set 12
        local.get 11
        local.get 12
        i32.add
        local.set 13
        local.get 4
        local.get 13
        i32.store offset=12
        local.get 11
        i32.load8_u
        local.set 14
        local.get 4
        local.get 14
        i32.store8 offset=10
        local.get 4
        i32.load8_u offset=11
        local.set 15
        i32.const 255
        local.set 16
        local.get 15
        local.get 16
        i32.and
        local.set 17
        block ;; label = @3
          local.get 17
          br_if 0 (;@3;)
          local.get 4
          i32.load8_u offset=11
          local.set 18
          i32.const 255
          local.set 19
          local.get 18
          local.get 19
          i32.and
          local.set 20
          local.get 4
          i32.load8_u offset=10
          local.set 21
          i32.const 255
          local.set 22
          local.get 21
          local.get 22
          i32.and
          local.set 23
          local.get 20
          local.get 23
          i32.sub
          local.set 24
          local.get 4
          local.get 24
          i32.store offset=28
          br 2 (;@1;)
        end
        local.get 4
        i32.load8_u offset=11
        local.set 25
        i32.const 255
        local.set 26
        local.get 25
        local.get 26
        i32.and
        local.set 27
        local.get 4
        i32.load8_u offset=10
        local.set 28
        i32.const 255
        local.set 29
        local.get 28
        local.get 29
        i32.and
        local.set 30
        local.get 27
        local.set 31
        local.get 30
        local.set 32
        local.get 31
        local.get 32
        i32.eq
        local.set 33
        i32.const 1
        local.set 34
        local.get 33
        local.get 34
        i32.and
        local.set 35
        local.get 35
        br_if 0 (;@2;)
      end
      local.get 4
      i32.load8_u offset=11
      local.set 36
      i32.const 255
      local.set 37
      local.get 36
      local.get 37
      i32.and
      local.set 38
      local.get 4
      i32.load8_u offset=10
      local.set 39
      i32.const 255
      local.set 40
      local.get 39
      local.get 40
      i32.and
      local.set 41
      local.get 38
      local.get 41
      i32.sub
      local.set 42
      local.get 4
      local.get 42
      i32.store offset=28
    end
    local.get 4
    i32.load offset=28
    local.set 43
    local.get 43
    return
  )
  (func (;2;) (type 2) (result i32)
    (local i32 i32 i32 i32 i32 i32 i32 i32 i32 i32 i32)
    i32.const 0
    local.set 0
    i32.const 1072
    local.set 1
    i32.const 1024
    local.set 2
    local.get 2
    local.get 1
    call 1
    local.set 3
    local.get 3
    local.set 4
    local.get 0
    local.set 5
    local.get 4
    local.get 5
    i32.ne
    local.set 6
    i32.const -1
    local.set 7
    local.get 6
    local.get 7
    i32.xor
    local.set 8
    i32.const 1
    local.set 9
    local.get 8
    local.get 9
    i32.and
    local.set 10
    local.get 10
    return
  )
  (func (;3;) (type 3) (param i32 i32)
    (local i32 i32 i32 i32 i32 i32 i32 i32 i32)
    global.get 0
    local.set 2
    i32.const 16
    local.set 3
    local.get 2
    local.get 3
    i32.sub
    local.set 4
    local.get 4
    local.get 0
    i32.store offset=12
    local.get 4
    local.get 1
    i32.store offset=8
    local.get 4
    i32.load offset=12
    local.set 5
    block ;; label = @1
      local.get 5
      i32.eqz
      br_if 0 (;@1;)
      local.get 4
      i32.load offset=12
      local.set 6
      i32.const 8
      local.set 7
      local.get 6
      local.get 7
      i32.xor
      local.set 8
      local.get 4
      local.get 8
      i32.store offset=12
    end
    local.get 4
    i32.load offset=12
    local.set 9
    local.get 4
    i32.load offset=8
    local.set 10
    local.get 10
    local.get 9
    i32.store8 offset=1072
    return
  )
  (table (;0;) 1 1 funcref)
  (memory (;0;) 2)
  (global (;0;) (mut i32) i32.const 66864)
  (global (;1;) i32 i32.const 1072)
  (global (;2;) i32 i32.const 1024)
  (global (;3;) i32 i32.const 1328)
  (global (;4;) i32 i32.const 1024)
  (global (;5;) i32 i32.const 66864)
  (global (;6;) i32 i32.const 0)
  (global (;7;) i32 i32.const 1)
  (export "memory" (memory 0))
  (export "__wasm_call_ctors" (func 0))
  (export "strcmp" (func 1))
  (export "check_flag" (func 2))
  (export "input" (global 1))
  (export "copy_char" (func 3))
  (export "__dso_handle" (global 2))
  (export "__data_end" (global 3))
  (export "__global_base" (global 4))
  (export "__heap_base" (global 5))
  (export "__memory_base" (global 6))
  (export "__table_base" (global 7))
  (data (;0;) (i32.const 1024) "xakgK\5cNsl<8?nmi:<i;0j9:;?nm8i=0??:=njn=9u\00\00") 👀
)

# CyberChef: XOR 8
https://cyberchef.io/#recipe=XOR(%7B'option':'Decimal','string':'8'%7D,'Standard',false)&input=eGFrZ0tcTnNsPDg/bm1pOjxpOzBqOTo7P25tOGk9MD8/Oj1uam49OXU ⌨️
    picoCTF{d407fea24a38b1237fe0a587725fbf51} 🔐

# Custom Script
# Note: use escape char w/ \ ⚠️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3

def decode_xor() -> None:
    encoded = "xakgK\\5cNsl<8?nmi:<i;0j9:;?nm8i=0??:=njn=9u"
    decoded = "".join(chr(ord(c) ^ 8) for c in encoded)
    print(decoded)

if __name__ == "__main__":
    decode_xor()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py 
picoCT=kF{d407fea24a38b1237fe0a587725fbf51} 👀 Almost gotta remove =k
```

## Flag
picoCTF{d407fea24a38b1237fe0a587725fbf51}

## Continue
[Continue](./picoGym0144.md)