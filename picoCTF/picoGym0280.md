# picoGym Level 280: morse-code
Source: https://play.picoctf.org/practice/challenge/280

## Goal
Morse code is well known. Can you decrypt this? <br>
Download the file here <br>
https://artifacts.picoctf.net/c/79/morse_chal.wav<br>
Wrap your answer with picoCTF{}, put underscores in place of pauses 👀, and use all lowercase 👀

## What I learned
```
Download Audacity: https://www.audacityteam.org/download/windows/

https://morsecodegenerator.org/morse-audio-translator
```

## Side Quest
```
AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
# Morse Code Dictionary
MORSE_CODE_DICT = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
    '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
    '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
    '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
    '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
    '--..': 'z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '-----': '0'
}

def decode_morse(morse_code: str) -> str:
    # Normalize and split on '/' which marks word boundaries
    # (works whether input uses "/"," / "," /")
    words = [w.strip() for w in morse_code.strip().split('/')]
    decoded_words = []
    for word in words:
        if word == "":
            # preserve empty word (in case of multiple slashes) -> becomes empty chunk
            decoded_words.append("")
            continue
        # split word into letters (whitespace separated)
        letters = word.split()
        decoded = "".join(MORSE_CODE_DICT.get(ch, "?") for ch in letters)
        decoded_words.append(decoded)
    # join words with underscore for pause indicator
    return "_".join(decoded_words)

def main() -> None:
    # Input
    morse_input = ".-- .... ....- --.../.... ....- --... ..../----. ----- -../.-- ..--- ----- ..- ----. .... --..."
    print(f"Decoded Message: picoCTF{{{decode_morse(morse_input)}}}")

if __name__ == "__main__":
    main()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️ 
Decoded Message: picoCTF{wh47_h47h_90d_w20u9h7} 🔐
```

## Solution
```
https://webshell.picoctf.org/

# Online Morse Code Decoder vs Audacity: https://morsecodegenerator.org/morse-audio-translator ⌨️
    Morse Code:
    .-- .... ....- --.../.... ....- --... ..../----. ----- -../.-- ..--- ----- ..- ----. .... --...
    Decoded Text:
    WH47 H47H 90D W20U9H7 👀

# Rules: make it lowercase and place _ where pauses are
picoCTF{wh47_h47h_90d_w20u9h7} 🔐
```

## Flag
picoCTF{wh47_h47h_90d_w20u9h7}

## Continue
[Continue](./picoGym0307.md)