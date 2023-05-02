#!/usr/bin/env python3

import telnetlib
import json
from random import randint


HOST = "socket.cryptohack.org"
PORT = 13385



tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def generate_basis(n):
    basis = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if basis[i]:
            basis[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if basis[i]]

def miller_rabin(n, b):
    """
    Miller Rabin test testing over all
    prime basis < b
    """
    basis = generate_basis(b)
    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for b in basis:
        x = pow(b, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

lower = 2**600 + 1
upper = 2**900 - 1

def gen_prime():
    global lower, upper
    found = False
    while not(found):
        res = randint(lower, upper)
        if res % 2 == 0: res += 1
        found = miller_rabin(res, 64)
    return res

def lengendre(a,p):
    return pow(a,(p-1)//2,p)


def tonelli_shanks(a, p):
    assert lengendre(a, p) == 1
    q = p- 1
    s = 0
    while q%2 == 0:
        s = s+1    
        q//=2
    
    if s == 1: return pow(a,(p-1)//4,p)     #p = 3 mod 4
    
    #find z
    for z in range(2,p):
        if p-1 == lengendre(z, p): break

    #assign
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q+1)//2, p)

    while (t-1)%p != 0:
        t2 = (t*t)%p
        for i in range(1,m):
            if (t2-1)%p == 0:
                break
            t2 = (t2*t2)%p
        b = pow(c, 1 << (m-i-1), p)
        r = (r*b)%p
        c = (b*b)%p
        t = (t*c)%p
        m = i   
    return r

def quadratic_residues(p):
    """Returns a list of all quadratic residues modulo p."""
    residues = []
    for a in range(2, p):
        root = tonelli_shanks(a, p)
        if root is not None:
            residues.append(root)
            residues.append(p - root)
    return residues

def primitive_root(p):
    """Returns the smallest primitive root modulo p."""
    if p == 2:
        return 1
    elif p == 3:
        return 2
    elif p == 5:
        return 2

    # Factorize p-1 into q * 2^k
    q, k = p - 1, 0
    while q % 2 == 0:
        k += 1
        q //= 2

    # Find a primitive root modulo p
    for g in range(2, p):
        if pow(g, q, p) == 1:
            continue
        for j in range(k):
            if pow(g, q * pow(2, j), p) == 1:
                break
        else:
            return g

    raise Exception("Failed to find a primitive root modulo p")
def first_quadratic_residue(p):
    """Returns the first quadratic residue modulo p."""
    g = primitive_root(p)
    return pow(g, 2, p)


a = gen_prime()
print(readline())

request = {
    "prime": a,
    "base": first_quadratic_residue(a)
}
json_send(request)

response = json_recv()

print(response)
