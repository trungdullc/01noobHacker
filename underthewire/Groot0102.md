# Groot Level 01 → 02 sed -n '1481110,1481117p' elements.txt | tr -d '\n'

## Previous Flag
```
464c3
```

## Goal
The password for groot3 is the word that is made up from the letters in the range of 1,481,110 to 1,481,117 within the file on the desktop.<br>

NOTE: The password will be lowercase no matter how it appears on the screen.

## What I learned
```
Linux:
    sed -n '1481110,1481117p' elements.txt | tr -d '\n'
        sed -n '1481110,1481117p' → print only those lines
        tr -d '\n' → remove newlines, effectively joining
    awk 'NR>=1481110 && NR<=1481117 {printf "%s", $0} END {print ""}' elements.txt
        NR is the line number
        printf "%s", $0 prints without adding a newline
        The final print "" ensures a newline at the end

sed vs awk
    sed (stream editor)
        Best for: simple substitutions, deleting lines, extracting ranges
        Line-oriented: processes text line by line
        Syntax is shorter for tasks like find/replace or grabbing ranges
        sed 's/foo/bar/g' file.txt              # Replace "foo" with "bar"
        sed -n '10,20p' file.txt                # Print lines 10–20
        sed '/error/d' file.txt                 # Delete lines containing "error"
    awk (Aho–Weinberger–Kernighan)
        Best for: working with structured text (fields/columns)
        Field-aware: splits lines into $1, $2, etc. (by default whitespace)
        Mini programming language with variables, conditionals, loops
        awk '{print $1}' file.txt                           # Print first column
        awk 'NR>=10 && NR<=20' file.txt                     # Print lines 10–20
        awk '{sum += $3} END {print sum}' file.txt          # Sum values in column 3
        awk '$2=="Alice"' file.txt                          # Only show lines where column 2 == "Alice"

PS C:\users\Groot2\desktop> -join(Get-Content elements.txt)[1481110..1481117]
hiding

-join is the join operator
    Get-Content elements.txt → reads the file into an array of strings (each line = one element)
    [1481110..1481117] → selects lines from index 1481110 through 1481117
    -join → merges those 8 lines into one continuous string (no separator by default)
    Note: array that made each line into an element
```

## Solution
```
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot2@groot.underthewire.tech -p 22 ⌨️
groot2@groot.underthewire.tech's password: ⌨️ 464c3

Windows PowerShell
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!

PS C:\users\Groot2\desktop> dir ⌨️

    Directory: C:\users\Groot2\desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/30/2018   5:52 AM        2357268 elements.txt 👀

PS C:\users\Groot2\desktop> (Get-Content elements.txt)[1481110..1481117] ⌨️
 
h
i
d
i
n
g

PS C:\users\Groot2\desktop> -join(Get-Content elements.txt)[1481110..1481117] ⌨️
hiding

 PS C:\users\Groot2\desktop> exit ⌨️
Connection to groot.underthewire.tech closed.
PS C:\Users\trung.DESKTOP-G7C81CH\Downloads\01noobHacker> ssh groot3@groot.underthewire.tech -p 22 ⌨️
groot3@groot.underthewire.tech's password: hiding ⌨️

Windows PowerShell 
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

Under the Wire... PowerShell Training for the People!
 
PS C:\users\Groot3\desktop> whoami ⌨️
underthewire\groot3
```

## Flag
hiding

## Continue
[Continue](./Groot0203.md)