######

## Lattices ##

######

import math
from math import sqrt

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





# Vectors

# v = [2,6,3]
# w = [1,0,0]
# u = [7,7,2]
# res = inner_dot(mul(sub(mul(v, 2),w), 3), mul(u, 2))
# print(res)





# Size and Basis
# v = [4, 6, 2, 5]

# res = sqrt(inner_dot(v, v))

# print(int(res))



# Gram Schmidt


# Sagemath:
# v = [vector([4,1,3,-1]),vector([2,1,-3,4]),vector([1,0,-2,7]),vector([6, 2, 9, -5])]

# u = []
# u += [v[0]]


# for i in range(1,len(v)):
#     proj_ij = []
#     for j in range(0,i):
#         a = v[i].dot_product(u[j]) / u[j].dot_product(u[j]) 
#         proj_ij += [a]
#     sum_proj_j = vector([0,0,0,0])
#     for j in range(0,i):
#         sum_proj_j += proj_ij[j]*u[j]


#     u += [v[i] - sum_proj_j]
# print(u)



# What's a Lattice?

# Sagemath:

# m = matrix(QQ, [[6, 2, -3],[5, 1, 4],[2, 7, 1]])
# print(m.det())


# Gaussian Reduction

def G_reduction(u, v):