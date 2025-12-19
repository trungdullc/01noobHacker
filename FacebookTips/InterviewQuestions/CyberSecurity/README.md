# Cyber Security Interview Questions
# Source: https://applyre.com/resources
```
Q: What is cybersecurity?
A: Cybersecurity is the practice of protecting systems, networks, and data from attacks.

Q: What are the main goals of cybersecurity (CIA triad)?
A: Confidentiality, Integrity, and Availability.

Q: What is the difference between threat, vulnerability, and risk?
A: A threat causes harm, vulnerability is a weakness, and risk is the potential impact.

Q: What is the difference between black hat, white hat, and grey hat hackers?
A: Black hats are malicious, white hats are ethical, and grey hats are in-between.

Q: What are common types of cyber attacks?
A: Phishing, malware, DDOS, ransomware, and SQL injection.

Q: What is malware? Name its types.
A: Malware is malicious software like viruses, worms, trojans, and ransomware.

Q: What is ransomware and how does it work?
A: Ransomware encrypts files and demands payment for decryption.

Q: What is phishing?
A: Phishing is tricking users into revealing sensitive information via fake messages.

Q: What is a brute-force attack?
A: It's trying many password until one works.

Q: What is the difference between DoS and DDoS attacks?
A: DoS uses one system, DDoS uses multiple systems to flood a target.

Q: What is a SOC?
A: A Security Operations Center monitors and defends an organization's network.

Q: What does a SOC analyst do?
A: A SOC analyst detects, analyzes, and responds to security incidents.

Q: What are Tier 1 , Tier 2, and Tier 3 levels?
A: Tier 1 monitors, Tier 2 investigates, Tier 3 handles deep analysis.

Q: What is an incident?
A: An event that could harm systems or data security.

Q: What is incident response?
A: The process of managing and mitigating a security incident.

Q: What is an IOC (Indicator of Compromise)?
A: A sign that a system may be compromised.

Q: What are SIEM tools?
A: Tools that collect and analyze security logs for threats.

Q: Give examples of popular SIEM tools.
A: Splunk, QRadar, ArcSight, and ELK Stack.

Q: What is log analysis in SOC?
A: Reviewing logs to find suspicious or abnormal activities.

Q: What is the purpose of correlation rules in SIEM?
A: To detect attack patterns across multiple events.

Q: What is the OSI model?
A: A 7-layer model describing how data moves through a network.

Q: What is the difference between TCP and UDP?
A: TCP is reliable and connection-based; UDP is faster and connectionless.

Q: What are IP, MAC, and DNS?
A: IP identifies devices, MAC identifies hardware, DNS translates domain names.

Q: What is a firewall?
A: A device or software that filters network traffic based on rules.

Q: What are types of firewalls?
A: Packet-filtering, proxy, stateful, and next-gen firewalls.

Q: What is an IDS and IPS?
A: IDS detects attacks; IPS detects and blocks them.

Q: What is port scanning?
A: Checking open ports on a system for vulnerabilities.

Q: What is a proxy server?
A: A server that forwards requests between a user and the intemet.

Q: What is NAT?
A: Network Address Translation maps private IPs to public IPs.

Q: What is VLAN and why is it used?
A: A VLAN divides networks for better security and performance.

Q: What are some basic Linux commands?
A: Is, pwd, mkdir, rm, cat, cp, mv.

Q: How to check network connections in Linux?
A: Use the netstat or ss

Q: What does the chmod do?
A: Changes file permissions in Linux.

Q: How can you see currently running processes?
A: Use ps or top

Q: What is used to view system logs?
A: Use tail or cat on /var/log files.

Q: How do you find a file in Linux?
A: Use the find or locate

Q: What is the difference between absolute and relative paths?
A: Absolute starts from root; relative starts from current directory.

Q: How can you check disk usage in Linux?
A: Use df -h or du -h command.

Q: What command is used to monitor network traffic?
A: Use tcpdump

Q: How do you check active network ports in Linux?
A: Use netstat -tuln or ss -Int.

Q: What is Wireshark used for?
A: It captures and analyzes network packets.

Q: What is a packet?
A: A small unit of data transmitted over a network.

Q: How can you filter traffic in Wireshark?
A: Use display filters like ip.addr 8.8.8.8.

Q: What is a capture filter vs display filter?
A: Capture limits what's recorded; display shows specific results.

Q: How you identify malicious activity in Wireshark?
A: Look for unusual IPs, ports, or traffic patterns.

Q: What are TCP handshake steps?
A: SYN, SYN-ACK, ACK.

Q: How can you find DNS requests in Wireshark?
A: Filter using dns in Wireshark.

Q: How to detect ARP spoofing in Wireshark?
A: Check multiple IPs linked to one MAC address.

Q: What is promiscuous mode?
A: Mode that captures all network traffic passing the NIC.

Q: How can you export packet data from Wireshark?
A: Use File -+ Export Packet Dissections option.

Q: What is SQL injection?
A: Injecting malicious SQL queries to manipulate databases.

Q: What is XSS?
A: Cross-Site Scripting injects scripts into web pages.

Q: What is CSRF?
A: Cross-Site Request Forgery tricks users into unwanted actions.

Q: What are cookies?
A: Small data files websites store on user devices.

Q: What is HTTPS and how is it more secure than HTTP?
A: HTTPS encrypts data with SSL/TLS for secure transmission.

Q: What is SSUTLS?
A: Protocols for encrypting data tm,veen client and server.

Q: What are OWASP Top 10 vulnerabilities?
A: A list of the most critical web app security risks.

Q: What is input validation?
A: Checking and sanitizing user inputs to prevent attacks.

Q: How do you secure a login page?
A: Use HTTPS, strong passwords, and input validation.

Q: What are session hijacking attacks?
A: Stealing session tokens to impersonate users.

Q: What is blue teaming?
A: Defensive team focusing on detecting and stopping attacks.

Q: What is red teaming?
A: Offensive team simulating real-world attacks.

Q: What is threat hunting?
A: Proactively searching for hidden threats in a network.

Q: What is endpoint security?
A: Protecting devices like laptops and mobiles from threats.

Q: What are antivirus and EDR solutions?
A: Antivirus detects malware; EDR provides continuous endpoint monitoring.

Q: What is patch management?
A: Updating systems to fix vulnerabilities.

Q: What is privilege escalation?
A: Gaining higher-level acæss than intended.

Q: What is least privilege principle?
A: Users get only the access needed for their job.

Q: What is data loss prevention?
A: Preventing sensitive data from leaving the organization.

Q: What steps do you take during incident response?
A: Identify, contain, eradicate, recover, and review.

Q: What is Nmap used for?
A: For network scanning and host discovery.

Q: What is Metasploit?
A: A tool used for penetration testing and exploiting vulnerabilities.

Q: What is Burp Suite?
A: A tool used for web application security testing.

Q: What is Shodan?
A: A search engine for internet-connected devices.

Q: What is OpenVAS or Nessus used for?
A: Vulnerability scanning and assessment.

Q: What is OSINT?
A: Gathering information from public sources.

Q: What is DNS enumeration?
A: Finding domain-related info like subdomains and IPs.

Q: What is hashing?
A: Converting data into a fixed-length string using an algorithm.

Q: What is the differenæ between hashing and encryption?
A: Hashing is one-way; encryption is reversible with a key.

Q: What are common encryption algorithms?
A: AES, RSA, and DES.

Q: What is cloud computing?
A: Delivering computing services like servers and storage via the internet.

Q: What are types of cloud services?
A: IaaS, PaaS, SaaS.

Q: What is AWS?
A: Amazon Web Services — a leading cloud platform.

Q: What is an AWS VPC?
A: A Virtual Private Cloud for isolated AWS resources.

Q: What are security groups in AWS?
A: Firewall rules controlling inbound/outbound traffic.

Q: What is IAM in AWS?
A: Identity and Access Management for users and permissions.

Q: What is the difference between public and private cloud?
A: Public is shared; private is dedicated to one organization.

Q: What is data encryption at rest and in transit?
A: At rest protects stored data; in transit protects moving data.

Q: What are cloud security best practices?
A: Use IAM, encryption, and regular audits.

Q: What is shared responsibility model in AWS?
A: AWS secures the cloud; users secure their data in the cloud.

Q: Tell me about yourself.
A: I'm a CSE student passionate about cybersecurity and network defense.

Q: Why do you want to work in cybersecurity?
A: Because it combines problem-solving with protecting digital assets.

Q: What are your strengths and weaknesses?
A: Strength: quick learner; Weakness: overanalyzing details sometimes.

Q: What motivates you to apply for a SOC Analyst role?
A: The challenge of identifying and stopping threats in real time.

Q: How do you stay updated cybersecurity trends?
A: By following blogs, news, and learning platforms like TryHackMe.

Q: Tell me about a time you solved a problem as a team.
A: We collaborated on a project and divided tasks efficiently to meet deadlines.

Q: How do you handle stress during critical incidents?
A: By staying calm, prioritizing issues, and following procedures.

Q: What are your future goals in cybersecurity?
A: To become a skilled SOC analyst and progress into threat hunting.

Q: What ærtifications do you plan to pursue next?
A: CompTIA SecuritY+ and CEH.

Q: Why should we hire you for this role?
A: Because I'm passionate, trainable, and eager to contribute to your team.

What is the first phase of the security lifecycle?
    Security Lifecycle Summary Table
    Phase	                    Purpose
    1. Identify / Assess	    Know assets, risks, threats
    2. Protect / Prevent	    Stop attacks
        Firewalls
        Access controls
        Encryption
        Patch management
        Security policies
        User training
    3. Detect	                Find attacks
        ntrusion Detection Systems (IDS)
        Log monitoring
        SIEM
        Antivirus alerts
    4. Respond	                Handle incidents
        Incident response plans
        Containment
        Eradication of malware
        Communication and escalation
    5. Recover	                Restore operations
        Backup restoration
        System rebuilding
        Business continuity
        Disaster recovery
    6. Review / Improve	        Strengthen security
        Post-incident analysis  
        Update policies
        Improve controls
        Security audits

Which threat modeling methodology focuses on assets, threats, and vulnerabilities?
OCTAVE stands for Operationally Critical Threat, Asset, and Vulnerability Evaluation, and its core emphasis is:
    Identifying critical assets
    Analyzing threats to those assets
    Evaluating vulnerabilities that could be exploited
It is commonly used for organizational and risk-based security assessments, rather than purely technical design analysis.

What does GDPR stand for in the context of cyber laws?
GDPR stands for the General Data Protection Regulation, which is a law established by the European Union to protect the personal data and privacy of individuals within the EU.

What is the primary purpose of event log analysis in the context of cybersecurity?
The primary purpose of event log analysis in cybersecurity is to detect, investigate, and respond to security incidents.

Which type of log is most crucial for identifying unauthorized access attempts?
The most crucial log for identifying unauthorized access attempts is the authentication log (also called security or access logs).

    Application logs: Record events, errors, and status messages generated by applications during execution
    System logs: Capture operating system–level events such as startup/shutdown, hardware issues, and service failures
    Audit logs: Provide a chronological record of user actions and system changes for compliance, accountability, and forensic analysis

What is a common technique for detecting anomalies in event logs?
A common technique for detecting anomalies in event logs is pattern recognition, which identifies deviations from normal or expected log behavior.
A common technique for detecting anomalies in event logs is baseline analysis, where normal system behavior is established and deviations from that baseline are flagged as potential anomalies.

How can event log analysis help in post-incident investigations?
By offering insights into user activities and system events leading up to the incident

Which of the following bests describes the concept of data integrity?
Ensuring data remains accurate and unaltered throughout its lifecycle

What is the primary objective of risk managment in cybersecurity?
To reduce the impact and likelihood of security threats

Which process involves identifying potential security threats and vulnerabilities?
Risk identification

Which technique is commonly used in risk evaluation to determine the likelihood and impact of identified risks?
Quantitative risk analysis is the process of evaluating risk using numerical values and statistical data to estimate the likelihood and impact of potential threats, often expressed in monetary terms (e.g., expected financial loss).

What is the purpose of risk mitigation strategies in cybersecurity?
To reduce the severity and likelihood of risks

Which of the following is NOT a common risk identification technique?
Market analysis

    Common risk identification techniques in cybersecurity and risk management include:
        Brainstorming: Gathering input from stakeholders to identify potential risks.
        Checklists: Using predefined lists of known risks to ensure thorough assessment.
        Interviews: Conducting structured discussions with experts or staff to uncover risks.
        Surveys/Questionnaires: Collecting risk-related information from multiple sources.
        SWOT Analysis: Evaluating Strengths, Weaknesses, Opportunities, and Threats.
        Scenario Analysis: Exploring “what-if” situations to identify possible risks.
        Document Reviews: Examining policies, procedures, and past incident reports for risks.
        Risk Workshops: Facilitated sessions to collaboratively identify risks with key stakeholders.

How does qualitative risk analysis differ from quantitative riskan analysis?
Qualitative risk analysis uses expert judgement,while quantitative risk analysis uses numerical data

Which risk mitigation strategy involves accepting the risk and choosing not to take any action unless risk occurs?
The risk mitigation strategy that involves accepting the risk and taking no proactive action unless it occurs is called risk acceptance. Choosing not to insure against a very low-probability event because the cost of mitigation exceeds potential loss.

What is a key benefit of conducting a risk assessment in cybersecurity?
Identifying and prioritizing risks for treatment

What is the primary goal of the "Design" phase in the security lifecycle?
To create a blueprint for addressing identified risks

Which organization developed the threat modeling technique known by the acrontm STRIDE?
The threat modeling technique STRIDE was developed by Microsoft. It is used to identify security threats in software systems, focusing on Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, and Elevation of privilege.

What US law requires certain financial institutions to protect consumers' personal financial information?
GLBA stands for Gramm-Leach-Bliley Act.  GLBA is about financial data security and consumer privacy.

Which of the following best ensures data confidentiality?
Data encryption

What does the "Maintain" phase of the security lifecycle primary involve?
Continuous monitoring and improvement

Which command would you use to display the IP routingtable on a Linux System?
route
ip route
netstat -r
All of the above
    All of the above

What information does the "netstat -a" command provide?
Both active connections and listening ports

What is the purpose of the ARP cache?
To map IP address to MAC addresses.  The ARP (Addrss Resolution Protocol) cache stores mappings between IP address and MAC addresses.  This allows devices to communicate on a local network without constantly sending ARP requests.

What is ARP?
A network protocol used to map a device’s IP address to its MAC (hardware) address on a local area network (LAN).  Helps devices communicate at the data link layer.

What is ARP Poisioning/Spoofing?
A cyberattack where an attacker sends fake ARP messages to a network.  Tricks devices into associating the attacker’s MAC address with the IP address of another device (like a gateway).  Enables man-in-the-middle attacks, eavesdropping, or data interception.
    It’s basically fooling the network into sending traffic to the wrong device.
    Ettercap – A widely used tool for man‑in‑the‑middle attacks, including ARP poisoning.
    dsniff / arpspoof – A suite of network auditing tools; arpspoof is specifically for ARP spoofing.
    Bettercap – A modern, powerful framework for network attacks and traffic manipulation, including ARP poisoning.

Which nslookup command would you use to query a specific DNS server for a domain?
nslookup domain.com dns_server_ip

What is the main difference between traceroute and tracert?
traceroute is for Linux/Unix, tracert is for Windows

Which tcpdump command would capture only TCP traffic on port 80?
tcpdump tcp port 80

Which iptables chain is checked first for incoming packets in the default policy?
PREROUTING: Checked first for all incoming packets (before routing decision).
INPUT: Checked if the packet is destined for the local machine.
FORWARD: Checked if the packet is being routed through the machine.
OUTPUT: Checked for packets originating from the local machine.
POSTROUTING: Checked after routing, just before the packet leaves the system.

Which of the following NOT a valid capture filter for tshark?
host 192.168.1.1
process firefox
port 80
protocol tcp
    process firefox, tshark like tcpdump uses libpcap filter syntax.

What type of biometric authentication has become increasingly common on smartphones?
Fingerprint scanning

Which of the following is an example of a hardware security token?
A YubiKey is a hardware authentication device that provides secure access to computers, networks, and online services.

At which layer of the OSI model does data encryption typically occurs?
Presentation Layer

Which nmap command would you use to perform a stealthy SYN scan on a target?
-sS (SYN scan): Performs a stealth scan by sending SYN packets without completing the TCP handshake.
-sT (TCP connect scan): Completes the full TCP handshake to determine open ports.
-sU (UDP scan): Scans for open UDP ports.
-sV (Service/version detection): Detects service versions running on open ports.

What does the nmap command 'nmap -p- 192.168.1.1' do?
Scan all 65535 ports of the target

Which nmap script would you use to detect vulnerabilities in a target system?
nmap --script=vuln

Which protocol is used for secure shell connections?
SSH (Secure Shell) is a cryptographic network protocol used for secure data communication, remote command-line login,remote command execution, and other secure network servicies between two networked computers.

Which port is common associated with HTTPS traffic?
443

What is the main difference between SSL and TLS?
TLS (Transport Layer Security) is the successor to SSL (Secure Sockets Layer)

What is the main difference betweenNAS and SAN?
NAS is file-level access, SAN is block-level access

NAS (Network Attached Storage):
    Provides file-level storage over a standard TCP/IP network (Ethernet).
    Accessed like a shared folder using protocols such as NFS, SMB/CIFS.
    Easy to set up and suitable for general file sharing.
SAN (Storage Area Network):
    Provides block-level storage over a high-speed dedicated network (Fibre Channel or iSCSI).
    Accessed like a local disk by servers.
    Designed for high-performance applications like databases and virtualization.

Which nmap option would you use to determine the operation system of a target?
The -O option in nmap enables OS detection

In Wireshark, what does the filter 'http.request.method == "POST"' do?
Shows only HTTP POST requests

What is the primary use of aircrack-ng?
Wireless network auditing

What type of attack does John the Ripper primarily perform?
Password cracking

Which of the following is NOT a common module type in Metasploit?
Firewall

What is the primary purpose of the Canvas penetration testing tool?
Exploit development and testing
Immunity CANVAS for Penetration Testing and Red Team Operations. Immunity CANVAS is world leading commercial security assessment tools (SAT) allowing penetration testing, hostile attack simulations and exploit research and development.

What is one of the main features of Core Impact?
It provides detailed reports and remediation advice. It’s a commercial tool for executing and managing penetration tests efficiently.

Which of the following in NOT typically part of the vulnerability management lifecycle?
Exploit Development
    In short: Identify → Assess → Prioritize → Remediate → Verify → Monitor.
    Discovery / Asset Identification: Identify all assets, systems, and software in the environment that need protection.
    Vulnerability Scanning / Assessment: Use tools to detect known vulnerabilities in systems, applications, and networks.
    Prioritization / Risk Assessment: Evaluate vulnerabilities based on severity, impact, and likelihood to prioritize remediation.
    Remediation / Mitigation: Apply patches, configuration changes, or other controls to fix or reduce vulnerabilities.
    Verification / Reporting: Confirm that vulnerabilities have been addressed and report findings to stakeholders.
    Monitoring / Continuous Improvement: Continuously monitor for new vulnerabilities and improve the process.
Which of the following is NOT a common technique in reverse enginering?
Port Scanning
    Reverse engineering often involves disassebly (converting machine code to assembly), debugging (examining the program's execution), and API hooking (intercepting function calls).

What does "Rule of Engagment" refer to in penetration testing?
The agreed-upon scope and limitation of the test

What is the main difference between an Intrusion Detection System (IDS) and an Intrusion Prevention System (IPS)?
IDS = detect and alert; IPS = detect and block.
    IDS (Intrusion Detection System) tools:
        Snort (in IDS mode): Monitors network traffic and generates alerts for suspicious activity.
        Suricata (IDS mode): High-performance network IDS with logging and alerting capabilities.
        OSSEC: Host-based IDS that monitors system logs, file integrity, and rootkit detection.
        Wazuh: Fork of OSSEC with added features for monitoring, alerting, and compliance.
    IPS (Intrusion Prevention System) tools:
        Snort (in IPS mode / inline mode): Can actively drop or block malicious packets.
        Suricata (IPS mode / inline mode): Detects and prevents attacks in real time.
        pfSense (with Snort/Suricata): Firewall platform with IDS/IPS integration for active blocking.
        Fail2Ban: Monitors logs for failed login attempts and blocks offending IPs (host-based prevention).
    Note: Some tools like Snort and Suricata can function as both IDS and IPS depending on configuration.

What is the primary purpose of a DMZ (Demilitarized Zone) in network segmentation?
The primary purpose of a DMZ (Demilitarized Zone) in network segmentation is to expose public-facing services to the internet while protecting the internal network.

Which of the following is NOT typically placed in a DMZ?
Database server with sensitive information

What is the primary purpose of salting in cryptography?
The primary purpose of salting in cryptography is to add random data to passwords before hashing to make them more secure.

In the context of password storage, what is the correct order of operations?
Salt → Combine → Hash → Store.
    1. Generate a random salt for the password.
    2. Append or prepend the salt to the password.
    3. Hash the combined value using a secure hashing algorithm (e.g., SHA-256, bcrypt, Argon2).
    4. Store both the hash and the salt in the database.

Which of the following is NOT a characteristic of a good cryptographic hash function?
Reversibility

What is the primary purpose of the Diffie-Hellman algorithm?
Secure key exchange
The primary purpose of the Diffie-Hellman algorithm is to securely establish a shared secret key between two parties over an untrusted network.

Which component of PKI (Public Key Infrastructure) is repsonsible for issuing and managing digital certificates?
The component of PKI responsible for issuing and managing digital certificates is the Certificate Authority (CA).

What is the main purpose of code obfuscation in software development?
To protect against reverse engineering

Which of the following is NOT typically ensured by a digital signature?
Confidentiality is ually achieved through encryption

What distinguishes whaling from regular phising attacks?
Whaling specifically targets high-profile individuals

What medium is primary used in vishing attacks?
voice calls

Which of the following best describes smishing?
Phishing via text messages (SMS + phishing)

What is the key difference between spam and phishing?
Phishing specifically aims to steal sensitive information, while spam is just unwanted bulk messages

Which physical security threat involves following an authroized person into an restricted area without proper credentials?
Tailgating, also known as piggybacking

What is the primary goal of dumpster diving in the context of information security?
To find discarded sensitive information

What is a zero-day vulnerability?
A vulnerbility that is known to the attacker but unknown to the vendor or public

Which of the following best describes a rogue access point
An unauthorized access pointset up to eavesdrop on network traffic

What is the primary risk associated with a buffer overflow vulnerability?
Arbitrary code execution

Which of the following best describes a memory leak?
“A situation where a program allocates memory but fails to release it after it is no longer needed, leading to progressively reduced available memory.”
    Key points:
        The program continues running but consumes more memory over time.
        Can cause performance degradation or system crashes if unchecked.
        Often occurs due to improper memory management in languages like C or C++.

What is the main security concern with memory leaks?
They can cause denial of service due to resource exhaustion

What is Two-Factor Authentication (2FA)?
Two-Factor Authentication (2FA) is a security process that requires two different types of verification before granting access to an account or system.
    Key points:
        Something you know: e.g., a password or PIN.
        Something you have: e.g., a hardware token, smartphone app, or security key.
        Something you are: e.g., biometric factor like fingerprint or facial recognition.

Which of the following is NOT a common factor used in 2FA?
Someone you know

What is a potential drawback of using SMS for 2FA?
SIM swapping attack: An attacker tricks the mobile carrier into transferring the victim’s phone number to a new SIM card.

Which layer of the OSI model is responsible for logical addressing and routing?
Network Layer

At which OSI layer does the TCP protocol operate?
Transport Layer

Which OSI layer is responsible for encryption and decryption?
Presentation Layer

Which command is used to display the IP configuration of a network interface?
ipconfig
ifconfig
ip addr
All of the above
    All of the above

What does the netstat command primarily show?
Network statistics
Active network connections
Routing table information
All of the above
    All of the above

What does ARP stand for in networking?
Address Resolution Protocol

What is the primary function of nslookup?
To find the IP address of a domain name
The primary function of nslookup is to query DNS (Domain Name System) servers to obtain domain name or IP address information.

Which command is commonly used to trace the route packets takes to reach a network host?
tracert

What is the primary purpose of tcpdump?
To capture and analyze network traffic

What is the main function of iptables in Linux systems?
To manage firewall rules
    iptables is a user-space utility program that allows a system admin to configure the IP packet filter rules of the Linux kernel firewall

What is nmap primarily used for?
Network discovery and security auditing

What is the main advantage of masscan over nmap?
Faster scanning speed

What is the relationship between Wireshark and tshark?
tshark is the command-line network protocol analyzer that comes with Wireshark.

What is the primary benefit of using 2AF?
It provides an additional layer of security

Which of the following is NOT a common type of biometric authentication?
Password complexity

What is the main advantage of using hardware tokens for authentication?
They provide stronger security than software tokens

Which layer of the OSI model is responsible for routing and forwarding?
Network Layer

Which of the following is NOT a common category in the PASTA threat modeling framework?
Implementing security controls
    PASTA (Process for Attack Simulation and Threat Analysis) threat modeling framework, threats are commonly categorized into seven stages, often grouped into threat categories such as:
        Reconnaissance – Gathering information about the target.
        Weaponization – Preparing attacks using collected information.
        Delivery – Transmitting the attack to the target system.
        Exploitation – Triggering vulnerabilities to gain access.
        Installation – Installing malicious code or backdoors.
        Command & Control (C2) – Establishing remote control over compromised systems.
        Actions on Objectives – Achieving the attacker’s ultimate goals (e.g., data theft, disruption).

What is the primary goal of a Pass-the-Hash attack?
The primary goal of a Pass‑the‑Hash (PtH) attack is to authenticate to a system using a stolen password hash without needing to know the actual plaintext password. Steal a hashed credential

Which of the following best describes a Directory Traversal vulnerability?
Unauthorized access to the directory structure of a website
A Directory Traversal vulnerability (also called path traversal) occurs when an attacker can manipulate the file path input to access files or directories that are outside the intended directory on a server. This typically happens because the application does not properly validate or sanitize user-supplied file paths.

What is the primary function of a firewall in network security?
To control incoming and outgoing network traffic based on predetermined security rules

Which of the following DNS-related tools is primarily used for testing and troubleshooting DNS servers?
dig (Domain Information Groper)

What is the main purpose of using traceroute?
To show the route packets route taken to reach network host

Which of the following best describes the primary use of curl in curl in cybersecurity?
To transfer data using various protocols

What is the primary function of Wireshark in network security?
To capture and analyze network packets

What is the main purpose of a memory dump in cybersecurity investigations?
To capture the contents of RAMat a specific point in time

In the context of cybersecurity, what does ISO primary refer to?
International Organization for Standardization

What does RMF stand for in the context of cybersecurity?
Risk Management Framework

What is the primary purpose of environmental controls in a data center?
To maintain optimal conditions for IT equipment operation

What is NIST best known for inthe field of cybersecurity?
Publishing cybersecurity standards and guidelines

What does CIS stand for in the context of cybersecurity?
Center for Internet Security (non-profit)

Which international standard provides guidelines for information security management systems?
ISO 27001

What aspect of the CIA triade does a Distributed Denial of Service (DDoS) attack primarily threaten?
Availability

In the context of threat modeling, what does DREAD stand for?
Damage potential, Reproducibility, Exploitability, Affected users, Discoverability

Which phase of the security lifecycle would typically include penetration testing?
Assess (identify)

What does the "non-repudiation" principle in cybersecurity ensure?
A party cannot deny having performed an action

What technique is commonly used to ensure data integrity during transmission?
Hashing is commonly used to ensure data integrity during transmission.  A hash function generates a fixed-size string of characters from input data.  The receiver can re-compute the hash and compare it to the transmitted hash to verify the data's integrity.

Which of the following best describes the principle of 'least privilege' in cybersecurity?
User should have the minimum levels of access necessary to perform their jobs functions

Which connection type is primarily used for contacless payments and data transfer over short distances?
NFC (Near Field Connections)

What is the main function of a hypervisior in virtualization?
Managing hardware resources

Which OS-independent tool can be used to troubleshoot network connectivity issues?
ping

What is the primary role of Docket in modern application deployment?
Docker is primarily used for containerization,allowing developers to package applications and their dependencies into a portable container.

Which command provides information about the netwrok interfaces and IP configuration on a Window system?
ipconfig

What type of wireless connection ismost commonly used in home networks for internet access?
WiFi

Which tool can be used to inspect and manipulate network traffic in a cross-plateform manner?
Wireshark

What is the function of a host OS in a virtualization environment?
The host OS runs and manages virtual machines in a virtulization environment.

Which wireless technology is commonly used for personal area networks and connecting peripherals?
Bluetooth

What does the 'ifconfig' command do on Unix-like systems?
Configures network interfaces

Which type of virtual machine is isolated from the underlying host OS and runs its own operating system?
Guest VM

Which command renews the IP address assigned to a network interface on Windows?
ipconfig /renew

Which connection type is typically used for secure, high-speed data transfer in enteprise networks?
Ethernet

What is the primary purpose of using a hypervisor in server virtualization?
The primary purpose of a hypervisor in server virtualization is to reduce hardware costs by allowing multiple virtual machines to run on a single physical server

What does the 'dockeer ps' command do?
List all running containers

Which technology is used to create isolated enviroments for running applications with their dependencies?
Containerization

What does 'NFC' stand for in the context of wireless communication?
Near Field Communication

What is the primary function of a protocol analyzer in network security?
To intercept and log network traffic

What is the primary purpose of the Kerberos authentication protocol?
Kereros is a network authentication protocol designed to provide strong authentication for client/server applications by using secret-key cryptography.

In the Kerberos protocol, what is the purpose of the Ticket Granting Ticket (TGT)?
The Ticket Granting Ticket (TGT) in Kerberos is issued by the Authentication Server and allows the user to request service tickets for specific services.

What is the primary function of the RADIUS protocol?
RADIUS is a networking protocol that provides centralized Authentication, Authorization, and Accounting (AAA) management for users who connect and use a network service.

Which of the following is a typical use case for the RADIUS protocol?
RADIUS is often used to authenticate users for network access services such as VPNs, wireless networks, and dial-up connections.

What is LDAP primarily used for?
LDAP is a protocol used to access and maintain distributed directory information services over an Internet Protocol network.

Which type of information is typically stored in an LDAP directory?
LDAP directories are conmonly used to store information about users, including usernames, passwords, email addresses, and other attributes.

What is the main purpose of Public Key Infrastructure (PKI)?
PKI is a framework for managing public-key encryption, including the issuance, revocation, and validation of digital certificates.

In PKI, what is the role of a Certificate Authority (CA)?
A Certificate Authority (CA) is an entity that issues digital certificates and verifies the identity of the certificate holders.

What is the primary goal of the COBIT framework?
COBIT is a framework for developing, implementing, monitoring, and improving IT governance and management practices.

What is the OWASP Top 10?
The OWASP Top 1B is a regularly updated report outlining the most critical security risks to web applications.

Which of the following is NOT considered a social engineering tactic?
Port scanning
Phishing
Pretexting
Baiting
    Social engineering tactics typically involve psychological manipulation rather than technical methods like port scanning.

What is 'tailgating' in the context of social engineering?
Gaining unauthorized physical access by following an authorized person

Which social engineering technique often involves creating a fake scenario to manipulate victims?
Pretexting involves creating an invented scenario to engage a targeted victim, often to extract information or influence behavior.

What is the primary goal of most social engineering attacks?
To gain unauthorized access to sensitive information or systems

Which of the following is the best defense against social engineering attacks?
Employee education and awareness training

What is the primary risk associated with dumpster diving in a corporate context?
Theft of proprietary information

Which of the following items is LEAST likely to be found during dumpster diving?
Encrypted backup tapes

What is the best practice to mitigate risks associated with dumpster diving?
Implementing proper document shredding and disposal policies

Which type of information is often targeted in dumpster diving attacks?
Employee personal information
Financial records
Technical specifications
All of the above
    All of the above

In the context of information security, what does 'clean desk policy' help prevent?
A clean desk policy helps ensure that sensitive information is not left out in the open, reducing the risk of it being discarded improperly and potentially retrieved through dumpster diving.

Which risk is included in the OWASP Top 10?
Cross-Site Scripting (XSS) is one of the vulnerabilities listed in the Top 10, which highlights critical security risks for web applications.

Which of the following is a secure coding practice?
Validating all user inputs is a fundamental secure coding practice to prevent injection attacks and other security vulnerabilities.

Which of the following is considered a best practice for secure coding?
Proper error handling helps to prevent information leakage and improves the security of the application by not exposing internal details.

What is the purpose of event log analysis in cybersecurity?
To detect and investigate security incidents

Which tool is commonly used for event log analysis?
Splunk is a powerful tool for searching, monitoring, and analyzing machine-generated big data via a web-style interface. It is widely used for event log analysis.

What is the purpose of using prepared statements in database queries?
Prepared statements separate SQL logic from data, preventing SQL injection attacks by ensuring that user input is treated as data and not executable code.

Which of the following is a secure way to implement password reset functionality?
Generating a time-limited, single-use token for password reset is a secure practice that prevents unauthorized access and limits the window of vulnerability.

What is the purpose of the HTTP Strict Transport Security (HSTS) header?
To force browsers to use HTTPS for all connections to the domain
    The HSTS header instructs browsers to only connect to the website using HTTPS, helping prevent downgrade attacks and cookie hijacking.

Which of the following is NOT a secure coding practice for preventing XML External Entity (XXE) attacks?
Enabling DTD processing in XML parsers can lead to XXE vulnerabilities. Secure practices include disabling external entity processing, using alternative formats, and implementing proper input validation.

What is the purpose of the Same-Origin Policy in web browsers?
The Same-Origin Policy is a security mechanism that restricts web pages from making requests to a different origin (domain, protocol, orport) than the one serving the web page, helping to prevent various cross-origin attacks.

What is the primary goal of input validation in secure coding?
Input validation is a crucial security practice that helps prevent various injection attacks and ensures that only properly formatted data enters the system.

Which of the following is NOT a secure way to store passwords?
Using bcrypt
Using MD5
Using SHA-256 with a salt
Using Argon2
    Using MD5
    MD5 is considered cryptographically broken and unsuitable for further use in password hashing. Secure
    alternatives include bcrypt, Argon2, and salted SHA-256.

What is the principle of least privilege?
The principle of least privilege is a fundamental security concept that involves providing users or processes with only the minimum level of access or permissions needed to perform their tasks.

Which of the following is a common method to prevent SQL injection attacks?
Prepared statements or parameterized queries separate SQL logic from data, preventing attackers from injecting malicious SQL code into queries.


What is Cross-Site Scripting (XSS)?
A vulnerability that allows attackers to inject malicious scripts into web pages

Which of the following is NOT a secure way to prevent directory traversal attacks?
Allowing the use of / ' in file paths can lead to directory traversal attacks. Secure practices include input validation, using absolute paths, and implementing proper access controls.

What is the purpose of Content Security Policy (CSP)?
Content Security Policy is a security standard that helps prevent cross-site scripting, clickjacking, and other code injection attacks by specifying which content sources are trusted and can be loaded by the browser.

What is the OWASP Top 10?
The %IASP Top le is a regularly updated report outlining the most critical web application security risks, serving as a standard awareness document for developers and security professionals.

Which of the following is a secure way to implement session management?
Secure session management involves using secure, HttpOn1y, and SameSite cookies, which help protect against various attacks like session hijacking and cross-site request forgery (CSRF).

What is the purpose of HTTPS?
HTTPS (Hypertext Transfer Protocol Secure) uses SSL/TLS to encrypt data in transit between the client and server, protecting against eavesdropping and man-in-the-middle attacks.

What is a buffer overflow attack?
A buffer overflow attack occurs when a program writes more data to a buffer than it can hold, potentially allowing an attacker to execute arbitrary code or crash the system.

Which of the following is NOT a secure coding practice for handling sensitive data?
Encrypting data at rest
Implementing proper access controls
Storing passwords in plain text
Using secure cormunication protocols
    Storing passwords in plain text

What is the principle of defense in depth?
Defense in depth is a cybersecurity strategy that employs multiple layers of security controls to protect assets, making it harder for attackers to compromise a system.

Which of the following is a secure way to generate random numbers for cryptographic purposes?
Cryptographically secure random number generators are designed to produce unpredictable and statistically random numbers suitable for use in cryptographic operations, unlike standard pseudo-random number generators.

What is the purpose of code signing?
Code signing is a security practice that uses digital signatures to verify the integrity and authenticity of software, ensuring it hasn't been tampered with since it was signed by the developer.

Which of the following is NOT a secure way to handle file uploads?
Validating file types and extensions
Allowing unrestricted file uploads to any directory
Storing uploaded files outside the web root
Scanning uploaded files for malware
    Allowing unrestricted file uploads to any directory

What is the purpose of input sanitization?
Input sanitization is the process of cleaning or filtering user input to remove or encode potentially dangerous characters, helping prevent various injection attacks.

Which of the following is a secure way to store API keys in a web application?
Storing them in environment variables
Hardcoding them in the source code
Saving them in a public GitHub repository
Including them in client-side JavaScript
    Storing API keys in environment variables is a secure practice
    that keeps sensitive information out of the source code and
    allows for easier management across different environments.

What is the principle of fail-safe defaults?
The principle of fail-safe defaults states that the default configuration should be secure, denying access unless explicitly granted. This helps prevent accidental exposure of resources.

Which of the following is NOT a secure coding practice for preventing integer overflow?
Using appropriate data types
Implementing bounds checking
Using unchecked arithmetic operations
Validating user input
    Using unchecked arithmetic operations can lead to integer
    overflow vulnerabilities. Secure practices include using
    appropriate data types, bounds checking, and input validation.

What does SIEM stand for?
SIEM stands for Security Information and Event Management, which refers to a comprehensive approach to
managing and analyzing security information and events.

What is the primary purpose of a SIEM tool?
The primary purpose of a SIEM tool is to collect, analyze, and report on security data from across an organization.

Which of the following is a key feature of SIEM tools?
Real-time monitoring and alerting

How can SIEM tools help in compliance reporting?
SIEM tools can help in compliance reporting by providing detailed logs and reports required for regulatory compliance.

What is the primary function of an Intrusion Prevention System (IPS)?
An IPS is designed to block or prevent detected threats in addition to detecting and alerting on them.

Which of the following is a type of IPS?
Network-based IPS
Host-based IPS
Signature-based IPS
All of the above
    All of the above

How does a network-based IPS operate?
A network-based IPS monitors network traffic for malicious activity and can take action to block detected threats.

What is one advantage of using an IPS over an IDS?
An advantage of an IPS is its ability to block detected threats, whereas an IDS only detects and alerts on them.

Why is it important to regularly update IPS signatures?
To ensure the IPS can detect the latest threats

What is the primary function of an Intrusion Detection System (IDS)?
To detect and alert on potential security breaches

Which type of IDS compares network traffic against known attack patterns?
Anomaly-based IDS
Host-based IDS
Signature-based IDS
Network-based IDS
    A signature-based IDS compares network traffic against
    known attack patterns to detect potential threats.

What is a common limitation of a signature-based IDS?
It cannot detect unknown or new attacks


What is the difference between an IDS and an IPS?
An IPS blocks traffic, an IDS does not

How can an IDS improve network security?
By providing real-time monitoring and alerting on suspicious activities

What is Group Policy in Windows environments?
A feature for managing user and computer settings

Which tool is commonly used to edit Group Policy settings?
Gpedit.msc is the tool used to edit Group Policy settings.

How does Group Policy improve security in a Windows environment?
By enforcing security settings and policies across multiple computers

What is the purpose of Group Policy Object (GPO) linking?
GPO linking is used to apply specific Group Policy Objects to Active Directory containers such as sites, domains, or organizational units.

What is the primary goal of port blocking?
To enhance network security

Which port is typically blocked to prevent HTTP traffic?
80

What is a common use case for blocking port 22?
To restrict SSH access

Which type of firewall rule would you use to block a specific port?
A deny rule is used to block a specific port in firewall configurations.

How can port blocking contribute to defense-in-depth?
By adding an additional layer of security to protect against unauthorized access

What does MAC stand for in the context of MAC-based filtering?
MAC stands for Media Access Control, which refers to a unique identifier assigned to network interfaces.

How does MAC-based filtering enhance network security?
MAC-based filtering enhances security by allowing only devices with specific MAC addresses to connect to the network.

What is a potential drawback of using MAC-based filtering?
A potential drawback of MAC-based filtering is that MAC addresses can be spoofed, reducing its effectiveness.

Which network devices commonly use MAC-based filtering?
Routers and switches commonly use MAC-based filtering to control access to the network.

What is the main purpose of MAC-based filtering in wireless networks?
To control access by allowing only specific devices

What does NAT stand for?
NAT stands for Network Address Translation, a method used to remap IP addresses.

What is the primary purpose of NAT?
NAT allows multiple devices on a local network to share a single public IP address.

Which type of NAT maps a single public IP address to a single private IP address?
Static NAT maps a single public IP address to a single private IP address.

What is the main difference between PAT and dynamic NAT?
PAT (Port Address Translation) uses port numbers to distinguish between multiple connections, whereas dynamic NAT does not.

How does NAT improve network security?
By masking internal IP addresses from external networks

What information can typically be found in a firewall log?
Blocked and allowed traffic details

What does a 'denied' entry in a firewall log indicate?
A packet was blocked by the firewall

Which field in a firewall log shows the source IP address of a packet?
The 'Source' field shows the originating IP address of a packet.

How can firewall logs help in identifying a security incident?
By recording unusual or suspicious traffic patterns

Which log analysis technique involves looking for repeated failed connection attempts?
Pattern recognition involves identifying repeated failed connection attempts, which could indicate a potential attack.

What is packet capture?
Intercepting and logging traffic

Which tool is commonly used for packet capture?
Wireshark

What is the purpose of a packet capture filter?
Filters are used to limit the captured data to specific criteria, reducing the volume of captured traffic.

Which of the following is NOT a packet capture file format?
LOG
PCAP
CAP
NG 
    LOG

Why is timestamping important in packet capture?
It helps in analyzing the sequence of network events

What is the purpose of User Account Control (UAC) in Windows?
User Account Control (UAC) is a security feature that helps prevent unauthorized changes to the operating system.

Which tool is used to manage security policies on a Windows machine?
Local Security Policy is a tool used to manage security policies on a Windows machine.

What is BitLocker used for?
BitLocker is a security feature in Windows used for full disk encryption.

How can you securely remove sensitive data from a Windows machine?
Using a file shredding tool securely removes sensitive data from a Windows machine by overwriting it multiple times.

Which feature in Windows helps protect against malicious software by preventing unauthorized programs from making changes to the system?
User Account Control (UAC) helps protect against malicious software by preventing unauthorized programs from making changes to the system.

What is the purpose of the 'sudo' command in Linux?
The 'sudo' conmand allows a permitted user to execute a conmand as
the superuser or another user, as specified by the security policy.

Which file contains user account information in Linux?
The /etc/passwd file contains user account information in Linux.

How can you set file permissions in Linux?
The 'chmod' conmand is used to set file permissions in Linux.

What is SELinux?
SELinux (Security-Enhanced Linux) is a security module that provides
access control policies to enhance the security of a Linux system.

Which command is used to display all active processes in Linux?
The 'top' comand is used to display all active processes in Linux.

What is FileVau1t used for in macOS?
Encrypting the entire disk

Which feature in macOS provides runtime protection and prevents malware from modifying system files?
System Integrity Protection SIP provides runtime protection in macOS and prevents malware from modifying system files.

What is the purpose of the macOS Gatekeeper?
Gatekeeper is a security feature in macOS designed to ensure that only trusted software runs on the system.

Which tool in macOS can be used to monitor system logs for security events?
The Console application in macOS can be used to monitor system logs for security events.

How can macOS users ensure their system is protected against known security vulnerabilities?
Regularly updating the macOS ensures that the system is protected against known security vulnerabilities.

What is a public IP address?
An IP address that is assigned by an ISP and is accessible over the internet

Which of the following is a private IP address?
192.168.1.1
8.8.8.8
172.217.16.142
216.58.207.46
    192.168.1.1 is an example of a private IP address.
    Private IP address ranges are:
        10.0.0.0 – 10.255.255.255
        172.16.0.0 – 172.31.255.255
        192.168.0.0 – 192.168.255.255

    192.168.1.1 →           Private IP
    8.8.8.8 →               Public (Google DNS)
    172.217.16.142 →        Public (Google)
    216.58.207.46 →         Public (Google)

Why are private IP addresses used in local networks?
To avoid IP address conflicts on the internet

Which organization is responsible for assigning public IP addresses?
The Internet Assigned Numbers Authority (IANA) is responsible for assigning public IP addresses.

What is a potential issue when using only public IP addresses within a network?
Using only public IP addresses within a network can lead to increased cost and limited availability of IP addresses.

What is the main purpose of subnetting?
Subnetting divides a network into smaller, more manageable segments, improving network performance and security.

Which of the following is a subnet mask for a Class C network?
255.255.255.0 is a conunon subnet mask for a Class C network.
    IP Address Classes (Classful Addressing)
    Class	    IP Range (First Octet)	Default Subnet Mask	    Example IP
    Class A	    1 – 126	                255.0.0.0	            10.0.0.1
    Class B	    128 – 191	            255.255.0.0	            172.16.0.1
    Class C	    192 – 223	            255.255.255.0	        192.168.1.1
    Class D	    224 – 239	            Multicast	            224.0.0.1
    Class E	    240 – 255	            Experimental	        240.0.0.1

How many subnets are created when a / 24 network is subnetted with a / 26 prefix?
A / 24 network subnetted with a / 26 prefix creates 4 subnets.

What is the host range for the subnet 192.168.10.0/28?
The host range for the subnet 192.168.10.0/28 is 192.168.10.1 to 192.168.10.14
    IPv4 address has 32 bits total
        28 bits = network
        4 bits = host
        Each octet has 8 bits
        11111111.11111111.11111111.11110000     255.255.255.240
        Block size = 16 addresses (256 − 240)
        Address breakdown:
            Network address: 192.168.10.0
            Broadcast address: 192.168.10.15
            Usable host range:  
                192.168.10.1 – 192.168.10.14

What is the purpose of the default gateway in a subnetted network?
The default gateway routes traffic from a subnet to other networks, typically outside the local network.

What does CIDR stand for?
CIDR stands for Classless Inter-Domain Routing, a method for allocating IP addresses and routing.

What does the '/24' represent in the CIDR notation 192.168.1.0/24?
The '/24' in the CIDR notation 192.168.1.0/24 represents the number of bits in the subnet mask.

How many hosts can a / 30 network support?
A / 30 network supports 2 hosts

What is the subnet mask for the CIDR notation / 16?
The subnet mask for the CIDR notation / 16 is 255.255.0.0

How does CIDR help in reducing the size of routing tables?
CIDR helps in reducing the size of routing tables by allowing more specific IP address allocation, which
aggregates routes and reduces the total number of entries.

What is the primary function of a default gateway?
The primary function of a default gateway is to route traffic from a local network to other networks.

Which command can be used to view the default gateway configuration on a Linux system?
The 'route' command can be used to view the default gateway configuration on a Linux system.

How can you set a default gateway on a Windows machine using the command line?
You can set a default gateway on a Windows machine using the 'netsh interface ip set address' conmand.

Why might a network device need a default gateway?
To access resources outside the local network

258. What could cause a device to be unable to reach external networks even if it has a valid IP address and subnet mask?
Incorrect default gateway configuration

What is the main purpose of a VLAN?
To create separate broadcast domains within a single network

Which protocol is commonly used for VLAN tagging?
The 802.1Q protocol is used for VLAN tagging.
    VLAN tagging is a networking method used to identify which VLAN (Virtual Local Area Network) a data frame belongs to as it travels across a network link.

How does a VLAN improve network security?
By isolating sensitive traffic from the rest of the network

What is a trunk port in the context of VLANs?
A trunk port carries traffic for multiple VLANs, allowing communication between VLANs across switches.

What is DHCP?
Dynamic Host Configuration Protocol.  It is a network protocol that automatically assigns IP configuration information to devices on a network, so they can communicate without manual setup.

Which of the following is a best practice for securing DHCP in an enterprise network?
DHCP snooping and authentication are security features that help prevent rogue DHCP servers and unauthorized clients, enhancing the overall security of DHCP in enterprise networks.

Which of the following is NOT a common security risk associated with DHCP?
DHCP security risks include DHCP starvation attacks, rogue DHCP servers, and man-in-the-middle attacks. DHCP doesn't inherently provide encryption, which is a limitation rather than a risk.

What is the purpose of DHCP snooping in network security?
DHCP snooping is a security feature that filters untrusted DHCP messages and prevents unauthorized DHCP servers from issuing IP addresses on a network.

Which of the following is a best practice for securing DHCP in an enterprise network?
DHCP authentication is a security feature that allows DHCP clients and servers to authenticate each other, reducing the risk of rogue DHCP servers and unauthorized clients.

What is the primary purpose of implementing DHCP Option 82?
DHCP Option 82, also known as the DHCP Relay Agent Information Option, allows a DHCP relay agent to insert circuit specific information into a request that is being forwarded to a DHCP server.

In the context of DHCP security, what is IP source guard?
IP source guard is a security feature that prevents IP spoofing attacks by filtering IP traffic based on the DHCP snooping binding database or manually configured IP source bindings.

Which of the following is NOT a common DNS security threat?
DNS cache poisoning
DNS encryption
DNS amplification attacks
DNS tunneling
    Common DNS security threats include cache poisoning, amplification attacks, and tunneling. DNS encryption (such as DNS over HTTPS) is actually a security measure, not a threat.

Which of the following is a best practice for securing DNS servers?
Implementing access controls and monitoring DNS traffic are important security measures. DNS servers should be
kept updated, run on dedicated machines, and recursive queries should be limited to authorized clients.

What is DNS over HTTPS (DOH) designed to protect against?
DNS over HTTPS (DOH) is designed to increase user privacy and security by preventing eavesdropping and manipulation of DNS data by man-in-the-middle attacks.

Which of the following is NOT a typical function of a DNS firewall?
Blocking access to known malicious domains
Encrypting DNS queries
Logging DNS requests for security analysis
Filtering out DNS requests to
undesired categories of websites
    DNS firewalls typically block malicious domains, log requests, and can filter categories. Encryption of 
    DNS queries is usually handled by protocols like DOH or DOT, not by the firewall itself.

What is the primary purpose of DNSSEC (Domain Name System Security Extensions)?
DNSSEC provides origin authentication of DNS data, data integrity, and authenticated denial of existence. It does not provide encryption of DNS data.

Which network protocol is vulnerable to ARP spoofing attacks?
ARP (Address Resolution Protocol) is vulnerable to spoofing attacks where an attacker can send falsified ARP messages on a local network, potentially leading to man-in-the-middle attacks.

What is a key security practice for router configuration?
Regularly updating router firnware is crucial for security as it often includes patches for known vulnerabilities and improves overall performance and security features.

Which encryption protocol is considered the most secure for protecting a WLAN?
WEP
WPA
WPA3
WPA2
    WPA3 is the latest and most secure Wi-Fi security protocol, offering stronger encryption and protection against various attacks compared to its predecessors.

Which of the following is NOT typically a switch security feature?
While port security, VLAN segmentation, and MAC address filtering are common switch security features, Intrusion Prevention Systems (IPS) are typically network or host-based and not a standard feature of switches.

What is the primary purpose of implementing port security on a switch?
Port security is used to limit the number of MAC addresses that can connect to a switch port, preventing unauthorized access and mitigating certain types of attacks like MAC flooding.

Which attack is mitigated by implementing DHCP snooping on a switch?
DHCP snooping on a switch helps prevent rogue DHCP server attacks by allowing the switch to act as a
filter between trusted ports connected to a DHCP server and untrusted ports connected to end users.

What is the purpose of implementing private VLANs on a switch?
Private VLANs are used to isolate ports within the same VLAN, providing an additional layer of security by restricting communication between devices in the same broadcast domain.

Which of the following is a best practice for securing switch management access?
Using strong passwords and encryption (such as SSH or HTTPS) for switch management sessions is a best practice to prevent unauthorized access and protect sensitive configuration information.

Which encryption protocol is considered the most secure for protecting a WLAN?
WEP
WPA3
WPA
WPA2
    WPA3 is the latest and most secure Wi-Fi security protocol, offering stronger encryption and protection against various attacks compared to its predecessors.

What is the purpose of implementing MAC address filtering on a wireless network?
MAC address filtering is used to limit access to a wireless network by allowing only devices with specific MAC addresses to connect, providing an additional layer of access control.

Which of the following is NOT a recommended practice for securing a wireless network?
While changing the default SSID, enabling strong encryption, and using a strong passphrase are recomended, broadcasting the SSID is generally not recomended for security-sensitive networks as it makes the network more visible to potential attackers.

What is the purpose of implementing a guest WLAN?
A guest WLAN is implemented to segregate guest traffic from internal network resources, providing internet access to guests while protecting sensitive internal network assets.

Which of the following is a characteristic of an Evil Twin attack in wireless networks?
An Evil Twin attack involves setting up a rogue access point that mimics a legitimate one, often using the same SSID, to trick users into connecting to it and potentially exposing their data.

At which layer of the OSI model does a router primarily operate?
Routers primarily operate at the Network Layer (Layer 3) of the OSI model, where they make decisions about forwarding data packets based on logical addressing.

Which of the following protocols provides both encryption and authentication for secure remote access?
SSH (Secure Shell) provides both encryption and authentication, making it a secure protocol for remote access and file transfer, unlike the other options which do not inherently provide encryption.

What type of network sniffing technique involves capturing all network traffic indiscriminately?
Promiscuous mode sniffing involves configuring a network interface to capture all network traffic, regardless of whether it's destined for that particular interface or not.

Which of the following is NOT a common use of network sniffing for legitimate purposes?
Network sniffing is conmonly used for troubleshooting, monitoring, and security auditing. Bypassing access controls is not a legitimate use and could be considered a security breach.

What technique is used to redirect traffic to a malicious host for the purpose of sniffing?
ARP poisoning (also known as ARP spoofing) is a technique used to associate an attacker's MAC address with a victim's IP address, redirecting traffic to the attacker for sniffing purposes.

Which protocol is particularly vulnerable to sniffing attacks due to its unencrypted nature?
HTTPS
Telnet
SSH
SFTP
    Telnet transmits data, including passwords, in plain text,making it particularly vulnerable to sniffing attacks. The other options use encryption to protect data in transit.

What is the primary purpose of using a network tap for sniffing?
A network tap is a hardware device used to passively capture network traffic without detection, providing a way to monitor network conmunications without affecting the flow of traffic.

Which of the following is NOT an effective countermeasure against shoulder surfing?
Increasing screen brightness in public places actually makes it easier for others to view your screen. The other options are effective countermeasures against shoulder surfing.

What type of authentication is most resistant to shoulder surfing attacks?
Biometric authentication methods like fingerprint or facial recognition are most resistant to shoulder surfing as they don't involve visible input that can be observed by others.

In the context of shoulder surfing, what is 'visual hacking'?
Visual hacking refers to the act of observing and potentially recording sensitive information displayed on screens, which is a form of shoulder surfing that can occur in public or shared spaces.

Which of the following environments is MOST susceptible to shoulder surfing attacks?
Crowded public transportation is most susceptible to shoulder surfing attacks due to the close proximity of people and the frequent use of mobile devices in such environments.

Which OSI layer is responsible for encryption and decryption of data?
The Presentation Layer (Layer 6) of the OSI model is responsible for data formatting, encryption, and decryption, ensuring that data from the application layer of one system can be read by the application layer of another.

At which OSI layer does the SSL/TLS protocol primarily operate?
SSL/TLS primarily operates at the Presentation Layer (Layer 6) of the OSI model. It provides encryption, authentication, and data integrity services, transforming application data before it's passed to the Transport Layer for transmission.

Which OSI layer is most vulnerable to ARP spoofing attacks?
ARP spoofing attacks primarily target the Data Link Layer (Layer 2) of the OSI model, where ARP operates to map IP addresses to MAC addresses.

At which OSI layer do firewalls that filter based on IP addresses and port numbers primarily operate?
Firewalls that filter based on IP addresses and port numbers primarily operate at the Transport Layer (Layer 4) of the OSI model, where TCP and UDP headers containing port information are processed.

Which protocol is designed to securely transfer email between servers?
SMTPS
POP3
IMAP
SMTP
    SMTPS (SMTP over SSL/TLS) is designed to securely transfer email between servers, providing encryption for the SMTP protocol which otherwise sends data in plain text.

What is the main security advantage of SFTP over FTP?
SFTP (SSH File Transfer Protocol) provides encryption of data in transit, unlike standard FTP which transfers data and credentials in plain text, making it much more secure for file transfers.

Which protocol is used to securely distribute encryption keys over a public network?
IKE (Internet Key Exchange) is a protocol used to set up a security association in the IPsec protocol suite, allowing for secure distribution of encryption keys over public networks.

What security mechanism does HTTPS use to protect data in transit?
HTTPS uses SSL/TLS encryption to protect data in transit, providing confidentiality and integrity for HTTP communications.

Which network protocol operates at the Data Link layer and is vulnerable to ARP spoofing attacks?
ARP (Address Resolution Protocol) operates at the Data Link layer (Layer 2) of the OSI model and is vulnerable to ARP spoofing attacks where an attacker sends falsified ARP messages on a local network.

What is the main security concern with the UDP protocol?
UDP (User Datagram Protocol) is connectionless and doesn't provide mechanisms for ensuring reliable delivery or flow control, which can be exploited in certain types of attacks.

Which of the following is a characteristic of the IPv6 protocol that enhances security compared to IPv4?
IPv6 requires the implementation of IPsec, which provides built-in security features like authentication and encryption, enhancing overall network security compared to IPv4.

What type of attack exploits the TCP three-way handshake process?
A SYN flood attack exploits the TCP three-way handshake process by sending a large number of SYN packets without completing the handshake, potentially exhausting server resources.

Which protocol is designed to provide confidentiality for IP packets?
IPsec (Internet Protocol Security) is designed to provide confidentiality, integrity, and authentication for IP packets, enhancing the security of IP-based communications.

What is a key security practice for router configuration?
Regularly updating router firmware is crucial for security as it often includes patches for known vulnerabilities and improves overall performance and security features.

Which of the following is NOT typically a secure method for accessing a router's administrative interface?
Telnet transmits data, including passwords, in plain text, making it insecure for router administration. SSH, HTTPS, and physical console access are more secure alternatives.

What is the purpose of implementing Access Control Lists (ACLs) on a router?
Access Control Lists (ACLs) on routers are used to filter network traffic based on specified criteria, enhancing security by controlling which packets are allowed to pass through the router.

Which of the following is a best practice for securing router passwords?
Using strong, unique passwords for each router and enabling password encryption are crucial practices for router security, protecting against unauthorized access and password cracking attempts.

What is the purpose of implementing RPF (Reverse Path Forwarding) on a router?
Reverse Path Forwarding (RPF) is a technique used on routers to prevent IP spoofing attacks by verifying the source address of incoming packets against the routing table.

Which of the following is NOT a common way to discover zero-day vulnerabilities?
Zero-day vulnerabilities, by definition, are unknown to the vendor and thus wouldn't appear in public patch notes. They are often discovered through active research or malware analysis.

What is the best defense against zero-day vulnerabilities?
While no single method can fully protect against zero-day vulnerabilities, a comprehensive, layered approach to security, combined with regular updates, provides the best defense.

What is a 'bug bounty program' in the context of zero-day vulnerabilities?
Bug bounty programs incentivize security researchers and ethical hackers to find and responsibly disclose vulnerabilities, potentially preventing zero-day exploits.

What is the primary goal of penetration testing?
Penetration testing aims to identify security weaknesses by simulating real-world attacks on a system or network, allowing organizations to address vulnerabilities before they can be exploited by malicious actors.

Which of the following is NOT a common phase in a typical penetration testing methodology?
While data recovery might be part of incident response, it's not typically a phase in penetration testing methodologies. The main phases usually include planning, reconnaissance, scanning, gaining access, maintaining access, and analysis.

What is the primary difference between black box and white box penetration testing?
Black box testing provides minimal information to the tester, simulating an external attacker, while white box testing provides full system information, simulating an insider threat or giving a more comprehensive view of the system's security.

Which of the following is NOT a common type of penetration test?
Firewall configuration testing
Network penetration testing
Web application penetration testing
Social engineering testing
    While firewall testing might be part of a network penetration test, it's not typically considered a standalone type of penetration test.  The other options are common, distinct types of penetration testing.

What is the purpose of the 'exploitation' phase in penetration testing?
The exploitation phase involves actively attempting to exploit vulnerabilities identified in earlier phases, demonstrating the potential impact of these vulnerabilities if exploited by a malicious actor.

What is the primary goal of reconnaissance in cybersecurity?
Reconnaissance is the first phase in many cyber attacks, focusing on gathering information about the target to identify potential vulnerabilities and attack vectors.

Which of the following is an example of passive reconnaissance?
Passive reconnaissance involves gathering information without directly interacting with the target system. WHOIS lookups can be performed without alerting the target.

What does the term 'footprinting' refer to in reconnaissance?
Footprinting is the process of creating a comprehensive profile of the target, including information about network infrastructure, security posture, and potential vulnerabilities.

Which tool is commonly used for DNS enumeration during reconnaissance?
DNSenum is a tool specifically designed for gathering DNS information, which is crucial during the reconnaissance phase to understand the target's network structure.

What is 'social media reconnaissance' in the context of cybersecurity?
Social media reconnaissance involves collecting publicly available information from social media platforms to build profiles of individuals or organizations, which can be used in further attacks or social engineering attempts.

What is the primary purpose of vulnerability scanning tools?
Vulnerability scanning tools are designed to proactively identify potential security weaknesses in systems or networks before they can be exploited by malicious actors.

Which of the following is NOT a common feature of vulnerability scanning tools?
While vulnerability scanners can identify and report on vulnerabilities, they typically do not automatically patch them. Patching usually requires human intervention and separate patch management processes.

What is the difference between an authenticated and unauthenticated vulnerability scan?
Authenticated scans use valid credentials to log into systems, allowing for more comprehensive internal scanning and potentially uncovering vulnerabilities that might not be visible externally.

Which of the following is a popular open-source vulnerability scanner?
Nessus
OpenVAS
Qualys
Rapid7 InsightVM
    OpenVAS (Open Vulnerability Assessment System) is a popular, comprehensive open-source vulnerability scanner used by many organizations for security assessments.

What potential issue should be considered when running vulnerability scans on production systems?
Vulnerability scans can be resource-intensive and might potentially disrupt normal system operations, especially on production systems. Care should be taken to schedule scans appropriately and use appropriate scan settings.

What is the main characteristic of a brute force attack?
Brute force attacks attempt to gain unauthorized access by systematically trying every possible combination of characters until the correct one is found.

Which of the following is a major disadvantage of brute force attacks?
Brute force attacks, while thorough, can be extremely time-consuming, especially for longer passwords or keys, making them impractical in many situations.

What is a 'hybrid' brute force attack?
A hybrid brute force attack combines elements of both brute force and dictionary attacks, often using word lists as a base and applying various transformations or additions.

Which of the following is an effective defense against brute force attacks?
Account lockout policies, which temporarily or permanently lock an account after a certain number of failed login attempts, can significantly mitigate the effectiveness of brute force attacks.

What is 'password salting' in the context of defending against brute force attacks?
Password salting involves adding random data to a password before hashing, making it much more difficult for attackers to use precomputed hash tables in brute force attacks.

What is the primary difference between a dictionary attack and a brute force attack?
Unlike brute force attacks that try all possible combinations, dictionary attacks use a curated list of likely passwords, often based on connon words or known password databases.

Which of the following is a common source for creating dictionary attack wordlists?
Leaked password databases from previous breaches are often used to create wordlists for dictionary attacks, as they contain real-world passwords that users have actually chosen.

What is 'password masking' in the context of dictionary attacks?
Password masking involves applying conunon character substitutions (e.g., for '1' for to dictionary words, expanding the attack to catch passwords that use these conunon variations).

Which of the following passwords is most resistant to a basic dictionary attack?
password123
Ietmein
Treub4dor&3
qwerty
    Treub4dor&3

What technique can make dictionary attacks more effective against complex password policies?
Rule-based mutations apply various transformations to dictionary words (like capitalization, adding numbers or symbols) to create passwords that meet complex policy requirements while still being based on dictionary words.

What is a rainbow table in the context of password cracking?
Rainbow tables are precomputed tables for reversing cryptographic hash functions, used to crack password hashes more quickly than brute force methods.

What is the main advantage of using rainbow tables over brute force attacks?
Rainbow tables trade computational time for storage space, allowing for faster password cracking compared to brute force methods, especially for shorter passwords.

Which of the following is an effective defense against rainbow table attacks?
Password salting adds random data to passwords before hashing, making precomputed rainbow tables ineffective as each salt creates a unique hash.

What is a limitation of rainbow tables?
Rainbow tables are ineffective against salted hashes because the salt introduces randomness that isn't precomputed in the table, requiring a unique table for each salt.

In the context of rainbow tables, what does the term 'chain' refer to?
In rainbow tables, a 'chain' refers to a sequence of alternating hash and reduction functions, allowing the table to cover a large password space with less storage.

What is SQL injection?
SQL injection is a code injection technique used to attack data-driven applications by inserting malicious SQL statements into application queries.

Which of the following is a common consequence of a successful SQL injection attack?
Unauthorized access to sensitive data

What is the purpose of using the UNION operator in SQL injection attacks?
The UNION operator is often used in SQL injection attacks to combine the result of the intended query with a malicious query, allowing attackers to retrieve additional data.

Which of the following is NOT a best practice for preventing SQL injection?
Using prepared statements with parameterized queries
Disabling error messages in production
Implementing proper input validation
Escaping user inputs
    While disabling detailed error messages in production is generally good practice, it doesn't prevent SQL injection. The other options are more effective in preventing SQL injection attacks.

What is a 'blind' SQL injection attack?
In a blind SQL injection attack, the attacker doesn't receive direct feedback from the application about
the results of the injection, requiring alternative methods to infer information about the database.

What is Cross-Site Scripting (XSS)?
A vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users

Which of the following is NOT a type of XSS attack?
Stored XSS
Encrypted XSS
Reflected XSS
DOM-based XSS
    The three main types of XSS attacks are Stored (or Persistent) XSS, Reflected XSS, and XSS.
    'Encrypted XSS' is not a recognized type of XSS attack.

Which of the following is a best practice for preventing XSS attacks?
Content Security Policy (CSP) is a powerful defense against XSS attacks, allowing developers to specify which sources of content are allowed to be loaded or executed by the browser.

What function does the 'httpOn1y' flag serve in preventing XSS attacks?
The 'httpOn1y' flag, when set on a cookie, prevents client-side script access to that cookie, mitigating the risk of cookie theft via XSS attacks.

Which encoding technique is commonly used to prevent XSS attacks in HTML contexts?
HTML entity encoding is used to convert potentially dangerous characters into their corresponding HTML entities, preventing them from being interpreted as code when rendered in a browser.

What is Cross-Site Request Forgery (CSRF)?
CSRF is an attack that tricks the victim into submitting a malicious request to a web application in which they' re authenticated, potentially leading to unauthorized actions being performed on behalf of the victim.

Which of the following is an effective method for preventing CSRF attacks?
Implementing CSRF tokens in forms and AJAX requests
    CSRF tokens are unique, unpredictable values generated by the server and included in forms or AJAX requests. The server verifies this token before processing the request, preventing CSRF attacks.

What is the main difference between XSS and CSRF attacks?
XSS attacks exploit the trust a user has in a particular site, injecting malicious scripts that the browser executes. CSRF attacks exploit the trust a site has in a user's browser, forging requests that the site believes come from the authenticated user.

Which HTTP header can be used to protect against CSRF attacks in modern browsers?
The SameSite cookie attribute, when set to 'Strict' or 'Lax' , can prevent cookies from being sent in cross-site requests, effectively mitigating CSRF attacks in supporting browsers.

Why is the 'Synchronizer Token Pattern' effective against CSRF attacks?
The Synchronizer Token Pattern generates a unique token for each form or request, which is then validated on the server. This ensures that the request originated from a legitimate page generated by the server, preventing CSRF attacks.

What is a buffer overflow vulnerability?
A buffer overflow vulnerability occurs when a program writes more data to a buffer than it can hold, potentially overwriting adjacent memory and leading to unexpected behavior.

Which of the following can result from a buffer overflow attack?
System crash
Execution of malicious code
Data corruption
All of the above
    All of the above

Which language is particularly susceptible to buffer overflow vulnerabilities?
C and C++ are particularly susceptible to buffer overflow vulnerabilities due to their lack of built-in bounds checking.

What is the primary method to mitigate buffer overflow vulnerabilities?
Input validation is a primary method to mitigate buffer overflow vulnerabilities by ensuring that inputs do not exceed buffer capacities.

Which of the following tools can be used to detect buffer overflow vulnerabilities?
GDB (GNU Debugger) can be used to detect buffer overflow vulnerabilities by analyzing and debugging programs.

What is a DDoS (Distributed Denial of Service) attack?
A DDoS attack involves multiple systems overwhelming the resources or bandwidth of a targeted system, rendering it unavailable to users.

Which type of DDoS attack targets the application layer?
Volumetric attack
Protocol attack
Application layer attack
Network layer attack
    Application layer attack

Which type of DDoS attack involves overwhelming a network's bandwidth?
Protocol attack
Volumetric attack
Application layer attack
Phishing attack
    Volumetric attacks overwhelm a network' s bandwidth with a high volume of traffic.

Which protocol is often targeted in a protocol-based DDoS attack?
Protocol-based DDoS attacks often target vulnerabilities in the TCP/IP protocol suite.

What is the primary defense mechanism against DDoS attacks?
Antivirus software
Firewall
DDoS mitigation services
Encryption
    DDoS mitigation services are primary defense mechanisms that can detect and block malicious traffic while allowing legitimate traffic to pass through.

What is a botnet?
A botnet is a network of computers infected with malware and controlled by a malicious actor for various purposes, including DDoS attacks.

How are computers typically infected to become part of a botnet?
Through phishing emails
By downloading malicious software
By visiting compromised websites
All of the above
    All of the above

What is the primary use of a botnet?
Botnets are primarily used to perform coordinated attacks like DDoS, send spam emails, and spread malware.

Which of the following is a common sign that a computer is part of a botnet?
Increased network traffic
Frequent crashes
Unusual emails being sent from the account
All of the above
    All of the above

What is a 'bot herder'?
A 'bot herder' is an individual who controls a botnet, directing the infected computers to perform various tasks.

What is a rootkit?
A rootkit is a type of malware designed to gain unauthorized root access to a computer and hide its presence.

Which of the following methods can be used to detect rootkits?
Signature-based detection
Heuristic analysis
Behavioral analysis
All of the above
    All of the above

What is the purpose of a rootkit?
The purpose of a rootkit is to hide the presence of malicioussoftware on a system and maintain unauthorized access.
 
Which tool is commonly used to scan for rootkits on Linux systems?
chkrootkit is a commonly used tool to scan for rootkits on Linux systems.

What is a common symptom of a rootkit infection?
Conmon symptoms of a rootkit infection include frequent
crashes, slow performance, and unusual system behavior.

What is ransomware?
A type of malware that encrypts files and demands payment for decryption

Which of the following is a key strategy to prevent ransomware infections?
Regular data backups are a key strategy to prevent data loss in the event of a ransomware infection.

How can software updates help in preventing ransomware attacks?
By patching vulnerabilities that could be exploited by ransomware

Which type of email attachment is commonly used to deliver ransomware?
PDF files
ZIP files
DOC files
All of the above
    All of the above

What should you do if your system is infected with ransomware?
If your system is infected with ransomware, disconnect from the network and seek professional help to avoid further damage and potential data loss.

What is phishing?
A type of cyber attack that attempts to steal sensitive information through deceptive emails or websites

Which of the following is a common sign of a phishing email?
Unexpected attachments or links
Urgent call to action
Generic greetings (e.g., 'Dear Customer')
All of the above
    All of the above

What should you do if you receive a suspicious email?
Delete the email and report it to your IT department

How can you verify the authenticity of a website to avoid phishing?
To verify the authenticity of a website, check for HTTPS in the URL, as it indicates a secure connection.

What is 'spear phishing'?
Spear phishing is a targeted phishing attack aimed at a specific individual or organization, often using personalized information to increase the likelihood of success.

What distinguishes spear phishing from regular phishing?
It targets specific individuals or organizations using personalized information

Which tactic is commonly used in spear phishing attacks?
Spear phishing attacks connonly use personal information to build trust and increase the likelihood of the target falling for the scam.

How can organizations protect themselves against spear phishing?
Regular employee training on phishing identification

Which of the following is a potential consequence of a successful spear phishing attack?
Compromise of sensitive information
Financial loss
Unauthorized access to systems
All of the above
    All of the above

What role does social engineering play in spear phishing?
Social engineering is a key component of spear phishing, where attackers deceive and manipulate targets to gain unauthorized access or information.

What is the primary characteristic that distinguishes a whaling attack from other phishing attacks?
It focuses on high-profile executives or senior management

Which of the following is NOT typically a characteristic of a whaling attack?
Mass distribution to multiple targets

What type of information do whaling attackers often use to make their messages more convincing?
Personal information gathered through social engineering

Which of the following actions is most likely to be requested in a whaling attack?
Whaling attacks often aim to manipulate high-level executives into authorizing financial transactions or disclosing sensitive information.

What is a common disguise used in whaling attack emails?
Whaling attacks often disguise themselves as important conmunications from other executives or board members to appear legitimate and urgent.

Which of the following is NOT an effective method for preventing man-in-the-middle attacks?
Using HTTPS for all web communications
Relying solely on WEP for wireless security
Implementing strong encryption protocols
Employing certificate pinning in mobile apps
    WEP (Wired Equivalent Privacy) is an outdated and insecure protocol that can be easily compromised in man-in-the-middle attacks.

What is the purpose of certificate pinning in preventing man-in-the-middle attacks?
To encrypt all network traffic
To generate unique passwords for each session
To verify the identity of the server
To block all unknown IP addresses
    To verify the identity of the server
    Certificate pinning involves hard-coding the expected certificate or public key into the application, helping to prevent attackers from using forged certificates in man-in-the-middle attacks.

Which protocol is commonly used to secure remote access and prevent man-in-the-middle attacks?
SSH (Secure Shell) provides encrypted communications for remote access, helping to prevent man-in-the-middle attacks.

What is the primary purpose of implementing mutual authentication in preventing man-in-the-middle attacks?
Mutual authentication ensures that both parties in a comunication verify each other's identity, reducing the risk of man-in-the-middle attacks.

Which of the following is a best practice for preventing man-in-the-middle attacks on public Wi-Fi networks?
Using a VPN (Virtual Private Network) on public Wi-Fi networks encrypts traffic and helps prevent man-in-the-middle attacks.

What is the primary goal of ARP poisoning?
ARP poisoning aims to redirect network traffic by manipulating the ARP cache of network devices.

Which tool is commonly used for ARP poisoning attacks?
Ettercap is a comprehensive suite for man-in-the-middle attacks, including ARP poisoning capabilities.

What is a common defense mechanism against ARP poisoning?
Disabling ARP
Increasing network traffic
Using static ARP entries
Removing all firewalls
    Using static ARP entries for critical network devices can help prevent ARP poisoning attacks.

Which layer of the OSI model does ARP operate on?
ARP (Address Resolution Protocol) operates on the Data Link Layer (Layer 2) of the OSI model.

What is the purpose of gratuitous ARP in the context of ARP poisoning?
Gratuitous ARP can be used to initiate an ARP poisoning attack by sending unsolicited ARP replies to update the ARP caches of other devices on the network.

Which of the following is a common method used in DNS spoofing?
DNS cache poisoning is a conynon method used in DNS spoofing attacks, where false DNS information is inserted into a DNS resolver's cache.

What is the primary goal of DNS spoofing?
The main goal of DNS spoofing is to redirect users to malicious websites by providing false DNS information.

Which of the following is NOT an effective mitigation against DNS spoofing?
Relying solely on DNS caching
Implementing DNSSEC
Using encrypted DNS protocols
Regular patching of DNS servers
    While DNS caching can improve performance, relying solely on it does not protect against DNS spoofing. DNSSEC and encrypted DNS protocols are more effective mitigations.

What is pharming in the context of DNS spoofing?
Pharming is a large-scale DNS spoofing attack that aims to redirect multiple users to malicious websites by compromising DNS servers or user devices.

Which protocol does DNSSEC use to help prevent DNS spoofing?
DNSSEC uses public key cryptography to digitally sign DNS records, helping to prevent DNS spoofing attacks.

What is a common method to prevent session hijacking?
Implementing HTTPS encrypts conmunication between the client and server, making it much harder for attackers to intercept and hijack sessions.

422. Which of the following is NOT a best practice for preventing session hijacking?
Using secure, httpOn1y cookies
Implementing strong session management
Storing session IDs in URLs
Regenerating session IDs after login
    Storing session IDs in URLs

What is the purpose of implementing IP binding in session management?
IP binding ties a session to a specific IP address, making it harder for attackers to use a stolen session ID from a different location.

Which of the following helps prevent session fixation attacks?
Regenerating session IDs after authentication prevents attackers from tricking users into using a known session ID, thus mitigating session fixation attacks.

What is the primary purpose of implementing secure flag for cookies?
To encrypt cookie contents
To increase cookie storage capacity
To prevent cookies from being
sent over unencrypted connections
To make cookies accessible to client-side scripts
    The secure flag ensures that cookies are only sent over HTTPS connections, preventing them from being intercepted over insecure channels.

Which of the following is NOT a common password cracking tool?
Wireshark
John the Ripper
Hashcat
Hydra
    Wireshark is a network protocol analyzer, not a password cracking tool. John the Ripper, Hashcat, and Hydra are well-known password cracking tools.

What technique does a rainbow table attack use for password cracking?
Rainbow tables use pre-computed hash chains to crack passwords, trading computational time for storage space.

What is the primary advantage of GPU-based password cracking tools like Hashcat?
GPU-based password cracking tools like Hashcat leverage the parallel processing power of GPUs to achieve significantly faster cracking speeds compared to CPU-based tools.

What is the primary purpose of cryptography in information security?
The primary purpose of cryptography is to protect the confidentiality of data by making it unreadable to unauthorized parties.

Which of the following is NOT a main goal of cryptography?
Confidentiality
Integrity
Availability
Non-repudiation
    Non-repudiation

What is the difference between encoding and encryption?
Encryption is a process that uses a key to secure data, while encoding is a method of transforming data into a different format without the need for a secret key.
    Encryption Examples:
        Base64 encoding
        ASCII ↔ Unicode
        URL encoding (%20 for space)
    Encrpytion Examples:
        AES
        RSA
        DES (legacy)

What is the purpose of a nonce in cryptography?
A nonce (number used once) is used to ensure uniqueness in encryption, preventing replay attacks and ensuring that encrypted messages are different even if the plaintext is the same.

Which of the following is a characteristic of a cryptographically secure hash function?
A cryptographically secure hash function should have a fixed output size, regardless of the input size, to maintain consistency and security.

What is the primary difference between MD5 and SHA-256 hashing algorithms?
MD5 is generally faster than SHA-256 but is considered cryptographically broken due to its vulnerability to collision attacks. SHA-256 is more secure but slower.

Which of the following is NOT a property of a good cryptographic hash function?
Reversibility
Pre-image resistance
Collision resistance
Avalanche effect
    A good cryptographic hash function should not be reversible. It should be a one-way function, making it computationally infeasible to determine the input from the hash value.

What is the purpose of salt in password hashing?
To speed up the hashing process
To reduce the size of the hash
To make the hash more secure
To make the hash reversible
    Salt is added to passwords before hashing to create unique hashes for identical passwords, protecting against rainbow table attacks and making the hashing process more secure.

Which hashing algorithm is commonly used for digital signatures in modern systems?
SHA-256, part of the SHA-2 family, is widely used for digital signatures due to its security strength and resistance to known attacks.

What is the main difference between symmetric and asymmetric encryption?
Symmetric encryption uses a single shared key and is generally faster than asymetric encryption, which uses a pair of public and private keys.

Which of the following is an example of a symmetric encryption algorithm?
AES
RSA
ECC
Diffie-Hellman
    AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm, while the others are asymmetric algorithms or key exchange protocols.

What is the primary advantage of asymmetric encryption over symmetric encryption?
Asymmetric encryption solves the key distribution problem by allowing secure communication without the need to exchange a secret key beforehand.

What is asymmetric encryption?
Asymmetric encryption uses a pair of keys: a public key for encryption and a private key for decryption.

Which of the following is NOT a characteristic of asymmetric encryption?
Asymmetric encryption uses different keys for encryption and decryption, making it more secure but slower than symmetric encryption.

Which of the following is a common example of asymmetric encryption?
RSA
AES
Blowfish
3DES
    RSA (Rivest-Shamir-Ad1eman) is a widely used asymmetric encryption algorithm.

What is steganography?
Steganography is the technique of hiding information within other non-secret text or data, such as images or audio files.

Which of the following is NOT a steganography technique?
LSB (Least Significant Bit) insertion
Masking and filtering
RSA encryption
Transform domain techniques
    RSA encryption is not a steganography technique; it is a method of asymetric encryption.

What does LSB (Least Significant Bit) insertion involve?
Modifying the least significant bits of pixel values in an image
Hiding information in the metadata of a file
Encoding information in the frequency domain
Using watermarks to hide information  
    LSB insertion involves modifying the least significant bits of pixel values in an image to hide information.

Which steganography technique uses the frequency domain?
Transform domain techniques involve hiding information in the frequency domain of a file, often making it more resistant to compression and transformation.

What is a common application of steganography?
A camon application of steganography is hiding watermarks in digital media to protect intellectual property.

What is cloud security?
Cloud security involves policies, technologies, and controls to protect data, applications, and infrastructure in cloud computing environments.

Which of the following is a primary concern in cloud security?
Data breaches are a primary concern In cloud security, as sensitive information can be exposed if not properly protected.

Which of the following is a key component of cloud security?
Access management is a key component of cloud security, ensuring that only authorized users can access specific resources.

What is the purpose of encryption in cloud security?
Encryption is used in cloud security to protect data from unauthorized access, ensuring that even if data is intercepted, it cannot be read without the decryption key.

Which of the following is a key difference between cloud and on-premises security?
Cloud security involves a shared responsibility model, where both the provider and the customer have roles in securing the environment.

In an on-premises environment, who is primarily responsible for security?
In an on-premises environment, the customer is primarily responsible for the security of their infrastructure and data.

What is a common security advantage of cloud environments over on-premises environments?
Cloud environments often come with built-in advanced security features and compliance certifications that can be more challenging to implement on-premises.

Which of the following is typically easier to achieve in a cloud environment compared to an on-premises environment?
Compliance with regulatory standards is often easier in cloud environments due to the provider's ability to implement and maintain compliance at scale.

What is one challenge unique to cloud security compared to on-premises security?
Ensuring data locality and sovereignty can be a challenge in cloud environments due to data being stored in various geographical locations.

What is Infrastructure as Code (IaC)?
Infrastructure as Code (IaC) is a technique for managing and provisioning infrastructure through machine-readable definition files, allowing for automated and consistent setups.

Which of the following is a security benefit of using IaC?
Using Iac ensures consistency and repeatability in configurations, reducing the risk of configuration drift and human error.

Which security risk is associated with IaC?
Misconfigured infrastructure as code can lead to vulnerabilities, making it crucial to ensure proper validation and testing of Iac scripts.

How can version control systems enhance Iac security?
Version control systems provide a historical record of changes, making it easier to track, review, and revert changes, enhancing the security and stability of IaC.

What role does automated testing play in Iac security?
Automated testing in Iac helps identify and fix configuration issues early in the development process, reducing the likelihood of security vulnerabilities.

What is serverless computing?
Serverless computing is a cloud computing execution model where the cloud provider dynamically manages the allocation of machine resources.

Which of the following is a security challenge unique to serverless computing?
Serverless computing introduces unique security challenges, such as protecting against function invocation attacks, where attackers exploit the serverless environment to execute unauthorized functions.

How can one mitigate the risk of insecure dependencies in serverless applications?
By regularly updating and patching third-party libraries

What is a common method for securing communication between serverless functions?
Implementing encryption protocols like TLS is a convnon method for securing comunication between serverless functions, ensuring data integrity and confidentiality.

What is the primary purpose of static code analysis tools in cybersecurity?
Static code analysis tools examine source code without executing it, helping identify potential security vulnerabilities, coding standards violations, and other issues early in the development process.

Which of the following is NOT typically a feature of static code analysis tools?
Identifying SQL injection vulnerabilities
Real-time monitoring of system performance
Detecting buffer overflow risks
Checking for compliance with coding standards
    Real-time monitoring of system performance

What is a common challenge when using static code analysis tools?
Static code analysis tools can sometimes flag issues that aren't actual vulnerabilities (false positives), requiring human review to validate results.

In the context of DevSecOps, when is the ideal time to run static code analysis?
In DevSecOps, static code analysis is typically integrated into the CI/CD pipeline to catch issues early and frequently throughout the development process.

Which of the following is an advantage of using static code analysis tools?
Static code analysis tools can help educate developers by highlighting potential security issues and best practices, improving overall code quality and security awareness.

What is the main purpose of antivirus software?
Antivirus software is designed to detect, prevent, and remove malicious software (malware) from computer systems, protecting them from various types of threats.

Which of the following is NOT a common detection method used by modern antivirus solutions?
While signature-based detection, heuristic analysis, and behavioral monitoring are common antivirus detection methods, social engineering is a type of attack rather than a detection method.

What is a potential drawback of relying solely on signature-based antivirus detection?
Signature-based detection relies on known malware signatures. It may fail to detect new or modified malware that doesn't match existing signatures, which is why modern antivirus solutions use multiple detection methods.

What is the purpose of anti-malware software's real-time protection feature?
Real-time protection in anti-malware software continuously monitors system activities, file operations, and network traffic to detect and prevent malware infections as they occur.

Which of the following best describes the relationship between antivirus and anti-malware software?
Antivirus software traditionally focused on viruses, while anti- malware is a broader term that includes protection against various types of malicious software, including viruses. Modern antivirus solutions often include comprehensive anti-malware capabilities.

What is the primary function of Endpoint Detection and Response (EDR) systems?
EDR systems are designed to continuously monitor endpoint devices for suspicious activities, detect security incidents, and provide tools for responding to and mitigating threats.

Which of the following is NOT typically a feature of EDR solutions?
While EDR solutions often include real-time detection, automated response, and forensic capabilities, network traffic encryption is typically a function of other security tools like VPNs or SSL/TLS protocols.

How does EDR differ from traditional antivirus software?
While traditional antivirus software primarily focuses on preventing and detecting known malware, EDR provides more comprehensive endpoint monitoring, advanced threat detection, incident response capabilities, and often includes behavioral analysis.

What is a key benefit of using EDR in conjunction with a Security Information and Event Management (SIEM) system?
Integrating EDR with SIEM allows organizations to correlate endpoint data with other security events across the network, providing a more holistic view of the security environment and enabling more effective threat detection and response.

Which of the following actions is typically part of the 'Response' capability in EDR?
The 'Response' in EDR often includes capabilities like isolating infected endpoints to prevent threat spread, killing malicious processes, or rolling back to a clean system state. Isolating an infected endpoint is a common response action to contain a threat.

What is the primary goal of patch management in cybersecurity?
The main purpose of patch management is to apply updates that fix known vulnerabilities, bugs, and security issues in software and systems, thereby reducing the attack surface and improving overall security posture.

Which of the following is NOT typically a step in the patch management process?
The patch management process typically involves identifying, testing, and deploying patches. Developing new software features is not part of patch management, but rather part of the software development lifecycle.

What is a potential risk of delayed patch management?
Delaying patch management can leave systems vulnerable to known exploits that have been fixed in available patches. This increases the risk of successful attacks targeting these unpatched vulnerabilities.

Which of the following best describes the concept of 'risk-based patch management' ?
Risk-based patch management involves assessing the potential impact of vulnerabilities and the criticality of affected systems to prioritize which patches should be applied first. This approach helps organizations balance security needs with operational considerations.

What is Mobile Device Management (MDM) in the context of mobile device security?
Mobile Device Management (MDM) is a type of security software used by IT departments to monitor, manage and secure employees' mobile devices across multiple service providers and operating systems.

Which of the following is NOT typically a feature of mobile device security solutions?
While mobile device security solutions often include remote wiping, password policy enforcement, and software update management, physical tracking of device location is typically a separate function and may have legal implications.

What is the primary purpose of app sandboxing in mobile device security?
App sandboxing is a security mechanism used in mobile operating systems to isolate apps from each other and from critical system components, limiting the potential damage from a compromised app.

What is a potential security risk of using public Wi-Fi on mobile devices?
Public Wi-Fi networks are often unsecured, making them vulnerable to man-in-the-middle attacks where an attacker can intercept data transmitted between the mobile device and the network.

Which of the following best describes the concept of 'containerization' in mobile device security?
Containerization in mobile security refers to the practice of separating personal and work data on a single device, often creating a secure 'container' for work-related apps and data that can be managed separately from personal content.

What is the primary goal of Identity and Access Management (IAM)?
IAM systems are designed to ensure that the right individuals access the right resources at the right times for the right reasons, maintaining the confidentiality and integrity of sensitive information.

Which of the following is NOT typically a component of IAM systems?
single sign-on (SSO)
Intrusion Detection System (IDS)
Multi-Factor Authentication (MFA)
Role-Based Access Control (RBAC)
    While SSO, MFA, and RBAC are common components of IAM systems, an Intrusion Detection System (IDS) is a separate security tool focused on detecting unauthorized access attempts rather than managing identities and access.

What is the purpose of federation in Identity and Access Management?
Federation in IAM allows organizations to share identity information across multiple systems or even organizations, enabling users to access various services with a single set of credentials while maintaining separate user directories.

Which of the following best describes the concept of 'identity lifecycle management' in IAM?
Identity lifecycle management refers to the end-to-end process of managing user identities within an organization, including creation, provisioning, modifications, and eventual deprovisioning or retirement of accounts.

What is the primary goal of digital forensic analysis in cybersecurity?
Digital forensic analysis aims to collect, preserve, and analyze digital evidence to reconstruct events, often for legal or investigative purposes in the aftermath of a security incident or cyber crime.

Which of the following is NOT typically a stage in the digital forensics process?
Collection of evidence
Deletion of all examined data
Analysis of data
Presentation of findings
    The digital forensics process typically involves collection, preservation, analysis, and presentation of evidence. Deletion of examined data is not a standard step and could potentially destroy important evidence.

What is the importance of maintaining a chain of custody in forensic analysis?
Maintaining a chain of custody documents the movement and handling of evidence from its collection through analysis and presentation. This is crucial for ensuring the integrity and admissibility of evidence in legal proceedings.

What is the purpose of 'write blockers' in digital forensics?
Write blockers are hardware or software tools used in digital forensics to prevent any data from being written to the storage device being examined, ensuring the integrity of the original evidence.

Which of the following best describes the concept of 'live forensics'?
Live forensics involves collecting and analyzing data from a computer system while it's still operational. This is particularly useful for capturing volatile data that would be lost when the system is powered down, such as running processes and network connections.

Which of the following is NOT a common technique in reverse engineering?
Disassembly
Port scanning
Debugging
API hooking
    Reverse engineering often involves disassembly (converting machine code to assembly), debugging (examining the program's execution), and API hooking (intercepting function calls). Port scanning is not a reverse engineering technique, but rather a network reconnaissance method.

What does RTO stand for in the context of disaster recovery?
RTO (Recovery Time Objective) is the targeted duration of time within which a business process must be restored after a disaster to avoid unacceptable consequences associated with a break in business continuity.

Which of the following is NOT typically part of a business continuity plan?
Business continuity plans focus on maintaining essential business functions during and after a disaster. While they include critical function identification, alternative procedures, and communication protocols, detailed employee vacation schedules are not typically part of these plans.

What is the difference between hot, warm, and cold sites in disaster recovery?
In disaster recovery, hot sites are fully operational alternate sites with real-time data replication, warm sites have hardware and connectivity but require some setup time, and cold sites only provide basic infrastructure and require significant setup time.

What is the purpose of conducting a Business Impact Analysis (BIA) in disaster recovery planning?
To identify and prioritize critical business processes and the impact of their disruption

What is the primary goal of post-incident analysis in cybersecurity?
Post-incident analysis aims to understand what happened during a security incident, how it was handled, and what can be improved in future responses. It's a learning opportunity rather than a blame-assignment exercise.

Which of the following is NOT typically a component of a post-incident report?
Timeline of the incident
Personal details of all employees involved
Analysis of the root cause
Recommendations for improvement
    While post-incident reports typically include timelines, root cause analysis, and reconnendations, they generally don't include personal details of all employees involved, as this could violate privacy and isn't necessary for improving security measures.

What is the purpose of a 'lessons learned' meeting in post-incident analysis?
A 'lessons learned' meeting is a crucial part of post- incident analysis where team members discuss what went well, what didn't, and how processes can be improved. It's focused on constructive learning rather than blame or punishment.

In the context of post-incident analysis, what does ' root cause analysis' refer to?
Identifying the fundamental reason the incident occurred

What is the importance of establishing a 'timeline of events' in post-incident reporting?
To provide a clear sequence of how the incident unfolded and was addressed

What is the primary purpose of an access control system in cybersecurity?
Access control systems are fundamental to cybersecurity, ensuring that only authorized entities (users, processes, devices) can access specific resources, thereby maintaining confidentiality and integrity of systems and data.

Which of the following is NOT a common type of access control model?
Role-Based Access Control (RBAC)
Random Access Control (RAC)
Mandatory Access Control (MAC)
Discretionary Access Control (DAC)
    RBAC, MAC, and DAC are well-established access control models. 'Random Access Control' is not a standard model in cybersecurity access control systems.

What is the principle of 'separation of duties' in access control?
Separation of duties is a principle where sensitive tasks are divided among multiple people to prevent fraud or errors. This ensures that no single individual has excessive control over critical processes.

What is a 'compensating control' in the context of access control?
A compensating control is an alternative security measure implemented when the primary control is not feasible or practical. It provides a similar level of protection as the original control while addressing specific limitations or constraints.

What is the primary purpose of network surveillance in cybersecurity?
Network surveillance in cybersecurity involves monitoring network activities to detect potential security threats, unusual behavior, or policy violations, helping organizations maintain a secure IT environment.

Which of the following is NOT typically a component of a comprehensive network monitoring system?
Intrusion Detection System (IDS)
Automatic Code Generator
Network Traffic Analyzer
Log Management Tool
    While IDS, network traffic analyzers, and log management tools are connon in network monitoring, automatic code generators are not typically part of surveillance systems. They are more related to software development processes.

What is 'packet sniffing' in the context of network surveillance?
Packet sniffing involves capturing and analyzing data packets as they travel across a network. It can be used legitimately for network troubleshooting and monitoring, but can also be misused for malicious purposes.

What ethical considerations should be taken into account when implementing employee monitoring systems?
Implementing employee monitoring systems requires careful consideration of both security needs and employee privacy rights. Organizations need to balance these concerns, often through clear policies, transparency, and limiting monitoring to what's necessary for legitimate business purposes.

What is the purpose of implementing 'honeypots' in network surveillance?
Honeypots are decoy systems or networks set up to attract potential attackers. They serve to detect, deflect, or study hacking attempts, providing valuable intelligence about attack methods and attacker behaviors.

What is 'data exfiltration' in the context of network surveillance?
Data exfiltration refers to the unauthorized transfer of data from a computer or network to an external destination. Detecting and preventing data exfiltration is a crucial goal of many network surveillance systems.

What is the role of 'behavioral analytics' in cybersecurity monitoring?
Behavioral analytics in cybersecurity involves analyzing patterns of behavior to identify anomalies that may indicate security threats. This can include unusual user activities, unexpected system behaviors, or abnormal network traffic patterns.

What is the principle of 'defense in depth' in relation to surveillance and monitoring?
Defense in depth is a cybersecurity approach that uses multiple layers of security controls throughout an IT system. In surveillance and monitoring, this might involve using various tools and techniques at different points in the network to provide comprehensive coverage.

What is the primary characteristic that defines malware?
Malware, short for malicious software, is any software intentionally designed to cause damage to a computer, server, client, or computer network, or to gain unauthorized access to a system.

Which of the following is NOT a common type of malware?
Virus
Trojan horse
Firewall
Ransomware
    While viruses, Trojan horses, and ransonware are types of malware, a firewall is a network security device that monitors and filters incoming and outgoing network traffic based on predetermined security rules.

What is the primary difference between a virus and a worm?
Worms can spread without user action, viruses require user action
    While both viruses and worms can self-replicate, worms can spread independently across networks without any action from the user, whereas viruses typically require some form of user action to spread.

What is a 'polymorphic' malware?
Polymorphic malware is designed to constantly change its code to avoid detection by antivirus software. This makes it particularly challenging for traditional signature-based detection methods.

What is the primary purpose of 'fileless' malware?
To avoid detection by not writing files to the disk
    Fileless malware operates in a computer's RAM and uses existing system tools to carry out malicious activities. By not writing files to the disk, it can evade many traditional antivirus detection methods.

What is the primary purpose of environmental controls in a data center?
Environmental controls in a data center are primarily designed to maintain optimal temperature, humidity, and air quality conditions to ensure the proper functioning and longevity of IT equipment.

Which of the following is NOT typically considered an environmental control in a data center?
HVAC systems
Intrusion detection systems
Fire suppression systems
Water leak detection systems
    While HVAC, fire suppression, and water leak detection are environmental controls, intrusion detection systems are part of physical security controls rather than environmental controls.

What is the recommended temperature range for a data center according to ASHRAE guidelines?
The American Society of Heating, Refrigerating and Air- Conditioning Engineers (ASHRAE) recomends a temperature range of 64.4-80.°F (18-27°C) for data centers to balance equipment performance and energy efficiency.

What is the purpose of a raised floor in a data center?
Raised floors in data centers create a space beneath the floor tiles for cable management and airflow distribution. This helps in efficient cooling and organized cable routing.

What is 'hot aisle containment' in data center design?
Hot aisle containment is a data center cooling technique where the hot air exhaust from server racks is isolated and directed to the cooling system, improving cooling efficiency and reducing energy consumption.

What is the primary goal of secure facilities design in cybersecurity?
Secure facilities design in cybersecurity aims to create a physical environment that protects IT assets, data, and personnel from unauthorized access, environmental hazards, and other physical threats.

Which of the following is NOT typically a component of secure facilities design?
Employee satisfaction surveys
Access control systems
Surveillance cameras
Secure storage areas
    While access control, surveillance, and secure storage are key components of secure facilities design, employee satisfaction surveys, though important for other reasons, are not directly related to physical security design.

What is the concept of 'defense in depth' in secure facilities design?
Implementing multiple layers of security controls

What is a 'mantrap' in secure facilities design?
A mantrap is a small space with two interlocking doors, where the second door won't open until the first one is closed and locked. It's used to control access and prevent tailgating in high-security areas.

What is the purpose of 'crime prevention through environmental design' (CPTED) in secure facilities?
CPTED is an approach to deter criminal behavior through environmental design. It includes strategies like natural surveillance, access control, and territorial reinforcement to create safer spaces.

What is the primary goal of cybersecurity employee training programs?
To educate employees about cyber threats and best practices

Which of the following is NOT typically included in a basic cybersecurity training program?
Password best practices
Phishing awareness
Advanced hacking techniques
Data handling procedures
    While password practices, phishing awareness, and data handling are common in basic training, advanced hacking techniques are typically not taught to general employees and are more relevant for specialized cybersecurity roles.

What is the concept of 'role-based' training in cybersecurity education?
Providing different levels of training based on an employee's job function

What is the purpose of conducting 'tabletop exercises' in cybersecurity training?
Tabletop exercises are discussion-based sessions where team members meet to discuss their roles and responses during an emergency situation. In cybersecurity, they're used to practice and evaluate incident response procedures.

What is the 'human firewall' concept in cybersecurity?
The 'human firewall' concept emphasizes that well-trained employees act as a critical layer of defense against cyber threats. It recognizes that human awareness and behavior are crucial components of an organization's overall security posture.

What is the primary purpose of conducting phishing simulations?
To test and improve employees' ability to recognize and report phishing attempts

Which of the following is NOT a typical component of a phishing simulation campaign?
Sharing individual results publicly within the organization
Crafting fake phishing emails
Tracking employee responses
Providing immediate feedback and education
    While crafting emails, tracking responses, and providing feedback are standard practices, sharing individual results publicly is generally avoided as it can lead to shame or embarrassment, which is counterproductive to the learning process.

What is 'spear phishing' in the context of phishing simulations?
Targeting specific individuals or groups with personalized phishing attempts

What is the purpose of including 'benign indicators' in phishing simulation emails?
Benign indicators are subtle clues included in simulation emails to indicate that they are not real threats. These can help prevent unnecessary panic or security responses, while still testing employees' awareness.

What ethical consideration is important when conducting phishing simulations?
Ethical phishing simulations should balance the need for realistic testing with respect for employees time, trust, and privacy. The goal is to educate and improve security, not to trick or embarrass employees.

Which of the following best describes how A1 can be used to enhance intrusion detection systems?
A1 can enhance intrusion detection systems by analyzing large volumes of network traffic data to identify patterns and anomalies that may indicate a security threat, often detecting subtle or novel attacks that traditional rule-based systems might miss.

What is a potential risk of using machine learning models in cybersecurity?
Machine learning in cybersecurity can be vulnerable to adversarial attacks, where an attacker manipulates input data to cause the model to make incorrect predictions or classifications, potentially bypassing security measures.

How can federated learning contribute to cybersecurity?
By allowxng model traxnxng on decentralized data sources
    Federated learning allows multiple parties to train a machine learning rnodel collaboratively without sharing raw data, enabling organizations to benefit from collective intelligence while maintaining data privacy and security.

Which of the following is NOT a common application of A1 in email security?
Spam detection
Automatic email encryption
Phishing identification
Malware attachment detection
    While A1 is conmonly used for spam detection, phishing identification, and malware attachment detection in email security, automatic email encryption is typically a separate process not directly tied to A1 capabilities.

What is the primary benefit of using A1-powered User and Entity Behavior Analytics (UEBA) in cybersecurity?
AI-powered UEBA can analyze user and entity behaviors to establish baselines and detect anomalies that may indicate insider threats or compromised accounts, providing an additional layer of security beyond traditional rule-based systems.

What is MQTT in the context of IoT security?
MQTT (Message Queuing Telemetry Transport) is a lightweight publish-subscribe messaging protocol designed for IoT devices with limited resources and unreliable networks.

Which of the following is a security vulnerability often associated with CoAP?
It's vulnerable to amplification attacks when used over UDP
    CoAP (Constrained Application Protocol) when used over UDP can be vulnerable to amplification attacks, where an attacker sends small requests that generate larger responses, potentially leading to DDoS attacks.

What is a key security feature of AMQP (Advanced Message Queuing Protocol)?
AMQP supports the use of TLS (Transport Layer Security) for encrypting communications, providing confidentiality and integrity for messages transmitted between clients and brokers.

Which of the following is NOT a common security measure for IoT devices?
Regular firmware updates
Strong, unique passwords
Disabling all remote access
Network segmentation
    While regular updates, strong passwords, and network segmentation are common security measures for IoT devices, completely disabling all remote access is not typically recommended as it can prevent necessary management and updates.

What is a key difference between MQTT and CoAP in terms of security?
MQTT typically uses TCP and can be secured with TLS, while CoAP often uses UDP and can be secured with DTLS (Datagram TLS). This difference stems from their design goals and typical use cases in IoT environments.

What is a 'software bill of materials' (SBOM) in the context of supply chain security?
A software bill of materials is a formal record containing the details and supply chain relationships of various components used in building software. It's crucial for understanding and managing potential vulnerabilities in the software supply chain.

Which of the following is NOT a common supply chain attack vector?
Third-party software compromises
Strong encryption protocols
Hardware tampering
Social engineering of employees
    Conmon supply chain attack vectors include third-party software compromises, hardware tampering, and social engineering. Strong encryption protocols are actually a defense against attacks, not an attack vector.

What is the purpose of the ISO 28000 standard in supply chain security?
ISO 28000 is an international standard that specifies the requirements for a security management system in the supply chain. It helps organizations identify security threats and implement controls to manage potential risks.

What is 'chain of custody' in supply chain security?
In supply chain security, 'chain of custody' refers to the documentation or paper trail showing the seizure, custody, control, transfer, analysis, and disposition of physical or electronic evidence. It's crucial for maintaining the integrity of products and information throughout the supply chain.

What is the primary goal of supply chain security?
The primary goal of supply chain security is to protect the integrity, quality, and distribution of products from manufacturer to end-user, safeguarding against tampering, counterfeiting, and other threats.

What is the primary purpose of a consensus mechanism in blockchain technology?
Consensus mechanisms are crucial in blockchain technology as they allow distributed networks to agree on the state of the blockchain without relying on a central authority.

Which of the following is NOT a characteristic of blockchain technology?
Decentralization
Immutability
Centralized control
Transparency
    Blockchain technology is characterized by decentralization, immutability, and transparency. Centralized control is contrary to the core principles of blockchain.

What is a 'smart contract' in the context of blockchain technology?
Smart contracts are self-executing contracts with the terms of the agreement directly written into lines of code. They automatically execute when predefined conditions are met.

What is the purpose of a 'nonce' in blockchain mining?
In blockchain mining, a nonce is a number used once to find a hash that meets the difficulty target set by the network, which is crucial for the proof-of-work consensus mechanism.

What is a '51% attack' in blockchain technology?
A 51% attack occurs when a single entity or organization is able to control more than of the network's mining power, potentially allowing them to manipulate the blockchain.

How does Grover's algorithm impact symmetric key cryptography?
Grover's algorithm can potentially reduce the security of symetric key cryptography by effectively halving the key length, requiring larger key sizes for the same level of security.

What is the primary challenge in implementing quantum-resistant algorithms today?
Implementing quantum-resistant algorithms often requires more computational resources, making it challenging to balance strong security with system performance and efficiency.

Which of the following is a potential positive impact of quantum computing on cybersecurity?
Quantum computing can potentially improve the generation of truly random numbers, which is crucial for strong cryptographic systems.

What is quantum key distribution (QKD) vulnerable to?
While QKD provides theoretical perfect security, practical implementations can be vulnerable to man-in-the-middle attacks on the classical communication channel used for key verification.

How does quantum computing potentially impact blockchain technology?
Quantum computing could potentially break the cryptographic algorithms used in some blockchain systems, particularly those relying on elliptic curve cryptography.

What is the concept of 'crypto-agility' in the context of quantum computing and cybersecurity?
Crypto-agility refers to the ability to quickly switch cryptographic algorithms without significant system changes, which is crucial for adapting to quantum computing threats.

Which organization is leading efforts to standardize post-quantum cryptography algorithms?
The National Institute of Standards and Technology (NIST) is leading efforts to evaluate and standardize post-quantum cryptography algorithms.

What is quantum entanglement and how does it relate to cybersecurity?
A phenomenon where quantum particles are connected regardless of distance, useful for secure communication
    Quantum entanglement is a phenomenon that can be leveraged for secure conmunication, as any attempt to intercept the communication would disturb the entangled state.

What is the primary advantage of quantum random number generators (QRNGs) over classical random number generators?
QRNGs leverage quantum phenomena to produce truly random numbers, which is crucial for strong encryption and security protocols.

What is the 'no-cloning theorem' in quantum mechanics and why is it important for quantum cryptography?
It demonstrates that it's impossible to create an identical copy of an arbitrary unknown quantum state

The no-cloning theorem is crucial for quantum cryptography as it ensures that quantum information can't be copied without detection, providing a basis for secure communication.

How does quantum computing impact the security of current public-key cryptography systems?
Quantum computers have the potential to break many current public-key cryptography systems, particularly those based on integer factorization and discrete logarithm problems.

What is 'harvest now, decrypt later' in the context of quantum computing and cybersecurity?
This strategy involves collecting currently encrypted data with the intention of decrypting it in the future when sufficiently powerful quantum computers become available.

Which of the following is NOT a characteristic of post-quantum cryptography?
Designed to be secure against both quantum and classical computers
Relies on quantum principles for its security
Can be implemented with existing computer hardware
Focuses on developing new mathematical problems that are hard for quantum computers to solve
    Post-quantum cryptography aims to develop new algorithms that are secure against quantum computers but can be implemented on classical hardware.

What is the primary threat that quantum computing poses to current cryptographic systems?
Increased processing speed
Potential to factor large numbers quickly
Ability to break symmetric encryption
Enhanced random number generation
    Quantum computers have the potential to break many current cryptographic systems by factoring large numbers exponentially faster than classical computers.

Which of the following algorithms is considered quantum-resistant?
RSA
Lattice-based cryptography
ECC
Diffie-Hellman key exchange
    Lattice-based cryptography is one of the promising post-quantum cryptographic algorithms that is believed to be resistant to quantum computing attacks.

What is Shor's algorithm primarily used for in the context of quantum computing?
Shor's algorithm is a quantum algorithm for integer factorization, which poses a significant threat to RSA encryption.

What is the concept of 'quantum supremacy' ?
Quantum supremacy refers to the potential ability of quantum computers to solve certain problems that classical computers practically cannot.

Which of the following is NOT a potential application of quantum computing in cybersecurity?
Enhancing random number generation
Slowing down network communication
Improving encryption algorithms
Accelerating brute-force attacks
    Quantum computing has various potential applications in cybersecurity, but slowing down network communication is not one of them.

What is quantum key distribution (QKD) ?
A protocol for securely sharing encryption keys using quantum mechanics principles
    Quantum key distribution is a method of distributing encryption keys leveraging principles of quantum mechanics to ensure secure communication.

Which of the following best describes the concept of superposition in quantum computing?
A state where a qubit can represent both and 1 at the same time
Superposition is a fundamental principle of quantum mechanics where a qubit can exist in multiple states simultaneously until measured.

What is the main purpose of a keylogger?
Keyloggers are designed to record keystrokes, often with the intention of capturing sensitive information like passwords or financial data.

What is a macro virus?
Macro viruses are written in macro languages used by applications like Microsoft Office, and can spread through infected documents.

Which of the following best describes a RAT in the context of malware?
RAT stands for Remote Access Tool, which is a type of malware that provides unauthorized remote access to a compromised system.

What is the primary characteristic of a multipartite virus?
Multipartite viruses are capable of infecting both files and boot sectors, making them particularly versatile and difficult to remove.

What is the main purpose of cryptojacking malware?
To mine cryptocurrency using victim's resources

What is the primary purpose of adware?
To display unwanted advertisements

What is a key characteristic of a logic bomb?
A logic bomb is a piece of code that executes malicious actions when certain conditions are met, such as a specific date or user action.

What is the main characteristic of a trojan horse?
A trojan horse is malware that disguises itself as legitimate software to trick users into installing it.

What is the primary purpose of spyware?
Spyware is designed to collect information about a user or organization without their consent, often for financial gain or espionage.
```

## Side Quest
```
Host-Based Tools
Purpose	                🔴 Red Team Tools	        🔵 Blue Team Tools	               OS
Rootkit detection	    —	                        chkrootkit, rkhunter	            Linux
Privilege escalation	LinPEAS, WinPEAS	        —	                                Linux / Windows
Credential dumping	    Mimikatz	                LSA Protection, EDR alerts	        Windows
Malware execution	    Metasploit, Cobalt Strike	Microsoft Defender, CrowdStrike	    Both
Persistence	Empire,     PowerShell scripts	        Autoruns, Sysmon	                Windows
File integrity	        —	                        AIDE, Tripwire	                    Linux
Log analysis	        —	                        OSSEC, Wazuh	                    Both

Network & Web Attacks / Defense
Attack / Activity	    🔴 Red Team Tool	        🔵 Blue Team Tool	               Notes
HTTP exploitation	    Metasploit, Burp Suite	    ModSecurity (WAF)	                Web attacks
Web scanning	        Nikto, Gobuster	WAF         logs, SIEM	                        Recon vs detection
Port scanning	        Nmap	                    Zeek, Suricata	                    Nmap used by both
Packet sniffing	        Wireshark, tcpdump	        Wireshark, tcpdump	                Used by both
DDoS	                LOIC, HOIC	                Cloudflare, Fail2ban	            Mitigation
Command & Control	    Cobalt Strike	            IDS/IPS alerts	                    Detection-based

SIEM, Detection & Monitoring
Function	            🔴 Red Team	                🔵 Blue Team	                   OS
Evasion testing	        Atomic Red Team	            —	                                Both
SIEM ingestion	        —	                        Splunk, ELK Stack	                Both
Endpoint detection	    —	                        CrowdStrike, Defender ATP	        Both
Behavior detection	    —	                        Sysmon + SIEM	                    Windows

Tools Commonly Used by BOTH
Tool	                Red Team Use	            Blue Team Use
Nmap	                Reconnaissance	            Network auditing
Wireshark	            Packet sniffing	            Traffic analysis
Metasploit	            Exploitation	            Security testing
Burp Suite	            Web exploitation	        Web security testing
PowerShell	            Living-off-the-land	        Incident response

Example: HTTP Attack vs Defense
Scenario	                Tools
🔴 Attack HTTP server	    Metasploit, Burp Suite
🔵 Detect attack	        ModSecurity (WAF), Suricata
🔵 Investigate	            Splunk, Zeek
🔵 Respond	                Firewall rules, IPS block

Red Team focuses on exploitation, privilege escalation, and evasion
Blue Team focuses on detection, logging, monitoring, and response
```

## Side Quest
```
ATTACK → DETECT → INVESTIGATE → RESPOND → RECOVER
🔴 🔵 🔵 🔵 🔵

Cyber Kill Chain / MITRE ATT&CK Overview
Recon → Initial Access → Execution → Persistence → Priv Esc
↓                           ↓
Detection & Prevention Controls
↓
Defense Evasion → Credential Access → Discovery → Lateral Movement
↓
Collection → Command & Control → Exfiltration → Impact

1️⃣ Reconnaissance
🔴 Attack Techniques	    🔴 Red Team Tools	        🔵 Blue Team Defenses
Network scanning	        Nmap, Masscan	            IDS (Zeek), Firewall logs
Web enumeration	            Nikto, Gobuster	            WAF, Web logs
OSINT	                    theHarvester	            Exposure management

2️⃣ Initial Access
🔴 Attack	                🔴 Tools	                🔵 Defense
Phishing	                GoPhish	                    Email gateway, user training
Exploit public app	        Metasploit	                WAF, patching
Brute force	                Hydra	                    Fail2Ban, MFA
Drive-by download	        Browser exploits	        EDR, DNS filtering

3️⃣ Execution
🔴 Attack	                🔴 Tools	                🔵 Defense
Malicious scripts	        PowerShell, Bash	        AppLocker, EDR
Macro execution	            Office macros	            Macro blocking
Living-off-the-land	        LOLBins	                    Behavior-based detection

4️⃣ Persistence
🔴 Attack	                🔴 Tools	                🔵 Defense
Registry Run Keys	        PowerShell	                Sysmon, Autoruns
Scheduled tasks	            schtasks	                Task auditing
Startup scripts	            rc.local	                File integrity monitoring

5️⃣ Privilege Escalation
🔴 Attack	                🔴 Tools	                🔵 Defense
Kernel exploits	            DirtyPipe	                Patch management
Misconfig abuse	            LinPEAS	                    CIS benchmarks
Token impersonation	        Mimikatz	                LSA protection

6️⃣ Defense Evasion
🔴 Attack	                🔴 Tools	                🔵 Defense
Disable AV	                PowerShell	                Tamper protection
Obfuscation	                Veil	                    AMSI, EDR
Log deletion	            wevtutil	                SIEM alerts

7️⃣ Credential Access
🔴 Attack	                🔴 Tools	                🔵 Defense
LSASS dump	                Mimikatz	                Credential Guard
Keylogging	                Meterpreter	                Behavior monitoring
Password spraying	        CrackMapExec	            MFA, alerting

8️⃣ Discovery
🔴 Attack	                🔴 Tools	                🔵 Defense
User discovery	            whoami, net user	        Command logging
Network discovery	        arp, netstat	            IDS
Domain mapping	            BloodHound	                AD monitoring

9️⃣ Lateral Movement
🔴 Attack	                🔴 Tools	                🔵 Defense
SMB/PSExec	                PsExec	                    Network segmentation
RDP abuse	                xfreerdp	                MFA, logs
Pass-the-hash	            Impacket	                NTLM restrictions

🔟 Command & Control (C2)
🔴 Attack	                🔴 Tools	                🔵 Defense
Beaconing	                Cobalt Strike	            DNS monitoring
Encrypted tunnels	        HTTPS C2	                TLS inspection
Dead drops	                GitHub, Pastebin	        Proxy logs

1️⃣1️⃣ Exfiltration
🔴 Attack	                🔴 Tools	                🔵 Defense
DNS exfil	                Iodine	                    DNS anomaly detection
HTTPS exfil	                Custom scripts	            DLP
Cloud abuse	                Rclone	                    CASB

1️⃣2️⃣ Impact
🔴 Attack	                🔴 Tools	                🔵 Defense
Ransomware	                LockBit	                    Backups, EDR
Data destruction	        wiper malware	            Immutable backups
Service disruption	        DDoS tools	                Cloud mitigation
```