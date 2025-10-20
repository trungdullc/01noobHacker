# Level 21

## Previous Flag
```
redavni
```

## Goal
AsianHacker-picoctf@webshell:/tmp$ cat readme.txt ⌨️<br>
Yes! This is really level 21 in here.<br>
And yes, After you solve it, you'll be in level 22!<br>

Now for the level:<br>

* We used to play this game when we were kids<br>
* When I had no idea what to do, I looked backwards

## What I learned
```
# Google: zlib decompress
The zlib module in Python provides functions for compression and decompression using the zlib library

import zlib

# Compressed data (example)
compressed_data = b'x\x9c+\xca\xcf\x07\x00\x02\x82\x01E'

# Decompress the data
decompressed_data = zlib.decompress(compressed_data)

# Print the decompressed data
print(decompressed_data.decode('utf-8'))

AsianHacker-picoctf@webshell:/tmp$ python3 -q
>>> import zlib ⌨️
>>> dir(zlib) ⌨️
['DEFLATED', 'DEF_BUF_SIZE', 'DEF_MEM_LEVEL', 'MAX_WBITS', 'ZLIB_RUNTIME_VERSION', 'ZLIB_VERSION', 'Z_BEST_COMPRESSION', 'Z_BEST_SPEED', 'Z_BLOCK', 'Z_DEFAULT_COMPRESSION', 'Z_DEFAULT_STRATEGY', 'Z_FILTERED', 'Z_FINISH', 'Z_FIXED', 'Z_FULL_FLUSH', 'Z_HUFFMAN_ONLY', 'Z_NO_COMPRESSION', 'Z_NO_FLUSH', 'Z_PARTIAL_FLUSH', 'Z_RLE', 'Z_SYNC_FLUSH', 'Z_TREES', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'adler32', 'compress', 'compressobj', 'crc32', 'decompress', 'decompressobj', 'error']
```

## Solution
```
Given: package.pack

AsianHacker-picoctf@webshell:/tmp$ file package.pack ⌨️
package.pack: zlib compressed data

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️ 
#!/usr/bin/env python3
import zlib
import bz2
import sys
from pathlib import Path

INFILE = "package.pack"
OUTFILE = "package.out"

# ensure file exists and is readable
p = Path(INFILE)
if not p.is_file():
    print(f"ERROR: {INFILE} not found in {Path.cwd()}", file=sys.stderr)
    sys.exit(1)

data = p.read_bytes()
print(f"Read {len(data)} bytes from {INFILE}")

# process until no known transformation applies
iters = 0
while True:
    iters += 1
    if data.startswith(b'x\x9c'):
        data = zlib.decompress(data)
        print(f"[{iters}] zlib -> {len(data)} bytes")
    elif data.startswith(b'BZh'):                                       # Magic byte
        data = bz2.decompress(data)
        print(f"[{iters}] bzip2 -> {len(data)} bytes")
    elif data.endswith(b'\x9cx'):                                       # From riddle
        data = data[::-1]
        print(f"[{iters}] reversed -> {len(data)} bytes")
    else:
        print("No more known transformations.")
        break

# write final output
Path(OUTFILE).write_bytes(data)
print(f"Wrote {len(data)} bytes to {OUTFILE}")

# try to display as UTF-8 text, otherwise show hexdump head
try:
    text = data.decode("utf-8")
    print("--- text preview ---")
    print(text[:1000])
except UnicodeDecodeError:
    print("--- binary output (first 64 bytes hex) ---")
    import binascii
    print(binascii.hexlify(data[:64]))

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
Read 239194 bytes from package.pack
[1] zlib -> 239113 bytes
[2] zlib -> 239032 bytes
[738] zlib -> 127 bytes
[739] zlib -> 116 bytes
[740] bzip2 -> 53 bytes
[741] bzip2 -> 17 bytes
No more known transformations.
Wrote 17 bytes to package.out
--- text preview ---
sgol ruoy ta kool 👀

# Remove: tracking and create result
AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import zlib, bz2

result = "" 👀

with open("package.pack", "rb") as f:
    data = f.read()

    while True:
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
            result += ' '
        elif data.startswith(b'BZh'):
            data = bz2.decompress(data)
            result += '#'
        elif data.endswith(b'\x9cx'):
            data = data[::-1]
            result += '\n' 👀
        else:
            break
    print(result)

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
      ###          ###      ########    ########    ##########  ########
    #######      #######    #########   #########   #########   #########
   ##     ##    ##     ##   ##      ##  ##      ##  ##          ##      ##
  ##           ##       ##  ##      ##  ##      ##  ##          ##      ##
  ##           ##       ##  #########   #########   ########    #########
  ##           ##       ##  ########    ########    ########    ######## 
  ##           ##       ##  ##          ##          ##          ##   ## 
   ##     ##    ##     ##   ##          ##          ##          ##    ## 
    #######      #######    ##          ##          #########   ##     ## 
      ###          ###      ##          ##          ##########  ##      ##
```

## Flag
http://www.pythonchallenge.com/pc/hex/copper.html

## Continue
[Continue](./Level22.md)