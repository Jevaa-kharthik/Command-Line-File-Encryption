# Command Line File Encryption in Python

This project provides a command line utility to encrypt files using various hashing algorithms.

## Features
- Encrypt files using different hashing algorithms.
- Command line interface for ease of use.
- Modular design for better maintainability.

## Encryption Algorithms Supported
The following encryption (hashing) algorithms are supported:

- **SHA1**
- **SHA224**
- **SHA256**
- **SHA384**
- **SHA512**
- **SHA3_224**
- **SHA3_256**
- **SHA3_384**
- **SHA3_512**
- **SHA512_224**
- **SHAKE128**

## Requirements
- Python 3.x
- `cryptography` library

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/Jevaa-kharthik/Command-Line-File-Encryption/tree/main
    cd encrypto
    ```
2. **Install dependencies**:
    ```sh
    pip install cryptography
    ```

## Usage
To encrypt a file, use the following command:
```sh
python Encrypto.py --filepath=<PathOfTheFile> --secret=<PassCode> --encryption=<TypeOfEncryption>
