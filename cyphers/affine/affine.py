from math import gcd as bltin_gcd
from random import choice, randint

def _affine__coprime2(a, b):
            return bltin_gcd(a, b) == 1
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

class affine:
    def __init__(self):
        self.alpha_i = {}
        self.alpha_o = {}
        self.alphabet = []
        self.a_list = []

        n = 97
        for i in range(0, 26):
            self.alpha_i[chr(n)] = i
            n += 1

        n = 97
        for i in range(0, 26):
            self. alpha_o[i] = chr(n)
            n += 1

        for i in range(97, 123):
            self.alphabet += chr(i)

        for i in range(1, 9999):
            if _affine__coprime2(i, 26) == 1:
                self.a_list.append(i)
        
        self.a = choice(self.a_list)
        self.b = randint(1, 1000)

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def cipher(self, x):
        li = int(self.alpha_i[x])

        y = ((self.a * li) + self.b) % 26

        lo = str(self.alpha_o[y])
        return lo

    def decipher(self, y):

        v = modinv(self.a, 26)
        li = self.alpha_i[y]

        x = v * (li - self.b) % 26

        lo = self.alpha_o[x]

        return lo