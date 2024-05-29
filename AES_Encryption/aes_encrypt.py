from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt(data, key):
    salt = get_random_bytes(16)
    derived_key = scrypt(key, salt, 32, N=2**14, r=8, p=1)
    cipher = AES.new(derived_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return b64encode(salt + cipher.nonce + tag + ciphertext).decode('utf-8')