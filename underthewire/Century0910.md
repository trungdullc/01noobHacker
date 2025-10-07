# Century Level 09 → 10 service --status-all

## Previous Flag
```
pierid
```

## Goal
The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.<br>

NOTE:<br>
– The password will be lowercase no matter how it appears on the screen<br>
– If the 10th and 8th word of the service description is “apple” and “juice” and the name of the file on the desktop is “88”, the password would be “applejuice88”

## What I learned
```
Get-Service                         systemctl list-units --type=service --state=running
                                    service --status-all
Get-Service wuauserv | Get-Member
Get-WmiObject -Query "select * from win32_service where name='wuauserv'" | Select-Object *
Get-CimInstance Win32_Service -Filter "Name='wuauserv'" | Select-Object Name, DisplayName, Description

                                    sudo systemctl start ssh
                                    sudo systemctl stop ssh
                                    sudo systemctl restart ssh
                                    sudo systemctl status ssh
                                    service ssh status

Web & Application
    apache2 / httpd → Apache web server
    nginx → Lightweight web server & reverse proxy
    tomcat → Java application server
    php-fpm → PHP FastCGI Process Manager

Database
    mysql / mariadb → Relational databases
    postgresql → Popular open-source SQL database
    mongodb → NoSQL document database
    redis → In-memory key/value store

Networking
    ssh / sshd → Secure Shell (remote login)
    vsftpd / proftpd → FTP servers
    samba → Windows file sharing (SMB/CIFS)
    bind9 / named → DNS server
    dhcpd → DHCP server

Mail
    postfix → Mail Transfer Agent (MTA)
    exim → Alternative MTA
    dovecot → IMAP/POP3 server

System & Monitoring
    cron → Scheduled jobs
    rsyslog / syslog → Logging service
    fail2ban → Security / intrusion prevention
    firewalld / ufw → Firewall management
    docker → Container runtime
    kubelet → Kubernetes node agent
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century10@century.underthewire.tech -p 22 ⌨️
century10@century.underthewire.tech's password: ⌨️ pierid
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century10\desktop> dir ⌨️

    Directory: C:\users\century10\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:34 AM             43 110 👀

PS C:\users\century10\desktop> Get-Service ⌨️

Status   Name               DisplayName
------   ----               -----------
Running  ADWS               Active Directory Web Services
Stopped  AJRouter           AllJoyn Router Service
Stopped  ALG                Application Layer Gateway Service     
Running  Appinfo            Application Information
Stopped  AppMgmt            Application Management
Stopped  AppReadiness       App Readiness
Stopped  AppVClient         Microsoft App-V Client
Stopped  AudioEndpointBu... Windows Audio Endpoint Builder        
Stopped  Audiosrv           Windows Audio
Stopped  AxInstSV           ActiveX Installer (AxInstSV)
Running  BFE                Base Filtering Engine
Stopped  BITS               Background Intelligent Transfer Ser...
Running  BrokerInfrastru... Background Tasks Infrastructure Ser...
Stopped  Browser            Computer Browser
Stopped  bthserv            Bluetooth Support Service
Running  BvSshServer        Bitvise SSH Server
Stopped  C-3PO              C-3PO
Running  CDPSvc             Connected Devices Platform Service
Stopped  ClipSVC            Client License Service (ClipSVC)
Stopped  COMSysApp          COM+ System Application
Running  CryptSvc           Cryptographic Services
Stopped  CscService         Offline Files
Running  DcomLaunch         DCOM Server Process Launcher
Stopped  DcpSvc             DataCollectionPublishingService
Stopped  defragsvc          Optimize drives
Stopped  DeviceAssociati... Device Association Service
Stopped  DeviceInstall      Device Install Service
Stopped  DevQueryBroker     DevQuery Background Discovery Broker
Running  Dfs                DFS Namespace
Running  DFSR               DFS Replication
Running  Dhcp               DHCP Client
Stopped  diagnosticshub.... Microsoft (R) Diagnostics Hub Stand...
Running  DiagTrack          Connected User Experiences and Tele...
Stopped  DmEnrollmentSvc    Device Management Enrollment Service
Stopped  dmwappushservice   dmwappushsvc
Running  DNS                DNS Server
Running  Dnscache           DNS Client
Stopped  dot3svc            Wired AutoConfig
Stopped  DsmSvc             Device Setup Manager
Stopped  DsRoleSvc          DS Role Server
Running  DsSvc              Data Sharing Service
Stopped  Eaphost            Extensible Authentication Protocol
Stopped  EFS                Encrypting File System (EFS)
Running  EventLog           Windows Event Log
Running  EventSystem        COM+ Event System
Stopped  fdPHost            Function Discovery Provider Host
Stopped  FDResPub           Function Discovery Resource Publica...
Running  FontCache          Windows Font Cache Service
Stopped  FrameServer        Windows Camera Frame Server
Stopped  hidserv            Human Interface Device Service
Stopped  HvHost             HV Host Service
Stopped  i_heart_robots     i_heart_robots
Stopped  icssvc             Windows Mobile Hotspot Service
Stopped  IKEEXT             IKE and AuthIP IPsec Keying Modules
Running  iphlpsvc           IP Helper
Running  IsmServ            Intersite Messaging
Running  Kdc                Kerberos Key Distribution Center
Stopped  KdsSvc             Microsoft Key Distribution Service
Running  KeyIso             CNG Key Isolation
Stopped  KPSSVC             KDC Proxy Server service (KPS)
Stopped  KtmRm              KtmRm for Distributed Transaction C...
Running  LanmanServer       Server
Running  LanmanWorkstation  Workstation
Stopped  lfsvc              Geolocation Service
Stopped  LicenseManager     Windows License Manager Service
Stopped  lltdsvc            Link-Layer Topology Discovery Mapper
Running  lmhosts            TCP/IP NetBIOS Helper
Running  LSM                Local Session Manager
Stopped  MapsBroker         Downloaded Maps Manager
Running  MDCoreSvc          Microsoft Defender Core Service
Running  MpsSvc             Windows Firewall
Running  MSDTC              Distributed Transaction Coordinator
Stopped  MSiSCSI            Microsoft iSCSI Initiator Service
Stopped  NcaSvc             Network Connectivity Assistant
Running  NcbService         Network Connection Broker
Running  Netlogon           Netlogon
Stopped  Netman             Network Connections
Running  netprofm           Network List Service
Stopped  NetSetupSvc        Network Setup Service
Stopped  NetTcpPortSharing  Net.Tcp Port Sharing Service
Stopped  NgcCtnrSvc         Microsoft Passport Container
Stopped  NgcSvc             Microsoft Passport
Running  NlaSvc             Network Location Awareness
Running  nsi                Network Store Interface Service
Running  NTDS               Active Directory Domain Services
Stopped  NtFrs              File Replication
Running  OneSyncSvc_657e663 Sync Host_657e663
Running  PcaSvc             Program Compatibility Assistant Ser...
Stopped  PerfHost           Performance Counter DLL Host
Stopped  PhoneSvc           Phone Service
Stopped  PimIndexMainten... Contact Data_657e663
Stopped  pla                Performance Logs & Alerts
Running  PlugPlay           Plug and Play
Running  PolicyAgent        IPsec Policy Agent
Running  Power              Power
Stopped  PrintNotify        Printer Extensions and Notifications
Running  ProfSvc            User Profile Service
Stopped  QWAVE              Quality Windows Audio Video Experience
Stopped  RasAuto            Remote Access Auto Connection Manager
Stopped  RasMan             Remote Access Connection Manager
Stopped  RemoteAccess       Routing and Remote Access
Stopped  RemoteRegistry     Remote Registry
Stopped  RmSvc              Radio Management Service
Running  RpcEptMapper       RPC Endpoint Mapper
Stopped  RpcLocator         Remote Procedure Call (RPC) Locator
Running  RpcSs              Remote Procedure Call (RPC)
Stopped  RSoPProv           Resultant Set of Policy Provider
Stopped  sacsvr             Special Administration Console Helper
Running  SamSs              Security Accounts Manager
Running  Schedule           Task Scheduler
Running  seclogon           Secondary Logon
Running  SENS               System Event Notification Service
Stopped  SensorDataService  Sensor Data Service
Stopped  SensorService      Sensor Service
Stopped  SensrSvc           Sensor Monitoring Service
Running  SessionEnv         Remote Desktop Configuration
Stopped  SharedAccess       Internet Connection Sharing (ICS)
Running  ShellHWDetection   Shell Hardware Detection
Stopped  smphost            Microsoft Storage Spaces SMP
Stopped  SNMPTRAP           SNMP Trap
Stopped  Spooler            Print Spooler
Stopped  sppsvc             Software Protection
Stopped  SSDPSRV            SSDP Discovery
Stopped  SstpSvc            Secure Socket Tunneling Protocol Se...
Stopped  stisvc             Windows Image Acquisition (WIA)
Stopped  StorSvc            Storage Service
Stopped  svsvc              Spot Verifier
Stopped  swprv              Microsoft Software Shadow Copy Prov...
Stopped  SysMain            Superfetch
Running  SystemEventsBroker System Events Broker
Running  TabletInputService Touch Keyboard and Handwriting Pane...
Stopped  TapiSrv            Telephony
Running  TermService        Remote Desktop Services
Running  Themes             Themes
Stopped  TieringEngineSe... Storage Tiers Management
Running  TimeBrokerSvc      Time Broker
Stopped  TrkWks             Distributed Link Tracking Client
Stopped  tzautoupdate       Auto Time Zone Updater
Running  UALSVC             User Access Logging Service
Stopped  UevAgentService    User Experience Virtualization Service
Stopped  UI0Detect          Interactive Services Detection
Running  UmRdpService       Remote Desktop Services UserMode Po...
Stopped  UnistoreSvc_657... User Data Storage_657e663
Stopped  upnphost           UPnP Device Host
Stopped  UserDataSvc_657... User Data Access_657e663
Running  UserManager        User Manager
Stopped  UsoSvc             Update Orchestrator Service for Win...
Running  VaultSvc           Credential Manager
Running  vds                Virtual Disk
Stopped  vmicguestinterface Hyper-V Guest Service Interface       
Stopped  vmicheartbeat      Hyper-V Heartbeat Service
Stopped  vmickvpexchange    Hyper-V Data Exchange Service
Stopped  vmicrdv            Hyper-V Remote Desktop Virtualizati...
Stopped  vmicshutdown       Hyper-V Guest Shutdown Service
Stopped  vmictimesync       Hyper-V Time Synchronization Service
Stopped  vmicvmsession      Hyper-V PowerShell Direct Service
Stopped  vmicvss            Hyper-V Volume Shadow Copy Requestor
Stopped  VSS                Volume Shadow Copy
Running  W32Time            Windows Time
Stopped  WalletService      WalletService
Stopped  WbioSrvc           Windows Biometric Service
Running  Wcmsvc             Windows Connection Manager
Running  WdNisSvc           Microsoft Defender Antivirus Networ...
Stopped  Wecsvc             Windows Event Collector
Stopped  WEPHOSTSVC         Windows Encryption Provider Host Se...
Stopped  wercplsupport      Problem Reports and Solutions Contr...
Stopped  WerSvc             Windows Error Reporting Service
Stopped  WiaRpc             Still Image Acquisition Events
Running  WinDefend          Microsoft Defender Antivirus Service  
Running  WinHttpAutoProx... WinHTTP Web Proxy Auto-Discovery Se...
Running  Winmgmt            Windows Management Instrumentation
Stopped  WinRM              Windows Remote Management (WS-Manag...
Stopped  wisvc              Windows Insider Service
Stopped  wlidsvc            Microsoft Account Sign-in Assistant
Stopped  wmiApSrv           WMI Performance Adapter
Stopped  WPDBusEnum         Portable Device Enumerator Service
Running  WpnService         Windows Push Notifications System S...
Stopped  WpnUserService_... Windows Push Notifications User Ser...
Running  WSearch            Windows Search
Stopped  wuauserv           Windows Update 👀
Running  wudfsvc            Windows Driver Foundation - User-mo...
Stopped  XblAuthManager     Xbox Live Auth Manager
Stopped  XblGameSave        Xbox Live Game Save

PS C:\users\century10\desktop> Get-Service wuauserv ⌨️

Status   Name               DisplayName
------   ----               -----------
Stopped  wuauserv           Windows Update 👀

PS C:\users\century10\desktop> Get-Service wuauserv | Get-Member ⌨️

   TypeName: System.ServiceProcess.ServiceController

Name                      MemberType    Definition
----                      ----------    ----------
Name                      AliasProperty Name = ServiceName
RequiredServices          AliasProperty RequiredServices = ServicesDependedOn
Disposed                  Event         System.EventHandler Disposed(System.Object, System.EventArgs)
Close                     Method        void Close()
Continue                  Method        void Continue()
CreateObjRef              Method        System.Runtime.Remoting.ObjRef CreateObjRef(type requestedType)
Dispose                   Method        void Dispose(), void IDisposable.Dispose()
Equals                    Method        bool Equals(System.Object obj)
ExecuteCommand            Method        void ExecuteCommand(int command)
GetHashCode               Method        int GetHashCode()
GetLifetimeService        Method        System.Object GetLifetimeService()
GetType                   Method        type GetType()
InitializeLifetimeService Method        System.Object InitializeLifetimeService()
Pause                     Method        void Pause()
Refresh                   Method        void Refresh()
Start                     Method        void Start(), void Start(string[] args)
Stop                      Method        void Stop()
WaitForStatus             Method        void WaitForStatus(System.ServiceProcess.ServiceControllerStatus desiredStatus), void WaitForStatus(System.... 
CanPauseAndContinue       Property      bool CanPauseAndContinue {get;}
CanShutdown               Property      bool CanShutdown {get;}
CanStop                   Property      bool CanStop {get;}
Container                 Property      System.ComponentModel.IContainer Container {get;}
DependentServices         Property      System.ServiceProcess.ServiceController[] DependentServices {get;}
DisplayName               Property      string DisplayName {get;set;}
MachineName               Property      string MachineName {get;set;}
ServiceHandle             Property      System.Runtime.InteropServices.SafeHandle ServiceHandle {get;}
ServiceName               Property      string ServiceName {get;set;}
ServicesDependedOn        Property      System.ServiceProcess.ServiceController[] ServicesDependedOn {get;}
ServiceType               Property      System.ServiceProcess.ServiceType ServiceType {get;}
Site                      Property      System.ComponentModel.ISite Site {get;set;}
StartType                 Property      System.ServiceProcess.ServiceStartMode StartType {get;}
Status                    Property      System.ServiceProcess.ServiceControllerStatus Status {get;}
ToString                  ScriptMethod  System.Object ToString();

PS C:\users\century10\desktop> Get-WmiObject -Query "select * from win32_service where name='wuauserv'" | Select-Object * ⌨️

PSComputerName          : UTW
Name                    : wuauserv
Status                  : OK
ExitCode                : 0
DesktopInteract         : False
ErrorControl            : Normal
PathName                : C:\Windows\system32\svchost.exe -k netsvcs
ServiceType             : Share Process
StartMode               : Manual
__GENUS                 : 2
__CLASS                 : Win32_Service
__SUPERCLASS            : Win32_BaseService
__DYNASTY               : CIM_ManagedSystemElement
__RELPATH               : Win32_Service.Name="wuauserv"
__PROPERTY_COUNT        : 26
__DERIVATION            : {Win32_BaseService, CIM_Service, CIM_LogicalElement, CIM_ManagedSystemElement}
__SERVER                : UTW
__NAMESPACE             : root\cimv2
__PATH                  : \\UTW\root\cimv2:Win32_Service.Name="wuauserv"
AcceptPause             : False
AcceptStop              : False
Caption                 : Windows Update
CheckPoint              : 0
CreationClassName       : Win32_Service
DelayedAutoStart        : False
Description             : Enables the detection, download, and installation of updates 👀 for Windows 👀 and other programs. If this service is disabled,    
                          users of this computer will not be able to use Windows Update or its automatic updating feature, and programs will not be    
                          able to use the Windows Update Agent (WUA) API.
DisplayName             : Windows Update
InstallDate             :
ProcessId               : 0
ServiceSpecificExitCode : 0
Started                 : False
StartName               : LocalSystem
State                   : Stopped
SystemCreationClassName : Win32_ComputerSystem
SystemName              : UTW
TagId                   : 0
WaitHint                : 0
Scope                   : System.Management.ManagementScope
Path                    : \\UTW\root\cimv2:Win32_Service.Name="wuauserv"
Options                 : System.Management.ObjectGetOptions
ClassPath               : \\UTW\root\cimv2:Win32_Service
Properties              : {AcceptPause, AcceptStop, Caption, CheckPoint...}
SystemProperties        : {__GENUS, __CLASS, __SUPERCLASS, __DYNASTY...}
Qualifiers              : {dynamic, Locale, provider, UUID}
Site                    :
Container               :

PS C:\users\century10\desktop> Get-CimInstance Win32_Service -Filter "Name='wuauserv'" | Select-Object Name, DisplayName, Description ⌨️

Name     DisplayName    Description
----     -----------    -----------
wuauserv Windows Update Enables the detection, download, and installation of updates 👀 for Windows 👀 and other programs. If this service is disabled, u...

PS C:\users\century10\desktop> (Get-CimInstance win32_service -Filter 'DisplayName like "Windows Update"').Description.Split(' ')[9,7].ToLower() + (ls -File).Name ⌨️
windows
updates
110
PS C:\users\century10\desktop> -join((Get-CimInstance win32_service -Filter 'DisplayName like "Windows Update"').Description.Split(' ')[9,7].ToLower() + (ls -File).Name) ⌨️
windowsupdates110 🔐

PS C:\users\century10\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century11@century.underthewire.tech -p 22 ⌨️
century11@century.underthewire.tech's password: ⌨️ windowsupdates110

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century11\desktop> whoami ⌨️
underthewire\century11
```

## Flag
windowsupdates110

## Continue
[Continue](./Century1011.md)