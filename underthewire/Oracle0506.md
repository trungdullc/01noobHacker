# Oracle Level 05 → 06 (Get-ADOrganizationalUnit -Filter 'Name -notlike "Groups"' -Properties * | Where-Object {-not $_.gPLink}).Name

## Previous Flag
```
charlie1337
```

## Goal
The password for oracle7 is the name of the OU that doesn’t have a GPO linked to it PLUS the name of the file on the user’s desktop.<br>

NOTE:<br>
– The password will be lowercase no matter how it appears on the screen.<br>
– Exclude the “Groups” OU.

## What I learned
```
(Get-ADOrganizationalUnit -Filter 'Name -notlike "Groups"' -Properties * | Where-Object {-not $_.gPLink}).Name
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle6@groot.underthewire.tech -p 22 ⌨️
oracle6@groot.underthewire.tech's password: ⌨️ charlie1337

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Oracle6\desktop> dir ⌨️

    Directory: C:\users\Oracle6\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018  10:50 AM              0 _97 👀

PS C:\users\Oracle6\desktop> Get-ADOrganizationalUnit -Filter 'Name -notlike "Groups"' -Properties * | Get-Member ⌨️

   TypeName: Microsoft.ActiveDirectory.Management.ADOrganizationalUnit

Name                            MemberType            Definition
----                            ----------            ----------
Contains                        Method                bool Contains(string propertyName)
Equals                          Method                bool Equals(System.Object obj)
GetEnumerator                   Method                System.Collections.IDictionaryEnumerator GetEnumerator()
GetHashCode                     Method                int GetHashCode()
GetType                         Method                type GetType()
ToString                        Method                string ToString()
Item                            ParameterizedProperty Microsoft.ActiveDirectory.Management.ADPropertyValueCollection Item(string propertyName) {get;}      
CanonicalName                   Property              System.String CanonicalName {get;}
City                            Property              System.String City {get;set;}
CN                              Property              System.String CN {get;}
Country                         Property              System.String Country {get;set;}
Created                         Property              System.DateTime Created {get;}
createTimeStamp                 Property              System.DateTime createTimeStamp {get;}
Deleted                         Property              System.Boolean Deleted {get;}
Description                     Property              System.String Description {get;set;}
DisplayName                     Property              System.String DisplayName {get;set;}
DistinguishedName               Property              System.String DistinguishedName {get;set;}
dSCorePropagationData           Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection dSCorePropagationData {get;}
gPLink                          Property              System.String gPLink {get;set;} 👀
instanceType                    Property              System.Int32 instanceType {get;}
isCriticalSystemObject          Property              System.Boolean isCriticalSystemObject {get;set;}
isDeleted                       Property              System.Boolean isDeleted {get;}
LastKnownParent                 Property              System.String LastKnownParent {get;}
LinkedGroupPolicyObjects        Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection LinkedGroupPolicyObjects {get;}       
ManagedBy                       Property              System.String ManagedBy {get;set;}
Modified                        Property              System.DateTime Modified {get;}
modifyTimeStamp                 Property              System.DateTime modifyTimeStamp {get;}
Name                            Property              System.String Name {get;}
nTSecurityDescriptor            Property              System.DirectoryServices.ActiveDirectorySecurity nTSecurityDescriptor {get;set;}
ObjectCategory                  Property              System.String ObjectCategory {get;}
ObjectClass                     Property              System.String ObjectClass {get;set;}
ObjectGUID                      Property              System.Nullable`1[[System.Guid, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c... 
ou                              Property              Microsoft.ActiveDirectory.Management.ADPropertyValueCollection ou {get;set;}
PostalCode                      Property              System.String PostalCode {get;set;}
ProtectedFromAccidentalDeletion Property              System.Boolean ProtectedFromAccidentalDeletion {get;set;}
sDRightsEffective               Property              System.Int32 sDRightsEffective {get;}
showInAdvancedViewOnly          Property              System.Boolean showInAdvancedViewOnly {get;set;}
State                           Property              System.String State {get;set;}
StreetAddress                   Property              System.String StreetAddress {get;set;}
systemFlags                     Property              System.Int32 systemFlags {get;}
uSNChanged                      Property              System.Int64 uSNChanged {get;}
uSNCreated                      Property              System.Int64 uSNCreated {get;}
whenChanged                     Property              System.DateTime whenChanged {get;}
whenCreated                     Property              System.DateTime whenCreated {get;}

PS C:\users\Oracle6\desktop> (Get-ADOrganizationalUnit -Filter 'Name -notlike "Groups"' -Properties * | Where-Object {-not $_.gPLink}).Name ⌨️
T-50 👀
PS C:\users\Oracle6\desktop> (Get-ADOrganizationalUnit -Filter 'Name -notlike "Groups"' -Properties * | Where-Object {-not $_.gPLink}).Name.ToLower() + (ls -File).Name ⌨️
t-50_97 🔐

PS C:\users\Oracle6\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh oracle7@groot.underthewire.tech -p 22 ⌨️
oracle7@groot.underthewire.tech's password: ⌨️ t-50_97

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\Oracle7\desktop> whoami ⌨️
underthewire\oracle7
```

## Flag
t-50_97

## Continue
[Continue](./Oracle0607.md)