from pwn import *
from Crypto.Util.number import *
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
    for i in range(len(state)):
        key.append([ bytes_to_long(xor(state[i][a], round_key[i][a])) for a in range(len(state[i]))])
    return key


# cur_key = (add_round_key(state, round_key))
# print(matrix2bytes(cur_key))