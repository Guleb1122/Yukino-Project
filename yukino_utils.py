import os
from cryptography.fernet import Fernet

def get_key():
    if not os.path.exists("yukino.key"):
        key = Fernet.generate_key()
        with open("yukino.key", "wb") as f: f.write(key)
    return open("yukino.key", "rb").read()

def encrypt_data(data):
    f = Fernet(get_key())
    return f.encrypt(data.encode() if isinstance(data, str) else data)

def decrypt_data(encrypted_data):
    f = Fernet(get_key())
    try:
        return f.decrypt(encrypted_data).decode('utf-8', errors='ignore')
    except:
        return "Decryption Error"