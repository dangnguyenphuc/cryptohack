#!/bin/python3 -f

# general/gcd
def gcd(number1, number2):
    if(number1 == 0): return number2
    return gcd(number2%number1, number1)

a = 66528
b = 52920
print(gcd(a, b))


# extended Euclide
def extended_gcd(a,b):
    s = 0
    old_s = 1
    r = b
    old_r = a