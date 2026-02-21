import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend

ITERATIONS = 200000 
SALT_SIZE = 16

def derive_key(password: str, salt: bytes):
    password_bytes = password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key

def encrypt_file(filepath, password):
    salt = os.urandom(SALT_SIZE)
    key = derive_key(password, salt)
    fernet = Fernet(key)

    with open(filepath, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    new_path = filepath + ".enc"

    with open(new_path, "wb") as f:
        f.write(salt + encrypted)  #início

    return new_path


def decrypt_file(filepath, password):
    with open(filepath, "rb") as f:
        file_data = f.read()

    salt = file_data[:SALT_SIZE]
    encrypted = file_data[SALT_SIZE:]

    key = derive_key(password, salt)
    fernet = Fernet(key)

    decrypted = fernet.decrypt(encrypted)

    original_path = os.path.splitext(filepath)[0]

    name, ext = os.path.splitext(original_path)

    new_path = name + "_restaurado" + ext

    with open(new_path, "wb") as f:
        f.write(decrypted)

    return new_path