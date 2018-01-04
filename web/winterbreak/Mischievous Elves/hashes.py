import hashlib
import base64

data = open("hashes.txt").read().splitlines()

# print("Hash Length: {}".format(len(data[0])))

matcher = {}
for code_point in range(256):
    character = chr(code_point)
    hashed = hashlib.sha256(character.encode()).hexdigest()
    # print("{}: {}".format(character, hashed))
    matcher[hashed] = character

decrypted = ""
for line in data:
    decrypted += matcher[line]

# print("Decrypted Hash:\n{}".format(decrypted))

decoded = base64.b64decode(decrypted)

print("Decoded Flag:\n{}".format(decoded))