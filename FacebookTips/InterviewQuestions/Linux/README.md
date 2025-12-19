# Linux Interview Questions
```
1. Give any 3 examples of operating systems.
• Windows, Linux, and macOS.

2. What is the root home directory?
• The root home directory is /root.

3. Your company has terminated a server administrator. What is the first thing as an
administrator you should do to enhance the security?
• Change the root password.

4. How to check kernel version?
• Use the command uname —a.

5. How to become a root user from a regular user?
• Use the su - or sudo su to switch to the root user.

6. How to check the computer name or hostname in Linux?
Use the hostname command.

7. List 3 basic commands to navigate the filesystem.
cd, pwd, and ls.

8. How to check network interfaces in Linux?
• Use ifconfig or ip addr or ip a

9. List 3 different methods Of adding a user.
• Methods include using useradd, adduser or manually editing /etc/passwd and /etc/shadow files.

10. What is the command to create a new user?
• useradd username

11. How to change a user password?
• Use the command passwd username.

12. Which directory has all the configuration files?
• The /etc directory.

13. List any 4 Linux distributions.
• Kali, Red Hat, CentOS, Ubuntu. and SUSE.

14. How to log off from the system?
• Use the exit command.

15. How to create a directory?
• Use the mkdir command.

16. Explain the purpose Of the "touch" command.
touch is used to create an empty file or update the timestamp of an existing file.

17. If a command hangs, how to stop it and get the prompt back?
• Press Ctrl c.

18. Which command is used to count words or lines?
• wc

19. How to rename a file or directory?
Use the mv command.

20. How to change a hostname in Linux?
• Edit /etc/hostname and /etc/ hosts, then restart the system or use
hostnamectl set—hostname newname.

21. What is the command to change file/directory permissions?
• Use chmod.

22. What is the purpose of pipe (|)?
• To pass the output of one command as input to another command.

23. What is /etc directory used for?
• It contains configuration files for the system.

24. Which command is used to list files in a directory?
• ls -l

25. There is a command which gives you information about other commands, please
explain that command and what is it used for?
• man is used to display the manual pages for other commands, providing
detailed information on usage and options.

26. How to delete a file and a directory?
• Use rm filename for files and rmdir dirname for directories.

27. What is the difference between "tail" and "tail -10"?
• tail displays the last 10 lines Of a file by default, while
tail —10 specifies to display the last 10 lines.

28. List 4 commands to display or read a file's contents.
• cat, more, less, vi.

29. Which command is used to read the top 5 Of a file?
• head —5 filename

30. What are the different commands or methods to write to a file?
• echo > filename, vi filename, cat > filename.

31. What are the different types of shells?
• sh, bash, ksh, csh, zsh

32. Which is the core of the operating system?
• Kernel

33. Which among the following interacts directly with system hardware?
• Kernel

34. List a few commands that are used in troubleshooting network-related issues?
• netstat:      Displays network connections.
• tcpdump:      Captures and analyzes network traffic.
• ping:         Tests connectivity to another host.
• traceroute:   Traces the route packets take to a network host.

35. How to 2 files into 1? E.g., you have 3 lines in file "A" and 5 lines in file "B",
which command syntax to use that will combine into one file Of 3+5 = 8 lines?**
• cat fileA fileB > combinedfile

36. What is the echo command used for?
• The 'echo' command is used to display a line of text or output a string to the screen.

37. What does the following command do?
• echo "This year the summer be great" > file1
• It creates a new file named "filel" and writes the text "This year the
summer will be great" into it. If the file already exists. it will be overwritten.

38. When you login you get "$" prompt, what is the prompt for root?
• The prompt for the root user is typically #.

39. Explain the difference between grep and egrep.
• grep is used for basic regular expression pattern matching, while egrep
(or grep -E) supports extended regular expressions, which allow more
complex pattern matching.

40. What is the port number for DNS, NTP, and NFS?
• DNS: 53, NTP: 123, NFS: 111 (portmapper) and 2049 (NFS).

41. What is the configuration file name Of DNS and where is it located?
• The DNS configuration file is named named.conf and is typically located in /etc.

42. How many new directories will be created after running the following command
mkdir (a..c){1..3}?
• 9 directories will be created: al , a2, a3, bl, b2, b3, cl. c2, c3.

43. Your PC is configured with a DNS server address but not the default gateway.
Can the PC access the internet?
• No, without a default gateway, the PC cannot access the internet.

44. What is the difference between IP and Gateway?
• An IP address is a unique identifier for a device on a network, while a
gateway is a network point that acts as an entrance to another network,
Often used to connect local networks to external networks like the
internet.

45. Can you assign one static IP to 2 computers, if not then why?
• No, assigning the same static IP to two computers will create an IP
conflict, causing network communication issues.

46. How to change IP address to static?
• You can change the IP address to static by editing the network
configuration files, such as /etc/network/interfaces on Debian-based
systems or /etc/sysconfig/network—scripts/ifcfg—ethO on Red
Hat-based systems, and setting the IP address manually.
• etc/netplan for the network configuration file on Ubuntu.

47. You are trying to ping a server by hostname and you get an error message, "ping:
unknown host What could be the reason and how to solve the problem so you
can ping it by hostname?
• The issue could due to a missing hostname-to-IP mapping in the /etc/hosts file or an incorrect DNS configuration. Check and update these files to resolve the issue.

48. Explain the difference between relative and absolute path.
• An absolute path starts from the directory / and the complete path to a file or directory. A relative path is based on the current
directory and does not start with /.

49. What is the command to change file/directory ownership and group?
• Use chown to change ownership and chgrp to change the group.

50. List any 3 types Of filesystem.
• ext4, NTFS, and FAT.

51. When you login you get a message on the screen. What is the name of that file
and where is it located?
The file is /etc/motd (Message Of the Day).

52. What is the /bin directory used for?
The /bin directory contains essential binary executables needed for booting and system repair.

53. What are the different types Of DNS Server?
• Master (Primary) and Secondary (Slave) DNS servers.

54. Where are the zone files located for DNS service?
Typically located in /var/named/zonefiles.

55. How many megabytes in 1 gigabyte?
• There are 1024 megabytes in 1 gigabyte.

56. What is the purpose of having different network ports?
• So the communication Of each application goes through a dedicated port
• Different network ports allow multiple applications to communicate over
the network simultaneously without interference.

57. How to display the first column of a file?
• Use cat filename | awk '(print $1)'
• awk '{print $1}' filename.

58. What is the name of the DNS rpm package?
The package is called bind.

59. What is the difference nslookup and dig commands?
•  nslookup is a simple tool for querying DNS servers, while dig provides more detailed information and is more flexible for DNS troubleshooting.

60. How to check your user id and group id?
• Use the id command.

61. What is the difference "kill" and "kill -9" command?
sends a signal to terminate a process gracefully, allowing it to clean
• kill: sends a SIGKILL signal, forcing the process to clean
up resources.
• kill -9 sends a SIGKILL signal, forcing the process to terminate immediately without cleanup.

62. What is a subnet?
• A subnet is a segmented piece of a larger network, designed to improve performance and security by grouping devices with similar network
requirements.

63. You are troubleshooting an issue with Redhat support and they have asked you to
send the contents Of /etc directory. How and which method will you use to
transfer the contents?
• Compress the /etc directory using tar and transfer it using ftp or scp.

64. What is rsyslogd daemon and its purpose?
• rsyslogd is a system utility providing support for message logging. It is an
enhanced version of syslogd.

65. What is the command to untar a tarred file?
• Use tar —xvf filename.tar.

66. What is the /proc directory used for?
• The /proc directory contains virtual files that provide a view into the
kernel's view Of the system.

67. What is the purpose of the nsswitch.conf file?
• It specifies the sources from which to obtain name-service information in
a range of categories and in what order.

68. Which service/daemon should be running on the server that allows you to
connect remotely?
• sshd (SSH Daemon).

69. What is the purpose of a firewall?
• A firewall controls incoming and outgoing network traffic based on
predetermined security rules.

70. List any 3 IT components.
• Hardware, Operating System, and Applications.

71. Which directory has all the commands we use, e.g., Is, cd, etc.?
/usr/bin or /bin.

72. What is the difference between memory, virtual memory, and cache?
• Memory (RAM) is the physical hardware inside a computer that
temporarily stores data.
• Virtual memory is a memory management capability that uses disk space
as an extension Of RAM.
• Cache is a smaller, faster memory component that stores copies of
frequently accessed data for quick access.

73. Correct order of interaction:
• a. User >> Operating System >> Hardware

74. Which of the following is a communication command?
• mail

75. Why is the "tail —f logfilename" command used most often and what it do?
• It outputs all incoming logs in real-time, useful for monitoring log files as
they are updated.

76. How to sort a file in reverse order?
• Use sort -r filename.

77. List all byte sizes from smallest to largest.
• Bit, Byte, Kilobyte (KB), Megabyte (MB), Gigabyte (GB), Terabyte (TB),
Petabyte (PB), Exabyte (EB).

78. How to check the total number of partitions in Linux?
Use fdisk —l.

79. How to access a Linux system from a Linux system?
• Use ssh

80. Explain the procedure of bonding 2 NICs or interfaces together.
• Use network bonding to combine two or more NICs into a single bonded interface for redundancy or increased throughput. This typically involves configuring /etc/network/interfaces or /etc/sysconfig/network—scripts/ifcfg-bond0 and using the bonding kernel module.

81. What is the exact command syntax to list the 5th column of a file and cut the first
3 letters?
• awk '(print $5)' filename | cut —c1—3

82. What is the /etc/hosts file used for?
• It is used to resolve hostnames to IP addresses locally.

83. List any 3 options Of 'df' command and what they are used for.
• —h: human-readable format, -i: inodes information, -T: file system type.

84. What is swap space and how to check swap space?
• Swap space is a portion Of the hard drive used as an extension Of RAM
Check swap space using swapon —s or free.

85. What is inode and how to find an inode Of a file?
• An inode is a data structure on a filesystem that stores information about
a file or directory. Use ls -i filename to find the inode number.

86. Which file to edit for kernel tuning?
• Edit /etc/sysctl.conf for kernel parameter tuning.

87. What is the latest version of Redhat?
• Search online for the most recent version as it frequently updates.

88. Name the command to find a specific word from a file.
grep word filename

89. You have scheduled a job using crontab but it does not run at the time you
specified, what could be the reason and how would you troubleshoot?
• Check system time, crontab entry syntax, and /var/log/cron for errors.

90. How to check system hardware information?
• Use dmidecode.

91. How to check network interface MAC address?
• Use ifconfig or ip link.

92. If I don't want others to read my filel, how do I do that?
• Remove read permission for others using chmod o-r file1.

93. What is the purpose of "uniq" and "sed" commands?
• uniq removes duplicate lines from sorted input, sed is a stream editor for
filtering and transforming text.

94. Which command is used to list the contents of a directory in the most recent
time and in reverse order, meaning the most updated file should be listed on the
bottom?
• ls —ltr

95. What is the difference between tar, gzip, and gunzip?
• tar is used for archiving files, gzip compresses files, and gunzip decompresses files.

96. What are the different ways to install an OS?
• Using a DVD, DVD ISQ or network boot.

97. How to view the difference between two files?
• Use diff filel file2.

98. You noticed that one Of the Linux servers has no disk spaæ left, how would you
troubleshoot that issue?
• If using LVM, add more disk spaæ and extend the logical volume. If not,
add a new disk, create a partition, and link it to an existing filesystem.

99. How to check Redhat version release?
• Use cat /etc/redhat—release or uname —a.

100. What is the difference between TCP and UDP?
• TCP is connection-oriented and reliable, while UDP is connectionless and
faster but less reliable.

101. What is a zombie process?
• A zombie proces is a process that has completed execution but still has an entry in the process table, waiting for the parent process to read its exit status.

102. How do you search for a pattern/word in a file and then replace it in an entire
file?
• Use sed for search and replace operations.

103. How to check the Of users logged in?
• - Use who command.

104. What is the command to view the calendar Of 2024?
• cal 2024

105. Which command is used to view disk spaæ?
• df -h

106. How to create a new group in Linux?
• groupadd groupname.

107. What is the command to send a message to everyone who is into the
system?
•  Use wall command

108. Which command is used to check the total of disks?
• f disk —i.

109. What is a mail server record in DNS?
• MX (Mail Exchange) record

110. What does the following command line do?
ps —ef | awk '(print $1)' |sort | uniq
• Lists the first column of all running processes, sorts them, and removes duplicates.

111. You get a call that when a user goes to www.yourwebsite.com it fails and gets
an error, how do you troubleshoot?
• Check user internet connectivity, DNS configuration, server status, and web service available

112. List 4 different directories in /?
• /etc, /bin, /tmp, home

113.What is the output of the following command:
$ tail —10 filename | head -1
• It will show the first line from the last 10 lines Of a file.

114. What are the different fields in /etc/passwd file?
• The /etc/passwd file contains the following fields separated by colons (:):
    Username: The user's login name.
    Password: An 'x' character indicates that the password is stored in the
    '/etc/shadow' file.
    UID: User ID number.
    GID: Group ID number.
    GECOS: User's full name or other information.
    Home Directory: The path to the user's home directory.
    Shell: The user's default shell.

115. Which command is used to list the processes?
• ps -ef
The •ps -ef command is used to list all the currently running processes.

116. What is the difference between "hostname" and "uname" commands?
• hostname: Displays or sets the system's hostname.
• uname: Prints system information, such as the kernel name, version, and
Other details. •uname -n' specifically prints the network node hostname,
similar to the 'hostname' command.

117. How to check system load?
• You can check system load using the top and uptime commands.

118. How to schedule jobs?
• You can schedule jobs using crontab for repetitive tasks and at for uptime one-time tasks.

119. What is the 3rd field when setting up crontab?
• The third field in a crontab entry is the "Day of the month'.

120. What is the "init #" for system reboot?
• The 'init' level for system reboot is '6'.

121. How to restart a service?
• systemctl restart servicename
• sudo service servicename restart

122. How to shutdown a system?"
• shutdown now
• init O
• systemcti poweroff

123. What is the "ftp" command used for?
• The "ftp" command is used to transfer files betwæn a local system and a
remote server using the FTP protocol.

124. Explain cron job syntax? First is minute, second is..?
The cron job syntax consists Of five fields followed by the command to executed:
1. Minute (0-59)
2. Hour (0-23)
3. Day of the month (1-31)
4. Month (1-12 or JAN-DEC)
5. Day of the week (0-6 or SUN-SAT).

125. How to delete a package in Linux?
• rpm —e packagenazne
• for RPM-based systems.

126. What is the file name where user password information is saved?
• The user password information is saved in the /etc/shadow file.

127. Which command would you use to find the location of the chmod command?
• which chmod

128. Which command is used to check if the other computer is online?
• ping othercomputer

129. Please explain about LAN, MAN and WAN?
• LAN (Local Area Network): Covers a small geographic area like a home, Office, or building.
• MAN (Metropolitan Area Network): Spans a city or a large campus.
• WAN (Wide Area Network): Covers a large area, such as a country or connecting multiple LANs.

130. How to list hidden files in a directory?
• ls -la

131. What is the difference telnet and ssh?
• SSH (Secure Shell): Provides encrypted communication and is secure.
• Telnet: Does not provide encryption and is not secure.

132. How to run a calculator on Linux and exit out of it?
• Run 'bc' to start the calculator and type •'quit' to exit.

133. List any 4 commands to monitor the system?
• top
• df —h
• iostat
• dmesg

134. You are notified that your server is down, list the steps you will take to
troubleshoot?
• - Check the system physically.
• - Login through the system console.
• - Ping the system.
• - Reboot or boot if possible.

135. What is the difference between static and DHCP IP?
• Static IP: Manually assigned and does not change.
• DHCP IP: Automatically assigned by a DHCP server and can change over time.

136. How to write in vi editor mode?
• - 'i' = insert
• - 'a' = insert after the cursor
• - 'o' = insert a new line below the current line

137. What is the difference between "crontab" and "at" jobs?
• crontab: Schedules repetitive jobs.
• at: Schedules one-time jobs.

138. What is vCenter server in VMWare?
• vCenter Server is a centralized management tool for managing VMware vSphere environments, providing control over virtual machines, ESXi hosts, and other components.

139. What is the "dmidecode" command used for?
• The 'dmidecode' command is used to retrieve system hardware information from the DMI (Desktop Management Interface) table.

140. What is the difference between SAN and NAS?
• SAN (Storage Area Network): Provides block-level storage and is typically used in enterprise environments.
• NAS (Network Attached Storage): Provides file-level storage and is often used for simpler file sharing.

141. What is the location of system logs? E.g. messages
• System logs are typically located in the /var/log directory.

142. How to set up an alias and what is it used for?
• alias alaiasname="command"
• It is used to create shortcuts for long commands.

143. What is the purpose of the "netstat" command?
• The 'netstat' command is used to display network connections, routing tables, interface statistics, masquerade connections, and multicast
memberships.

144. What are terminal control keys, list any 3?
• Ctrl+C:   Interrupt a process.
• Ctrl+D:   End of input (EOF).
• Ctrl+Z:   Suspend a process.

145. Which command(s) you would run if you need to find out how many processes are running on your system?
• ps -ef | wc -1

146. How to delete a line when in vi editor mode?
• Press 'dd' to delete a line.

147. How to save and quit from vi editor?
• Press 'Shift ZZ or type ':wq!' and press Enter.

148. What is the difference between a process and daemon?
• Process: A running instance of a program.
• Daemon: A background process that starts at boot time and runs continuously.

149. What is the process or daemon name for NTP?
• The process or daemon name for NTP is 'ntpd'.

150. What are a few commands you would run if your system is running slow?
• 'top':        To view running processes and their resource usage.
• 'iostat:      To monitor system input/output device loading.
• 'df -h:       To check disk space usage.
• 'netstat':    To display network connections and statistics.

151. How to install a package in Redhat Linux?
• yum install packagename

152. What is the difference between "ifconfig" and "ipconfig" commands?
• ifconfig: Used in Linux to configure and display network interface parameters.
• ipconfig: Used in Windows to display all current TCP/IP network configuration values.

153. What is the first line written in a shell script?
• The first line in a shell script is the shebang, which defines the shell to interpret the script, e.g.,

154. Where is the network (Ethernet) file located, please provide the exact directory location and file name?
• The network configuration file is located at '/etc/sysconfig/network-scripts/ifcfg-nic', where 'nic' represents the network interface card name (e.g., 'ethO').

155. Why do we use the "last" command?
• The 'last' command is used to display a list of the last logged-in users, showing both active and logged-off sessions.

156. What does RHEL Linux stand for?
• RHEL stands for Red Hat Enterprise Linux.

157. To view your command history, which command is used and how to run a specific command?
• Use history to view the command history
• To run a specific command, use !n, where 'n' is the command number from the history list.

158. What is NTP and briefly explain how it works and where are the config files and related commands of NTP?
• NTP (Network Time Protocol): Used to synchronize the clocks of computers over a network.
• How it works: NTP servers provide time information to clients, which adjust their clocks accordingly.
• Config files: Located at '/etc/ntp.conf'.
• Related commands**: 'ntpd' for the daemon, 'ntpq' for querying NTP servers.

159. How to disable the firewall in Linux?
• To disable the firewall, you can use:
    systemctl stop firewaLLd
    systemctl disable firewalld

160. How to configure mail server relay for sendmail service?
• Edit the '/etc/mail/sendmail.mc' file and add the 'SMART_HOST' entry to specify the relay host.

161. Where is the samba log file located?
• The Samba log file is located at var/log/samba.

162. What is the 'mkfs' command used for?
• The 'mkfs' command is used to create a new filesystem on a device.

163. If you create a new group, which file does it get created in?
• The new group information is stored in the '/etc/group' file.

164. Which file has DNS server information (e.g., DNS resolution)?
• DNS server information is stored in the '/etc/resolv.conf' file.

165. What are the commands you would run if you need to find out the version and build date of a package (e.g., http)?
• rpm -qi http

166. On the file permissions, what are the first 3 bits for and who is it for?
• The first three bits represent the permissions for the file owner: read (r), write (w), and execute (x).

167. How to create a soft link?
• ln —s target linkname

168. How to write a script to delete messages in a log file older than 30 days automatically?
• You can use the 'find' command in a script:
• find /path/to/logs -type f —mtime +30 —exec rm () \;

169. How to quit out of the "man" command?
• Press q to quit the manual page viewer.

170. Which command is used to partition a disk in Linux?
• The fdisk command is used to partition a disk.

171. What is the difference the "shutdown" and "halt" command?
• shutdown: Gracefully shutdown the system, allowing to terminate properly.
• halt: Stops all processes and halts the system without powering it off.

172. What is the exact syntax of mounting an NFS share on a client and also how to un-mount?
• Mount: 'mount -t nfs server:/path/to/share/mount/point'
• Unmount: 'umount/mount/point'

173. What experience do you have with scripting, explain?
• Experience with scripting includes using control structures like 'if-then', 'do-while', 'case', and 'for' loops to automate tasks.

174. How to get information on all the packages installed on the system?
• rpm -qa

175. Explain VMWare?
• VMWare is a company that provides cloud computing and virtualization technology, including products like vSphere, ESXi, and vCenter.

176. You are tasked to examine a log file in order to find out why a particular application keeps crashing. The log file is very lengthy, which command can you use to simplify the log search using a search string?
• Use the 'grep' command to search for specific strings like "error", "warning", or "failure" in the log file:
• grep "error" /var/log/messages

177. What is an /etc/fstab file and explain each column of this file?
• The '/etc/fstab' file contains information about filesystems and their mount points. Each line has six fields:
    1. **Device**:              The block device or remote filesystem.
    2. **Mount Point**:         Directory where the filesystem is mounted.
    3. **Filesystem Type**:     Type of filesystem (e.g., ext4, nfs).
    4. **Options**:             Mount options (e.g., defaults, ro).
    5. **Dump**:                Backup utility flag (O or 1).
    6. **Pass**:                Filesystem check order at (O, 1, or 2).

178. What is the latest version of Windows server?
• The latest version as of 2023 is Windows Server 2022.

179. What is the exact command to list only the first 2 lines of history output?
• history | head —2

180. How to upgrade Linux from 7.3 to 7.4?
• yum update: This command updates all packages to their latest versions, including upgrading the distribution version.

181. How to tell which shell you are in or running?
echo $0

182. You have tried to "cd" into a directory but you have been denied. You are not the owner of that directory, what permissions do you need and where?
• You need execute ('x') permission on the directory to change into it.

183. What is CNAME record in DNS?
• A CNAME (Canonical Name) record is a type of DNS record that maps an alias name to a true or cznonical domain name.

184. What is the name of the VMWare operating system?**
• The VMWare operating system is called ESXi.

185. What is the client name used to connect to ESXi or vCenter server?
• The client used to connect to ESXi or vCenter is the vSphere Client.

186. You get a call from a user saying that I cannot write to a file because it says, permission denied. The file is owned by that user, how do you troubleshoot?
• Check the file permissions and ensure the user has write ('w') permission.

187. What is the latest version of VMWare?
• As of 2023, the latest version of VMware vSphere is 8.0.

188. What is the name of the firewall daemon in Linux?
• The firewall daemon in Linux is called 'firewalld'.

189. Which command syntax can you use to list only the 20th line of a file?
• sed —n '20p' filename

190. What is the difference run level 3 and 5?
• Run level 3: Multi-user mode with networking, but without a graphical interface.
• Run level 5: Multi-user mode with networking and a graphical interface (GUI).

191. What is the difference between domain and nameserver?
• Domain: A domain is a human-readable address used to a-cæss resources on the internet.
• Nameserver. A server that translates domain names into IP addresses.

192. You open up a file and it has 3000 lines and it scrolls up really fast, which
command will you use to view it one page at a time?
• Use 'less' or 'more' to view the file one page at a time.

193. How to start a new shell. E.g., start a new ksh shell?
• Simply type 'ksh' or 'bash' to start a new shell session.

194. How to kill a process?
• kill processID

195. How to check scheduled jobs?
• crontab —l

196. How to check system memory and CPU usage?
• Memory: Use 'free'.
• CPU Usage: Use 'top' or 'htop'.

197. Which utility could you use to repair the corrupted file system?**
• Use the 'fsck' (File System Consistency Check) utility.

198. What is the command to make a service start at boot?**
• systemctl enable servicename

199. Which file to modify to allow users to run root commands?**
• Modify the '/etc/sudoers' file, typically using 'visudo' for safe editing.

200. You need to modify the httpd.conf file but you cannot find it. Which command
line tool can you use to find the file?
• find / —name "httpd.conf"

201. Your system crashed and is being restarted, but a message appears indicating that the operating system cannot be found. What is the most likely cause of the problem?
• The  '/boot' partition or bootloader is most likely corrupted or missing.

202. What are the most essential [70+] Linux Commands you NEED to know?
```