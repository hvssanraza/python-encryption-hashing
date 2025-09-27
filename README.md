# 🔐 Python Encryption & Hashing

This repository demonstrates **encryption, decryption, and hashing techniques in Python** using Google Colab.  
It includes practical examples of the **CIA Triad** (Confidentiality, Integrity, Availability) and the **Avalanche Effect** in hashing.

---

## ✨ Features
✅ Symmetric Encryption & Decryption using **Fernet (AES)**  
✅ File Hashing with **MD5, SHA-1, and SHA-256**  
✅ Demonstration of the **Avalanche Effect** 🔄  
✅ Practical verification of the **CIA Triad**  
✅ Simple, easy-to-understand **Colab Notebook**  

---

## 📂 Files
| File | Description |
|------|-------------|
| `python_encryption_hashing.ipynb` | Jupyter/Colab notebook containing all encryption, decryption, and hashing code |
| `file.txt` | Example input file (original) |
| `file_modified.txt` | Modified file for Avalanche Effect demonstration |
| `hashes.txt` | Saved hash values (MD5, SHA-1, SHA-256) |

---

## 🛠️ Requirements
- Python 3.x  
- [`cryptography`](https://pypi.org/project/cryptography/)  
- Built-in `hashlib`  

Install dependencies:
```bash
pip install cryptography
🚀 How to Run
Open the notebook in Google Colab or Jupyter.

Upload a sample file.txt to your Drive.

Run the notebook cells to:

Encrypt & decrypt files 🔑

Generate hash values 🧾

Compare original vs modified file hashes 🔍

📊 Example Output
Original File Hashes:

makefile
Copy code
MD5:    8dd986dcec9ba31cd6ffc6624f84ba43
SHA1:   b2d7e568fa8948cd63437e846d322810e981849f
SHA256: 7ac32839f53fe7e60cfe681deead1c0368c3aa6e755383e54de4be3e4ae64119
Modified File Hashes:

makefile
Copy code
MD5:    d39cc9b6e527e16f00ab63d7c4eb669
SHA1:   bfdc732a9e7239e3c8c6fba33ac4997627fb4e17
SHA256: fea1d5409f913c98b6b75fbab8c172d7fb2d45cfbe7d1d8f8fa52e6dc3726ed
🔄 Comparison: All values are different → proves Avalanche Effect ⚡

🌐 CIA Triad Demonstration
Confidentiality → Encryption ensures only key holders can access the data.

Integrity → Hashing ensures detection of even the smallest modification.

Availability → Files accessible anytime via Google Drive + Colab.

📌 Avalanche Effect
A tiny change in input (e.g., adding one word to a file) causes a completely different hash output.
This property ensures high sensitivity of hashing functions to data integrity.

👨‍💻 Author
Hassan Raza
BS Artificial Intelligence – Security & AI Enthusiast
