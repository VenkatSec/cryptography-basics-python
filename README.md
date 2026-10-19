
@'
# Cryptography Basics: AES & RSA in Python

A practical cybersecurity portfolio project demonstrating symmetric and asymmetric encryption using Python and the `cryptography` library.

## Overview

This project explores two cryptographic techniques:

- **AES-256-GCM:** Authenticated symmetric encryption.
- **RSA-OAEP with SHA-256:** Public-key encryption.
- **Automated testing:** Seven unit tests covering successful encryption, decryption, and selected failure cases.

## Features

- Encrypt and decrypt UTF-8 text.
- Generate a random 256-bit AES key and 96-bit nonce.
- Detect modified AES-GCM ciphertext.
- Generate a 2048-bit RSA key pair.
- Use RSA-OAEP with SHA-256.
- Test cryptographic operations using Python's built-in `unittest` framework.
- Redact cryptographic keys and ciphertext in demonstration output.

## Technology Stack

- Python
- `cryptography`
- `unittest`
- Git and GitHub
- Visual Studio Code

## Project Structure

```text
cryptography-basics-python/
├── main.py
├── Test_crypto.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/VenkatSec/cryptography-basics-python.git
cd cryptography-basics-python
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the demonstration

```powershell
python main.py
```

Enter a short test message when prompted. The program demonstrates encryption and decryption while redacting the AES key and encrypted data from its output.

### 5. Run the unit tests

```powershell
python -m unittest -v
```

The project currently includes seven unit tests for encryption/decryption round trips, empty messages, modified ciphertext, and incorrect keys.

## Cryptographic Concepts

### AES-256-GCM

AES is a symmetric encryption algorithm that uses the same secret key for encryption and decryption.

GCM provides authenticated encryption, allowing the application to detect unauthorized changes to protected data.

**Important:** Never reuse a nonce with the same AES-GCM key.

### RSA-OAEP with SHA-256

RSA is an asymmetric cryptographic algorithm that uses a public key and a private key.

This project uses OAEP padding with SHA-256. RSA can encrypt only limited amounts of data directly; practical systems commonly use hybrid encryption for larger messages.

## Security Considerations

- This project is for educational purposes and is not a production-ready encryption application.
- AES keys and RSA key pairs are generated in memory for the demonstration.
- The terminal output redacts the AES key and ciphertext; redaction does not replace secure key management.
- The demonstration does not persist generated private keys to disk.
- Production systems require appropriate key storage, access controls, nonce management, and key lifecycle procedures.
- Do not commit real secrets, private keys, credentials, or sensitive user data to a public repository.

## Learning Outcomes

- Understand symmetric and asymmetric cryptography.
- Implement AES-GCM encryption and authenticated decryption.
- Explore RSA public-key encryption and private-key decryption.
- Test successful operations and selected failure cases.
- Practice Python development, unit testing, and Git workflows.
- Apply privacy-conscious output handling in a security project.

## Author

Cybersecurity Learning Portfolio

---

**Disclaimer:** This project is an educational demonstration and should not be treated as a complete or production-ready security solution.
'@ | Set-Content -Path README.md -Encoding utf8
