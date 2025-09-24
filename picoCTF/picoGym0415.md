# picoGym Level 415: endianness-v2
Source: https://play.picoctf.org/practice/challenge/415

## Goal
Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is.<br>
Download it here and see what you can get out of it<br>
https://artifacts.picoctf.net/c_titan/114/challengefile

## What I learned
```
swap endianness
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/114/challengefile ⌨️
--2025-09-22 21:23:33--  https://artifacts.picoctf.net/c_titan/114/challengefile
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.72, 3.170.131.33, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3428 (3.3K) [application/octet-stream]
Saving to: 'challengefile'

challengefile                                              100%[======================================================================================================================================>]   3.35K  --.-KB/s    in 0s      

2025-09-22 21:23:33 (1.12 GB/s) - 'challengefile' saved [3428/3428]

AsianHacker-picoctf@webshell:~$ file challengefile ⌨️
challengefile: data
AsianHacker-picoctf@webshell:~$ binwalk challengefile ⌨️ 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

AsianHacker-picoctf@webshell:~$ exiftool challengefile ⌨️
ExifTool Version Number         : 12.40
File Name                       : challengefile
Directory                       : .
File Size                       : 3.3 KiB
File Modification Date/Time     : 2024:03:12 00:36:50+00:00
File Access Date/Time           : 2025:09:22 21:23:36+00:00
File Inode Change Date/Time     : 2025:09:22 21:23:33+00:00
File Permissions                : -rw-rw-r--
Warning                         : Processing JPEG-like data after unknown 1-byte header 👀
AsianHacker-picoctf@webshell:~$ strings challengefile ⌨️
 '.$
#,")7(
410,'
4428=943.<
!2222222222222222222222222222222222222222222222222
)('&654*:987FEDCJIHGVUTSZYXWfedcjihgvutszyxw
5*)(9876EDC:IHGFUTSJYXWVedcZihgfutsjyxwv
Tx+(
(<yA
G2PF
Y'@2
o/IB
*klv
77T4
F8Yx$
1O3F
,UQk
hM|A
kV.l
X^5q
24.h
0Rg~
sodmn@
#iRy
yskg
[H%'
0>0U
3Gb}
XdW6
JGr ^
4)|/
OdX|
''      YP4w
Xk}N
H13O
-2yD
=ouY
+oh[
hcY 
~/EQ

AsianHacker-picoctf@webshell:~$ xxd challengefile | head -n 10 ⌨️
00000000: e0ff d8ff 464a 1000👀 0100 4649 0100 0001  ....FJ....FI....
00000010: 0000 0100 4300 dbff 0606 0800 0805 0607  ....C...........
00000020: 0907 0707 0c0a 0809 0b0c 0d14 1219 0c0b  ................
00000030: 1d14 0f13 1d1e 1f1a 201c 1c1a 2027 2e24  ........ ... '.$
00000040: 1c23 2c22 2937 281c 3431 302c 271f 3434  .#,")7(.410,'.44
00000050: 3238 3d39 3433 2e3c 00db ff32 0909 0143  28=943.<...2...C
00000060: 0c0b 0c09 180d 0d18 211c 2132 3232 3232  ........!.!22222
00000070: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222
00000080: 3232 3232 3232 3232 3232 3232 3232 3232  2222222222222222
00000090: 3232 3232 3232 3232 3232 3232 c0ff 3232  222222222222..22

# Notice: first 4 bytes, also the header signature seems to be reversed of a JPG header
# Every 4 bytes is flipped

# Method 1:
# Sort every 4 byte into an array
# Reverse order/Flip

AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/env python3
"""
Fixed pipeline:
 1) get_hex: read binary input and write continuous hex to analyzed.txt
 2) split_into_array: split hex into 8-char chunks and write comma-separated list to array.txt
 3) reverse_each_chunk: read array.txt, reverse byte-order inside each 8-char chunk and write reversedHex.txt
"""

from pathlib import Path

def get_hex(input_path: Path, output_path: Path):
    """Read binary file and write continuous hex string to output_path."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    data = input_path.read_bytes()
    hex_str = data.hex()
    output_path.write_text(hex_str)
    return output_path

def split_into_array(input_path: Path, array_output: Path, chunk_size: int = 8):
    """
    Read a hex string file (no whitespace expected), split into chunk_size characters,
    write as a comma+space separated single-line file and also return the list.
    """
    s = input_path.read_text().strip().replace('\n', '').replace(' ', '')
    if len(s) == 0:
        return []
    # Pad if necessary (not strictly required, but keeps last chunk full)
    # If you prefer not to pad, comment out the next 2 lines.
    pad_len = (-len(s)) % chunk_size
    if pad_len:
        s += '0' * pad_len
    chunks = [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]
    array_output.write_text(', '.join(chunks))
    return chunks

def reverse_hex_strings(hex_strings):
    """
    For each hex string (like "aabbccdd"), reverse byte order to produce "ddccbbaa".
    Works for any even-length hex string; splits into bytes (2 chars).
    """
    out = []
    for h in hex_strings:
        # remove non-hex characters just in case
        h = ''.join(c for c in h if c.isalnum())
        if len(h) % 2 != 0:
            # if odd length, pad with leading zero
            h = '0' + h
        bytes_list = [h[i:i+2] for i in range(0, len(h), 2)]
        bytes_list.reverse()
        out.append(''.join(bytes_list))
    return out

def reverse_from_array_file(array_file: Path, reversed_output: Path):
    """
    Read array_file which contains comma-separated hex chunks on one or multiple lines.
    Reverse each chunk's byte-order and write each reversed chunk on its own line to reversed_output.
    """
    if not array_file.exists():
        raise FileNotFoundError(f"Array file not found: {array_file}")
    text = array_file.read_text()
    # split on comma to recover chunks, strip whitespace/newlines
    parts = [p.strip() for p in text.split(',') if p.strip()]
    reversed_chunks = reverse_hex_strings(parts)
    reversed_output.write_text('\n'.join(reversed_chunks))
    return reversed_chunks

if __name__ == "__main__":
    # paths used in your original snippet (normalized/consistent)
    input_file = Path('challengefile')        # binary input (your original)
    analyzed_file = Path('analyzed.txt')     # hex output (was inconsistent in your snippet)
    array_file = Path('array.txt')           # comma-separated 8-char chunks
    reversed_file = Path('reversedHex.txt')  # reversed-byte-order lines

    try:
        print(f"1) Extracting hex from {input_file} -> {analyzed_file}")
        get_hex(input_file, analyzed_file)

        print(f"2) Splitting {analyzed_file} into 8-char chunks -> {array_file}")
        split_into_array(analyzed_file, array_file, chunk_size=8)

        print(f"3) Reversing byte-order for each chunk in {array_file} -> {reversed_file}")
        reverse_from_array_file(array_file, reversed_file)

        print("Done. Files created/overwritten:")
        print(f"  - {analyzed_file}")
        print(f"  - {array_file}")
        print(f"  - {reversed_file}")
    except Exception as e:
        print("Error:", e)
        raise

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
1) Extracting hex from challengefile -> analyzed.txt
2) Splitting analyzed.txt into 8-char chunks -> array.txt
3) Reversing byte-order for each chunk in array.txt -> reversedHex.txt
Done. Files created/overwritten:
  - analyzed.txt
  - array.txt
  - reversedHex.txt 👀

AsianHacker-picoctf@webshell:~$ ls ⌨️
README.txt  analyzed.txt  array.txt  challengefile  pythonScript.py  reversedHex.txt
AsianHacker-picoctf@webshell:~$ xxd -r -p reversedHex.txt reversedHex.jpg ⌨️
AsianHacker-picoctf@webshell:~$ file reversedHex.jpg ⌨️
reversedHex.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 300x150, components 3
AsianHacker-picoctf@webshell:~$ sz reversedHex.jpg ⌨️

Open: picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_94cc03f3}

# Method 2:
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
new_hex = ""
 
with open("challengefile", "rb") as file:
    hexdata = file.read().hex()
 
hex_chunks = [hexdata[i:i+8] for i in range(0, len(hexdata), 8)]
 
for chunk in hex_chunks:
    for i in range(len(chunk)-2,-1,-2):
        new_hex += chunk[i] + chunk[i+1]
 
with open("solved.jpg", "wb") as file:
    file.write(bytes.fromhex(new_hex))
 
print("File created successfully")

AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️
File created successfully
AsianHacker-picoctf@webshell:~$ sz solved.jpg ⌨️

Open: picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_94cc03f3}

Method 3: CyberChef
https://gchq.github.io/CyberChef/#recipe=To_Hex('Space',0)Swap_endianness('Hex',4,true)From_Hex('Auto')Render_Image('Raw')&input=4P/Y/0ZKEAABAEZJAQAAAQAAAQBDANv/BgYIAAgFBgcJBwcHDAoICQsMDRQSGQwLHRQPEx0eHxogHBwaICcuJBwjLCIpNygcNDEwLCcfNDQyOD05NDMuPADb/zIJCQFDDAsMCRgNDRghHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIywP8yMgAIEQADLAGWAgAiAREDAREAxP8BAQAAHwEBAQUAAQEBAAAAAAEAAAAFBAMCCQgHBsT/CwoAELUAAwMBAgUDBAIABAQFAX0BAAQAAwIhEgUREwZBMSIHYVGBMhRxIwihkRXBsUIk8NFSgnJiMxcWCgklGhkYKSgnJjY1NCo6OTg3RkVEQ0pJSEdWVVRTWllYV2ZlZGNqaWhndnV0c3p5eHeGhYSDiomIh5WUk5KZmJeWpKOimqinpqWzsqqpt7a1tMK6ubjGxcTDysnIx9XU09LZ2NfW4%2BLh2ufm5eTx6uno9fTz8vn49/YAxP/6AwABHwEBAQEBAQEBAAAAAQEAAAAFBAMCCQgHBsT/CwoAEbUABAIBAgcEAwQABAQFAHcCAREDAgExIQUEUUESBhNxYQcIgTIioZFCFCMJwbEV8FIzCtFyYuE0JBYYF/ElJyYaGTUqKSg5ODc2RURDOklIR0ZVVFNKWVhXVmVkY1ppaGdmdXRzanl4d3aEg4J6iIeGhZOSiomXlpWUopqZmKalpKOqqaintbSzsrm4t7bEw8K6yMfGxdPSysnX1tXU4trZ2Obl5OPq6ejn9fTz8vn49/YA2v/6AAEDDBEDEQL3AD8AgKIo%2BoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKAqAoigKgKIoCoCiKApuqCgKbaztruLu4tqAVHgrKMKVZE8GgCT3AJIcFTUBNKa3Hp9XJKlKxQOv1p11wiQDQhUKLKDnnPIMejJdA0VGmG0Z0m4ltmoXua2YOEiJCY75eSE0gOJ4X0usKDx5QRPvjRUr1hnu2Xmq6NY4QQV3yHCbX1CwIFZm5MFxRsx4mw6aDC%2B6ZL%2BqTUDOhpjSzLm9xCi26Tnk/AMontdPsaKnjXoMiIzVraV7ayKW6h6Zi5GUx2hhJ8EYjjI5ZbUaAOP5o7v9an/ydix3%2BdhC%2BwZWCA5SYueYn1NCAyiOvNTJiiLpok9aqXlBFEvxxi7nRzJQRtroB3KGu25PDs7jI1V6Fuo8PXmSarap3JuT0hZ4IwKq3Bh2YMlZJ0AygNEBFLF48lzR27QJtt10uAtvL0lC246yJckqa2x2v5sX7gcK5xWnv1/axPNiy5aefrxn33qSGJa4zozlyWqskgyAIIZ2eIIkWxtA6Qc3N1Q0skbaMUirQkqosuSR6lUwy8dAUkcTAEhSM952WL2ibtNN5Yp0dJqinouh6Ih1BeK0ni%2BU58at/HqiAyhGDzWwohL2aBkFLsTdV5aW1KulszcN1pij3I3Umw8w3jGrGMmhnfW6d%2Bmmt451jXkSYawzqKM2IReA51w%2BpB4wQjUAEns6VqooM6qXzlmpny52qLLdhKzzFglO6CkNddPgstJLb2sL9S9R2vJ37ICSHBdiCaqlB8CpsaJfAGNLPK14D1c03IZpsvst0kY4WXgkjBiyjXMOBDFPM0aQlybxvP3yDGfP/imuSJDOsG2j0K7kDOP9nxgMKADN8%2B4sVVFrB3UYdZssELsZMKctgF0bCMjzths5PZUECFU7UvdoTXxB3VuyCRJicbBrVi5sFI%2BIZe/fFeen3EBjz8ELK6oNgNrE7x6XbBpsoi6ztmxF3LE3lrJjFkkybwFYXjVxpI7LG%2BJpS2mTi2vd2TI0LmiEq5RhNVrEMFJnfo4qMGfrflLXADgYt7%2Bzoi2xb/SHvfbna8xd2WNT2j8NlQQ4nABnnC1XA3q3uyDuo2mLS%2BQGGZqsDDaSGhxBPceKlgBtR3zSRRLLq9wKc29kbW5AiFsomGG6AIFP5gOJh/kBvIufHRVvyFv025E3Z5td2lus0zUzV%2BwjaVJ5EsrB92AcARKMI99lRbmwSot4Q96rE0shzCW0IsVaoAqxxFmScybMB85AJPy/KiTN1sgloWZaM7xyxB7GKlt3DFUWbYBwsc7NRyrcAIrh8ZS5ovzNjbXzNrZWMLa83ldCot6QlGTMjhFrg4BYLAEwP6%2BgiXdaqwv11GHdbXg7uLe6Y9ywM5QUqQSPfWTAiJAgGOeQYHtwoijKDaIoCoCiKAqA/OcKgHlza2elDdHh7Z%2B4uGUjTNaoW0glJ8CWmHGSAGhB1wTAl3AARS/VDV5a1OQvlaYoS1egneSZP4xm2pnIZocWVgnO5cBxfG%2BpAT7fqy9KiyGnX3u1hW553LKcAbf5/ewQieT8kOOVnignHEBR2%2Bumh/Z%2BGlw6jVnymKU8wTZZmh2VGitV4wgBlbI5hiQYVRPYK3Mz/O8XsQ579q0am6V6Z6%2BKZXRkG2%2BzL/dbZZTrHowP0dTtyLt2HECLq3vhb6cR63W3Y2hpuLp3EzzrMpZcrkaKVN4oHG6ccT5qqmI7tdQOoam7y8Hf0NOG4Xn2jCTi8uycbwavkufbdL9gyCjvWg/3Wg6gppKXw2Mb8LRnreY1KvcOf7ItwAoJkkKsDzA%2BMFXUB97Swz%2BNl3br2IkgyGhk6h01bq7FLPIRmGOylY%2BBtwxkO6Bo6FrC7zYOuumL2iQYMXy7WduS5EUZ1JSj27ZEApXcnofBUgzHGLlLsY4zR2J94QTsWGRXNupTcrc80kNeJM1kVpRFyGLly8MuR2Kit%2BsdKDUwgFHLde/s6TRot7Y3zI%2BXWwLEFYtkjl0wcuNQJcdKR3IgXvC5xUvKwqB1ku1p6%2BKe1S3ZNnNQuvGNgOv7OJz5eAZz15xncXAARZJSM3ixGzva0GBtZJKFtO6fZZkZ2GExzYhDyJgFez/JtWbzszQpfC/WsSa%2BkUv1Ldxc%2BLJXlidFgkiCYGP37qcwttAvc8xHzgEURV0e/mjJvG3Qu%2BcY4jySRittmK1oxjBWlgag7aYcLOfEjHHqUUcafsRPZFh81DZNtmS1das7BjI3uIkZRpQ3vmvMuVPJ4ScnCVlQNHel4XEjB/tTU832oc5FXZq6FXbiGDhrq/x4So45j0m3uYPRfYyB7LWmnuYNYXRD0iW/0p1aJMwZF8iKKN5iN6pHts198BwcQNFrd2%2BL9mgPv%2BFs9kf6a0GS92rNcxwAEuzxHfOxN9my5VhrfU7GusL3Kqtvpb4dnc6ZPpHm3bCIZ5wIwG43G2yU5Bt4gHagY/u%2BQFHbFeGxphzLi9urWjyNuwTTZAWD7EgxM0%2B3NgKcQgIPEKCsuqqgI421hadv6vBWzBeELTJ5RMVtaxzFUXUacyWX%2Bby8DSCIWnuOc9KJAyhDqCP87z1vdVmPSNknKNH%2By4KweSAzAMh0w2/LMZ0OAFdk%2BlrYpxW65z2dzj91eZuE8WqZkrhljal7B0XAGVfI31oPPb04gKLHU8E3MnXNLFvG4tq4seQYZWTFcjau6iwIF/fDg5MAufC1odLrpKtul/ZXF%2Bzo1zbpvRXpaGPRWHzc4y0MDIC4goF2G%2BckqIc4gKK6dUT4f3oasDVb5ZOma/sb3swfrI2byoTzBLX7cTtmyGxyqxhAlrQ66H1r5vdzauwqF5aXvHkcxg59mMZxIaKShI8lI/xo6wpML0oOoFL26g5aXJH5xAD/XmTKzrqvi8q6bxLPK29oW/kPEFg1pxhBKrwf3mgdHXXTsj%2BOJIxdWtneyEbE42hjWSCq1EFgAMl1XZ1%2BL0VRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFEVRABRFUQAURVEAFNn/ARQ

Method 4: CyberChef (no need DL)
https://cyberchef.io/#recipe=Swap_endianness('Raw',4,true)Render_Image('Raw')
```

## Flag
picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_94cc03f3}

## Continue
[Continue](./picoGym0456.md)