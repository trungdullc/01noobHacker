# Oracle Level 11 → 12 Get-ChildItem 'HKCU:\Software\Microsoft\Terminal Server Client

## Previous Flag
```
m
```

## Goal
The password for oracle13 is the IP of the system that this user has previously established a remote desktop with.

## What I learned
```
Don’t see Get-ItemProperty in Get-Member
    Get-ItemProperty is a cmdlet, not a property or method

Get-ChildItem 'HKCU:\Software\Microsoft\Terminal Server Client
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle12@groot.underthewire.tech -p 22 ⌨️
oracle12@groot.underthewire.tech's password: ⌨️ m

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\oracle12\desktop> Get-ChildItem 'HKCU:\Software\Microsoft\Terminal Server Client'

    Hive: HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client

Name                           Property
----                           --------
192.168.2.3                    UsernameHint : MyServer\raccoon 👀

PS C:\users\oracle12\desktop> Get-ChildItem 'HKCU:\Software\Microsoft\Terminal Server Client' | Get-Member ⌨️

   TypeName: Microsoft.Win32.RegistryKey

Name                      MemberType   Definition
----                      ----------   ----------
Close                     Method       void Close()
CreateObjRef              Method       System.Runtime.Remoting.ObjRef CreateObjRef(type requestedType)
CreateSubKey              Method       Microsoft.Win32.RegistryKey CreateSubKey(string subkey), Microsoft.Win32.RegistryKey CreateSubKey(string subkey,...
DeleteSubKey              Method       void DeleteSubKey(string subkey), void DeleteSubKey(string subkey, bool throwOnMissingSubKey)
DeleteSubKeyTree          Method       void DeleteSubKeyTree(string subkey), void DeleteSubKeyTree(string subkey, bool throwOnMissingSubKey)
DeleteValue               Method       void DeleteValue(string name), void DeleteValue(string name, bool throwOnMissingValue)
Dispose                   Method       void Dispose(), void IDisposable.Dispose()
Equals                    Method       bool Equals(System.Object obj)
Flush                     Method       void Flush()
GetAccessControl          Method       System.Security.AccessControl.RegistrySecurity GetAccessControl(), System.Security.AccessControl.RegistrySecurit... 
GetHashCode               Method       int GetHashCode()
GetLifetimeService        Method       System.Object GetLifetimeService()
GetSubKeyNames            Method       string[] GetSubKeyNames()
GetType                   Method       type GetType()
GetValue                  Method       System.Object GetValue(string name), System.Object GetValue(string name, System.Object defaultValue), System.Obj... 
GetValueKind              Method       Microsoft.Win32.RegistryValueKind GetValueKind(string name)
GetValueNames             Method       string[] GetValueNames()
InitializeLifetimeService Method       System.Object InitializeLifetimeService()
OpenSubKey                Method       Microsoft.Win32.RegistryKey OpenSubKey(string name, bool writable), Microsoft.Win32.RegistryKey OpenSubKey(strin... 
SetAccessControl          Method       void SetAccessControl(System.Security.AccessControl.RegistrySecurity registrySecurity)
SetValue                  Method       void SetValue(string name, System.Object value), void SetValue(string name, System.Object value, Microsoft.Win32... 
ToString                  Method       string ToString()
Property                  NoteProperty string[] Property=System.String[]
PSChildName               NoteProperty string PSChildName=192.168.2.3
PSDrive                   NoteProperty PSDriveInfo PSDrive=HKCU
PSIsContainer             NoteProperty bool PSIsContainer=True
PSParentPath              NoteProperty string PSParentPath=Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client 
PSPath                    NoteProperty string PSPath=Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\19... 
PSProvider                NoteProperty ProviderInfo PSProvider=Microsoft.PowerShell.Core\Registry
Handle                    Property     Microsoft.Win32.SafeHandles.SafeRegistryHandle Handle {get;}
Name                      Property     string Name {get;}
SubKeyCount               Property     int SubKeyCount {get;}
ValueCount                Property     int ValueCount {get;}
View                      Property     Microsoft.Win32.RegistryView View {get;}

PS C:\users\oracle12\desktop> Get-ChildItem 'HKCU:\Software\Microsoft\Terminal Server Client' | Get-ItemProperty | Get-Member ⌨️

   TypeName: System.Management.Automation.PSCustomObject

Name         MemberType   Definition
----         ----------   ----------
Equals       Method       bool Equals(System.Object obj)
GetHashCode  Method       int GetHashCode()
GetType      Method       type GetType()
ToString     Method       string ToString()
PSChildName  NoteProperty string PSChildName=192.168.2.3 👀
PSParentPath NoteProperty string PSParentPath=Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client
PSPath       NoteProperty string PSPath=Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\192.168.2.3        
PSProvider   NoteProperty ProviderInfo PSProvider=Microsoft.PowerShell.Core\Registry
UsernameHint NoteProperty string UsernameHint=MyServer\raccoon

PS C:\users\oracle12\desktop> Get-ChildItem 'HKCU:\Software\Microsoft\Terminal Server Client' | Get-ItemProperty | Select-Object -ExpandProperty PSChildName ⌨️
192.168.2.3 🔐

PS C:\users\oracle12\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle13@groot.underthewire.tech -p 22 ⌨️
oracle13@groot.underthewire.tech's password: ⌨️ 192.168.2.3

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle13\desktop> whoami ⌨️
underthewire\oracle13
```

## Flag
192.168.2.3

## Continue
[Continue](./Oracle1213.md)