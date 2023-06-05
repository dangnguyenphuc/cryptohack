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
    
    # print(old_s, bezout_t)
    # print("GCD: " + str(old_r))
    return (old_s,bezout_t,old_r)

def inv(number1, number2):
    if number1 < 0: number1 += number2
    (old_s,bezout_t,old_r) = extended_gcd(number1, number2)
    if old_r > 1: return None
    if old_s < 0: old_s+=number2
    return old_s



# ------------------------------------------------------------------------------------------------------------
# Point Negation
# E: Y2 = X3 + 497 X + 1768, p: 9739 

'''
https://trustica.cz/2018/03/08/elliptic-curves-point-negation/
−Py mod p = p−Py
'''
# p = 9739
# A = (8045,6936)
# A_neg = (A[0], p-A[1])
# print(A_neg)
# (8045, 2803)
# ------------------------------------------------------------------------------------------------------------
#  Point Addition
'''
Algorithm for the addition of two points: P + Q

(a) If P = O, then P + Q = Q.
(b) Otherwise, if Q = O, then P + Q = P.
(c) Otherwise, write P = (x1, y1) and Q = (x2, y2).
(d) If x1 = x2 and y1 = −y2, then P + Q = O.
(e) Otherwise:
  (e1) if P ≠ Q: λ = (y2 - y1) / (x2 - x1)
  (e2) if P = Q: λ = (3x12 + a) / 2y1
(f) x3 = λ2 − x1 − x2,     y3 = λ(x1 −x3) − y1
(g) P + Q = (x3, y3) 
'''
A = 497
B = 1768
MOD = 9739

def pointAddition(p, q, a = A, b = B, mod = MOD):
    if p == (0,0): return q
    if q == (0,0): return p
    if p[0] == q[0] and ((p[1] + q[1])%mod == 0): return (0,0)
    if p != q: lam = (q[1]-p[1])*inv(q[0]-p[0], mod)%mod 
    else: lam = (3*(p[0]**2) + a)*inv(2*p[1], mod)%mod
    
    x3 = (lam**2 - p[0] - q[0])%mod
    y3 = (lam*(p[0]-x3) - p[1])%mod
    return (x3,y3)

# P = (493, 5564)
# Q = (1539, 4742) 
# R = (4403,5202)

# res = pointAddition(pointAddition(pointAddition(P,P),Q),R)
# print(res)

# ------------------------------------------------------------------------------------------------------------
# Scalar Multiplication

def scalarMultiplication(n, p, a = A, b = B, mod = MOD):
    q = p
    res = (0,0)
    loop_index = n
    while loop_index > 0:
        if loop_index % 2 == 1:
            res = pointAddition(res, q)
            loop_index -= 1
            
        q = pointAddition(q, q, a, b, mod)
        loop_index = loop_index//2
    return res

# P = (2339, 2213)
# n = 7863
# print(scalarMultiplication(n, P))

# ------------------------------------------------------------------------------------------------------------
#  Curves and Logs
'''txt
Alice generates a secret random integer nA and calculates QA = nAG

Bob generates a secret random integer nB and calculates QB = nBG

Alice sends Bob QA, and Bob sends Alice QB. Due to the hardness of ECDLP, an onlooker Eve is unable to calculate nA/B in reasonable time.

Alice then calculates nAQB, and Bob calculates nBQA.

Due to the associativity of scalar multiplication, S = nAQB = nBQA.

Alice and Bob can use S as their shared secret.
'''
import hashlib


QA = (815, 3190)
nB = 1829

res = (scalarMultiplication(nB, QA))

hashObj = hashlib.sha1(bytes(str(res[0]),"ascii"))
print(hashObj.hexdigest())