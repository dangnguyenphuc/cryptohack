import base64 #chal hex->byte->b64
from Crypto.Util.number import *
import pwn
from var_dump import var_dump
from binascii import unhexlify
two = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
three = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" #hex->byte->b64
# print(bytes.fromhex(two))
# byte = bytes.fromhex(three);
# print(base64.b64encode(byte))
four = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# print(long_to_bytes(four))
five = "label"
# print(pwn.xor(five,13))
six_1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313" #KEY1
six_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e" #KEY1^KEY2
six_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1" #KEY2^KEY3
six_4 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" #FLAG^KEY1^KEY2^KEY3

six_1=bytes.fromhex(six_1)
six_2=bytes.fromhex(six_2)
six_3=bytes.fromhex(six_3)
six_4=bytes.fromhex(six_4)

# print(pwn.xor(six_4,six_3,six_1))

seven = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
# str_ord = [o for o in bytes.fromhex(seven)]
# for i in range(256):
#     pos_flag_odr = [i ^ o for o in str_ord]
#     pos_flag = "".join(chr(o) for o in pos_flag_odr)
#     if(pos_flag.startswith("crypto")):
#         print(pos_flag)
#         break

#EIGHT
def brute(input, key):
    out = b''
    for b1,b2 in zip(input,key):
        out+=bytes([b1^b2])
    return out.decode('utf-8')

#A^B=C => C^B=A
eight = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = unhexlify(eight)
#res = crypto{

# key = brute(cipher[:7], "crypto{".encode())
# key = (key+'y').encode()
#
# key += key*int((len(cipher)-len(key))/len(key))
# key += key[:(len(cipher)-len(key))%len(key)]
#
# flag = brute(cipher, key)
# print(flag)

#



