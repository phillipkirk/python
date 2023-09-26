from affine import affine
from random import choice, randint

aff = affine()

# Set a & b, a is best set using a choice from variable a_list, b can be any number > 0
aff.set_a(choice(aff.a_list))
aff.set_b(randint(1, 100))

print(f"Running with settings a = {aff.a}, b = {aff.b}")

# Set message
message = "Hello, World!"

# Encipher the message
message_c = ''
for l in message:
    l = l.lower()
    if l in aff.alphabet:
        message_c += aff.cipher(l)
    else:
         message_c += l
     
print(f'Encript: {message} -> {message_c}')

# Decipher the message
message_d = ''
for l in message_c:
    l = l.lower()
    if l in aff.alphabet:
        message_d += aff.decipher(l)
    else:
         message_d += l
print(f"Decript: {message_c} -> {message_d}")