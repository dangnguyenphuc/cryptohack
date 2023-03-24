#!/bin/python3 -f

# general/gcd
def gcd(number1, number2):
    if(number1 == 0): return number2
    return gcd(number2%number1, number1)

# a = 66528
# b = 52920
# print(gcd(a, b))


# extended Euclide
def extended_gcd(a,b):
    s = 0
    old_s = 1
    r = b
    old_r = a

    bezout_t = None

    q = None
    while r!= 0:
        q = int(old_r / r)
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s - q*s

    if b!=0 :
        bezout_t = int((old_r - old_s*a) / b)
    else: 
        bezout_t = 0
    
    print(old_s, bezout_t)
    print("GCD: " + str(old_r))


# mod 1
# p = 8146798528947
# q = 17
# print(p%q)



# mod 2
print(gcd(273246787654,65537))