# Cyborg Level 05 → 06 echo "YwB5AGIAZQByAGcAZQBkAGQAbwBuAA==" | base64 -d

## Previous Flag
```
rowray_timer
```

## Goal
The password for cyborg7 is the decoded text of the string within the file on the desktop.<br>

NOTE:<br>
– The password is the last word of the string. For example, if it is “I like PowerShell”, the password would be “powershell”.<br>
– The password will be lowercase no matter how it appears on the screen.<br>
– There are no spaces in the answer.

## What I learned
```
# Valid PowerShell, but not a cmdlet but a direct call into .NET Framework classes that PowerShell exposes
# .NET static method call
[System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String("YwB5AGIAZQByAGcAZQBkAGQAbwBuAA=="))

CyberChef: https://cyberchef.io/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=WXdCNUFHSUFaUUJ5QUdjQVpRQmtBR1FBYndCdUFBPT0
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg6@cyborg.underthewire.tech -p 22 ⌨️
cyborg6@cyborg.underthewire.tech's password: ⌨️ rowray_timer

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg6\desktop> dir ⌨️

    Directory: C:\users\cyborg6\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         2/8/2022  10:47 PM             32 cypher.txt 👀

PS C:\users\cyborg6\desktop> cat .\cypher.txt ⌨️
YwB5AGIAZQByAGcAZQBkAGQAbwBuAA== 👀
PS C:\users\cyborg6\desktop> Get-Content .\cypher.txt ⌨️
YwB5AGIAZQByAGcAZQBkAGQAbwBuAA== 👀

PS C:\users\cyborg6\desktop> $encoded = "YwB5AGIAZQByAGcAZQBkAGQAbwBuAA==" ⌨️❤️❤️❤️

PS C:\users\cyborg6\desktop> Get-Variable ⌨️

Name                           Value
----                           -----
$                              )
?                              True
^                              [
args                           {}
ConfirmPreference              High
ConsoleFileName
DebugPreference                SilentlyContinue
encoded                        YwB5AGIAZQByAGcAZQBkAGQAbwBuAA== 👀👀👀👀👀
Error                          {The term 'base64' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelli... 
ErrorActionPreference          Continue
ErrorView                      NormalView
ExecutionContext               System.Management.Automation.EngineIntrinsics
false                          False
FormatEnumerationLimit         4
HOME                           C:\Users\TEMP.underthewire.156
Host                           System.Management.Automation.Internal.Host.InternalHost
InformationPreference          SilentlyContinue
input                          System.Collections.ArrayList+ArrayListEnumeratorSimple
LASTEXITCODE                   -2147024891
MaximumAliasCount              4096
MaximumDriveCount              4096
MaximumErrorCount              256
MaximumFunctionCount           4096
MaximumHistoryCount            4096
MaximumVariableCount           4096
MyInvocation                   System.Management.Automation.InvocationInfo
NestedPromptLevel              0
null
OutputEncoding                 System.Text.ASCIIEncoding
PID                            6816
PROFILE                        C:\Users\TEMP.underthewire.156\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
ProgressPreference             Continue
PSBoundParameters              {}
PSCommandPath
PSCulture                      en-US
PSDefaultParameterValues       {}
PSEdition                      Desktop
PSEmailServer
PSHOME                         C:\Windows\System32\WindowsPowerShell\v1.0
PSSessionConfigurationName     http://schemas.microsoft.com/powershell/Microsoft.PowerShell
PSSessionOption                System.Management.Automation.Remoting.PSSessionOption
PSUICulture                    en-US
PSVersionTable                 {PSVersion, PSEdition, PSCompatibleVersions, BuildVersion...}
PWD                            C:\users\cyborg6\desktop
ShellId                        Microsoft.PowerShell
StackTrace                        at System.Management.Automation.CommandDiscovery.LookupCommandInfo(String commandName, CommandTypes commandTypes, Searc....
true                           True                                                                                                                          
VerbosePreference              SilentlyContinue
WarningPreference              Continue
WhatIfPreference               False

PS C:\users\cyborg6\desktop> Get-Variable encoded ⌨️                        

Name                           Value
----                           -----
encoded                        YwB5AGIAZQByAGcAZQBkAGQAbwBuAA== 👀

PS C:\users\cyborg6\desktop> certutil -decode .\cypher.txt decoded.txt ⌨️
Input Length = 32
EncodeToFile returned Access is denied. 0x80070005 (WIN32: 5 ERROR_ACCESS_DENIED)
CertUtil: -decode command FAILED: 0x80070005 (WIN32: 5 ERROR_ACCESS_DENIED)
CertUtil: Access is denied.

PS C:\users\cyborg6\desktop> [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($encoded)) ⌨️
cybergeddon 🔐
PS C:\users\cyborg6\desktop> [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String("YwB5AGIAZQByAGcAZQBkAGQAbwBuAA==")) ⌨️
cybergeddon 🔐

# Note: No vi, vim, nano, notepad in terminal environment
# Custom function in terminal or name Convert-FromBase64.ps1 ❤️❤️❤️❤️❤️
PS C:\users\cyborg7\desktop> function Convert-FromBase64 {
>>     param([string]$String)   
>>     [System.Text.Encoding]::Unicode.GetString(
>>         [System.Convert]::FromBase64String($String)
>>     )
>> }
>> 
PS C:\users\cyborg7\desktop> Convert-FromBase64 "YwB5AGIAZQByAGcAZQBkAGQAbwBuAA==" ⌨️
cybergeddon 🔐

PS C:\users\cyborg6\desktop> exit ⌨️                                                               
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg7@cyborg.underthewire.tech -p 22 ⌨️
cyborg7@cyborg.underthewire.tech's password: ⌨️ cybergeddon

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg7\desktop> whoami ⌨️
underthewire\cyborg7   
```

## Flag
cybergeddon

## Continue
[Continue](./Cyborg0607.md)