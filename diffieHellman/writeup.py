from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import telnetlib
import json
from pwn import *
from Crypto.Util.number import *

HOST = "socket.cryptohack.org"



def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    #===============
    # Parameter Injection
    # if is_pkcs7_padded(plaintext):
    #     return unpad(plaintext, 16).decode('ascii')
    # else:
    #     return plaintext.decode('ascii')

    # ==============
    # Export-grade
    return plaintext


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 1
# p = 991
# g = 209
# print(inv(g, p))


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 2
'''We just need to detect Cycle :))'''
# p = 28151

# found = False
# for i in range(2,p):
#     found = True
#     for j in range(2,p):
#         a = pow(i, j, p)
#         if a == i:
#             found = False
#             break
#     if found:
#         print("Found: " + str(i))


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 3

# SageMath :))


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 4
# g = 2

# p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

# b = 12019233252903990344598522535774963020395770409445296724034378433497976840167805970589960962221948290951873387728102115996831454482299243226839490999713763440412177965861508773420532266484619126710566414914227560103715336696193210379850575047730388378348266180934946139100479831339835896583443691529372703954589071507717917136906770122077739814262298488662138085608736103418601750861698417340264213867753834679359191427098195887112064503104510489610448294420720

# A = 70249943217595468278554541264975482909289174351516133994495821400710625291840101960595720462672604202133493023241393916394629829526272643847352371534839862030410331485087487331809285533195024369287293217083414424096866925845838641840923193480821332056735592483730921055532222505605661664236182285229504265881752580410194731633895345823963910901731715743835775619780738974844840425579683385344491015955892106904647602049559477279345982530488299847663103078045601

'''
Bod share secret: A^b mod p
Alice __________: B^a mod p 
'''

# print(pow(A,b,p))


# ------------------------------------------------------------------------------------------------------------
#  Diffie-Hellman Starter 5
# recv = {'iv': '737561146ff8194f45290f5766ed6aba', 'encrypted_flag': '39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c'}

# g = 2

# p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

# A = 112218739139542908880564359534373424013016249772931962692237907571990334483528877513809272625610512061159061737608547288558662879685086684299624481742865016924065000555267977830144740364467977206555914781236397216033805882207640219686011643468275165718132888489024688846101943642459655423609111976363316080620471928236879737944217503462265615774774318986375878440978819238346077908864116156831874695817477772477121232820827728424890845769152726027520772901423784

# b = 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944

# B = 1241972460522075344783337556660700537760331108332735677863862813666578639518899293226399921252049655031563612905395145236854443334774555982204857895716383215705498970395379526698761468932147200650513626028263449605755661189525521343142979265044068409405667549241125597387173006460145379759986272191990675988873894208956851773331039747840312455221354589910726982819203421992729738296452820365553759182547255998984882158393688119629609067647494762616719047466973581

# d = pow(A,b, p)
# d = 1547922466740669851136899009270554812141325611574971428561894811681012510829813498961168330963719034921137405736161582760628870855358912091728546731744381382987669929718448423076919613463237884695314172139247244360699127770351428964026451292014069829877638774839374984158095336977179683450837507011404610904412301992397725594661037513152497857482717626617522302677408930050472100106931529654955968569601928777990379536458959945351084885704041496571582522945310187
# print(decrypt_flag(d, recv['iv'], recv["encrypted_flag"]))

# ------------------------------------------------------------------------------------------------------------
#  Parameter Injection

"""
https://cryptopals.com/sets/5/challenges/34

Normal traffic:

A->B
Send "p", "g", "A"
B->A
Send "B"
A->B
Send AES-CBC(SHA1(s)[0:16], iv=random(16), msg) + iv
B->A
Send AES-CBC(SHA1(s)[0:16], iv=random(16), A's msg) + iv

Injected traffic:

A->M
Send "p", "g", "A"
M->B
Send "p", "g", "p"
B->M
Send "B"
M->A
Send "p"
A->M
Send AES-CBC(SHA1(s)[0:16], iv=random(16), msg) + iv
M->B
Relay that to B
B->M
Send AES-CBC(SHA1(s)[0:16], iv=random(16), A's msg) + iv
M->A
Relay that to A

Result

A: A = pow(g, a, p)
B: B = pow(g, p, p)
A: k = pow(p, a, p)
B: k = pow(p, b, p)

So k = 0
"""
# PORT = 13371 # Parameter Injection

# def injection():
#     s = remote(HOST, PORT)
#     try:
#         recv = s.readuntil(": ")
#         A_message = json.loads(s.readline().strip().decode())
#         print(A_message)
        
#         p = int(A_message['p'],16)
#         g = int(A_message['g'],16)
#         A = int(A_message['A'],16)
        
#         # print(p)
#         # print(g)
#         # print(A)

#         B_send = json.dumps({
#             "p": hex(p),
#             "g": hex(g),
#             "A": hex(p)
#         })

#         # 'b{"Send to Bob: Intercepted from Bob:"}'
#         s.sendlineafter(": ", B_send)
#         recv = s.readuntil(": ")
#         B_message = json.loads(s.readline().strip().decode())

#         B = int(B_message["B"], 16)
#         print(B)
        
#         A_send = json.dumps({
#             "B": hex(p),
#         })
#         # 'b{"Send to Alice: Intercepted from Alice:"}'
#         s.sendlineafter(": ", A_send)
#         recv = s.readuntil(": ")
#         A_message = json.loads(s.readline().strip().decode())
        
#         print(A_message)
#         # iv = int(A_message["iv"], 16)
#         # encrypted_flag = int(A_message["encrypted_flag"], 16)

#         print(decrypt_flag(0, A_message["iv"],A_message["encrypted_flag"]))

#     finally:
#         s.close()
#     return

# injection()


# ------------------------------------------------------------------------------------------------------------
# Export-grade
PORT = 13379


def secret_by_SageMath(p, g, A):
    R = GF(p)
    g = R(g)
    A = R(A)   
    return A.log(g)

def ruin():
    s = remote(HOST, PORT)
    try:
        recv = s.readuntil(": ")

        message = json.loads(s.readline().strip().decode())
        print(message)

        supported = message["supported"]

        message = json.dumps(
            {
                "supported": [supported[-1]]
            })

        s.sendlineafter(": ", message.encode())
        recv = s.readline()

        message = json.dumps(
            {
                "chosen": supported[-1]
            })
        s.sendlineafter(": ", message.encode())
        s.readuntil(": ")
        message = json.loads(s.readline().strip().decode())
        print(message)

        p = int(message["p"],16)
        g = int(message["g"],16)
        A = int(message["A"],16)


        # p = 16007670376277647657
        # g = 2
        # A = 12572908971821654424

        # a = secret_by_SageMath(p, g, A)
        # a = 2560063736234422204

        message = json.dumps(
            {
                "p": hex(p),
                "g": hex(g),
                "A": hex(p)
            })
        s.sendlineafter(": ", message.encode())
        message = json.loads(s.readline().strip().decode())
        print(message)
        B = int(message["B"], 16)

        # B = 7505388001506019908
        message = json.dumps(
            {
                "B": hex(B)
            })
        s.sendlineafter(": ", message.encode())
        message = json.loads(s.readline().strip().decode())
        
        iv = message["iv"]
        encrypted_flag = message["encrypted_flag"]

        # iv = "3e2c55331fe31f359b2161d06e954563"
        # encrypted_flag = "83fae9e89da6f512d50e03f0bdd59b2dd4e42c012f4de3d7ed73664a5b5c5051"

        # secret = pow(B, a, p)

        # print(decrypt_flag(secret, iv, encrypted_flag))
    finally:
        s.close()
    return p, g, A, B, iv, encrypted_flag


# p, g, A, B, iv, encrypted_flag = ruin()


def decrypt(shared_secret, iv, ciphertext):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode())
    key = sha1.digest()[:16]
    # Decrypt flag
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


p = 16007670376277647657
g = 2
A = 10874835087207164016
B = 4297078264925671801
iv = "275692e1e9c66e4ad10342bc64cc6f1c"
encrypted_flag = "77a810fec3acddb6781fdb8ed2cafd34bf233e2efea495641638922631e26c49"

iv = bytes.fromhex(iv)
encrypted_flag = bytes.fromhex(encrypted_flag)

# a = secret_by_SageMath(p, g, A)
# secret = pow(B, a, p)
secret = 4522118087793640820

print(decrypt(secret, iv, encrypted_flag))





