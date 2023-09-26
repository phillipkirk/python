from affine import affine
from random import choice, randint

aff = affine()

# Set a & b, a is best set using a choice from variable a_list, b can be any number > 0
aff.set_a(choice(aff.a_list))
aff.set_b(randint(1, 100))

print(f"Running with settings a = {aff.a}, b = {aff.b}")

# Set message
message = input('Enter secret: ')

# Encipher the message and save to file
message_c = ''
for l in message:
    l = l
    if l in aff.alphabet:
        message_c += aff.cipher(l)
    else:
         message_c += l
print('Secret written to file!')
with open('secret.txt', 'w') as file:
    file.write(message_c)

# Decipher the message
print('Decipher from file:')

with open('secret.txt', 'r') as file:
    secret = file.read()

print(f'The secret is: {secret}')
print('Deciphering...')

message_d = ''
for l in secret:
    l = l
    if l in aff.alphabet:
        message_d += aff.decipher(l)
    else:
         message_d += l

print(message_d)