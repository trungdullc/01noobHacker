# Prepare GitHub
```bash
Create README.md and .gitignore
git clone git@github.com:trungdullc/01noobHacker.git
cd 01noobHacker
vi README.md
git add .
git commit -m "Updated README.md"
git status
git push
```

# 📖 Basic Skills Needed 📚
```
Linux: ssh, cli tools (sed, grep, awk), basic scripting, nano/vi
Programming: Python, Bash
Networking: Ports, IP, HTTP, DNS, TLS/SSL,
Crypto Basics: XOR, base64, hashing, AES, RSA
Web Tech: HTTP methods, RESTful, Cookies, JavaScript basics, XSS, SQL Injection
Tools: strings, file, netcat, nmap, wireshark, Burpsuite, Ghidra, pwntools
```
https://github.com/paragonie/awesome-appsec<br><br>

# 🦔 CTF Categories 🦔
```
Web exploitation
Steganography
Cryptography
Binary exploitation
OSINT (Open-Source Intelligence)
Forensics
Reverse Engineering
```

# 🏎️ Start with overTheWire 🚓
Purpose: Learn Linux commands<br>
Source: https://overthewire.org/wargames/<br>
[Start](/overthewire/0000.md)

# Continue to underTheWire
Purpose: Learn Powershell<br>
Source: https://underthewire.tech/wargames<br>
<b>TODO Later</b>

# Continue to picoCTF
Purpose: Learn CTF basic scenarios<br>
Source: https://www.picoctf.org/<br>
Guide: https://primer.picoctf.org/<br>
<b>TODO Later</b>

# Continue to RootMe
Purpose: Learn more CTF basic scenarios<br>
Source: https://www.root-me.org/en/Challenges/<br>
<b>TODO Later</b>

# Continue to 247CTF
Purpose: Competitive Jeopardy-style CTFs<br>
Source: https://247ctf.com/<br>
<b>TODO Later</b>

# Continue to HackThisSite
Purpose: Web Exploitations<br>
Source: https://www.hackthissite.org/<br>
<b>TODO Later</b>

# Continue to VulnHub
Purpose: Downloadable boot2root VMs<br>
Source: https://www.vulnhub.com/<br>
<b>TODO Later</b>

# Continue to CryptoHack
Purpose: Modern cryptography<br>
Source: https://cryptohack.org/<br>
<b>TODO Later</b>

# Continue to ROP Emporium
Purpose: ROP (Return-Oriented Programming) is exploitation technique used in binary exploitation<br>
Source:https://ropemporium.com/<br>
<b>TODO Later</b>

# Continue to TryHackMe
Purpose: Guided labs for real-world skills<br>
Source: https://tryhackme.com/<br>
<b>TODO Later</b>

# Continue to HackTheBox
Purpose: VM-based hacking playground, harder than TryHackMe<br>
Source: https://www.hackthebox.com/<br>
<b>TODO Later</b>

# End with Interactive CTF
https://try2hack.me/

# 💻 Tools to create/host CTF 🛜
- Creating CTF Enviornment
    - <a href="https://repo.tzku.at/book/security/pentest/Kali%20Linux%20CTF%20Blueprints%20-%20Buchanan,%20Cam.pdf" target="_blank">Kali Linux CTF Blueprints</a>
- Platforms
    - [CTFd](https://github.com/CTFd/CTFd)
    - [echoCTF.RED](https://github.com/echoCTF/echoCTF.RED)
    - [FBCTF](https://github.com/facebookarchive/fbctf)
    - [Haaukins](https://github.com/aau-network-security/haaukins)
    - [HackTheArch](https://github.com/mcpa-stlouis/hack-the-arch)
    - [Mellivora](https://github.com/Nakiami/mellivora)
    - [MotherFuckingCTF](https://github.com/andreafioraldi/motherfucking-ctf)
    - [NightShade](https://github.com/akama/NightShade)
    - [LibreCTF](https://github.com/easyctf/librectf)
    - [picoCTF](https://github.com/picoCTF/picoCTF)
    - [mkCTF](https://github.com/koromodako/mkctf)
    - [RootTheBox](https://github.com/moloch--/RootTheBox)
    - [ScoreBot](https://github.com/legitbs/scorebot)
    - [SecGen](https://github.com/cliffe/SecGen)
- Web (JavaScript Obfustcators)
    - [Uglify](https://github.com/mishoo/UglifyJS)
- Forensics
    - [Magnet AXIOM](https://www.magnetforensics.com/dlaxiom/)

# 🔨 Tools to use during CTF🔧
- Converting
    - [awk](https://www.gnu.org/software/gawk/manual/gawk.html): Kali Linux | ParrotOS, Search pattern inside files <b>w/ column field awareness</b>
    - [base64](https://www.man7.org/linux/man-pages/man1/base64.1.html): Encoding/Decoding base64
    - [hexdump](https://www.man7.org/linux/man-pages/man1/hexdump.1.html): Display file contents in hexadecimal, decimal, octal, or ascii
    - [xxd](https://www.commandlinux.com/man-page/man1/xxd.1.html): Kali Linux | ParrotOS, Convert binary data to hexadecimal format
- General
    - [bgrep](https://github.com/nneonneo/bgrep): Kali Linux | ParrotOS Search binary strings in binary file
    - [file](https://www.geeksforgeeks.org/linux-unix/how-to-find-out-file-types-in-linux/): Kali Linux | ParrotOS, Identify file types base on content
    - [grep](https://www.man7.org/linux/man-pages/man1/grep.1.html): Kali Linux | ParrotOS, Search pattern inside files
    - [HackTricks](https://book.hacktricks.wiki/en/index.html) ⭐⭐
    - [sed](): Kali Linux | ParrotOS, Stream EDitor reads text line by line, allows search, <b>replace, delete</b>, & transform text using patterns
    - [tmux](https://github.com/tmux/tmux/wiki): Run & manage multiple terminal sessions inside 1 terminal window
- Attack (<b>Beware: Man in Middle</b>)
    - [bettercap](https://github.com/bettercap/bettercap)
    - [yersinia](https://github.com/tomac/yersinia)
- Binary Exploitation/Pwn
    - [DLLInjector](https://github.com/OpenSecurityResearch/dllinjector): Inject DLL into running processes
    - [formatStringExploiter](https://formatstringexploiter.readthedocs.io/en/latest/): Exploiting format string vulnerabilities
    - [libformatstr](https://github.com/hellman/libformatstr): Exploiting format string vulnerabilities
    - [LNjector](https://github.com/DataSearchers/LNjector---Windows-DLL-injector): DLL Injector
    - [readelf](https://thelinuxcode.com/readelf-linux-command/): Kali Linux | ParrotOS, analyzing ELF
- Brute Force/Dictonary Attack
    - [Hashcat](https://hashcat.net/hashcat/): Kali Linux | ParrotOS ⭐
    - [Hydra](https://www.kali.org/tools/hydra/): Kali Linux | ParrotOS ⭐
    - [John The Riper: Jumbo](https://github.com/openwall/john): enhanced John the Ripper
    - [John The Riper](https://www.openwall.com/john/): Kali Linux | ParrotOS ⭐
    - [Nozzlr](https://github.com/intrd/nozzlr): deprecated
    - [Ophcrack](https://ophcrack.sourceforge.io/): Windows LM and NTLM hashes
    - [Patator](https://github.com/lanjelot/patator)
    - [pdfcrack](https://github.com/alitrack/PDFCrack): Kali Linux | ParrotOS, recovering PDF passwords
- Cryptography
    - [Cryptii](https://cryptii.com/): Web App for encypt/decrypt & encoding
    - [<b>CyberChef</b>](https://gchq.github.io/CyberChef): Analysing/Decoding data ⭐⭐⭐
    - [FeatherDuster](https://github.com/nccgroup/featherduster): Cryptanalysis: Identify/Exploit weakness
    - [hash_extender](https://github.com/iagox86/hash_extender): Hash length extension attack
    - [padding-oracle-attacker](https://github.com/KishanBagaria/padding-oracle-attacker): Padding oracle attacks
    - [Keyboard Shift Cipher](https://www.dcode.fr/keyboard-shift-cipher): Web App decryption
    - [PkCrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html): Breaking PkZip-encryption
    - [QuipQuip](https://quipqiup.com/): Substitution/vigenere Cryptogram solver
    - [RSACTFTool](https://github.com/RsaCtfTool/RsaCtfTool): Recovering RSA private key
    - [RSATool](https://github.com/ius/rsatool): Generate private key w/o p | q
    - [ShiftCipher](https://github.com/CyberJarvis/ShiftCipher): Caesar Cipher encryption/decryption
    - [XORTool](https://github.com/hellman/xortool): Analyze multi-byte XOR cipher
- Forensics (File Format/Memory Dump/Network Packet Capture Analysis)
    - [Audacity](https://www.audacityteam.org/download/): Web App analying audio files (chromatography)
    - [binwalk](https://github.com/ReFirmLabs/binwalk): Kali Linux | ParrotOS, Analyzing firmware images
    - [dnscat2](https://github.com/iagox86/dnscat2): Tunneling data over DNS
    - [foremost](https://www.kali.org/tools/foremost/): Kali Linux | ParrotOS, Recovering files based on headers & footers
    - [JPG Repair](https://jpg.repair/): Repair corrupted images online
    - [pdfinfo](https://linux.die.net/man/1/pdfinfo): Kali Linux | ParrotOS, Analyzing PDF
    - [pefile](https://github.com/erocarrera/pefile): Analyzing Windows PE (Portable Executable) files
    - [photorec](https://www.geeksforgeeks.org/linux-unix/photorec-recover-deleted-or-lost-files-in-linux/): Kali Linux | ParrotOS, Recovering lost files from HD & memory cards
    - [pngcheck](https://github.com/pnggroup/pngcheck): Kali Linux | ParrotOS, Checks PNG for errors
    - [pingcsum](https://www.libpng.org/pub/png/apps/pngcheck.html): Check integrity of PNG for errors
    - [qpdf](https://github.com/qpdf/qpdf): CLI manipulation PDF
    - [Registry Dumper](https://www.kahusecurity.com/posts/registry_dumper_find_and_dump_hidden_registry_keys.html): Dumping Windows registry
    - [scalpel](https://awjunaid.com/kali-linux/scalpel-a-file-carving-tool-for-recovering-files-from-disk-images/): Kali Linux | ParrotOS, recovering deleted files from disk images
    - [Sonic Visualiser](https://sonicvisualiser.org/): Analyzing audio files
    - [split](https://www.man7.org/linux/man-pages/man1/split.1.html) Kali Linux | ParrotOS, split files
    - [Xplico](https://www.xplico.org/): Network Forensic Analysis Framework
- Network
    - [GTFOBins](https://gtfobins.github.io/): Unix binaries
    - [Network Miner](https://www.netresec.com/?page=NetworkMiner): Network Protocol Analyzer
    - [PcapXray](https://github.com/Srinivas11789/PcapXray?utm_source=cybersectools.com): Network Protocol Analyzer
    - [tcpdump](https://www.tcpdump.org/manpages/tcpdump.1.html): Kali Linux | ParrotOS CLI Network Protocol Analyzer
    - [tcpflow](https://linux.die.net/man/1/tcpflow): Kali Linux | ParrotOS, CLI Network Protocol Analyzer
    - [Wireshark](https://www.wireshark.org/): Kali Linux | ParrotOS, Network Protocol Analyzer
- Reverse Engineering
    - [androguard](https://github.com/androguard/androguard): Analyzing Android Apps
    - [apktool](https://github.com/iBotPeaches/Apktool): Kali Linux | ParrotOS, reverse engineering Android APK
    - [Binary Ninja](https://binary.ninja/): Demo, Disassembler/Decompiler
    - [gdb](https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_toc.html): C/C++/Fortran Debugger ⭐⭐
    - [Ghidra](https://github.com/NationalSecurityAgency/ghidra): Kali Linux | ParrotOS, reverse engineer framework ⭐⭐
    - [Hopper](https://www.hopperapp.com/): Not Free, Disassembler/Decompiler Mac OSX and Linux
    - [IDA Free](https://hex-rays.com/ida-free): Disassembler/Decompiler Cross Platform
    - [ltrace](https://www.man7.org/linux/man-pages/man1/ltrace.1.html): Kali Linux | ParrotOS, tracing library calls
    - [radare2](https://github.com/radareorg/radare2): Kali Linux | ParrotOS, Disassembler/Debugger
- Steganography
    - [ffmpeg](https://ffmpeg.org/ffmpeg-utils.html): Kali Linux | ParrotOS, Extract strings from media files
    - [OpenStego](https://www.openstego.com/)
    - [pdfdetach](https://www.xpdfreader.com/pdfdetach-man.html): Kali Linux | ParrotOS, Extract Embedded files from PDF
    - [pdfimages](https://man.archlinux.org/man/pdfimages.1.en): Kali Linux | ParrotOS, extract hidden images from PDF
    - [stegcracker](https://www.kali.org/tools/stegcracker/): Kali Linux | ParrotOS
    - [steghide](https://steghide.sourceforge.net/): Kali Linux | ParrotOS
    - [Steganography Online](https://stylesuxx.github.io/steganography/): Web App
    - [Steg Online](https://www.georgeom.net/StegOnline/upload): Web App
    - [StegSolve](https://github.com/Giotino/stegsolve/releases)
    - [zsteg](https://linuxcommandlibrary.com/man/zsteg): Kali Linux | ParrotOS, Detect steganography in PNG/BMP
- Web exploitation (also look Network)
    - [Burp Suite](https://portswigger.net/burp/communitydownload): Kali Linux | ParrotOS, Web App security testing platform ⭐⭐
    - [CloudflareBypassForScraping](https://github.com/sarperavci/CloudflareBypassForScraping): Bypass CloudFlare protection (testing)
    - [commix](https://www.kali.org/tools/commix/): Kali Linux | ParrotOS, Command Injection vulnerabilities
    - [dirbuster](https://github.com/KajanM/DirBuster): Kali Linux | ParrotOS, find hidden directories in Web App
    - [Edit-This-Cookie](https://github.com/ETCExtensions/Edit-This-Cookie): Editing cookies
    - [gobuster](https://github.com/OJ/gobuster): Kali Linux | ParrotOS, find hidden directories in Web App
    - [HackBar](https://github.com/PhHitachi/HackBar): Manual SQL injection atk
    - [nikito](https://github.com/sullo/nikto): Kali Linux | ParrotOS, Web Server vunerability scanner
    - [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings): Payload Library ⭐⭐⭐
    - [Racoon](https://github.com/evyatarmeged/Raccoon): Scrapping/Enumerating endpoints in Web App
    - [sqlmap](https://www.kali.org/tools/sqlmap/): Kali Linux | ParrotOS, automating SQL injection atk
    - [wpscan](https://github.com/wpscanteam/wpscan): Kali Linux | ParrotOS, Vulnerability scan for WordPress
- Help
    - [HackTricksAI](https://www.hacktricks.ai/): Unfiltered
    - [Phind](https://www.phind.com/): Unfiltered
    - [Perplexity](https://www.perplexity.ai/): Unfiltered
    - [ChatGPT](https://chatgpt.com/): Filtered, Popular
    - [ClaudeAI](https://claude.ai/): Filtered, Game Approved
    - [DeepSeek](https://www.deepseek.com/en): IP Blocked

# 🏆 Current CTF Competitions 🏆
https://ctftime.org/

# 🥷🏻 Bug Bounty 💰
https://www.bugcrowd.com/

# Continue Education
```
CompTIA Security+               	                            Security fundamentals (1st)
CompTIA CySA+                                                   Security analyst, threat detection
Cisco CCNA (Cyber Ops)                                          Networking + security
CEH (Certified Ethical Hacker)                                  Penetration testing basics
CompTIA PenTest+                                                Hands-on pen testing
OSCP (Offensive Security Certified Professional)                Hands-on ethical hacking (2nd)
CISSP (Certified Information Systems Security Professional)     Security domains
OSCE/OSWE/OSEP                                                  Advanced offensive security
```