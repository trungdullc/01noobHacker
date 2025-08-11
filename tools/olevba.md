# olevba 
```
Description: Look for Macros within office documents

# Install oletools (which includes olevba)
pip3 install oletools                                   git clone https://github.com/decalage2/oletools.git
                                                        cd oletools
                                                        python3 setup.py install
```

## Malware Analysis
```
olevba "REPORT.xlsm"                                    Basic macro scan
olevba -j "REPORT.xlsm"                                 JSON output (for scripting)
olevba -a "REPORT.doc"                                  Show only suspicious lines
olevba -c                                               Analyze from clipboard
oleid "FILE.msg"                                        Analyze email attachments
```

## Back to README.md
[BACK](../README.md)