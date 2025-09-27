!pip install cryptography
from google.colab import drive
drive.mount('/content/drive')

with open("/content/drive/My Drive/file.txt", "r") as f:
    print(f.read())

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Generated Key:", key.decode())

cipher = Fernet(key)
input_file = "/content/drive/My Drive/file.txt"
with open(input_file, "rb") as f:
    data = f.read()

encrypted_data = cipher.encrypt(data)

encrypted_file = "/content/drive/My Drive/encrypted_file.txt"
with open(encrypted_file, "wb") as f:
    f.write(encrypted_data)

print("File encrypted successfully:", encrypted_file)

with open(encrypted_file, "rb") as f:
    encrypted_data = f.read()

decrypted_data = cipher.decrypt(encrypted_data)

decrypted_file = "/content/drive/My Drive/decrypted_file.txt"
with open(decrypted_file, "wb") as f:
    f.write(decrypted_data)

print("Decryption successful. Decrypted file saved as:", decrypted_file)

import hashlib

input_file = "/content/drive/My Drive/file.txt"
with open(input_file, "rb") as f:
    data = f.read()

md5_hash = hashlib.md5(data).hexdigest()
sha1_hash = hashlib.sha1(data).hexdigest()
sha256_hash = hashlib.sha256(data).hexdigest()

print("Original File Hashes:")
print("MD5:   ", md5_hash)
print("SHA1:  ", sha1_hash)
print("SHA256:", sha256_hash)

with open("/content/drive/My Drive/hashes.txt", "w") as f:
    f.write("MD5:    " + md5_hash + "\n")
    f.write("SHA1:   " + sha1_hash + "\n")
    f.write("SHA256: " + sha256_hash + "\n")

# Read original file
with open("/content/drive/My Drive/file.txt", "r") as f:
    original_content = f.read()

# Modify content (add a new line)
modified_content = original_content + "\nThis is a modified version."

# Save as file_modified.txt
modified_file = "/content/drive/My Drive/file_modified.txt"
with open(modified_file, "w") as f:
    f.write(modified_content)

print("Modified file created at:", modified_file)

modified_file = "/content/drive/My Drive/file_modified.txt"
with open(modified_file, "rb") as f:
    mod_data = f.read()

md5_mod = hashlib.md5(mod_data).hexdigest()
sha1_mod = hashlib.sha1(mod_data).hexdigest()
sha256_mod = hashlib.sha256(mod_data).hexdigest()

print("Modified File Hashes:")
print("MD5:   ", md5_mod)
print("SHA1:  ", sha1_mod)
print("SHA256:", sha256_mod)

print("\n--- Comparison ---")
print("MD5 same?   ", md5_hash == md5_mod)
print("SHA1 same?  ", sha1_hash == sha1_mod)
print("SHA256 same?", sha256_hash == sha256_mod)
