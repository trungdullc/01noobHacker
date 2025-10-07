# Trebek Level 06 → 07

## Previous Flag
```
40_reader
```

## Goal
The password for trebek8 is the name of the program set to run prior to login if sticky keys are activated PLUS the name of the file on the desktop.<br>

NOTE:<br>
– Don’t include the file extension (i.e.- .vbs). If the name is “script.vbs” and the file on the desktop is named “1234”, then the password would be “script1234”.<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
The sethc.exe binary is activated when press the SHIFT key multiple times. Old bypass when recovering systems where the password is unknown (and not encrypted with BitLocker as you'd need the key).

Boot into a recovery disk, backup sethc.exe to sethc.exe.bak and copy cmd.exe to sethc.exe. Then, when the computer boots, tap the SHIFT key a bunch of times and the command prompt launches.
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek7@groot.underthewire.tech -p 22 ⌨️
trebek7@groot.underthewire.tech's password: ⌨️ 40_reader

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek7\desktop> dir ⌨️

    Directory: C:\users\trebek7\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:47 AM              0 99 👀

PS C:\users\trebek7\desktop> Get-Item "C:\Windows\System32\sethc.exe" ⌨️

    Directory: C:\Windows\System32

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         1/7/2021  10:42 PM         273408 sethc.exe

PS C:\users\trebek7\desktop> Get-Item 'HKCU:\Control Panel\Accessibility\StickyKeys' ⌨️

    Hive: HKEY_CURRENT_USER\Control Panel\Accessibility

Name                           Property
----                           --------
StickyKeys                     Flags : 510

PS C:\users\trebek7\desktop> Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options' ⌨️

    Hive: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options

Name                           Property
----                           --------
chrome.exe                     MaxLoaderThreads : 1
cscript.exe                    DisableExceptionChainValidation : 3
dllhost.exe                    DisableExceptionChainValidation : 3
DllNXOptions                   Apitrap.dll         : 1
                               ASSTE.dll           : 1
                               AVSTE.dll           : 1
                               Cleanup.dll         : 1
                               divx.dll            : 1
                               divxdec.ax          : 1
                               DJSMAR00.dll        : 1
                               DRMINST.dll         : 1
                               eMigrationmmc.dll   : 1
                               EncryptPatchVer.dll : 1
                               eProcedureMMC.dll   : 1
                               eQueryMMC.dll       : 1
                               fullsoft.dll        : 1
                               ISSTE.dll           : 1
                               javai.dll           : 1
                               jvm.dll             : 1
                               jvm_g.dll           : 1
                               main123w.dll        : 1
                               msci_uno.dll        : 1
                               mscoree.dll         : 1
                               mscorsvr.dll        : 1
                               mscorwks.dll        : 1
                               msjava.dll          : 1
                               mso.dll             : 1
                               NAVOPTRF.dll        : 1
                               NPMLIC.dll          : 1
                               NSWSTE.dll          : 1
                               PMSTE.dll           : 1
                               ppw32hlp.dll        : 1
                               symlcnet.dll        : 1
                               TFDTCTT8.dll        : 1
                               udtapi.dll          : 1
                               ums.dll             : 1
                               vb40032.dll         : 1
                               vbe6.dll            : 1
                               Vegas60k.dll        : 1
                               xlmlEN.dll          : 1
drvinst.exe                    DisableExceptionChainValidation : 3
ehexthost32.exe                DisableExceptionChainValidation : 3
explorer.exe                   DisableExceptionChainValidation : 3
ExtExport.exe                  MitigationOptions : 256
ie4uinit.exe                   MitigationOptions : 256
ieinstal.exe                   MitigationOptions : 256
ielowutil.exe                  MitigationOptions : 256
ieUnatt.exe                    MitigationOptions : 256
iexplore.exe                   DisableExceptionChainValidation : 0
                               DisableUserModeCallbackFilter   : 1
                               MitigationOptions               : 256
InetMgr.exe                    MitigationOptions : 1152921504606846976
MiracastView.exe               MitigationOptions : 4294967296
mmc.exe                        DisableExceptionChainValidation : 3
MRT.exe                        CFGOptions : 1
mscorsvw.exe                   MitigationOptions : 4294967296
msfeedssync.exe                MitigationOptions : 256
mshta.exe                      MitigationOptions : 256
MsMpEng.exe                    CFGOptions : 1
ngen.exe                       MitigationOptions : 4294967296
ngentask.exe                   MitigationOptions : 4294967296
PresentationHost.exe           MitigationOptions : 1118481
PrintDialog.exe                MitigationOptions : 4294967296
rundll32.exe                   DisableExceptionChainValidation : 3
runtimebroker.exe              MitigationOptions : 4294967296
searchprotocolhost.exe         DisableExceptionChainValidation : 3
sethc.exe
spoolsv.exe                    DisableExceptionChainValidation : 3
svchost.exe                    MinimumStackCommitInBytes : 32768
SystemSettings.exe             MitigationOptions : 4294967296
wpr.exe                        MitigationOptions : {0, 0, 0, 0...}
wprui.exe                      MitigationOptions : {0, 0, 0, 0...}
wscript.exe                    DisableExceptionChainValidation : 3

# Note: Couldn't solve this one used old WriteUp: han_solo99 ⚠️

PS C:\users\trebek7\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek8@groot.underthewire.tech -p 22 ⌨️
trebek8@groot.underthewire.tech's password: ⌨️ han_solo99

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek8\desktop> whoami ⌨️
underthewire\trebek8
```

## Flag
han_solo99

## Continue
[Continue](./Trebek0708.md)