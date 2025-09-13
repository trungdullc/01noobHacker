# steghide
```
Source: https://steghide.sourceforge.net/
Description: hide text files or zip files in audio/image

Supported cover file formats:
    Images: JPEG, BMP
    Audio: WAV, AU

# Hide a note
echo "This is my secret message" > secret.txt
steghide embed -cf cover.jpg -ef secret.txt
# Extract the hidden note
steghide extract -sf cover.jpg ❤️❤️❤️❤️❤️

# Hide a ZIP file
zip secret.zip file1.txt file2.txt
steghide embed -cf cover.wav -ef secret.zip
# Extract hidden zip file
steghide extract -sf cover.jpg

# Better Tool
Aperi'Solve
```

## CTF
[picoGym0186: Forensic](../picoCTF/picoGym0186.md)<br>
[picoGym0351](../picoCTF/picoGym0351.md)

## Back to README.md
[BACK](../README.md)