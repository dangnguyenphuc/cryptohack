from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 1
# p = 991
# g = 209
# print(inv(g, p))


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 2
'''We just need to detect Cycle :))'''
p = 28151

found = False
for i in range(2,p):
    found = True
    for j in range(2,p):
        a = pow(i, j, p)
        if a == i:
            found = False
            break
    if found:
        print("Found: " + str(i))


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 3

# SageMath :))


