from math import gcd as bltin_gcd

alpha_i = {}
alpha_o = {}

n = 97
for i in range(0, 26):
    alpha_i[chr(n)] = i
    n += 1

n = 97
for i in range(0, 26):
    alpha_o[i] = chr(n)
    n += 1

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

a_list = []
for i in range(1, 9999):
    if coprime2(i, 26) == 1:
         a_list.append(i)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def cipher(a, b, x):
    global alpha_i, alpha_o

    li = int(alpha_i[x])

    y = ((a * li) + b) % 26

    lo = str(alpha_o[y])
    return lo

def decipher(a, b, y):
    global alpha_i, alpha_o

    v = modinv(a, 26)
    li = alpha_i[y]

    x = v * (li - b) % 26

    lo = alpha_o[x]

    return lo