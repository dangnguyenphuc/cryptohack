# from pwn import *
from Crypto.Util.number import *
import json
import requests
from Crypto.Cipher import AES
import hashlib
import random
import threading
from Crypto.Util.Padding import pad, unpad
import time
from datetime import datetime, timedelta
import os
from PIL import Image
import numpy
from Crypto.Cipher import DES3
import zlib

# hex byte_list
byte_list = ['0'+hex(i)[2:] if len(hex(i)[2:]) == 1 else hex(i)[2:] for i in range(1,256)]

def string2hex(s):
    return "".join([byte_list[ord(i)-1] for i in s])




#  Keyed Permutations

'''
What is the mathematical term for a one-to-one correspondence? 

Solution: bijection
'''

# Resisting Bruteforce
'''
What is the name for the best single-key attack against AES?

biclique
'''

# Structure of AES

def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    res = ""

    for i in range(len(matrix)):
        res += "".join(chr(a) for a in matrix[i])

    return res

# matrix = [
#     [99, 114, 121, 112],
#     [116, 111, 123, 105],
#     [110, 109, 97, 116],
#     [114, 105, 120, 125],
# ]

# print(matrix2bytes(matrix))

# Round Keys
# state = [
#     [206, 243, 61, 34],
#     [171, 11, 93, 31],
#     [16, 200, 91, 108],
#     [150, 3, 194, 51],
# ]

# round_key = [
#     [173, 129, 68, 82],
#     [223, 100, 38, 109],
#     [32, 189, 53, 8],
#     [253, 48, 187, 78],
# ]

def add_round_key(s, k):
    assert len(s)==len(k), "States and Key are not same size!!!"
    key = []
    for i in range(len(s)):
        key.append([ bytes_to_long(xor(s[i][a], k[i][a])) for a in range(len(s[i]))])
    return key

# cur_key = (add_round_key(state, round_key))
# print(matrix2bytes(cur_key))


# Confusion through Substitution
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

# inv_s_box = (
#     0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
#     0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
#     0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
#     0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
#     0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
#     0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
#     0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
#     0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
#     0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
#     0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
#     0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
#     0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
#     0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
#     0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
#     0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
#     0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
# )

# state = [
#     [251, 64, 182, 81],
#     [146, 168, 33, 80],
#     [199, 159, 195, 24],
#     [64, 80, 182, 255],
# ]



def sub_bytes(s, sbox=s_box):
    hexstate = []
    key = []
    for i in range(len(s)):
        hexstate += [[hex(a)[2:] for a in s[i]]]
        print(hexstate)
        key += [[
            sbox[ 16*int("0x0"+hexstate[i][a][0],16) + int("0x0"+hexstate[i][a][1],16) ] if len(hexstate[i][a]) == 2
            else sbox[ int("0x0"+hexstate[i][a][0],16) ]
            for a in range(len(hexstate[i]))
            ]]
    return key


# key = (sub_bytes(state, sbox=inv_s_box))
# print(matrix2bytes(key))

# Diffusion through Permutation

def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]
    return s


def inv_shift_rows(s):
    s[1][1], s[2][1], s[3][1], s[0][1] = s[0][1], s[1][1], s[2][1], s[3][1]
    s[2][2], s[3][2], s[0][2], s[1][2] = s[0][2], s[1][2], s[2][2], s[3][2]
    s[3][3], s[0][3], s[1][3], s[2][3] = s[0][3], s[1][3], s[2][3], s[3][3]
    return s

# learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])
    return s


def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    s = mix_columns(s)
    return s


# state = [
#     [108, 106, 71, 86],
#     [96, 62, 38, 72],
#     [42, 184, 92, 209],
#     [94, 79, 8, 54],
# ]

'''
We've provided code to perform MixColumns and the forward ShiftRows operation. After implementing inv_shift_rows, take the state, run inv_mix_columns on it, then inv_shift_rows, convert to bytes and you will have your flag.
'''

# key = (inv_shift_rows(inv_mix_columns(state)))
# print(matrix2bytes(key))


# Bringing It All Together

# file aes_decrypt.py

#  Modes of Operation Starter

# r = requests.get('https://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
# encrypt_flag = (r.json()['ciphertext'])
# flag_in_hex = requests.get(f'https://aes.cryptohack.org/block_cipher_starter/decrypt/{encrypt_flag}/')
# flag = flag_in_hex.json()['plaintext']
# print(bytes.fromhex(flag).decode("utf-8"))

# Passwords as Keys

# def decrypt(wordslist, ciphertext):
#     ciphertext = bytes.fromhex(ciphertext)
#     for w in wordslist:
#         key = bytes.fromhex(hashlib.md5(w.encode()).hexdigest())
#         cipher = AES.new(key, AES.MODE_ECB)
#         try:
#             decrypted = cipher.decrypt(ciphertext)
#             f.write(f"{str(decrypted)}\n")
#         except ValueError as e:
#             return {"error": str(e)}


# def getFlag(wordslist, encrypt_flag):
#     for w in wordslist:
#         key = (hashlib.md5(w.encode()).hexdigest())
#         flag_in_hex = requests.get(f'https://aes.cryptohack.org/passwords_as_keys/decrypt/{encrypt_flag}/{key}/')
#         f.write(f"{(bytes.fromhex(flag_in_hex.json()['plaintext']))}\n")


# words = []
# with open("/usr/share/dict/words") as f:
#     words = [w.strip() for w in f.readlines()]
        
# # r = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
# # r = c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66
# encrypt_flag = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'


# space = int(len(words)/8)
# breakpoint_index = [space-1, 2*space-1, 3*space-1, 4*space-1, 5*space-1, 6*space-1, 7*space-1] 
# f = open("course3_symmetric/Password_as_key.txt", "a")
# t1 = threading.Thread(target=decrypt, args=(words[0:breakpoint_index[0]],encrypt_flag))
# t2 = threading.Thread(target=decrypt, args=(words[breakpoint_index[0]:breakpoint_index[1]],encrypt_flag))
# t3 = threading.Thread(target=decrypt, args=(words[breakpoint_index[1]:breakpoint_index[2]],encrypt_flag))
# t4 = threading.Thread(target=decrypt, args=(words[breakpoint_index[2]:breakpoint_index[3]],encrypt_flag))
# t5 = threading.Thread(target=decrypt, args=(words[breakpoint_index[3]:breakpoint_index[4]],encrypt_flag))
# t6 = threading.Thread(target=decrypt, args=(words[breakpoint_index[4]:breakpoint_index[5]],encrypt_flag))
# t7 = threading.Thread(target=decrypt, args=(words[breakpoint_index[5]:breakpoint_index[6]],encrypt_flag))
# t8 = threading.Thread(target=decrypt, args=(words[breakpoint_index[6]:],encrypt_flag))

# # starting thread
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()


# f.close()



# ECB Oracle

# explain in course3_symmetric/ECB_Oracle.txt

# def get_pad(length):
#     return byte_list[15 - length]

# def get_cipher(s):
#     r = requests.get(f'https://aes.cryptohack.org/ecb_oracle/encrypt/{s}/')
#     return r.json()['ciphertext']

# print(byte_list)

# res = ""
# res = "63627d"

# res = '6e3675316e355f683437335f3363627d'
# # for i in range(len(res)//2+1,26):

# #     payload = "aa" * (7+i) 
# #     if(i>=16): valid_last_block = get_cipher(payload)[-64:-32]
# #     else: 
# #         valid_last_block = get_cipher(payload)[-32:]

# #     for item in byte_list:
# #         if(i<=16):
# #             plain = item + res +get_pad(i)*(16-i)
# #         else:
# #             plain = item + res[:-(i-16)*2]
# #         print(plain)
# #         last_block = get_cipher(plain)[:32]
# #         if valid_last_block == last_block:
# #             print(f'Found: {item}')
# #             res = item+res
# #             break

# res = "70336e3675316e355f683437335f3363627d"

# print(bytes.fromhex(res))


# ECB CBC WTF

# encrypt by CBC:
'''
input:
    plaintext = t_1 t_2 ... t_n
    key: key
    initialization vector
output: ciphertext = c_1 c_2 ... c_n
encryption:
    c_1 = encrypt (t_1 xor init. vector) by key
    c_2 = encrypt (t_2 xor c_1) by key
    c_3 = encrypt (t_3 xor c_2) by key
    ...
    c_n = encrypt (t_n xor c_(n-1) ) by key

#### DECRYPTION IN CBC MODE:
input:
    ciphertext = c_1 c_2 ... c_n
    key: key
output: plaintext = t_1 t_2 ... t_n
decryption:
    t_1 = decrypt (c_1 xor init. vector) by key
    t_2 = decrypt (c_2 xor c_1) by key
    t_3 = decrypt (c_3 xor c_2) by key
    ...
    t_n = decrypt (c_n xor c_(n-1) ) by key
'''
# decrypt by ECB:
''' 
input:
    ciphertext = c_1 c_2 ... c_n
    key: key
output: plaintext = t_1 t_2 ... t_n
decryption:
    t_1 = decrypt (c_1) by key
    t_2 = decrypt (c_2) by key
    t_3 = decrypt (c_3) by key
    ...
    t_n = decrypt (c_n) by key
'''

'''
XOR: 
    a XOR b = c -> c xor b = a and c xor a = b

As we can see, CBC & ECB decryptions diff is just XOR.

flow in this challenge:
    t ------CBC encrypt------> [init.vec,c] ---------ECB decrypt--------> [block,t']

    if we want flag: 
    t ------CBC encrypt------> [init.vec,c] ---------CBC decrypt--------> [block,t]

    We have: [block,t'] xor [init.vec,c] = [block,t], we just dont care the block.
    -> flag = [block,t'] xor c
'''
# re = requests.get("https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/")
# full_c = re.json()["ciphertext"]
# c = full_c[32:]    # init. vec is 16 bytes

# re = requests.get(f"https://aes.cryptohack.org/ecbcbcwtf/decrypt/{c}/")
# t = re.json()["plaintext"]
# flag = xor(bytes.fromhex(full_c), bytes.fromhex(t))


# print(flag)



# Flipping Cookie 

'''
Get cookie: 
248cd757f0488dccfa0bd08655545aa8 -> IV

0b32f8dc246f167f0eca88ebc21d3057 -> admin=False;expi
d2b6cd5e2359f8863d945bfe9f90d832 -> dont care
'''

'''
we need to use IV to 
t1 = c1 xor IV
c1 new = t1 xor IV new

IV new = IV xor [admin=False;expi] xor [admin=True;00000]
-> c1_new = encrypt(admin=False;expi)[32:64] xor IV new
'''

# re = requests.get("https://aes.cryptohack.org/flipping_cookie/get_cookie/")

# cipher = re.json()["cookie"]
# iv = cipher[:32]
# cookie = cipher[32:]

# iv_new = xor(bytes.fromhex(string2hex("admin=True;00000")), bytes.fromhex(string2hex("admin=False;expi")), bytes.fromhex(iv)).hex()

# print(iv_new)

# re = requests.get(f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv_new}/")
# print(re.json()["flag"])


# Symmetry

''' 
XOR: 
    a XOR b = c -> c xor b = a and c xor a = b
'''

# re = requests.get("https://aes.cryptohack.org/symmetry/encrypt_flag/")
# cipher = re.json()["ciphertext"]
# iv = cipher[:32]
# encrypt_flag = cipher[32:]

# re = requests.get(f"https://aes.cryptohack.org/symmetry/encrypt/{encrypt_flag}/{iv}/")
# flag = re.json()["ciphertext"]
# print(bytes.fromhex(flag))



# Bean Counter

''' 
PNG file exploit: https://www.nayuki.io/page/png-file-chunk-inspector
First 16 bytes of PNG file are unchanged
'''

# re = requests.get("https://aes.cryptohack.org/bean_counter/encrypt/")

# encrypt_flag = (re.json()["encrypted"])

# first_16byte = encrypt_flag[:32]

# # 89 50 4e 47 0d 0a 1a 0a
# # 00 00 00 0d 49 48 44 52

# flag_0 = "89504e470d0a1a0a0000000d49484452"

# nonce = xor(bytes.fromhex(flag_0),bytes.fromhex(first_16byte))

# res = ""
# res += flag_0

# for i in range(1,len(encrypt_flag)//32):
#     res += xor(nonce,bytes.fromhex(encrypt_flag[32*i:32*i+32])).hex()


# with open('course3_symmetric/bean_counter.png', 'wb') as fd:
#     fd.write(bytes.fromhex(res))


# Lazy CBC

'''
plain: m0m1m2
encrypt:   
    m0 ^ key-> c0
    c0 ^ m1 -> c1
    c1 ^ m2 -> c2
    ...

'''


# a0 = "aaaaaaaaaaaaaaaa0000000000000000aaaaaaaaaaaaaaaa"
# re = requests.get(f"https://aes.cryptohack.org/lazy_cbc/encrypt/{string2hex(a0)}/")

# encrypted = re.json()["ciphertext"]

# # plain:
#     # Key = dec(c0) ^ aaaaaaaaaaaaaaaa
#     # 
#     # p0 = dec(c0)^key
#     # p1 = dec(c1)^c0
#     # p2 = dec(c2)^c1

# '''
#     if c1 == 0 -> p2 = dec(c2)^0 = dec(c2)
#     and if c0 = c2 -> p2 = dec(c0)

#     then p0 ^ p2 = dec(c0) ^ key ^ dec(c0) = key
#     (")> 
# '''

# c0 = encrypted[:32] 
# c1 = ("0"*32)

# ciphertext_injection = c0+c1+c0
# print(ciphertext_injection)
# re = requests.get(f"https://aes.cryptohack.org/lazy_cbc/receive/{ciphertext_injection}/")
# encrypted = re.json()["error"].split()[2]

# p0 = bytes.fromhex(encrypted[:32])
# p2 = bytes.fromhex(encrypted[-32:])

# key = xor(p0,p2).hex()
# re = requests.get(f"https://aes.cryptohack.org/lazy_cbc/get_flag/{key}/")
# print(bytes.fromhex(re.json()["plaintext"]))


# Triple DES

'''
https://security.stackexchange.com/questions/6510/is-tdea-tripledes-invulnerable-to-the-weak-keys-of-des
"A weak key for a block cipher is a key such that encryption and decryption turn out to be the same function."
'''
key = "0000000000000000ffffffffffffffff0000000000000000"

# re = requests.get(f"https://aes.cryptohack.org/triple_des/encrypt_flag/{key}/")
# cipher = re.json()['ciphertext']

# re = requests.get(f"https://aes.cryptohack.org/triple_des/encrypt/{key}/{cipher}/")
# plain = bytes.fromhex(re.json()['ciphertext'])
# print(plain)

# CTRIME
print(bytes.fromhex(string2hex("crypto{")))

a = (zlib.compress(bytes.fromhex(string2hex("crypto{"))))

print(zlib.decompress(a))