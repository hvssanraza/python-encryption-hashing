# Python Encryption & Hashing

This repository contains Python implementations of basic **encryption, decryption, and hashing** operations, created and tested in Google Colab.  

## Features
- Symmetric encryption & decryption using **Fernet (AES)**.
- File hashing using **MD5, SHA-1, and SHA-256**.
- Demonstration of the **Avalanche Effect** (small input change → large hash difference).
- Practical verification of the **CIA Triad** (Confidentiality, Integrity, Availability).

## Files
- `python_encryption_hashing.ipynb` → Colab notebook with code and outputs.

## Requirements
- Python 3.x
- `cryptography` library
- `hashlib` (built-in)

## How to Run
1. Open in Google Colab or Jupyter Notebook.
2. Upload a sample `file.txt` to your Google Drive.
3. Run cells to:
   - Encrypt & decrypt files.
   - Generate hash values.
   - Compare original vs modified file hashes.

## Example Output
MD5: 8dd986dcec9ba31cd6ffc6624f84ba43
SHA1: b2d7e568fa8948cd63437e846d322810e981849f
SHA256: 7ac32839f53fe7e60cfe681deead1c0368c3aa6e755383e54de4be3e4ae64119

shell
Copy code

## Author
Hassan Raza
