# Level 13

## Previous Flag
```
http://www.pythonchallenge.com/pc/return/disproportional.html
```

## Goal
phone that evil

## What I learned
```
xmlrpclib was Python-2 name, in Python-3 it’s built in as xmlrpc.client
```

## Side Quest: Only works on Python2
```
import xmlrpclib

servername = "http://www.pythonchallenge.com/pc/phonebook.php"
# Function to create server
client = xmlrpclib.ServerProxy(servername)
print(client.system.listMethods())
['phone',
 'system.listMethods',
 'system.methodHelp',
 'system.methodSignature',
 'system.multicall']
print(client.system.methodHelp("phone"))
print(client.phone("Bert"))
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/return/disproportional.html

View Page Source

<html>
<head>
  <title>call him</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<center>
<img src="disprop.jpg" width="640" height="480" border="0" usemap="#evil" />
	<map name="evil">
		<area shape="circle" coords="326,177,45" href="../phonebook.php" /> 👀
	</map>
<font color="gold"/>
<br><b>
	phone that <remote /> evil 👀
</br>
</html>

Browser: http://www.pythonchallenge.com/pc/phonebook.php ⌨️
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<methodResponse>
    <fault>
        <value>
            <struct>
                <member>
                    <name>faultCode</name>
                    <value>
                        <int>105</int>
                    </value>
                </member>
                <member>
                    <name>faultString</name>
                    <value>
                        <string>XML error 5: empty document</string>
                    </value>
                </member>
            </struct>
        </value>
    </fault>
</methodResponse>

Google: google xml remote python
To work with XML and remote servers in Python, you can use the xmlrpc.client module for XML-RPC (Remote Procedure Call) or libraries like urllib for fetching remote XML documents.
https://www.bing.com/ck/a?!&&p=b31fd0b9dc39ed1452e85932ec1188aef315688c30a3a151987433a22787cac3JmltdHM9MTc2MDQwMDAwMA&ptn=3&ver=2&hsh=4&fclid=0541fa48-4042-677e-1b82-e90741676627&psq=google+xml+remote+python&u=a1aHR0cHM6Ly9kb2NzLnB5dGhvbi5vcmcvMy9saWJyYXJ5L3htbHJwYy5jbGllbnQuaHRtbA

Method 1: python3
ChatGPT:
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import requests
import xml.etree.ElementTree as ET

url = "http://www.pythonchallenge.com/pc/phonebook.php"
auth = ("huge", "file")  # your credentials

# Build XML-RPC request body
payload = """<?xml version="1.0"?>
<methodCall>
  <methodName>phone</methodName>
  <params>
    <param>
      <value><string>Bert</string></value>
    </param>
  </params>
</methodCall>"""

headers = {"Content-Type": "text/xml"}

response = requests.post(url, auth=auth, data=payload, headers=headers)

# Parse XML response
tree = ET.fromstring(response.content)
result = tree.find(".//string").text
print("Bert ->", result)

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
Bert -> 555-ITALY 👀

Browser: http://www.pythonchallenge.com/pc/return/ITALY.html ⌨️
SMALL letters.

Browser: http://www.pythonchallenge.com/pc/return/italy.html 🔐

# Method 2: bash
AsianHacker-picoctf@webshell:/tmp$ vi bashScript.sh ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat bashScript.sh ⌨️
 #!/bin/bash
 site="http://www.pythonchallenge.com/pc/phonebook.php"
 curl --header "Content-Type: text/xml"  --data "
 <methodCall>
   <methodName>phone</methodName>
   <params>
      <param>
        <value><string>Bert</string></value> 
      </param>
    </params>
 </methodCall>" $site 
 echo

AsianHacker-picoctf@webshell:/tmp$ chmod u+x bashScript.sh ⌨️
AsianHacker-picoctf@webshell:/tmp$ ./bashScript.sh ⌨️
<?xml version="1.0"?>
<methodResponse>
<params>
<param>
<value><string>555-ITALY</string></value> 👀
</param>
</params>
</methodResponse>

Method 3: bash 1 liner
AsianHacker-picoctf@webshell:/tmp$ curl --header "Content-Type: text/xml"  --data "<methodCall><methodName>phone</methodName><params><param><value> \
>  <string>Bert</string></value></param></params></methodCall>" "http://www.pythonchallenge.com/pc/phonebook.php" ⌨️
<?xml version="1.0"?>
<methodResponse>
<params>
<param>
<value><string>555-ITALY</string></value> 👀
</param>
</params>
</methodResponse>
```

## Flag
http://www.pythonchallenge.com/pc/return/italy.html

## Continue
[Continue](./Level14.md)