#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import long_to_bytes
from pwn import *
from binascii import unhexlify
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")
############### INTRO
#2
# ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# print("Here is your flag:")
# print("".join(chr(o) for o in ords))


#3
# cipher = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# print(bytes.fromhex(cipher))

#4
# cipher = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# print(base64.b64encode(bytes.fromhex(cipher)))

#5
# cipher = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# print(long_to_bytes(cipher))

#6

# cipher = "label"
# print("".join(chr(ord(o)^13) for o in cipher))

# 7 

'''
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0 
'''

'''
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
'''

# k1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
# k1_xor_k2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
# k2_xor_k3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
# flag_xor_so_on = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# so_on = xor(k1,k2_xor_k3) #k1^k2^k3

# flag = xor(flag_xor_so_on, so_on)   # flag
# print(flag)

# 8 
# cipher = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
# byte = bytes.fromhex(cipher)
# print(byte)

# key = b'crypto'

# output = {}
# for i in range(256):
#     output[i] = [xor(byte, i)]
#     print(xor(byte, i))

# print(outputs for outputs in output.values() if "crypto" in outputs)

# 9
# cipher = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
# byte = bytes.fromhex(cipher)
# #b"\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4.\x17]\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e\x07~&4Q\x15\x01\x04"
# key = b'crypto'
# subbyte = byte[0:8]

# print(subbyte)

# print(xor(subbyte, key))
# # b'myXORk}'
# key = b'myXORkey'
# print(xor(byte, key))

#