# RSA Starter 1

# SageMath

# print(pow(101,17, 22663))

# RSA Starter 2

# SageMath

# print(pow(12, 65537,17*23))


# RSA Starter 3

# p = 857504083339712752489993810777

# q = 1029224947942998075080348647219

# print((p-1)*(q-1))


# RSA Starter 4

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
    return (old_s,bezout_t,old_r)

def inv(number1, number2):
    (old_s,bezout_t,old_r) = extended_gcd(number1, number2)
    if old_r > 1: return None
    if old_s < 0: old_s+=number2
    return old_s

# p = 857504083339712752489993810777

# q = 1029224947942998075080348647219

# e = 65537

# phi = (p-1)*(q-1)
# print(inv(e,phi))
# 121832886702415731577073962957377780195510499965398469843281



# RSA Starter 5

# #======= Public K
# N = 882564595536224140639625987659416029426239230804614613279163

# e = 65537
# #======= 

# ######## Private K
# d = 121832886702415731577073962957377780195510499965398469843281

# # message
# c = 77578995801157823671636298847186723593814843845525223303932


# print(pow(c, d,N))



# RSA Starter 6

