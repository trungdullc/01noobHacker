# vim

```
Description: CLI text editor
Note: You can run commands inside vi/vim w/ :! ls (sudo -l) ⭐

vim FILE.txt

Tips: [ESC] /flag [enter] jump to next result with [N] ⭐

# Edit SQL query
vim sqlFile.txt
:%! sqlformat --reindent --keywords upper --identifiers lower

# Edit hexcode of a file
vim file.txt
:%! xxd
```

# Advanced
```
Range       Description                                 Example
21          line 21                                     :21s/old/new/g
1           first line                                  :1s/old/new/g
$           last line                                   :$s/old/new/g
.           current line                                :.w single.txt
%           all lines (same as 1,$)                     :%s/old/new/g
21,25       lines 21 to 25 inclusive	                :21,25s/old/new/g
21,$        lines 21 to end                             :21,$s/old/new/g
.,$         current line to end                         :.,$s/old/new/g
.+1,$       line after current line to end              :.+1,$s/old/new/g
.,.+5       6 lines (current to current+5 inclusive)    :.,.+5s/old/new/g
.,.5        same (.5 is interpreted as .+5)             :.,.5s/old/new/g

:s/// command substitutes in specified lines
:w command writes a file

For most commands, default range is . (current line,  :s/// substitutes in current line)
:g// and :w default is % (all lines)

Example                 Equivalent	        Description
:s/old/new/g            :.s/old/new/g	    substitute in current line
:g/old/	                :%g/old/            list all lines matching old
:w my.txt               :%w my.txt          write all lines to file my.txt

'<,'> is entered automatically to identify the lines that were last visually selected
:'<,'>s/old/new/g

:d (delete lines)
:t or :co (copy lines)
:m (move lines)


Command         Description
:21,25d         delete lines 21 to 25 inclusive
:$d             delete the last line
:1,.-1d         delete all lines before the current line
:.+1,$d         delete all lines after the current line
:21,25t 30      copy lines 21 to 25 inclusive to just after line 30
:$t 0           copy the last line to before the first line
:21,25m 30      move lines 21 to 25 inclusive to just after line 30
:$m 0           move the last line to before the first line

A mark ('x is the line containing mark x)
A search (/pattern/ is the next line matching pattern)

Command	                Description
:'a,'bd                 delete lines from mark a to mark b, inclusive
:.,'bd	                delete lines from the current line to mark b, inclusive
:'a,'bm 0	            move lines from mark a to b inclusive, to the beginning
:'a,'bw file.txt	    write lines from mark a to b to file.txt
:'a,'bw >> file.txt	    append lines from mark a to b to file.txt

Copy lines from current line to next line containing 'green' (inclusive), to end of the buffer
:.,/green/co $

Replace all "old" in next line in which "apples" occurs and line following it
:/apples/,/apples/+1s/old/new/g

Same (.1 is .+1, and because ; used, cursor position set to line matching "apples" before interpreting .+1)
:/apples/;.1s/old/new/g

Replace all "old" in next line in which "apples" occurs, and all lines up to and including 100 lines after the current line (where command was entered)
:/apples/,.100s/old/new/g

Replace all "old" in first block that starts with "apples" and ends with "peaches"
:/apples/,/peaches/ s/old/new/g
    /apples/ identifies first line after cursor containing "apples"
    /peaches/ is similar (first line after current line, not first after "apples")
    Be aware of backwards ranges
    The block is all lines from "apples" to "peaches", inclusive

Same, but "peaches" identifies first occurrence after "apples"
:/apples/;/peaches/ s/old/new/g

Insert "# " at start of each line in first block
:/apples/,/peaches/ s/^/# /g

Insert "# " at start of each line inside the block
:/apples/+1,/peaches/-1 s/^/# /g

To do a global replace in all blocks with the same patterns, use :g:
Insert "# " at the start of each line in all identified blocks
:g/apples/,/peaches/ s/^/# /g

In each such line, .,/peaches/ s/^/# /g is executed (. is assumed; it means current line, where "apples" occurs)
:g/apples/ identifies each line containing "apples".

Vim script where functions start with function or function! and end with endfunction
:g/^function!\? \(s:\)\?My/;/^endfunction/s/^/" /
    Insert "" " at the start of each line in each block
    All functions that start with function My or function s:My will be commented out
    The last line in each block is where endfunction first occurs (at the left margin), after where function My is found

Item	        Description
/pattern/	    next line where pattern matches
?pattern?	    previous line where pattern matches
\/	            next line where the previously used search pattern matches
\?	            previous line where the previously used search pattern matches
\&	            next line where the previously used substitute pattern matches
0;/that	        first line containing "that" (also matches in the first line)
1;/that	        first line after line 1 containing "that"
```

## Back to README.md
[BACK](../README.md)