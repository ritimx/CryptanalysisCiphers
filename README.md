# Cryptanalysis of Simple Ciphers

## Description

Cryptanalysis of Simple Ciphers is a Python-based project that allows users to encrypt, decrypt, and break three classic ciphers: Caesar Cipher, Vigenère Cipher, and Playfair Cipher. The application features a modern, interactive GUI, offering both manual encryption/decryption and automated cryptanalysis techniques to crack these ciphers.

## Features

- **Caesar Cipher**: Simple substitution cipher where each letter is shifted by a fixed number of positions.
- **Vigenère Cipher**: Polyalphabetic substitution cipher using a keyword for multiple shifts.
- **Playfair Cipher**: Digraph substitution cipher that uses a 5x5 grid to substitute pairs of letters.
- **Cryptanalysis**: Tools to break the ciphers using techniques like frequency analysis, brute force, and more.

## Technologies Used

- **Python**: Main programming language.
- **Tkinter/CustomTkinter**: For creating the modern GUI.
- **Pillow**: For handling and processing images.
- **Cryptography Techniques**: Caesar, Vigenère, and Playfair cipher implementations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ritimx/CryptanalysisCiphers.git
   
## Project Structure
```
.
cryptanalysis_ciphers/
├── main.py
├── ciphers/
│   ├── caesar.py
│   ├── vigenere.py
│   └── playfair.py
└── gui/
    ├── main_window.py
    └── widgets.py

```
