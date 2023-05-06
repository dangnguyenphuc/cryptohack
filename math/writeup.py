######

## Lattices ##

######

import math
from math import *


def inner_dot(u, v):
    res = 0
    for i in range(len(u)):
        res += u[i]*v[i]
    return res

def add(u, v):
    res = []
    for i in range(len(u)):
        res += [u[i]+v[i]]
    return res

def sub(u, v):
    res = []
    for i in range(len(u)):
        res += [u[i]-v[i]]
    return res

def mul(u, number):
    return [u[i]*number for i in range(len(u))]

def Gram_Schmidt(v): 
    u = []
    u += [v[0]]


    for i in range(1,len(v)):
        proj_ij = []
        for j in range(0,i):
            a = v[i].dot_product(u[j]) / u[j].dot_product(u[j]) 
            proj_ij += [a]
        sum_proj_j = vector([0]*len(v))
        for j in range(0,i):
            sum_proj_j += proj_ij[j]*u[j]


        u += [v[i] - sum_proj_j]
    return u

def Gram_Schmidt_mi(v, u, i, j):
    return v[i].dot_product(u[j])/u[j].dot_product(u[j])

def LLL(v, beta=1):
    res = v
    b = Gram_Schmidt(res)
    k = 1
    while k < len(res):

        for j in reversed(range(0,k)):
            mi = Gram_Schmidt_mi(res, b, k, j)
            if abs(mi) > 1/2:
                res[k] = res[k] - floor(mi)*res[j]
                b = Gram_Schmidt(res)
        
        if res[k].dot_product(res[k]) > (beta-Gram_Schmidt_mi(res, b, k, k-1)**2)*res[k-1].dot_product(res[k-1]):
            k = k + 1
        else: 
            res[k], res[k-1] = res[k-1], res[k]
            b = Gram_Schmidt(res)
            k = max(k-1, 1)
    return res


# ------------------------------------------------------------------------------------------------------------
# Vectors

# v = [2,6,3]
# w = [1,0,0]
# u = [7,7,2]
# res = inner_dot(mul(sub(mul(v, 2),w), 3), mul(u, 2))
# print(res)



# ------------------------------------------------------------------------------------------------------------
# Size and Basis
# v = [4, 6, 2, 5]

# res = sqrt(inner_dot(v, v))

# print(int(res))


# ------------------------------------------------------------------------------------------------------------
# Gram Schmidt


# Sagemath:
# v = [vector([4,1,3,-1]),vector([2,1,-3,4]),vector([1,0,-2,7]),vector([6, 2, 9, -5])]

# print(Gram_Schmidt(v))


# ------------------------------------------------------------------------------------------------------------
# What's a Lattice?

# Sagemath:

# m = matrix(QQ, [[6, 2, -3],[5, 1, 4],[2, 7, 1]])
# print(m.det())

# ------------------------------------------------------------------------------------------------------------
# Gaussian Reduction

v = [vector([846835985, 9834798552]), vector([87502093, 123094980])]


'''
LLL Algorithm:
INPUT
    a lattice basis b1, b2, ..., bn in Zm
    a parameter δ with 1/4 < δ < 1, most commonly δ = 3/4



PROCEDURE
    B* <- GramSchmidt({b1, ..., bn}) = {b1*, ..., bn*};  and do not normalize
    μi,j <- InnerProduct(bi, bj*)/InnerProduct(bj*, bj*);   using the most current values of bi and bj*
    k <- 2;
    while k <= n do
        for j from k−1 to 1 do
            if |μk,j| > 1/2 then
                bk <- bk − ⌊μk,j⌉bj;
               Update B* and the related μi,j's as needed.
               (The naive method is to recompute B* whenever bi changes:
                B* <- GramSchmidt({b1, ..., bn}) = {b1*, ..., bn*})
            end if
        end for
        if InnerProduct(bk*, bk*) > (δ − μ2k,k−1) InnerProduct(bk−1*, bk−1*) then
            k <- k + 1;
        else
            Swap bk and  bk−1;
            Update B* and the related μi,j's as needed.
            k <- max(k−1, 2);
        end if
    end while
    return B the LLL reduced basis of {b1, ..., bn}
OUTPUT
    the reduced basis b1, b2, ..., bn in Zm
'''

# ------------------------------------------------------------------------------------------------------------
#  Find the Lattice




