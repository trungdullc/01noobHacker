# Trebek Level 00 → 01 -Flags

## Previous Flag
```
trebek1
```

## Goal
The password for trebek2 is the name of the script referenced in a deleted task as depicted in the event logs on the desktop.<br>

NOTE:<br>
– Don’t include the file extension (i.e.- .vbs)<br>
– The password will be lowercase no matter how it appears on the screen.

## What I learned
```
([xml]$evt[-1].Message.Split("`n")[-12]).Arguments.Split('\\')[-1].Split('\.')[0].ToLower()
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek1@groot.underthewire.tech -p 22 ⌨️
trebek1@groot.underthewire.tech's password: ⌨️ trebek1

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\trebek1\desktop> dir ⌨️

    Directory: C:\users\trebek1\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:55 AM       99684352 security.evtx

PS C:\users\trebek1\desktop> Get-Command "Get-*Event*" ⌨️

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        Get-NetEventNetworkAdapter                         1.0.0.0    NetEventPacketCapture
Function        Get-NetEventPacketCaptureProvider                  1.0.0.0    NetEventPacketCapture
Function        Get-NetEventProvider                               1.0.0.0    NetEventPacketCapture
Function        Get-NetEventSession                                1.0.0.0    NetEventPacketCapture
Function        Get-NetEventVFPProvider                            1.0.0.0    NetEventPacketCapture
Function        Get-NetEventVmNetworkAdapter                       1.0.0.0    NetEventPacketCapture
Function        Get-NetEventVmSwitch                               1.0.0.0    NetEventPacketCapture
Function        Get-NetEventVmSwitchProvider                       1.0.0.0    NetEventPacketCapture
Function        Get-NetEventWFPCaptureProvider                     1.0.0.0    NetEventPacketCapture
Function        Get-SMServerEvent                                  1.0.0.0    ServerManagerTasks
Cmdlet          Get-Event                                          3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Get-EventLog                                       3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Get-EventSubscriber                                3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Get-WinEvent                                       3.0.0.0    Microsoft.PowerShell.Diagnostics 👀

PS C:\users\trebek1\desktop> Get-Help Get-WinEvent ⌨️
PS C:\users\trebek1\desktop> (Get-Command Get-WinEvent) | Get-Member ⌨️

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
Name                Property       string Name {get;}
Noun                Property       string Noun {get;}
Options             Property       System.Management.Automation.ScopedItemOptions Options {get;set;}
OutputType          Property       System.Collections.ObjectModel.ReadOnlyCollection[System.Management.Automation.PSTypeName] OutputType {get;}
Parameters          Property       System.Collections.Generic.Dictionary[string,System.Management.Automation.ParameterMetadata] Parameters {get;} 👀
ParameterSets       Property       System.Collections.ObjectModel.ReadOnlyCollection[System.Management.Automation.CommandParameterSetInfo] ParameterSet...
PSSnapIn            Property       System.Management.Automation.PSSnapInInfo PSSnapIn {get;}
RemotingCapability  Property       System.Management.Automation.RemotingCapability RemotingCapability {get;}
Source              Property       string Source {get;}
Verb                Property       string Verb {get;}
Version             Property       version Version {get;}

PS C:\users\trebek1\desktop> (Get-Command Get-WinEvent).Parameters ⌨️

Key                 Value
---                 -----
ListLog             System.Management.Automation.ParameterMetadata
LogName             System.Management.Automation.ParameterMetadata
ListProvider        System.Management.Automation.ParameterMetadata
ProviderName        System.Management.Automation.ParameterMetadata
Path                System.Management.Automation.ParameterMetadata
MaxEvents           System.Management.Automation.ParameterMetadata
ComputerName        System.Management.Automation.ParameterMetadata
Credential          System.Management.Automation.ParameterMetadata
FilterXPath         System.Management.Automation.ParameterMetadata 👀
FilterXml           System.Management.Automation.ParameterMetadata
FilterHashtable     System.Management.Automation.ParameterMetadata
Force               System.Management.Automation.ParameterMetadata
Oldest              System.Management.Automation.ParameterMetadata
Verbose             System.Management.Automation.ParameterMetadata
Debug               System.Management.Automation.ParameterMetadata
ErrorAction         System.Management.Automation.ParameterMetadata
WarningAction       System.Management.Automation.ParameterMetadata
InformationAction   System.Management.Automation.ParameterMetadata
ErrorVariable       System.Management.Automation.ParameterMetadata
WarningVariable     System.Management.Automation.ParameterMetadata
InformationVariable System.Management.Automation.ParameterMetadata
OutVariable         System.Management.Automation.ParameterMetadata
OutBuffer           System.Management.Automation.ParameterMetadata
PipelineVariable    System.Management.Automation.ParameterMetadata

PS C:\users\trebek1\desktop> (Get-Command Get-WinEvent).Parameters.Keys ⌨️
ListLog        
LogName        
ListProvider   
ProviderName   
Path
MaxEvents      
ComputerName   
Credential     
FilterXPath 👀
FilterXml      
FilterHashtable
Force
Oldest
Verbose
Debug
ErrorAction
WarningAction
InformationAction
ErrorVariable
WarningVariable
InformationVariable
OutVariable
OutBuffer
PipelineVariable

PS C:\users\trebek1\desktop> $evt = Get-WinEvent -Path .\security.evtx -FilterXPath "*[System[EventID=4699]]" ⌨️
PS C:\users\trebek1\desktop> Get-Variable evt ⌨️

Name                           Value
----                           -----
evt                            {System.Diagnostics.Eventing.Reader.EventLogRecord, System.Diagnostics.Eventing.Reader.EventLogRecord, System.Diagnostic... 

PS C:\users\trebek1\desktop> $evt.Message ⌨️
A scheduled task was deleted.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-500
        Account Name:           Administrator
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x338C9

Task Information:
        Task Name:              \Bitvise\Persistent BvSshServer Control Panel\S-1-5-21-3968311752-1263969649-2303472966-500
        Task Content:           <?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo />
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
      <LogonType>InteractiveToken</LogonType>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>Parallel</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>false</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>6</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Program Files\Bitvise SSH Server\BssCtrl.exe</Command>
      <Arguments>-startMinimized</Arguments>
    </Exec>
  </Actions>
</Task>

A scheduled task was deleted.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-500
        Account Name:           Administrator
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x74703

Task Information:
        Task Name:              \Bitvise\Persistent BvSshServer Control Panel\S-1-5-21-3968311752-1263969649-2303472966-500
        Task Content:           <?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo />
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
      <LogonType>InteractiveToken</LogonType>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>Parallel</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>false</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>6</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Program Files\Bitvise SSH Server\BssCtrl.exe</Command>
      <Arguments>-startMinimized</Arguments>
    </Exec>
  </Actions>
</Task>

A scheduled task was deleted.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-500
        Account Name:           Administrator
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x13069DD

Task Information:
        Task Name:              \Bitvise\Persistent BvSshServer Control Panel\S-1-5-21-3968311752-1263969649-2303472966-500
        Task Content:           <?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo />
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
      <LogonType>InteractiveToken</LogonType>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>Parallel</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>false</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>6</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Program Files\Bitvise SSH Server\BssCtrl.exe</Command>
      <Arguments>-startMinimized</Arguments>
    </Exec>
  </Actions>
</Task>

A scheduled task was deleted.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-500
        Account Name:           Administrator
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x12B5275

Task Information:
        Task Name:              \Bitvise\Persistent BvSshServer Control Panel\S-1-5-21-3968311752-1263969649-2303472966-500
        Task Content:           <?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo />
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
      <LogonType>InteractiveToken</LogonType>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>Parallel</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>false</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>6</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Program Files\Bitvise SSH Server\BssCtrl.exe</Command>
      <Arguments>-startMinimized</Arguments>
    </Exec>
  </Actions>
</Task>

A scheduled task was deleted.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-500
        Account Name:           Administrator
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x128CC45

Task Information:
        Task Name:              \Bitvise\Persistent BvSshServer Control Panel\S-1-5-21-3968311752-1263969649-2303472966-500
        Task Content:           <?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo />
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
      <LogonType>InteractiveToken</LogonType>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>Parallel</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>false</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>6</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Program Files\Bitvise SSH Server\BssCtrl.exe</Command>
      <Arguments>-startMinimized</Arguments>
    </Exec>
  </Actions>
</Task>

A scheduled task was deleted.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-500
        Account Name:           Administrator
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x12053FB

Task Information:
        Task Name:              \Bitvise\Persistent BvSshServer Control Panel\S-1-5-21-3968311752-1263969649-2303472966-500
        Task Content:           <?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo />
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
      <UserId>UNDERTHEWIRE\Administrator</UserId>
      <LogonType>InteractiveToken</LogonType>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>Parallel</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>false</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>6</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Program Files\Bitvise SSH Server\BssCtrl.exe</Command>
      <Arguments>-startMinimized</Arguments>
    </Exec>
  </Actions>
</Task>

A scheduled task was deleted.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1135
        Account Name:           trebek1
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x644A01

Task Information:
        Task Name:              \cleanup mess
        Task Content:           <?xml version="1.0" encoding="UTF-16"?>
<Task version="1.3" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo />
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>2017-05-10T01:00:00</StartBoundary>
      <Enabled>true</Enabled>
      <RandomDelay>P0DT0H0M0S</RandomDelay>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe</Command>
      <Arguments>-NonInteractive -NoLogo -NoProfile -File 'c:\users\trebek1\mess_cleaner.ps1'</Arguments>
    </Exec>
  </Actions>
  <Principals>
    <Principal id="Author">
      <UserId>UNDERTHEWIRE\trebek1</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
</Task>

PS C:\users\trebek1\desktop> $evt[-1].Message.Split("`n") ⌨️
A scheduled task was deleted.

Subject:
        Security ID:            S-1-5-21-3968311752-1263969649-2303472966-1135
        Account Name:           trebek1
        Account Domain:         UNDERTHEWIRE
        Logon ID:               0x644A01

Task Information:
        Task Name:              \cleanup mess
        Task Content:           <?xml version="1.0" encoding="UTF-16"?>
<Task version="1.3" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo />
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>2017-05-10T01:00:00</StartBoundary>
      <Enabled>true</Enabled>
      <RandomDelay>P0DT0H0M0S</RandomDelay>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <Duration>PT10M</Duration>
      <WaitTimeout>PT1H</WaitTimeout>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe</Command>
      <Arguments>-NonInteractive -NoLogo -NoProfile -File 'c:\users\trebek1\mess_cleaner.ps1'</Arguments>
    </Exec>
  </Actions>
  <Principals>
    <Principal id="Author">
      <UserId>UNDERTHEWIRE\trebek1</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
</Task>

PS C:\users\trebek1\desktop> $evt[-1].Message.Split("`n")[-12] ⌨️
      <Arguments>-NonInteractive -NoLogo -NoProfile -File 'c:\users\trebek1\mess_cleaner.ps1'</Arguments>

PS C:\users\trebek1\desktop> [xml]$evt[-1].Message.Split("`n")[-12] ⌨️

Arguments
---------
-NonInteractive -NoLogo -NoProfile -File 'c:\users\trebek1\mess_cleaner.ps1'

PS C:\users\trebek1\desktop> ([xml]$evt[-1].Message.Split("`n")[-12]).Arguments.Split('\\')[-1].Split('\.')[0].ToLower() ⌨️
mess_cleaner 🔐

PS C:\users\trebek1\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh trebek2@groot.underthewire.tech -p 22 ⌨️
trebek2@groot.underthewire.tech's password: ⌨️ mess_cleaner

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\trebek2\desktop> whoami ⌨️
underthewire\trebek2
```

## Flag
mess_cleaner

## Continue
[Continue](./Trebek0102.md)