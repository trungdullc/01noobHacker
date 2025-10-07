# Century Level 01 → 02 wget but for PS

## Previous Flag
```
10.0.14393.8422
```

## Goal
The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.

NOTE:
– If the name of the cmdlet is “get-web” and the file on the desktop is named “1234”, the password would be “get-web1234”.
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Invoke-Webrequest               wget
dir                             ls
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century2@century.underthewire.tech -p 22 ⌨️
century1@century.underthewire.tech's password: ⌨️ 10.0.14393.8422
PS C:\users\century2\desktop> dir ⌨️

    Directory: C:\users\century2\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:29 AM            693 443 👀

PS C:\users\century2\desktop> Get-Alias ls ⌨️

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           ls -> Get-ChildItem

PS C:\users\century2\desktop> Get-Alias wget ⌨️   

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           wget -> Invoke-WebRequest 👀

PS C:\users\century2\desktop> Get-Command wget ⌨️

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           wget -> Invoke-WebRequest 👀

PS C:\users\century2\desktop> Get-Command Invoke-WebRequest | Get-Member ⌨️

   TypeName: System.Management.Automation.CmdletInfo

Name                MemberType     Definition
----                ----------     ----------
Equals              Method         bool Equals(System.Object obj)
GetHashCode         Method         int GetHashCode()
GetType             Method         type GetType()
ResolveParameter    Method         System.Management.Automation.ParameterMetadata ResolveParameter(string name)
ToString            Method         string ToString()
CommandType         Property       System.Management.Automation.CommandTypes CommandType {get;}
DefaultParameterSet Property       string DefaultParameterSet {get;}
Definition          Property       string Definition {get;}
HelpFile            Property       string HelpFile {get;}
ImplementingType    Property       type ImplementingType {get;}
Module              Property       psmoduleinfo Module {get;}
ModuleName          Property       string ModuleName {get;}
Name                Property       string Name {get;} 👀
Noun                Property       string Noun {get;}
Options             Property       System.Management.Automation.ScopedItemOptions Options {get;set;}
OutputType          Property       System.Collections.ObjectModel.ReadOnlyCollection[System.Management.Automation.PSTypeName] OutputType {get;}
Parameters          Property       System.Collections.Generic.Dictionary[string,System.Management.Automation.ParameterMetadata] Parameters {get;}
ParameterSets       Property       System.Collections.ObjectModel.ReadOnlyCollection[System.Management.Automation.CommandParameterSetInfo] ParameterSet... 
PSSnapIn            Property       System.Management.Automation.PSSnapInInfo PSSnapIn {get;}
RemotingCapability  Property       System.Management.Automation.RemotingCapability RemotingCapability {get;}
Source              Property       string Source {get;}
Verb                Property       string Verb {get;}
Version             Property       version Version {get;}
Visibility          Property       System.Management.Automation.SessionStateEntryVisibility Visibility {get;set;}
DLL                 ScriptProperty System.Object DLL {get=$this.ImplementingType.Assembly.Location;}
HelpUri             ScriptProperty System.Object HelpUri {get=$oldProgressPreference = $ProgressPreference...

PS C:\users\century2\desktop> (Get-Command Invoke-WebRequest).Name | Get-Member ⌨️

   TypeName: System.String

Name             MemberType            Definition
----             ----------            ----------
Clone            Method                System.Object Clone(), System.Object ICloneable.Clone()
CompareTo        Method                int CompareTo(System.Object value), int CompareTo(string strB), int IComparable.CompareTo(System.Object obj), in...
Contains         Method                bool Contains(string value)
CopyTo           Method                void CopyTo(int sourceIndex, char[] destination, int destinationIndex, int count)
EndsWith         Method                bool EndsWith(string value), bool EndsWith(string value, System.StringComparison comparisonType), bool EndsWith(... 
Equals           Method                bool Equals(System.Object obj), bool Equals(string value), bool Equals(string value, System.StringComparison com... 
GetEnumerator    Method                System.CharEnumerator GetEnumerator(), System.Collections.IEnumerator IEnumerable.GetEnumerator(), System.Collec... 
GetHashCode      Method                int GetHashCode()
GetType          Method                type GetType()
GetTypeCode      Method                System.TypeCode GetTypeCode(), System.TypeCode IConvertible.GetTypeCode()
IndexOf          Method                int IndexOf(char value), int IndexOf(char value, int startIndex), int IndexOf(char value, int startIndex, int co... 
IndexOfAny       Method                int IndexOfAny(char[] anyOf), int IndexOfAny(char[] anyOf, int startIndex), int IndexOfAny(char[] anyOf, int sta... 
Insert           Method                string Insert(int startIndex, string value)
IsNormalized     Method                bool IsNormalized(), bool IsNormalized(System.Text.NormalizationForm normalizationForm)
LastIndexOf      Method                int LastIndexOf(char value), int LastIndexOf(char value, int startIndex), int LastIndexOf(char value, int startI... 
LastIndexOfAny   Method                int LastIndexOfAny(char[] anyOf), int LastIndexOfAny(char[] anyOf, int startIndex), int LastIndexOfAny(char[] an... 
Normalize        Method                string Normalize(), string Normalize(System.Text.NormalizationForm normalizationForm)
PadLeft          Method                string PadLeft(int totalWidth), string PadLeft(int totalWidth, char paddingChar)
PadRight         Method                string PadRight(int totalWidth), string PadRight(int totalWidth, char paddingChar)
Remove           Method                string Remove(int startIndex, int count), string Remove(int startIndex)
Replace          Method                string Replace(char oldChar, char newChar), string Replace(string oldValue, string newValue)
Split            Method                string[] Split(Params char[] separator), string[] Split(char[] separator, int count), string[] Split(char[] sepa... 
StartsWith       Method                bool StartsWith(string value), bool StartsWith(string value, System.StringComparison comparisonType), bool Start... 
Substring        Method                string Substring(int startIndex), string Substring(int startIndex, int length)
ToBoolean        Method                bool IConvertible.ToBoolean(System.IFormatProvider provider)
ToByte           Method                byte IConvertible.ToByte(System.IFormatProvider provider)
ToChar           Method                char IConvertible.ToChar(System.IFormatProvider provider)
ToCharArray      Method                char[] ToCharArray(), char[] ToCharArray(int startIndex, int length)
ToDateTime       Method                datetime IConvertible.ToDateTime(System.IFormatProvider provider)
ToDecimal        Method                decimal IConvertible.ToDecimal(System.IFormatProvider provider)
ToDouble         Method                double IConvertible.ToDouble(System.IFormatProvider provider)
ToInt16          Method                int16 IConvertible.ToInt16(System.IFormatProvider provider)
ToInt32          Method                int IConvertible.ToInt32(System.IFormatProvider provider)
ToInt64          Method                long IConvertible.ToInt64(System.IFormatProvider provider)
ToLower          Method                string ToLower(), string ToLower(cultureinfo culture) 👀
ToLowerInvariant Method                string ToLowerInvariant()
ToSByte          Method                sbyte IConvertible.ToSByte(System.IFormatProvider provider)
ToSingle         Method                float IConvertible.ToSingle(System.IFormatProvider provider)
ToString         Method                string ToString(), string ToString(System.IFormatProvider provider), string IConvertible.ToString(System.IFormat... 
ToType           Method                System.Object IConvertible.ToType(type conversionType, System.IFormatProvider provider)
ToUInt16         Method                uint16 IConvertible.ToUInt16(System.IFormatProvider provider)
ToUInt32         Method                uint32 IConvertible.ToUInt32(System.IFormatProvider provider)
ToUInt64         Method                uint64 IConvertible.ToUInt64(System.IFormatProvider provider)
ToUpper          Method                string ToUpper(), string ToUpper(cultureinfo culture)
ToUpperInvariant Method                string ToUpperInvariant()
Trim             Method                string Trim(Params char[] trimChars), string Trim()
TrimEnd          Method                string TrimEnd(Params char[] trimChars)
TrimStart        Method                string TrimStart(Params char[] trimChars)
Chars            ParameterizedProperty char Chars(int index) {get;}
Length           Property              int Length {get;}

PS C:\users\century2\desktop> (Get-Command Invoke-WebRequest).Name | Get-Member "ToLow*" ⌨️

   TypeName: System.String

Name             MemberType Definition
----             ---------- ----------
ToLower          Method     string ToLower(), string ToLower(cultureinfo culture) 👀
ToLowerInvariant Method     string ToLowerInvariant()

PS C:\users\century2\desktop> (Get-Command Invoke-WebRequest).Name.ToLower() + (Get-ChildItem -File).Name ⌨️
invoke-webrequest443🔐

PS C:\users\century2\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century3@century.underthewire.tech -p 22 ⌨️
century3@century.underthewire.tech's password: ⌨️ invoke-webrequest443 
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century3\desktop> whoami ⌨️
underthewire\century3
```

## Flag
invoke-webrequest443 

## Continue
[Continue](./Century0203.md)