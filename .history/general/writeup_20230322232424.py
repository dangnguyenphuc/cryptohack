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

def mulMod(number1,number2, number3):
    return (number1*number2)%number3

def powMod(number1,number2, number3):
    assert number2 >= 0 
    res = 1
    while number2 > 0:
        if(number2 & 1 == 1): res = mulMod(res, number1, number3)
        number1 = mulMod(number1, number1, number3)
        number2 = number2 >> 1
    return res
# mod 1
# p = 8146798528947
# q = 17
# print(p%q)



# mod 2
# print(gcd(273246787654,65537))

# mod inverting
# res = [x for x in range(13) if int((13*x+1)%3) == 0 and int((13*x+1)/3) < 13]
# print(int((13*res[0]+1)/3))

# Quadratic Residues: square root modulo
'''
This feels good, but now let's think about the square root of 18. From the above, we know we need to find some integer a such that a2 = 18

Your first idea might be to start with a = 1 and loop to a = p-1. In this discussion p isn't too large and we can quickly look.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a ∈ Fp* you never find an a such that a2 = 18.
'''

# p = 29
# ints = [14, 6, 11] 
# res = []
# for items in ints:
#     for i in range(29):
#         if i*i % p == items: 
#             res += [items]
#             print(i)
#             break

# print(res)


# Legendre Symbol:
'''
Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue 
'''

'''
So what's the trick? The Legendre Symbol gives an efficient way to determine whether an integer is a quadratic residue modulo an odd prime p.

Legendre's Symbol: (a / p) ≡ a(p-1)/2 mod p obeys:

(a / p) = 1 if a is a quadratic residue and a ≢ 0 mod p
(a / p) = -1 if a is a quadratic non-residue mod p
(a / p) = 0 if a ≡ 0 mod p

Which means given any integer a, calculating pow(a,(p-1)//2,p) is enough to determine if a is a quadratic residue.
'''

print(powMod(5, 2, 313))
