# Level 29

## Previous Flag
```
http://www.pythonchallenge.com/pc/ring/guido.html
```

## Goal
Given image of bottle with glasses

## What I learned
```
# Add an HTTP Basic Authentication header using username "repeat" and password "switch"
# The credentials are base64-encoded as required by the HTTP Basic Auth standard
req.add_header('Authorization', 'Basic %s' % base64.b64encode(b'repeat:switch').decode())

# Open the URL and read its content, splitting it into individual lines
# Only keep the lines starting from index 12 onward (the meaningful "silent" lines)
raw = urlopen(req).read().splitlines()[12:]
```

## Solution
```
# Browser: http://www.pythonchallenge.com/pc/ring/guido.html

View Page Source

<html>
<head>
  <title>silence!</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<font color="gold">
	<img src="whoisit.jpg" border="0"/>
</body>
</html>
                                                                  
                                                                                          
                                                                                                        
                                                         
                                                 
                                                                 
                                                                                         
                                      
                                                                                   
                                                                                         
                                                                                                                                                                                                                         
                                                                                                                                                                                                  
                                                                                                                
                        


    
                                                                                                                                                             
                                                                                                                                
                                                                                                
                                                                                                                                


                                                                                                                                
                                
                                              
                                               
                                                                                                                                                            
                                
                                

                                                 
                                                                            
                                                                                                                                                        
                                                                                                                                                         
      
                                                                      
                 
                                                  
                                                                                                        
                                                                                                    
      
                                                                                                          
                                                                                     
                                                                                                    
                                                                                                                                                                                         
                                                                                                                                                              
                                                                                                                                                                                                      
                        
                                                                                                                                                                                                     
                                                                                                                                                  
                                                                                  
                                                                        
                                                                                                                                                                                                                                     
                                                                                          
                                  
 
                                                                                                                                                                                          
                                                                                                                                                                       
                                                                                                                                
                                                                                                                               
                                                                                                                                           
                                                                                                                                                                                         
                                  
                                                                                                                                                            
                                        
                                                                        
                                                                                                            
                                                                                                                                                                                                                                 
                                                        
            


# Note: There is silent lines after html tag
# Convert the lengths to bytes and decompress by bz2

AsianHacker-picoctf@webshell:/tmp$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
from urllib.request import Request, urlopen
import bz2, base64

# Create an HTTP request to access the given URL (a protected web page)
req = Request('http://www.pythonchallenge.com/pc/ring/guido.html')

# Add an HTTP Basic Authentication header using username "repeat" and password "switch"
# The credentials are base64-encoded as required by the HTTP Basic Auth standard
req.add_header('Authorization', 'Basic %s' % base64.b64encode(b'repeat:switch').decode())

# Open the URL and read its content, splitting it into individual lines
# Only keep the lines starting from index 12 onward (the meaningful "silent" lines)
raw = urlopen(req).read().splitlines()[12:]

# For each line, calculate its length (number of characters/spaces)
# Then convert those lengths into a sequence of bytes
data = bytes([len(i) for i in raw])

# Decompress the byte data using BZ2 to reveal the hidden message
print(bz2.decompress(data))

AsianHacker-picoctf@webshell:/tmp$ chmod u+x pythonScript.py ⌨️
AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
b"Isn't it clear? I am yankeedoodle!"

Browser: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

## Continue
[Continue](./Level30.md)