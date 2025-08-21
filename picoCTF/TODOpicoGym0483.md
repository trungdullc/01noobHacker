# picoGym Level 0483: YaraRules0x100
Source: https://play.picoctf.org/practice/challenge/483

## Goal
Dear Threat Intelligence Analyst,<br>
Quick heads up - we stumbled upon a shady executable file on one of our employee's Windows PCs. Good news: the employee didn't take the bait and flagged it to our InfoSec crew.<br>
Seems like this file sneaked past our Intrusion Detection Systems, indicating a fresh threat with no matching signatures in our database.
Can you dive into this file and whip up some YARA rules? We need to make sure we catch this thing if it pops up again.<br>
The suspicious file can be downloaded here. <br>
Unzip the archive with the password <b>picoctf</b>

Once you have created the YARA rule/signature, submit your rule file as follows:
socat -t60 - TCP:standard-pizzas.picoctf.net:61872 < sample.txt
(In the above command, modify "sample.txt" to whatever filename you use).
When you submit your rule, it will undergo testing with various test cases. If it successfully passes all the test cases, you'll receive your flag.

## What I learned
```
YARA (Yet Another Recursive Acronym) a tool and rule language that identify and classify malware or suspicious files based on text, binary strings, or more complex patterns

YARA Documentation: https://yara.readthedocs.io/en/stable/

Windows executable file, some strings within this binary can be "wide" strings
Declaring your string variables $str = "Some Text" wide ascii wherever necessary
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/
AsianHacker-picoctf@webshell:/tmp$ wget https://challenge-files.picoctf.net/c_standard_pizzas/b7b0bf41d5c596a1c68888444b1c63cd551ce583576526adf21b545a5f3df1c8/suspicious.zip
--2025-08-20 19:56:04--  https://challenge-files.picoctf.net/c_standard_pizzas/b7b0bf41d5c596a1c68888444b1c63cd551ce583576526adf21b545a5f3df1c8/suspicious.zip
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.95, 3.160.5.40, 3.160.5.64, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.95|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16506 (16K) [application/octet-stream]
Saving to: 'suspicious.zip'

suspicious.zip                                             100%[======================================================================================================================================>]  16.12K  --.-KB/s    in 0.006s  

2025-08-20 19:56:04 (2.59 MB/s) - 'suspicious.zip' saved [16506/16506]

AsianHacker-picoctf@webshell:/tmp$ unzip suspicious.zip 
Archive:  suspicious.zip
[suspicious.zip] suspicious.exe password: 
  inflating: suspicious.exe  
AsianHacker-picoctf@webshell:/tmp$ file suspicious.exe 
suspicious.exe: PE32 executable (GUI) Intel 80386, for MS Windows, UPX compressed
AsianHacker-picoctf@webshell:/tmp$ whatis upx
upx (1)              - compress or expand executable files
AsianHacker-picoctf@webshell:/tmp$ upx -d suspicious.exe -o suspicious_unpacked.exe
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     40960 <-     26624   65.00%    win32/pe     suspicious_unpacked.exe

Unpacked 1 file.
AsianHacker-picoctf@webshell:/tmp$ strings suspicious_unpacked.exe 
!This program cannot be run in DOS mode.
xRich
.text
`.rdata
@.data
.rsrc
@.reloc
hX<@
h8=@
hP8@
h0b@
t8hP9@
u%h@:@
t3h8;@
h >@
ht>@
hx>@
hp?@
h$A@
h(A@
h 7@
h0b@
t%j@h
h@A@
%X0@
%\0@
hc$@
h0H@
VPWh
Y_^[
hPH@
Y_^[
h}&@
>csm
hlH@
SVW3
Genu
5ineI
5ntel
t#=`
_^[3
%01@
%$1@
% 1@
%,1@
%(1@
%41@
%H1@
%D1@
%h1@
%`1@
%p1@
%l1@
%x1@
%X1@
%P1@
%L1@
%t1@
%|1@
        _            _____ _______ ______  
       (_)          / ____|__   __|  ____| 
  _ __  _  ___ ___ | |       | |  | |__    
 | '_ \| |/ __/ _ \| |       | |  |  __|   
 | |_) | | (_| (_) | |____   | |  | |      
 | .__/|_|\___\___/ \_____|  |_|  |_|      
 | |                                       
 |_|                                       
  Welcome to the YaraRules0x100 challenge!
                       .,,                
              ****************.         
            ***************.  .*,       
           ********,     ,*%%#(,        
           ******.  %%%%%&@@@@@@@@@%    
           *****   #%%%%%@@@@@@@@@@%%#  
    ****  ,,****  ***%%%%%%%%%%%%%%%%%  
   *****  ,,*****  ******/%%%%%%/****   
   ,,,,,  ,,******    ,*********        
   ,,,,,  ,,,*********.         .**     
   ,,,,,  ,,,,*********************     
   ,,,,,  ,,,,,,*******************     
   ,,,,,  ,,,,,,,,,,,,********,,,,,     
    ,,,,  ,,,,,,,,,,,,,,,,,,,,,,,,,     
    ,,,,  .,,,,,,,,,,,,,,,,,,,,,,,,     
           ,,,,,,,,,,       .,,,,,      
           ,,,,,,,,,       ,,,,,,,      
           ,,,,,,,,,      .,,,,,,,      
           .,,,,,,,         ,,.
NtQueryInformationProcess
%ws %d
Unknown exception
bad allocation
bad array new length
GCTL
.text$di
.text$mn
.idata$5
.00cfg
.CRT$XCA
.CRT$XCAA
.CRT$XCU
.CRT$XCZ
.CRT$XIA
.CRT$XIAA
.CRT$XIAC
.CRT$XIZ
.CRT$XPA
.CRT$XPZ
.CRT$XTA
.CRT$XTZ
.rdata
.rdata$r
.rdata$sxdata
.rdata$voltmd
.rdata$zzzdbg
.rtc$IAA
.rtc$IZZ
.rtc$TAA
.rtc$TZZ
.xdata$x
.idata$2
.idata$3
.idata$4
.idata$6
.data
.data$r
.data$rs
.bss
.rsrc$01
.rsrc$02
GetCommandLineW
OutputDebugStringW
DebugActiveProcess
DebugActiveProcessStop
CloseHandle
GetLastError
WaitForSingleObject
CreateMutexW
Sleep
GetCurrentProcess
GetCurrentProcessId
TerminateProcess
GetExitCodeProcess
CreateThread
CreateProcessA
OpenProcess
GetModuleFileNameW
GetModuleHandleW
GetProcAddress
MultiByteToWideChar
WideCharToMultiByte
CreateToolhelp32Snapshot
Process32FirstW
Process32NextW
KERNEL32.DLL
LoadStringW
GetMessageW
TranslateMessage
DispatchMessageW
DefWindowProcW
PostQuitMessage
RegisterClassExW
CreateWindowExW
DestroyWindow
ShowWindow
DialogBoxParamW
EndDialog
LoadAcceleratorsW
TranslateAcceleratorW
DrawIcon
UpdateWindow
BeginPaint
EndPaint
GetClientRect
MessageBoxW
FillRect
GetDesktopWindow
LoadCursorW
LoadIconW
USER32.dll
CreateSolidBrush
DeleteObject
SetBkColor
SetTextColor
TextOutW
GDI32.dll
OpenProcessToken
AdjustTokenPrivileges
LookupPrivilegeValueW
ADVAPI32.dll
CommandLineToArgvW
SHELL32.dll
memset
__current_exception
__current_exception_context
_except_handler4_common
__std_exception_copy
__std_exception_destroy
_CxxThrowException
VCRUNTIME140.dll
free
malloc
exit
atoi
__stdio_common_vsprintf
_seh_filter_exe
_set_app_type
__setusermatherr
_configure_wide_argv
_initialize_wide_environment
_get_wide_winmain_command_line
_initterm
_initterm_e
_exit
_set_fmode
_cexit
_c_exit
_register_thread_local_exe_atexit_callback
_configthreadlocale
_set_new_mode
__p__commode
_callnewh
_initialize_onexit_table
_register_onexit_function
_crt_atexit
_controlfp_s
terminate
api-ms-win-crt-heap-l1-1-0.dll
api-ms-win-crt-runtime-l1-1-0.dll
api-ms-win-crt-convert-l1-1-0.dll
api-ms-win-crt-stdio-l1-1-0.dll
api-ms-win-crt-math-l1-1-0.dll
api-ms-win-crt-locale-l1-1-0.dll
QueryPerformanceCounter
GetCurrentThreadId
GetSystemTimeAsFileTime
InitializeSListHead
IsDebuggerPresent
UnhandledExceptionFilter
SetUnhandledExceptionFilter
GetStartupInfoW
IsProcessorFeaturePresent
.?AVbad_alloc@std@@
.?AVexception@std@@
.?AVbad_array_new_length@std@@
.?AVtype_info@@
<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<assembly xmlns='urn:schemas-microsoft-com:asm.v1' manifestVersion='1.0'>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level='asInvoker' uiAccess='false' />
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>

AsianHacker-picoctf@webshell:/tmp$ whatis socat
socat (1)            - Multipurpose relay (SOcket CAT)

AsianHacker-picoctf@webshell:/tmp$ vi sample.txt
AsianHacker-picoctf@webshell:/tmp$ cat sample.txt 
rule Rule{
    strings:
        $str1 = {4D 5A} 
        $str2 = "YaraRules0x100"
        $str3 = "UPX"
        $str4 = "NtQuery"
        $str5 = "debugger process" wide ascii
        
    condition:
        ($str1 and $str2 and ($str3 or $str4)) or $str5
}

AsianHacker-picoctf@webshell:/tmp$ socat -t60 - TCP:standard-pizzas.picoctf.net:52141 < sample.txt
2025/08/20 20:18:01 socat[286] E connect(5, AF=2 3.22.195.189:52141, 16): Connection refused
```

## Flag
Not Solved prob do on kali linux

## Continue
[Continue](./picoGym0483.md)