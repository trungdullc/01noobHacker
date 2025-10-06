# Century Level 08 → 09 grep -o '\S\+' Word_File.txt | tail -n +161

## Previous Flag
```
696
```

## Goal
The password for Century10 is the 161st word within the file on the desktop.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```
(Get-Content Word_File.txt) -replace '^(\S+\s+){160}'
                                                    awk '{for (i=1; i<=NF; i++) {count++; if (count==161) print $i}}' Word_File.txt
                            # everything after 160th word (like PowerShell -replace)
                            grep -o '\S\+' Word_File.txt | tail -n +161
                            # split into words first then one-per-line, then prints the 161st
                            tr -s '[:space:]' '\n' < Word_File.txt | sed -n '161p'
                            # grep -o outputs each word (\S+ = non-whitespace sequence) on a new line, then sed picks the 161st
                            grep -o '\S\+' Word_File.txt | sed -n '161p'

Normally, grep prints the whole line where a match occurs
grep -o prints only the part of the text that matched the pattern ❤️

\S+
    \S means “non-whitespace character” (the opposite of \s)
    + means one or more
    So together: a word (continuous run of non-whitespace)

\s+
    \s means “whitespace character” (space, tab, newline)
    + means one or more
    So together: the spaces that follow the word

Common Regex Shorthand Classes
    \s  → whitespace (space, tab, newline)
    \S  → non-whitespace (the opposite of \s)
    \d  → digit (0–9)
    \D  → non-digit (anything except 0–9)
    \w  → "word character" = letters, digits, underscore ([A-Za-z0-9_])
    \W  → non-word character (opposite of \w)
    .   → any character (except newline, unless in “dotall” mode)
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century9@century.underthewire.tech -p 22 ⌨️
century9@century.underthewire.tech's password: ⌨️ 696

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\century9\desktop> dir ⌨️

    Directory: C:\users\century9\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   3:34 AM           2131 Word_File.txt

PS C:\users\century9\desktop> (Get-Content Word_File.txt) -replace '^(\S+\s+){160}' ⌨️
pierid 👀 nonapplicabness patinas rabific scandaliser waggel reauthenticate sufeism lairds cookee bragget ledgering perceptual chomper obscurities merino 
ganguela unproposed epulis loppard ignoblesse carrotage heartbrokenly unfusibness degenerate lacunae cirrocumulus knightlike overwhelmingness oxyrrhyncha capitalizations dimethylamine uninucleate syndicship graspable tropophil telchines abaiser overclement pursive

PS C:\users\century9\desktop> exit ⌨️
Connection to century.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh century10@century.underthewire.tech -p 22 ⌨️
century10@century.underthewire.tech's password: ⌨️ pierid
Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
PS C:\users\century10\desktop> whoami ⌨️
underthewire\century10
```

## Flag
pierid

## Continue
[Continue](./Century0910.md)