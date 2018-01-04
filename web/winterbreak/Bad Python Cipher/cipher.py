def encrypt(message, key):
    part0 = message[::2]
    part1 = message[1::2]
    a = 0
    e0 = ""
    for c in part0:
        e0 += chr(ord(c)^key^a)
        a = ord(c)+1
    a = 0
    e1 = ""
    for c in part1:
        e1 += chr(ord(c)^key^a)
        a = ord(c)+1
    return "".join("".join(x) for x in zip(e0,e1))

def hex_decode(string):
    return "".join(chr(int(s[0]+s[1],16)) for s in zip(string[::2],string[1::2]))

ciphertext = hex_decode("414b212d3e276b2626065931073e223562204979344a30772c263b6b")

# print("Ciphertext: {}".format(ciphertext))

key = ord(ciphertext[0]) ^ ord("f")

# print("Key: {}".format(key))

special = 0
alpha = ciphertext[::2]
part0 = ""
for character in alpha:
    part0 += chr(ord(character) ^ key ^ special)
    special = ord(part0[-1]) + 1

# print("Partial Flag: {}".format(part0))

special = 0
beta = ciphertext[1::2]
part1 = ""
for character in beta:
    part1 += chr(ord(character) ^ key ^ special)
    special = ord(part1[-1]) + 1

# print("Partial Flag: {}".format(part1))

print("Flag: {}".format(''.join(''.join(pair) for pair in zip(part0, part1))))