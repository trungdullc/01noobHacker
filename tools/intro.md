# intro to Hacking Techniques

```
Description: intro

Phishing
Social Engineering
SIM swap attack
Keylogging
Credential Stuffing
Brute Force Attack
Session Hijacking
Man in the middle Attack
Evil Twin
DNS Spoofing
SQL Injection
Cross-Site Scripting
Remote Code Execution
Command Injection
Privilege Escalation
Backdoor Access
Trojan Horse
Supply Chain Attack
Malware
Ransomware
Drive-by Download
Denial of Service
Old School Attack
Zero Day Exploits
```

## Phishing
```
Phishing: type of social-engineering attack where an attacker pretends to be a trusted person or organization to trick you into giving up sensitive information, clicking a malicious link, or installing malware
    Email phishing — fake emails (ILOVEU virus)
    Spear-phishing — targeted phishing aimed at a specific person or company using personal details to look convincing
    Smishing — phishing via SMS/text message
    Vishing — phishing by phone call (often urgent-sounding voice messages)
    Pharming — attackers redirect you from a legitimate website to a fake one (DNS manipulation)
    Malicious attachments — documents or executables that install malware when opened
```

## Social Engineering
```
Social engineering is when someone uses psychological manipulation — not hacking tools — to trick people into giving information, access, or doing something they normally wouldn’t do

Instead of attacking computers, social engineering attacks people
```

## Sim Swap Attack
```
Attacker convinces your mobile carrier to move your phone number to a SIM card they control — then they use your phone number to bypass SMS-based two-factor auth, reset passwords, get bank codes, and take over accounts
```

## Keylogging
```
Act of recording every key someone types on a keyboard, often without their knowledge

History: Olympic Vision is a keylogger malware, Rubber Ducky, Bad USB, Flipper Zero
```

## Credential Stuffing
```
Automated attack where attackers take large lists of stolen username/password pairs (from previous data breaches) and try them across many sites and services to take over accounts because user was to lazy to use different username and passwords
```

## Brute Force Attack
```
Longest and weakness w/ number of attempts and tries and location
```

## Session Hijacking
```
Attacker takes over a valid authenticated session so they can act as that user without knowing their password. The attacker uses whatever secret the server accepts as proof of an authenticated session (cookies, bearer tokens, JWTs, session IDs)
```

## Man in the middle Attack
```
Man‑in‑the‑Middle (MITM) attack is when an attacker secretly intercepts, reads, alters, or injects messages between two parties who believe they’re communicating directly with each other. The victims think they have a private link, but the attacker sits in the middle and relays (and possibly tampers with) the traffic.
```

## Evil Twin
```
Rogue Wi‑Fi access point designed to look like a legitimate Wi‑Fi network, tricking users into connecting. It’s conceptually very similar to what tools like the Wi‑Fi Pineapple
```

## DNS Spoofing
```
DNS spoofing (aka DNS cache poisoning) is an attack that makes a domain name (like example.com) resolve to a wrong IP address controlled by an attacker. Victims who try to visit the real site are silently sent to the attacker’s server instead — often a fake site that steals credentials, serves malware, or performs MITM.
```

## SQL Injection
```
SQL injection (SQLi) is a web‑security vulnerability where an attacker supplies malicious input that gets treated as part of a database query, allowing them to read, modify, or delete data they shouldn’t have access to — or in severe cases, take control of the backend database.
```

## Cross-Site Scripting
```
Cross-Site Scripting (XSS) is a type of web security vulnerability where an attacker injects malicious scripts (usually JavaScript) into web pages viewed by other users. Unlike SQL injection, XSS attacks run in the user’s browser, so the attacker can steal session cookies, manipulate the page content, or perform actions on behalf of the user.
```

## Remote Code Execution (RCE)
```
Remote Code Execution (RCE) is a critical security vulnerability that lets an attacker run arbitrary code on a target system over the network — usually with the privileges of the vulnerable process. In plain terms: an attacker makes your server or device execute commands that you didn’t intend.
```

## Command Injection
```
Command injection is a vulnerability where an application constructs and executes operating‑system commands (shell commands) using attacker‑controlled input. If that input is not properly handled, an attacker can make the application run arbitrary shell commands on the host (e.g., list files, create processes, read sensitive files, spawn a reverse shell). Command injection often leads to remote code execution on the machine running the app.

Common entry points: calls to system(), exec(), popen(), Runtime.getRuntime().exec(), backticks in many languages, or any code that concatenates user data into shell commands.
```

## Privilege Escalation
```
Privilege escalation is any technique an attacker (or a program) uses to gain higher privileges than they should have. A setuid (SUID) exploit is one common way to do vertical privilege escalation on Unix-like systems, but it’s far from the only one.

Types of privilege escalation
    Vertical escalation (privilege elevation): a low‑privileged user (www-data or a normal user) gains higher privileges (root/Administrator). SUID abuses fall into this category
    Horizontal escalation: a user gains access to another user’s data or permissions at the same privilege level (viewing another user’s files or acting as another user)
```

## Backdoor Access
```
Backdoor access refers to a method that allows someone to bypass normal authentication or security mechanisms to gain access to a system, application, or network. Essentially, it’s a secret entry point that can be exploited by attackers (or sometimes left intentionally by developers) to control or monitor a system without going through normal security checks.
```

## Trojan Horse
```
Malware that disguises itself as a legitimate or useful program, but secretly performs malicious actions once installed.
```

## Malware
```
“malicious software”—any software designed to harm, exploit, or take control of a computer, device, or network without the user’s consent. It’s a broad term that includes many types of harmful programs, including viruses, worms, Trojans, ransomware, spyware, adware, and more.
```

## Ransomware
```
Ransomware is a type of malware that encrypts a victim’s files or locks their system, then demands a ransom (usually money, often in cryptocurrency) to restore access.
```

## Drive-by Download
```
A Drive-by Download is a type of cyberattack where malware is automatically downloaded and sometimes installed on a user’s device just by visiting a compromised or malicious website, without the user explicitly clicking anything or approving the download.
```

## Supply Chain Attack
```
A supply‑chain attack (software or hardware) is when an attacker compromises a third‑party component, service, or process that you trust — and uses that trusted channel to get malicious code, firmware, or access into your environment. Instead of attacking you directly, they attack something you depend on (a vendor, library, build system, update server, CI/CD pipeline, or hardware supplier).
```

## Denial of Service (DOS)
```
Attacker intentionally makes a system, network, or service unavailable to legitimate users. The goal is to disrupt normal operations by overwhelming resources or exploiting vulnerabilities that crash or hang the service.

DDos (Distributed Denial of Service)
```

## Old School Attack
```
Bats, Knives, Guns
Look in garbage for unshredded documents
```

## Zero Day Exploits
```
Black Markets and Gray Markets, Gangs, Dark Web pay high
```

## Back to README.md
[BACK](../README.md)