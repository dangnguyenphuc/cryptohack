#!/bin/python3 -f


def gcd(number1, number2):
    if(number1 == 0): return number2
    return gcd(number2%number1, number1)

print(gcd(32, 32*3131))