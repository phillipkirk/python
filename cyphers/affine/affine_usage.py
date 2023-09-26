from affine import a_list, cipher, decipher
from random import choice, randint

a = int(choice(a_list))
b = randint(1, 100)

print(f"Running with settings a = {a}, b = {b}")

alpha = []
for i in range(97, 123):
    alpha += chr(i)

message = "Hello, World!"
message_c = ''

for l in message:
    l = l.lower()
    if l in alpha:
        message_c += cipher(a, b, l)
    else:
         message_c += l
     
print(f'{message} -> {message_c}')

message_d = ''
for l in message_c:
    l = l.lower()
    if l in alpha:
        message_d += decipher(a, b, l)
    else:
         message_d += l
print(f"Decript: {message_d}")