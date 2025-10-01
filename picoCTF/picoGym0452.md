# picoGym Level 452: Binary Instrumentation 2
Source: https://play.picoctf.org/practice/challenge/452

## Goal
I've been learning more Windows API functions to do my bidding.<br>
Hmm... I swear this program was supposed to create a file and write the flag directly to the file.<br>
Can you try and intercept the file writing function to see what went wrong?<br>
Download the exe here. Unzip the archive with the password picoctf<br>
https://challenge-files.picoctf.net/c_verbal_sleep/4aee1b9778a8e56724d015b027431fb236853a94f53e5dcf32c5ed32aed404da/bininst2.zip

## What I learned
```
Reverse Engineering

handler = function = method = definition

Frida: a dynamic instrumentation toolkit
# Traces ALL API calls from every library
frida-trace -f bininst2.exe -i "*"

# Possible flag being written/read from a file, Use specific frida-trace
# Only traces APIs that contain “File” in their name (CreateFile, ReadFile, WriteFile)
# excludes KERNDEL32.dll APIs
frida-trace -i *File* -f bininst2.exe -X KERNEL32

Convert a Windows API EXE back to code
  dnSpy
  Unpy2exe
  IDA Pro
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://challenge-files.picoctf.net/c_verbal_sleep/4aee1b9778a8e56724d015b027431fb236853a94f53e5dcf32c5ed32aed404da/bininst2.zip ⌨️
--2025-09-30 07:03:04--  https://challenge-files.picoctf.net/c_verbal_sleep/4aee1b9778a8e56724d015b027431fb236853a94f53e5dcf32c5ed32aed404da/bininst2.zip
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.40, 3.160.5.18, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.40|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17104 (17K) [application/octet-stream]
Saving to: 'bininst2.zip'

bininst2.zip                                               100%[======================================================================================================================================>]  16.70K  --.-KB/s    in 0.006s  

2025-09-30 07:03:04 (2.51 MB/s) - 'bininst2.zip' saved [17104/17104]

AsianHacker-picoctf@webshell:~$ unzip bininst2.zip ⌨️
Archive:  bininst2.zip
[bininst2.zip] bininst2.exe password: ⌨️
  inflating: bininst2.exe            
AsianHacker-picoctf@webshell:~$ rm bininst2.zip ⌨️
AsianHacker-picoctf@webshell:~$ file bininst2.exe ⌨️ 
bininst2.exe: PE32+ executable (console) x86-64, for MS Windows
AsianHacker-picoctf@webshell:~$ sz bininst2.exe ⌨️

# Method 1:
$ frida-trace -i CreateFileA -i WriteFile .\bininst2.exe ⌨️
    16 ms  CreateFileA()

__handlers__/KERNEL32.DLL/CreateFileA.js
defineHandler({
  onEnter(log, args, state) {
    log('CreateFileA()');
    log('filename: ' + args[0].readAnsiString());
  },

  onLeave(log, retval, state) {
  }
});

$ frida-trace -i CreateFileA -i WriteFile .\bininst2.exe ⌨️
    16 ms  CreateFileA()
    16 ms  filename: <Insert path here>

defineHandler({
  onEnter(log, args, state) {
    log('CreateFileA()');
    log('filename: ' + args[0].readAnsiString());
    this.newFileName = Memory.allocUtf8String('.\\flag.txt');
    args[0] = this.newFileName;
  },


  onLeave(log, retval, state) {
  }
});

$ frida-trace -i CreateFileA -i WriteFile .\bininst2.exe ⌨️
    16 ms  CreateFileA()
    16 ms  filename: <Insert path here>
    16 ms     | CreateFileA()
    16 ms  WriteFile()

__handlers__/KERNEL32.DLL/WriteFile.js
defineHandler({
  onEnter(log, args, state) {
    log('WriteFile()');
    log('buffer: ' + args[1].readAnsiString())
  },


  onLeave(log, retval, state) {
  }
});

$ frida-trace -i CreateFileA -i WriteFile .\bininst2.exe ⌨️
    16 ms  CreateFileA()
    16 ms  filename: <Insert path here>
    16 ms     | CreateFileA()
    16 ms  WriteFile()
    16 ms  buffer: cGljb0NURntmcjFkYV9mMHJfYjFuX2luNXRydW0zbnQ0dGlvbiFfYjIxYWVmMzl9 👀
    16 ms     | WriteFile()

https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=Y0dsamIwTlVSbnRtY2pGa1lWOW1NSEpmWWpGdVgybHVOWFJ5ZFcwemJuUTBkR2x2YmlGZllqSXhZV1ZtTXpsOQ

# Method 2:
# Modifying handlers
$ frida-trace -i *File* -f bininst2.exe -X KERNEL32 ⌨️
Instrumenting...

...

Started tracing 547 functions. Web UI available at http://localhost:51013/
           /* TID 0x18bc */
   501 ms  NtDeviceIoControlFile()
   501 ms  RtlDosApplyFileIsolationRedirection_Ustr()
   501 ms  RtlDosApplyFileIsolationRedirection_Ustr()
   501 ms  RtlDosApplyFileIsolationRedirection_Ustr()
   501 ms  NtQueryAttributesFile()
   501 ms  NtQueryAttributesFile()
   501 ms  NtOpenFile()
   501 ms  RtlDosApplyFileIsolationRedirection_Ustr()
   511 ms  GetSystemTimeAsFileTime()
   511 ms     | GetSystemTimeAsFileTime()
   511 ms  GetModuleFileNameW()
   511 ms     | GetModuleFileNameW()
   511 ms  AreFileApisANSI()
   511 ms     | AreFileApisANSI()
   511 ms  CreateFileA() 👀
   511 ms     | CreateFileA() 👀
Process terminated

FLARE-VM Sun 05/04/2025  4:46:25.91

https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilea
HANDLE CreateFileA(
  [in]           LPCSTR                lpFileName,
  [in]           DWORD                 dwDesiredAccess,
  [in]           DWORD                 dwShareMode,
  [in, optional] LPSECURITY_ATTRIBUTES lpSecurityAttributes,
  [in]           DWORD                 dwCreationDisposition,
  [in]           DWORD                 dwFlagsAndAttributes,
  [in, optional] HANDLE                hTemplateFile
);

# CreateFileA modification:
defineHandler({
  onEnter(log, args, state) {
    // Log the filename being created
    state.filename = Memory.readUtf8String(args[0]);
    log('CreateFileA called with filename: "' + state.filename + '"');
  },
  
  onLeave(log, retval, state) {
    // Log the result
    log('CreateFileA returned: ' + retval);
  }
});

# Output
$ frida-trace -i CreateFileA -f bininst2.exe -X KERNEL32 ⌨️

Started tracing 4 functions. Web UI available at http://localhost:64949/
           /* TID 0x1a40 */
    19 ms  CreateFileA()
    19 ms     | CreateFileA called with filename: "<Insert path here>"
    19 ms  CreateFileA returned: 0xffffffffffffffff
Process terminated```

# Modify CreateFileA again:
defineHandler({
  onEnter(log, args, state) {
    // Read original filename
    state.originalPath = Memory.readUtf8String(args[0]);
    log('CreateFileA - Original path: "' + state.originalPath + '"');
    
    // Replace the invalid path with a valid one
    const newPath = Memory.allocUtf8String('flag.txt');
    args[0] = newPath;
    
    // Save reference to prevent garbage collection
    state.newPath = newPath;
    
    log('CreateFileA - Replaced with: "flag.txt"');
  },
  
  onLeave(log, retval, state) {
    log('CreateFileA returned: ' + retval);
  }
});

# Output:
$ frida-trace -i CreateFileA -f bininst2.exe -X KERNEL32 ⌨️

Started tracing 2 functions. Web UI available at http://localhost:49254/
           /* TID 0xb4c */
    20 ms  CreateFileA()
    20 ms     | CreateFileA - Original path: "<Insert path here>"
    20 ms     | CreateFileA - Replaced with: "flag.txt"
    20 ms  CreateFileA returned: 0x274
Process terminated

# Modifying WriteFile handler to see if we can intercept the data it’s attempting to write
https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-writefile
BOOL WriteFile(
  [in]                HANDLE       hFile,
  [in]                LPCVOID      lpBuffer,
  [in]                DWORD        nNumberOfBytesToWrite,
  [out, optional]     LPDWORD      lpNumberOfBytesWritten,
  [in, out, optional] LPOVERLAPPED lpOverlapped
);

# WriteFile.js modification:
{
  onEnter(log, args, state) {
    // Log basic info
    log('WriteFile called with handle: ' + args[0]);
    log('WriteFile buffer content:');
    log(hexdump(args[1]));
  },
  
  onLeave(log, retval, state) {
    // Log result
    log('WriteFile returned: ' + retval);
  }
}

# Output:
$ frida-trace -i CreateFileA -i WriteFile -f bininst2.exe -X KERNEL32 ⌨️

Instrumenting...
CreateFileA: Loaded handler at "C:\Users\river\Desktop\ctf\pico\BinaryInstrumentation2\__handlers__\KERNELBASE.dll\CreateFileA.js"
WriteFile: Loaded handler at "C:\Users\river\Desktop\ctf\pico\BinaryInstrumentation2\__handlers__\KERNELBASE.dll\WriteFile.js"
CreateFileA: Loaded handler at "C:\Users\river\Desktop\ctf\pico\BinaryInstrumentation2\__handlers__\KERNEL32.DLL\CreateFileA.js"
WriteFile: Loaded handler at "C:\Users\river\Desktop\ctf\pico\BinaryInstrumentation2\__handlers__\KERNEL32.DLL\WriteFile.js"
Started tracing 4 functions. Web UI available at http://localhost:49342/
           /* TID 0x1838 */
    20 ms  CreateFileA()
    20 ms     | CreateFileA - Original path: "<Insert path here>"
    20 ms     | CreateFileA - Replaced with: "flag.txt"
    20 ms  CreateFileA returned: 0x270
    20 ms  WriteFile()
    20 ms     | WriteFile called with handle: 0x270
    20 ms     | WriteFile buffer content:
    20 ms     |             0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
140002270  63 47 6c 6a 62 30 4e 55 52 6e 74 6d 63 6a 46 6b  cGljb0NURntmcjFk
140002280  59 56 39 6d 4d 48 4a 66 59 6a 46 75 58 32 6c 75  YV9mMHJfYjFuX2lu
140002290  4e 58 52 79 64 57 30 7a 62 6e 51 30 64 47 6c 76  NXRydW0zbnQ0dGlv
1400022a0  62 69 46 66 59 6a 49 78 59 57 56 6d 4d 7a 6c 39  biFfYjIxYWVmMzl9 👀
1400022b0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
1400022c0  40 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00  @...............
1400022d0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
1400022e0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
1400022f0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002300  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002310  00 00 00 00 00 00 00 00 00 30 00 40 01 00 00 00  .........0.@....
140002320  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002330  a0 21 00 40 01 00 00 00 b0 21 00 40 01 00 00 00  .!.@.....!.@....
140002340  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002350  00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
140002360  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
    20 ms  WriteFile returned: 0x1
Process terminated
```

## Flag
picoCTF{fr1da_f0r_b1n_in5trum3nt4tion!_b21aef39}

## Continue
[Continue](./picoGym0458.md)