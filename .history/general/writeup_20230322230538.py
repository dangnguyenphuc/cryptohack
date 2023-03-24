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
# print(gcd(273246787654,65537))

# mod inverting
res = [x for x in range(13) if int((13*x+1)%3) == 0 and int((13*x+1)/3) < 13]
print(int((13*res[0]+1)/3))

# Quadratic Residues: square root modulo
'''
This feels good, but now let's think about the square root of 18. From the above, we know we need to find some integer a such that a2 = 18

Your first idea might be to start with a = 1 and loop to a = p-1. In this discussion p isn't too large and we can quickly look.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a ∈ Fp* you never find an a such that a2 = 18.
'''

p = 29
ints = [14, 6, 11] 
res = []
for items in ints:
    for i in range(29):
        if i*i % p == items: 
            res += [items]
            break

print(res)