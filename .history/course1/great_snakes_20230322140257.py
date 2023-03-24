#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import long_to_bytes
from pwn import *
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

cipher = "label"
print(chr(pwn.xor(ord(cipher),13) for o in label))