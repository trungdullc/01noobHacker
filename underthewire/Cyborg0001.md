# Cyborg Level 00 → 01 Get-ADUser -Identity chris.rogers -Properties * | Format-List

## Previous Flag
```
cyborg1
```

## Goal
The password for cyborg2 is the state that the user Chris Rogers is from as stated within Active Directory.<br>

NOTE:<br>
– The password will be lowercase no matter how it appears on the screen.<br>
– “State” refers to the location within the country and NOT the “state” of the account (enabled/ disabled).

## What I learned
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> Get-Help Get-Module

With PowerShell, it's recommended to use the -Filter parameter where available, rather than pipe to Where-Object, as it's more efficient to have the filter apply at runtime, rather than piping all of the output to Where-Object

# List all modules currently loaded in the session
Get-Module

# List all modules installed and available to import
Get-Module -ListAvailable

Get-ADUser -Filter 'GivenName -eq "Chris" -and Surname -eq "Rogers"'
    Name: Rogers, Chris
    SamAccountName: chris.rogers

Get-ADUser -Identity chris.rogers -Properties * | Format-List
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg1@cyborg.underthewire.tech -p 22 ⌨️
cyborg1@cyborg.underthewire.tech's password: ⌨️ cyborg1

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\cyborg1\desktop> Get-Module ⌨️
PS C:\users\cyborg1\desktop> Get-Module -ListAvailable ⌨️

    Directory: C:\Program Files\WindowsPowerShell\Modules

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0.1      Microsoft.PowerShell.Operation.V... {Get-OperationValidation, Invoke-OperationValidation}
Binary     1.0.0.1    PackageManagement                   {Find-Package, Get-Package, Get-PackageProvider, Get-PackageSource...}
Script     3.4.0      Pester                              {Describe, Context, It, Should...}
Script     1.0.0.1    PowerShellGet                       {Install-Module, Find-Module, Save-Module, Update-Module...}
Script     1.2        PSReadline                          {Get-PSReadlineKeyHandler, Set-PSReadlineKeyHandler, Remove-PSReadlineKeyHandler, Get-PSReadlin... 
Script     1.0.6      PSSlack                             {Find-SlackMessage, Get-PSSlackConfig, Get-SlackAuth, Get-SlackChannel...}
Script     1.0.0      PSSlack                             {Find-SlackMessage, Get-PSSlackConfig, Get-SlackAuth, Get-SlackChannel...}
Script     0.1.3      PSSlack                             {Find-SlackMessage, Get-PSSlackConfig, Get-SlackAuth, Get-SlackChannel...}
Script     0.1.0      PSSlack                             {Find-SlackMessage, Get-PSSlackConfig, Get-SlackAuth, Get-SlackChannel...}

    Directory: C:\Windows\system32\WindowsPowerShell\v1.0\Modules

ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Manifest   1.0.0.0    ActiveDirectory                     {Add-ADCentralAccessPolicyMember, Add-ADComputerServiceAccount, Add-ADDomainControllerPasswordR... 
Manifest   1.0.0.0    ADDSDeployment                      {Add-ADDSReadOnlyDomainControllerAccount, Install-ADDSForest, Install-ADDSDomain, Install-ADDSD... 
Manifest   1.0.0.0    AppBackgroundTask                   {Disable-AppBackgroundTaskDiagnosticLog, Enable-AppBackgroundTaskDiagnosticLog, Set-AppBackgrou... 
Manifest   2.0.0.0    AppLocker                           {Get-AppLockerFileInformation, Get-AppLockerPolicy, New-AppLockerPolicy, Set-AppLockerPolicy...}   
Manifest   1.0.0.0    AppvClient                          {Add-AppvClientConnectionGroup, Add-AppvClientPackage, Add-AppvPublishingServer, Disable-Appv...}  
Manifest   2.0.0.0    Appx                                {Add-AppxPackage, Get-AppxPackage, Get-AppxPackageManifest, Remove-AppxPackage...}
Script     1.0.0.0    AssignedAccess                      {Clear-AssignedAccess, Get-AssignedAccess, Set-AssignedAccess}
Manifest   8.9.8.9    bacon                               Get-bacon
Manifest   1.0        BestPractices                       {Get-BpaModel, Get-BpaResult, Invoke-BpaModel, Set-BpaResult}
Manifest   2.0.0.0    BitsTransfer                        {Add-BitsFile, Complete-BitsTransfer, Get-BitsTransfer, Remove-BitsTransfer...}
Manifest   1.0.0.0    BranchCache                         {Add-BCDataCacheExtension, Clear-BCCache, Disable-BC, Disable-BCDowngrading...}
Manifest   1.0.0.0    CimCmdlets                          {Get-CimAssociatedInstance, Get-CimClass, Get-CimInstance, Get-CimSession...}
Manifest   1.0        ConfigCI                            {Get-SystemDriver, New-CIPolicyRule, New-CIPolicy, Get-CIPolicy...}
Manifest   1.0        ConfigDefender                      {Get-MpPreference, Set-MpPreference, Add-MpPreference, Remove-MpPreference...}
Manifest   1.0        ConfigDefenderPerformance           {New-MpPerformanceRecording, Get-MpPerformanceReport}
Manifest   1.0        Defender                            {Get-MpPreference, Set-MpPreference, Add-MpPreference, Remove-MpPreference...}
Manifest   1.0        DFSN                                {Get-DfsnRoot, Remove-DfsnRoot, Set-DfsnRoot, New-DfsnRoot...}
Binary     2.0.0.0    DFSR                                {New-DfsReplicationGroup, Get-DfsReplicationGroup, Set-DfsReplicationGroup, Remove-DfsReplicati... 
Manifest   1.0.0.0    DirectAccessClientComponents        {Disable-DAManualEntryPointSelection, Enable-DAManualEntryPointSelection, Get-DAClientExperienc...
Script     3.0        Dism                                {Add-AppxProvisionedPackage, Add-WindowsDriver, Add-WindowsCapability, Add-WindowsImage...}        
Manifest   1.0.0.0    DnsClient                           {Resolve-DnsName, Clear-DnsClientCache, Get-DnsClient, Get-DnsClientCache...}
Manifest   2.0.0.0    DnsServer                           {Add-DnsServerConditionalForwarderZone, Add-DnsServerDirectoryPartition, Add-DnsServerForwarder... 
Manifest   1.0.0.0    EventTracingManagement              {New-EtwTraceSession, Get-EtwTraceSession, Set-EtwTraceSession, Send-EtwTraceSession...}
Manifest   1.0.0.0    GroupPolicy                         {Backup-GPO, Block-GPInheritance, Copy-GPO, Get-GPInheritance...}
Script     1.0.0.0    IISAdministration                   {Get-IISAppPool, Start-IISCommitDelay, Stop-IISCommitDelay, Get-IISSite...}
Manifest   2.0.0.0    International                       {Get-WinDefaultInputMethodOverride, Set-WinDefaultInputMethodOverride, Get-WinHomeLocation, Set... 
Manifest   1.0.0.0    iSCSI                               {Get-IscsiTargetPortal, New-IscsiTargetPortal, Remove-IscsiTargetPortal, Update-IscsiTargetPort... 
Manifest   2.0.0.0    IscsiTarget                         {Add-ClusteriSCSITargetServerRole, Add-IscsiVirtualDiskTargetMapping, Checkpoint-IscsiVirtualDi... 
Script     1.0.0.0    ISE                                 {New-IseSnippet, Import-IseSnippet, Get-IseSnippet}
Manifest   1.0.0.0    Kds                                 {Add-KdsRootKey, Get-KdsRootKey, Test-KdsRootKey, Set-KdsConfiguration...}
Manifest   1.0.1.0    Microsoft.PowerShell.Archive        {Compress-Archive, Expand-Archive}
Manifest   3.0.0.0    Microsoft.PowerShell.Diagnostics    {Get-WinEvent, Get-Counter, Import-Counter, Export-Counter...}
Manifest   3.0.0.0    Microsoft.PowerShell.Host           {Start-Transcript, Stop-Transcript}
Manifest   1.0.0.0    Microsoft.PowerShell.LocalAccounts  {Add-LocalGroupMember, Disable-LocalUser, Enable-LocalUser, Get-LocalGroup...}
Manifest   3.1.0.0    Microsoft.PowerShell.Management     {Add-Content, Clear-Content, Clear-ItemProperty, Join-Path...}
Script     1.0        Microsoft.PowerShell.ODataUtils     Export-ODataEndpointProxy
Manifest   3.0.0.0    Microsoft.PowerShell.Security       {Get-Acl, Set-Acl, Get-PfxCertificate, Get-Credential...}
Manifest   3.1.0.0    Microsoft.PowerShell.Utility        {Format-List, Format-Custom, Format-Table, Format-Wide...}
Manifest   3.0.0.0    Microsoft.WSMan.Management          {Disable-WSManCredSSP, Enable-WSManCredSSP, Get-WSManCredSSP, Set-WSManQuickConfig...}
Manifest   1.0        MMAgent                             {Disable-MMAgent, Enable-MMAgent, Set-MMAgent, Get-MMAgent...}
Manifest   1.0.0.0    MsDtc                               {New-DtcDiagnosticTransaction, Complete-DtcDiagnosticTransaction, Join-DtcDiagnosticResourceMan... 
Manifest   2.0.0.0    NetAdapter                          {Disable-NetAdapter, Disable-NetAdapterBinding, Disable-NetAdapterChecksumOffload, Disable-NetA... 
Manifest   1.0.0.0    NetConnection                       {Get-NetConnectionProfile, Set-NetConnectionProfile}
Manifest   1.0.0.0    NetEventPacketCapture               {New-NetEventSession, Remove-NetEventSession, Get-NetEventSession, Set-NetEventSession...}
Manifest   2.0.0.0    NetLbfo                             {Add-NetLbfoTeamMember, Add-NetLbfoTeamNic, Get-NetLbfoTeam, Get-NetLbfoTeamMember...}
Manifest   1.0.0.0    NetNat                              {Get-NetNat, Get-NetNatExternalAddress, Get-NetNatStaticMapping, Get-NetNatSession...}
Manifest   2.0.0.0    NetQos                              {Get-NetQosPolicy, Set-NetQosPolicy, Remove-NetQosPolicy, New-NetQosPolicy}
Manifest   2.0.0.0    NetSecurity                         {Get-DAPolicyChange, New-NetIPsecAuthProposal, New-NetIPsecMainModeCryptoProposal, New-NetIPsec... 
Manifest   1.0.0.0    NetSwitchTeam                       {New-NetSwitchTeam, Remove-NetSwitchTeam, Get-NetSwitchTeam, Rename-NetSwitchTeam...}
Manifest   1.0.0.0    NetTCPIP                            {Get-NetIPAddress, Get-NetIPInterface, Get-NetIPv4Protocol, Get-NetIPv6Protocol...}
Manifest   1.0.0.0    NetworkConnectivityStatus           {Get-DAConnectionStatus, Get-NCSIPolicyConfiguration, Reset-NCSIPolicyConfiguration, Set-NCSIPo... 
Manifest   1.0.0.0    NetworkSwitchManager                {Disable-NetworkSwitchEthernetPort, Enable-NetworkSwitchEthernetPort, Get-NetworkSwitchEthernet... 
Manifest   1.0.0.0    NetworkTransition                   {Add-NetIPHttpsCertBinding, Disable-NetDnsTransitionConfiguration, Disable-NetIPHttpsProfile, D...
Manifest   1.0        NFS                                 {Get-NfsMappedIdentity, Get-NfsNetgroup, Install-NfsMappingStore, New-NfsMappedIdentity...}        
Manifest   1.0.0.0    PcsvDevice                          {Get-PcsvDevice, Start-PcsvDevice, Stop-PcsvDevice, Restart-PcsvDevice...}
Manifest   1.0.0.0    PKI                                 {Add-CertificateEnrollmentPolicyServer, Export-Certificate, Export-PfxCertificate, Get-Certific... 
Manifest   1.0.0.0    PlatformIdentifier                  Get-PlatformIdentifier
Manifest   1.0.0.0    PnpDevice                           {Get-PnpDevice, Get-PnpDeviceProperty, Enable-PnpDevice, Disable-PnpDevice}
Manifest   1.1.0.0    PowerShellWebAccess                 {Get-PswaAuthorizationRule, Add-PswaAuthorizationRule, Remove-PswaAuthorizationRule, Test-PswaA... 
Manifest   1.1        PrintManagement                     {Add-Printer, Add-PrinterDriver, Add-PrinterPort, Get-PrintConfiguration...}
Manifest   1.1        PSDesiredStateConfiguration         {Set-DscLocalConfigurationManager, Start-DscConfiguration, Test-DscConfiguration, Publish-DscCo...
Script     1.0.0.0    PSDiagnostics                       {Disable-PSTrace, Disable-PSWSManCombinedTrace, Disable-WSManTrace, Enable-PSTrace...}
Binary     1.1.0.0    PSScheduledJob                      {New-JobTrigger, Add-JobTrigger, Remove-JobTrigger, Get-JobTrigger...}
Manifest   2.0.0.0    PSWorkflow                          {New-PSWorkflowExecutionOption, New-PSWorkflowSession, nwsn}
Manifest   1.0.0.0    PSWorkflowUtility                   Invoke-AsWorkflow
Manifest   2.0.0.0    RemoteDesktop                       {Get-RDCertificate, Set-RDCertificate, New-RDCertificate, New-RDVirtualDesktopDeployment...}       
Manifest   1.0.0.0    ScheduledTasks                      {Get-ScheduledTask, Set-ScheduledTask, Register-ScheduledTask, Unregister-ScheduledTask...}        
Manifest   2.0.0.0    SecureBoot                          {Confirm-SecureBootUEFI, Set-SecureBootUEFI, Get-SecureBootUEFI, Format-SecureBootUEFI...}
Manifest   1.0.0.0    SecurityCmdlets                     {Backup-SecurityPolicy, Restore-SecurityPolicy, Backup-AuditPolicy, Restore-AuditPolicy}
Script     1.0.0.0    ServerCore                          {Get-DisplayResolution, Set-DisplayResolution}
Script     2.0.0.0    ServerManager                       {Get-WindowsFeature, Install-WindowsFeature, Uninstall-WindowsFeature, Enable-ServerManagerStan...
Cim        1.0.0.0    ServerManagerTasks                  {Get-SMCounterSample, Get-SMPerformanceCollector, Start-SMPerformanceCollector, Stop-SMPerforma... 
Manifest   2.0.0.0    SmbShare                            {Get-SmbShare, Remove-SmbShare, Set-SmbShare, Block-SmbShareAccess...}
Manifest   2.0.0.0    SmbWitness                          {Get-SmbWitnessClient, Move-SmbWitnessClient, gsmbw, msmbw...}
Manifest   2.0.0.0    SoftwareInventoryLogging            {Get-SilComputer, Get-SilComputerIdentity, Get-SilSoftware, Get-SilWindowsUpdate...}
Manifest   1.0.0.0    StartLayout                         {Export-StartLayout, Import-StartLayout, Get-StartApps}
Manifest   2.0.0.0    Storage                             {Add-InitiatorIdToMaskingSet, Add-PartitionAccessPath, Add-PhysicalDisk, Add-TargetPortToMaskin... 
Manifest   2.0.0.0    TLS                                 {New-TlsSessionTicketKey, Enable-TlsSessionTicketKey, Disable-TlsSessionTicketKey, Export-TlsSe... 
Manifest   1.0.0.0    TroubleshootingPack                 {Get-TroubleshootingPack, Invoke-TroubleshootingPack}
Manifest   2.0.0.0    TrustedPlatformModule               {Get-Tpm, Initialize-Tpm, Clear-Tpm, Unblock-Tpm...}
Binary     2.1.639.0  UEV                                 {Clear-UevConfiguration, Clear-UevAppxPackage, Restore-UevBackup, Set-UevTemplateProfile...}       
Manifest   1.0.0.0    UserAccessLogging                   {Enable-Ual, Disable-Ual, Get-Ual, Get-UalDns...}
Manifest   2.0.0.0    VpnClient                           {Add-VpnConnection, Set-VpnConnection, Remove-VpnConnection, Get-VpnConnection...}
Manifest   1.0.0.0    Wdac                                {Get-OdbcDriver, Set-OdbcDriver, Get-OdbcDsn, Add-OdbcDsn...}
Manifest   1.0.0.0    WebAdministration                   {Start-WebCommitDelay, Stop-WebCommitDelay, Get-WebConfigurationLock, Remove-WebConfigurationLo... 
Manifest   2.0.0.0    Whea                                {Get-WheaMemoryPolicy, Set-WheaMemoryPolicy}
Manifest   1.0.0.0    WindowsDeveloperLicense             {Get-WindowsDeveloperLicense, Unregister-WindowsDeveloperLicense, Show-WindowsDeveloperLicenseR... 
Script     1.0        WindowsErrorReporting               {Enable-WindowsErrorReporting, Disable-WindowsErrorReporting, Get-WindowsErrorReporting}
Manifest   1.0.0.0    WindowsSearch                       {Get-WindowsSearchSetting, Set-WindowsSearchSetting}
Manifest   1.0.0.0    WindowsUpdate                       Get-WindowsUpdateLog

PS C:\users\cyborg1\desktop> Get-ADUser -Filter 'GivenName -eq "Chris" -and Surname -eq "Rogers"' ⌨️

DistinguishedName : CN=Rogers\, Chris\ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Chris
Name              : Rogers, Chris
ObjectClass       : user
ObjectGUID        : ee6450f8-cf70-4b1d-b902-a837839632bd
SamAccountName    : chris.rogers 👀
SID               : S-1-5-21-758131494-606461608-3556270690-2177
Surname           : Rogers
UserPrincipalName : chris.rogers

PS C:\users\cyborg1\desktop> Get-ADUser -Identity chris.rogers -Properties * | Format-List ⌨️

AccountExpirationDate                :
accountExpires                       : 9223372036854775807
AccountLockoutTime                   :
AccountNotDelegated                  : False
AllowReversiblePasswordEncryption    : False
AuthenticationPolicy                 : {}
AuthenticationPolicySilo             : {}
BadLogonCount                        : 0
badPasswordTime                      : 0
badPwdCount                          : 0
CannotChangePassword                 : False
CanonicalName                        : underthewire.tech/X-Wing/T-65/Rogers, Chris 
Certificates                         : {}
City                                 :
CN                                   : Rogers, Chris
codePage                             : 0
Company                              :
CompoundIdentitySupported            : {}
Country                              :
countryCode                          : 0
Created                              : 8/30/2018 3:28:44 AM
createTimeStamp                      : 8/30/2018 3:28:44 AM
Deleted                              :
Department                           :
Description                          :
DisplayName                          : Rogers, Chris
DistinguishedName                    : CN=Rogers\, Chris\ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Division                             :
DoesNotRequirePreAuth                : False
dSCorePropagationData                : {1/1/1601 12:00:00 AM}
EmailAddress                         : chris.rogers@underthewire.tech
EmployeeID                           :
EmployeeNumber                       :
Enabled                              : False
Fax                                  :
GivenName                            : Chris
HomeDirectory                        :
HomedirRequired                      : False
HomeDrive                            :
HomePage                             :
HomePhone                            :
Initials                             :
instanceType                         : 4
isDeleted                            :
KerberosEncryptionType               : {}
LastBadPasswordAttempt               : 
LastKnownParent                      :
lastLogoff                           : 0
lastLogon                            : 0
LastLogonDate                        :
LockedOut                            : False
logonCount                           : 0
LogonWorkstations                    :
mail                                 : chris.rogers@underthewire.tech
Manager                              :
MemberOf                             : {}
MNSLogonAccount                      : False
MobilePhone                          :
Modified                             : 11/18/2018 8:43:51 PM
modifyTimeStamp                      : 11/18/2018 8:43:51 PM
msDS-User-Account-Control-Computed   : 8388608
Name                                 : Rogers, Chris
nTSecurityDescriptor                 : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                       : CN=Person,CN=Schema,CN=Configuration,DC=underthewire,DC=tech
ObjectClass                          : user
ObjectGUID                           : ee6450f8-cf70-4b1d-b902-a837839632bd
objectSid                            : S-1-5-21-758131494-606461608-3556270690-2177
Office                               :
OfficePhone                          :
Organization                         :
OtherName                            :
PasswordExpired                      : True
PasswordLastSet                      :
PasswordNeverExpires                 : False
PasswordNotRequired                  : False
POBox                                :
PostalCode                           :
PrimaryGroup                         : CN=Domain Users,CN=Users,DC=underthewire,DC=tech
primaryGroupID                       : 513
PrincipalsAllowedToDelegateToAccount : {}
ProfilePath                          :
ProtectedFromAccidentalDeletion      : False
pwdLastSet                           : 0
SamAccountName                       : chris.rogers 👀
sAMAccountType                       : 805306368
ScriptPath                           :
sDRightsEffective                    : 0
ServicePrincipalNames                : {}
SID                                  : S-1-5-21-758131494-606461608-3556270690-2177
SIDHistory                           : {}
SmartcardLogonRequired               : False
sn                                   : Rogers
st                                   : kansas
State                                : kansas 🔐
StreetAddress                        :
Surname                              : Rogers
Title                                :
TrustedForDelegation                 : False
TrustedToAuthForDelegation           : False
UseDESKeyOnly                        : False
userAccountControl                   : 514
userCertificate                      : {}
UserPrincipalName                    : chris.rogers
uSNChanged                           : 38765
uSNCreated                           : 19675
whenChanged                          : 11/18/2018 8:43:51 PM
whenCreated                          : 8/30/2018 3:28:44 AM

PS C:\users\cyborg1\desktop> Get-ADUser -Identity chris.rogers -Properties st | Select-Object Name, st ⌨️

Name           st
----           --
Rogers, Chris  kansas 🔐

PS C:\users\cyborg1\desktop> Get-ADUser -Filter 'GivenName -eq "Chris" -and Surname -eq "Rogers"' -Properties State ⌨️

DistinguishedName : CN=Rogers\, Chris\ ,OU=T-65,OU=X-Wing,DC=underthewire,DC=tech
Enabled           : False
GivenName         : Chris
Name              : Rogers, Chris
ObjectClass       : user
ObjectGUID        : ee6450f8-cf70-4b1d-b902-a837839632bd
SamAccountName    : chris.rogers
SID               : S-1-5-21-758131494-606461608-3556270690-2177
State             : kansas 🔐
Surname           : Rogers
UserPrincipalName : chris.rogers

PS C:\users\cyborg1\desktop> exit ⌨️
Connection to cyborg.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh cyborg2@cyborg.underthewire.tech -p 22 ⌨️
cyborg2@cyborg.underthewire.tech's password: ⌨️ kansas

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg2\desktop> whoami ⌨️
underthewire\cyborg2
```

## Flag
kansas

## Continue
[Continue](./Cyborg0102.md)