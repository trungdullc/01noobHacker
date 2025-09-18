# picoGym Level 290: Redaction gone wrong
Source: https://play.picoctf.org/practice/challenge/290

## Goal
Now you DON’T see me<br>
This report has some critical data in it, some of which have been redacted correctly, while some were not<br>
Can you find an important key that was not redacted properly?<br>
https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf

## What I learned
```
pdf2text and PyPDF2
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf ⌨️
--2025-09-16 07:36:33--  https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.72, 3.170.131.77, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.72|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34915 (34K) [application/octet-stream]
Saving to: 'Financial_Report_for_ABC_Labs.pdf'

Financial_Report_for_ABC_Labs.pdf                          100%[======================================================================================================================================>]  34.10K  --.-KB/s    in 0.02s   

2025-09-16 07:36:33 (2.09 MB/s) - 'Financial_Report_for_ABC_Labs.pdf' saved [34915/34915]

AsianHacker-picoctf@webshell:~$ file Financial_Report_for_ABC_Labs.pdf ⌨️
Financial_Report_for_ABC_Labs.pdf: PDF document, version 1.7, 1 pages
AsianHacker-picoctf@webshell:~$ binwalk Financial_Report_for_ABC_Labs.pdf ⌨️ 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PDF document, version: "1.7"
33166         0x818E          Zlib compressed data, default compression
34716         0x879C          Zlib compressed data, default compression

AsianHacker-picoctf@webshell:~$ exiftool Financial_Report_for_ABC_Labs.pdf ⌨️
ExifTool Version Number         : 12.40
File Name                       : Financial_Report_for_ABC_Labs.pdf
Directory                       : .
File Size                       : 34 KiB
File Modification Date/Time     : 2023:03:16 03:15:40+00:00
File Access Date/Time           : 2025:09:16 07:36:52+00:00
File Inode Change Date/Time     : 2025:09:16 07:36:33+00:00
File Permissions                : -rw-rw-r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Create Date                     : 2021:07:17 19:44:11Z
Creator                         : Word
Modify Date                     : 2021:07:17 21:44:49+02:00
Producer                        : macOS Version 11.4 (Build 20F71) Quartz PDFContext
Title                           : Microsoft Word - Financial Report for ABC Labs.docx
Page Count                      : 1
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)

AsianHacker-picoctf@webshell:~$ pdf2text Financial_Report_for_ABC_Labs.pdf ⌨️❤️❤️❤️❤️❤️
-bash: pdf2text: command not found

# Method 1: extract text from a PDF using Python PyPDF2 module 
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
import PyPDF2
import sys

pdf_file = sys.argv[1]

with open(pdf_file, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    for page in reader.pages:
        print(page.extract_text())

AsianHacker-picoctf@webshell:~$ python pythonScript.py Financial_Report_for_ABC_Labs.pdf 
Traceback (most recent call last):
  File "/home/AsianHacker-picoctf/pythonScript.py", line 1, in <module>
    import PyPDF2
ModuleNotFoundError: No module named 'PyPDF2'
AsianHacker-picoctf@webshell:~$ python3 -m pip install --user PyPDF2 ⌨️
Collecting PyPDF2
  Downloading pypdf2-3.0.1-py3-none-any.whl.metadata (6.8 kB)
Downloading pypdf2-3.0.1-py3-none-any.whl (232 kB)
WARNING: Error parsing dependencies of send2trash: Expected matching RIGHT_PARENTHESIS for LEFT_PARENTHESIS, after version specifier
    sys-platform (=="darwin") ; extra == 'objc'
                 ~^
Installing collected packages: PyPDF2
Successfully installed PyPDF2-3.0.1

[notice] A new release of pip is available: 25.0.1 -> 25.2
[notice] To update, run: python3 -m pip install --upgrade pip
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py Financial_Report_for_ABC_Labs.pdf ⌨️
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.    Breakdown - Just painted over in MS word.         Cost Benefit Analysis  Credit Debit  This is not the flag, keep looking  Expenses from the     picoCTF{C4n_Y0u_S33_m3_fully}🔐  Redacted document. 

# Method 2: Open pdf and highlight all and paste into notepad
AsianHacker-picoctf@webshell:~$ sz Financial_Report_for_ABC_Labs.pdf 
```

## Flag
picoCTF{C4n_Y0u_S33_m3_fully}

## Continue
[Continue](./picoGym0130.md)