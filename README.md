
# Cryptography Basics: AES & RSA in Python

A hands-on cybersecurity project exploring symmetric and asymmetric encryption using Python.

## Overview

This project demonstrates two cryptographic techniques using the Python `cryptography` library:

- **AES-256-GCM:** Symmetric encryption with authenticated decryption.
- **RSA-OAEP:** Asymmetric encryption using a public/private key pair.
- **Automated testing:** Seven unit tests covering successful operations and selected failure cases.

## Features

- Encrypt and decrypt UTF-8 text.
- Generate a random 256-bit AES key and 96-bit nonce.
- Detect modified AES-GCM ciphertext.
- Generate a 2048-bit RSA key pair.
- Use RSA-OAEP with SHA-256.
- Verify functionality with Python's built-in `unittest`.

## Technology Stack

- Python 3.14
- cryptography
- unittest
- Git and GitHub
- Visual Studio Code

## Project Structure

```text
cryptography-basics-python/
├── main.py
├── test_crypto.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd cryptography-basics-python
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the demonstration

```bash
python main.py
```

Enter a short test message when prompted.

### 5. Run automated tests

```bash
python -m unittest -v
```

## Cryptographic Concepts

### AES-256-GCM

AES is a symmetric encryption algorithm: the same secret key is used to encrypt and decrypt data.

GCM provides authenticated encryption, helping detect unauthorized changes to the ciphertext.

**Important:** Never reuse a nonce with the same AES-GCM key.

### RSA-OAEP

RSA is an asymmetric algorithm that uses a public key and a private key.

This project uses OAEP padding with SHA-256 for encryption.

RSA supports only limited message sizes. For larger data, real-world applications commonly use hybrid encryption, combining symmetric encryption with public-key cryptography.

## Security Considerations

- This is an educational demonstration, not a production-ready encryption application.
- The AES key is displayed in the terminal for learning purposes.
- RSA private keys are generated in memory and are not saved to disk.
- Real applications require secure key storage, access controls, and appropriate key lifecycle management.
- Never commit private keys, credentials, or real sensitive data to a public repository.

## Learning Outcomes

- Understand symmetric and asymmetric cryptography.
- Implement AES-GCM encryption and decryption.
- Understand RSA public/private key operations.
- Test cryptographic success and failure cases.
- Practice Python development, unit testing, and Git workflows.

## Author

Cybersecurity Learning Portfolio
    