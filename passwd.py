from random import randrange

def password_generator(plen):
    Lchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Hchar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ['!', '£', '$', '%', '^', '&', '*', '<', '>', '?', '@']
    chars = [Lchar, Hchar, nums, symbols]

    i = 0
    passwd = ""
    while i < plen:
        m = randrange(0, 4)
        if m < 2:
            n = randrange(0, 26)
        elif m == 2:
            n = randrange(0, 10)
        elif m == 3:
            n = randrange(0, 11)
        else:
            print("ERROR!")

        passwd += str(chars[m][n])

        i += 1
        
    return passwd

for i in range(50):
    print(password_generator(64))
