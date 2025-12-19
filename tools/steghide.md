# steghide
```bash
Source: https://steghide.sourceforge.net/
Description: hide text files or zip files in audio/image

Supported cover file formats:
    Images: JPEG, BMP
    Audio: WAV, AU

# Hide a note
echo "This is my secret message" > secret.txt
steghide embed -cf cover.jpg -ef secret.txt
# Displays info if file has embedded data or not
steghide info cover.jpg ❤️❤️❤️
# Extract the hidden note
steghide extract -sf cover.jpg ❤️❤️❤️❤️❤️

# Hide a ZIP file
zip secret.zip file1.txt file2.txt                  # create a zip file
steghide embed -cf cover.wav -ef secret.zip
# Extract hidden zip file
steghide extract -sf cover.jpg

# Better Tool (slow)
Aperi Solve
zsteg (png/bmp)
stegsolve (png/bmp)
steghide extract -sf image.jpg (jpg)                # jpg
```

## CTF
[picoGym0186: Forensic](../picoCTF/picoGym0186.md)<br>
[picoGym0351](../picoCTF/picoGym0351.md)

## Back to README.md
[BACK](../README.md)