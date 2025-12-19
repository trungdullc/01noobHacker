# OSI Model: 7 layer
```
Open System Interconnection Reference Model it explains how data moves thru network

All People Seem To Need Data Processing (Top-Down)          Please Do Not Throw Sausage Pizza Away (Bottom-Up)

Layer Name          Common Protocols / Standards	        What It Does
7 Application	    HTTP, HTTPS, FTP, SFTP, SMTP,           Provides network services to end-user applications
                    IMAP, POP3, DNS, DHCP, SNMP,            (web browsing, email, file transfer)
                    Telnet, SSH	
6 Presentation	    SSL/TLS, MIME, ASCII, JPEG, MP3,        Translates, encrypts, compresses data so apps can understand it
                    GIF, PNG                                (encryption, data formats)
5 Session	        NetBIOS, RPC, PPTP, SIP, RTCP	        Manages sessions between devices—opening, maintaining, 
                                                            and closing communication sessions (control and tunneling protocols)
4 Transport	        TCP segments, UDP datagram,	            Ensures reliable or best-effort data delivery, flow control, 
                    SCTP, DCCP                              segmentation, error control
3 Network	        IP, ICMP, ARP, RARP, OSPF, BGP,         Handles routing, addressing, packet forwarding between networks
                    RIP, IPv4/IPv6                          Frames fragmented (into smaller packets) to move btwn different networks (ethernet→WAN)
2 Data Link	        Ethernet (IEEE 802.3), Wi-Fi (802.11),  Ensures reliable link-to-link transfer, error detection (frames)
                    PPP, HDLC, ATM, Frame Relay, ARP        MAC (Media Access Control) Address
1 Physical	        Ethernet PHY, DSL, Fiber Optics,        Transmits raw bits over physical media (cables, radio waves, electrical signals)
                    RS-232, Bluetooth, USB, Wi-Fi Radio

TCP/IP (Transmission Control Protocol / Internet Protocol) is a set of communication protocols that allows computers and devices to connect and communicate over networks like the Internet.

How to learn about OSI better:
    Wireshark
    tshark

    Filezilla
    Putty
    Burp Suite
```

# Layer 1 Problems:
```
Problem                                     Fix (Solution)
Old / damaged cables	                    Replace cables
Loose punch-down connection	                Fix punch-down cables (re-terminate using punch-down tool)
Incorrect wiring order (T568A/B mismatch)	Re-punch the cable correctly using correct color code
Bent, crimped, or stretched cables	        Install new cable run (cable cannot be repaired)
Faulty NIC (Network Interface Card)	        Swap adapter cards or replace NIC
Bad patch panel port	                    Move to another port or replace that patch panel jack
Dirty or damaged fiber connectors	        Clean the fiber ends or replace fiber patch cable
Broken RJ-45 connector clip	                Re-crimp a new connector or replace cable
Crosstalk or interference	                Re-route cables, keep away from power lines, fluorescent lights
Bad cable termination (too much untwist)	Re-terminate properly while maintaining twist
Faulty switch/router port	                Swap port or test using another device
Bad Ethernet wall jack	                    Re-punch or replace keystone jack
Long cable runs exceeding length limits     Shorten cable or use a switch/repeater
(over 100m for copper)
Damaged fiber or kinked fiber	            Replace fiber cable
Loose SFP/SFP+ module	                    Reseat module or replace if faulty
Power issues on PoE devices	                Test cable, swap injector, or use a different PoE port
Bad cable shielding	                        Use shielded cable (STP) in high-interference areas
Faulty cable tester result	                Run loopback test or use a certified cable tester
Incorrect or missing grounding	            Properly ground racks and cables

What Is a Loopback Test?
A loopback test sends data from a device (NIC, switch port, router port, cable tester, serial port) back into itself to verify:
    The port works
    The transmit (TX) and receive (RX) pairs are functioning
    The cable is good
    There is no hardware failure

Software Loopback Test (Ping 127.0.0.1)
    ping 127.0.0.1
        Tests NIC drivers
        Tests TCP/IP stack
        Tests local networking functions
        Does not test the cable     Note: This does NOT test the cable or external port

    Checks	                        Explanation
    TCP/IP stack working	        Ensures Windows/Linux networking is functioning internally
    NIC driver installed correctly	Tests driver, not the physical NIC
    OS network services working	    Verifies internal network processes

    If it fails…	                The problem is likely…
    No replies	                    Corrupt TCP/IP stack
    100% packet loss	            NIC driver broken
    General failure	                OS networking failure

Hardware Loopback Test (Using RJ45 Loopback Plug)
    This tests the physical NIC, TX/RX pairs, and port hardware

    Turn off Wi-Fi (so you test wired only)
    Unplug the Ethernet cable
    Plug in an RJ45 loopback plug (or loopback tester) into the NIC
    Run a network diagnostic tool (Windows built-in NIC test or vendor tool)
    It sends signals out → signals return to NIC
    Check if test passes or fails

    Checks	                    Explanation
    NIC transmit function (TX)	Can the NIC send signals?
    NIC receive function (RX)	Can the NIC receive signals back?
    RJ45 port hardware	        Physically working pins and internal circuits
    Physical NIC chip	        Tests internal electronics
    Ethernet PHY layer	        Basic Layer 1 functionality

    If it fails…	            Likely problem
    TX error	                NIC cannot send data → damaged NIC
    RX error	                NIC cannot receive data → port failure
    No signal returned	        Broken NIC port or loopback plug not seated
    Link not detected	        Hardware dead or incorrect loopback wiring
    Intermittent signal	        Damaged port or electrical issue

Cable Tester Loopback (Testing Cable Only)
    Plug cable into tester main unit
    Plug other end into remote module
    Start test
    Tester sends signal out → loops it back via remote
    Results show wiring (1–8) and problems

    Checks
        Broken wire
        Split pair
        Shorts
        Miswiring
        Reversed pairs
        Cable length
        Signal quality

    Failures Indicate
        Bad cable termination
        Damaged or old cable
        Wrong wiring order (A/B mismatch)
        Shorts or opens
        Excessive cable length
```

# Layer 2: How to link the data from physical to IP Network Layer
```
MAC (Media Access Control) address is a unique hardware identifier (permanent, burned-in address) assigned to a network interface card (NIC)
It works at Layer 2 (Data Link Layer) of OSI model

It identifies a device on a local network (LAN, Wi-Fi, Ethernet)

Where MAC Addresses Are Used
    Ethernet networks
    Wi-Fi networks
    Switches for forwarding frames
    ARP for IP-to-MAC mapping
    Filtering, security, VLANs, and port-based authentication

Why It's Important
    Layer 2 devices like switches rely on MAC addresses to make forwarding decisions
    When a device sends a frame, it includes:
        Source MAC (sender)
        Destination MAC (receiver)
    Switches use this to build their MAC address table

MAC Address Structure
    A MAC address is 48 bits (6 bytes)
    First 3 bytes	        OUI (Organizationally Unique Identifier) → identifies manufacturer
    Last 3 bytes	        Device-specific ID assigned by manufacturer

    00:1B:44:11:3A:B7
    ^  ^  ^   ^  ^  ^
      OUI    Device ID

Types of MAC Addresses
    Type	        Meaning
    Unicast	        One-to-one (most common)
    Multicast	    One-to-many group communication
    Broadcast	    FF:FF:FF:FF:FF:FF → everyone on LAN

Is a MAC Address Permanent?
    Yes
    Hacker: can spoof it in software (not recommended unless needed for testing)

MAC Address vs IP Address
    MAC Address	                    IP Address
    Physical, burned into NIC	    Logical, assigned by DHCP or manually
    Layer 2	                        Layer 3
    Doesn't change on network	    Changes depending on network
    Local communication only	    Global communication (routing)
```

# Example: Mail OSI
```
Layer7  Application         https//mail.google.com
Layer6  Presentation        SSL encryption
Layer5  Session             Link transport to Presentation
Layer4  Trasnport           TCP encapsulation
Layer3  Network             IP encapsulation
Layer2  Data Link           Ethernet
Layer1  Physical            Electric Signal from data
```

# PDU (Protocol Data Unit)
```
What Is a PDU (Protocol Data Unit)?
A PDU is the package of data exchanged between network layers or devices, including:
    User data
    Protocol headers
    (Sometimes) trailers

Each OSI layer has a different name for its PDU

OSI Layer	            PDU Name	                        What It Contains
Layer 7 – Application	Data	                            Application data (HTTP request, email, file data)
Layer 6 – Presentation	Data	                            Formatted, encrypted, compressed data
Layer 5 – Session	    Data	                            Session control info
Layer 4 – Transport	    Segment (TCP) / Datagram (UDP)	    Port numbers, sequence numbers, error control
Layer 3 – Network	    Packet	                            Source & destination IP addresses
Layer 2 – Data Link	    Frame	                            MAC addresses, error detection (FCS)
Layer 1 – Physical	    Bits	                            Electrical/light/radio signals

# Visualization
+---------------------------------------------------------+
|                   Layer 2 : MAC / Ethernet              |
|              (physical addressing, frames)              |
|                                                         |
|   +-------------------------------------------------+   |
|   |                 Layer 3 : IP                    |   |
|   |            (routing, IP addressing)             |   |
|   |                                                 |   |
|   |   +-----------------------------------------+   |   |
|   |   |            Layer 4 : TCP / UDP          |   |   |
|   |   |     (ports, sequencing, reliability)    |   |   |
|   |   |                                         |   |   |
|   |   |   +---------------------------------+   |   |   |
|   |   |   |     Layers 5-7: Application /   |   |   |   |
|   |   |   |   Session / Presentation        |   |   |   |
|   |   |   |  (SSH, IMAP, HTTPS)             |   |   |   |
|   |   |   +---------------------------------+   |   |   |
|   |   +-----------------------------------------+   |   |
|   +-------------------------------------------------+   |
+---------------------------------------------------------+


How PDUs Are Created (Encapsulation)
    As data moves down the OSI stack:
        Application creates data                            Application Data
        Transport adds TCP/UDP header → segment             TCP Header + App Data
        Network adds IP header → packet                     IP Header + TCP Header + App Data
        Data Link adds MAC header & trailer → frame         Frame Header + IP + TCP + App Data + Frame Trailer
        Physical sends bits

On receive, the process is reversed (decapsulation)

Why PDUs Matter?
    Helps troubleshoot where a network failure occurs
    Explains how data changes across layers
    Used in exams (Network+, CCNA)
    Essential for packet analysis (Wireshark)

Example: Sending a web request:
    Application	        HTTP GET request
    Transport	        TCP segment (port 80/443)
    Network	            IP packet
    Data Link	        Ethernet frame
    Physical	        Bits on the wire

What Is Port 443?
Port 443 is used by HTTPS (Hypertext Transfer Protocol Secure), which is HTTP encrypted with TLS/SSL

Why we even need fragmentation since makes delivery slower?
The Maximum Transmission Unit (MTU) is the largest size of a single data packet or frame that a network protocol can transmit in one go without needing to fragment it
    Usually measured in bytes
    Depends on the network technology (Ethernet, Wi-Fi, etc.)

    Network Type	    Typical MTU
    Ethernet	        1500 bytes
    Wi-Fi (802.11)	    2304 bytes (max)
    PPP	1               492 bytes
    IPv6 Minimum	    1280 bytes

Test MTU using ping
    ping w/ Don't Fragment set and force a maximum size of 1472 byte
    Note: Have to calculate since ping doesn't
        1500 bytes: - 8 bytes ICMP header - 20 bytes IP address = 1472 bytes
    Windows:        ping -f -l 1472 8.8.8.8 (Google DNS Server)     # Should be able to send
    Linux/macOS:    ping -D -s 1472 8.8.8.8
```

# Network Topologies
```
Star (Hub and spoke) Topology
    All devices connected to central device (Hub/Router)
    Most common
Ring Topology
    Metro Area Networks (MANs)
    Wide Area Networks (WANs)
    Rarely used
Bus Topology
    Coaxial cable
    Old and worst than Ring since doesn't have loopback to fix disconnected point
    Automobiles uses CAN bus
        Controller Area Network
Mesh Topology
    Load balance Network
    Fault-tolerance Network
    Wide Area Networks (WANs)
    Popular as well
Hybrid Topology
    Combo 1 or more
    Most networks are hybrids

Wireless topology
    Infrastructure Topology
        All devices communicate through an access point
        Most common wireless communication
    Ad hoc networking Topology
        No pre-existing infrastructure
        Devices communication amongst themselves
    Mesh Topology
        Ad hoc devices work together to form a mesh "cloud"
```

# Network Types
```
Client-Server
    Central Server
Peer to Peer
    All devices are both clients and servers

LAN (Local Area Network)
    Local within building or group of building
    Ethernet or 802.11 wireless
MAN (Metropolitan Area Network)
    Smaller than WAN
    governement uses this
WAN (Wide Area Network)
    World-wide
    Point-to-point Serial
    WPLS (WAN Private Line Service) is a type of dedicated point-to-point WAN connection that connects two locations over a service provider’s network.

WLAN (Wireless LAN)
    802.11 technologies
PAN (Personal Area Network)
    Bluetooth                               # Phone, Headset, Speakers
    IR (Infrared)                           # TV remotes
    NFC (Near Field Communication)          # Payment Systems
CAN (Campus Area Network)
    Corporate Area Network

Network Attached Storage (NAS)
    Shared storage device across the network
Storage Area Network (SAN)
    Block level access (doesn't override like NAS)

MPLS (Multiprotocol Label Switching)
MPLS is a high-performance WAN data-carrying technique that directs data from one node to another based on short path labels rather than long network addresses (like IP)
    Works at a layer between Layer 2 (Data Link) and Layer 3 (Network) → sometimes called Layer 2.5
    Can carry multiple protocols (IP, ATM, Ethernet)
    Speeds up packet forwarding because routers/switches only read the label, not the full IP header

mGRE (Multipoint Generic Router Encapsulation)
    Used for Dynamic Multipoint VPN (DMVPN)
    common on Cisco routers

SD-WAN (Software Defined Networking)
    WAN build for the cloud
```

# Demarcation point (demarc)
```
point where you connect to world
    internet service provider
    customer premise equipment (CPE): router

Smartjack
    Network interface unit (NIU) installed so employee not need go directly in home router to troubleshoot
```

# Virtual Networks
```
Network functional virtualization (NFV)
NFV is a technology that replaces traditional physical network devices (like routers, firewalls, load balancers) with software-based virtualized versions running on standard servers

Instead of needing hundreds of physical devices, you can run many virtual network functions (VNFs) on a single physical server or network managed from the hypervisor

# hypervisor
Virtual Machine Manager
    A hypervisor is software that allows multiple virtual machines (VMs) to run on a single physical host.
    vSphere Client
    Types of Hypervisors:

    Type	            Description	                        Example
    Type 1 (Bare Metal)	Runs directly on physical hardware	VMware ESXi, Microsoft Hyper-V, KVM
    Type 2 (Hosted)	    Runs on top of a host OS	        VMware Workstation, VirtualBox

Virtual Switch
    A virtual switch is software that connects VMs to each other and to physical networks
    Works like a physical Ethernet switch, but entirely in software
    Enables VMs to communicate

vNIC (Virtual Network Interface Card)
```

# Provider Links
```
# Other ways to connect to internet
Satellite Networking/StarLink
    Non-terrestrial communication

Copper
    Coaxial Line
        Digital TV
        Cable Modem
    Twinaxial Cable
        10 Gigabit Ethernet
    Twisted Copper Line (4 Pairs)
        ADSL (Asymmetric Digital Subscriber Line)
            Uses telephone lines
        Cable Broadband
            Multiple frequencies
            DOCSIS (Data Over Cable Service Interface Specification)
Fiber Optic
    Frequency of light
Metro Ethernet (Metro-E)
    Metropoltan-area network uses ethernet

Structured Cabling Standards: International ISO/IEC 11801 cabling standards
    USA:    ANSI/TIA-568: Commercial Building Telecommunications Cabling Standards
    Ask building if using 568A or 568B standards
    https://www.smartechcables.com/media/magefan_blog/differencesbetweenwiringcodest568avst568b-ezgif.com-optiwebp.webp
```

# Copper Cabling
```
Copper Cable Categories

Copper cables are commonly twisted pair cables, classified by Category (Cat).

Category	Max Frequency	    Notes
Cat 3	    16 MHz	            Old, for 10 Mbps Ethernet (10Base-T)
Cat 5	    100 MHz	            Supports 100 Mbps (Fast Ethernet), sometimes 1 Gbps (short distances)
Cat 5e	    100 MHz	            Enhanced Cat 5, supports Gigabit Ethernet
Cat 6	    250 MHz	            Supports 1 Gbps up to 100 m, 10 Gbps up to 55 m
Cat 6a	    500 MHz	            Supports 10 Gbps up to 100 m
Cat 7	    600 MHz	            Shielded, supports 10 Gbps up to 100 m
Cat 8	    2000 MHz	        Supports 25–40 Gbps up to 30 m  

Ethernet Standards over Copper
Standard	                    Speed	        Max Distance	                Cable Type
10Base-T	                    10 Mbps	        100 m	                        Cat 3+
100Base-TX	                    100 Mbps	    100 m	                        Cat 5+
1000Base-T (Gigabit Ethernet)	1 Gbps	        100 m	                        Cat 5e+
10GBase-T	                    10 Gbps	        55 m (Cat 6), 100 m (Cat 6a)	Cat 6 / Cat 6a
25GBase-T	                    25 Gbps	        30 m	                        Cat 8
40GBase-T	                    40 Gbps	        30 m	                        Cat 8
```

# Optical Fiber
```
Transmission bylight
No Radio Frequency Signal (difficult to monitor or tap)

```