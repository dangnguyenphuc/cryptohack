from pwn import *
from Crypto.Util.number import *
import json
import requests
from Crypto.Cipher import AES
import hashlib
import random
r = requests.get('https://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
encrypt_flag = (r.json()['ciphertext'])
flag_in_hex = requests.get(f'https://aes.cryptohack.org/block_cipher_starter/decrypt/{encrypt_flag}/')
flag = flag_in_hex.json()['plaintext']
print(bytes.fromhex(flag))