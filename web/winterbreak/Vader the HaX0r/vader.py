from PIL import Image

file = open("vader.png", "rb").read()

# print("End of file:\n{}".format(file[-500:]))

image = Image.open("vader.png")
pixels = image.load()

width, height = image.size
# print("Dimensions: {}, {}".format(width, height))

least_significant_bits = ""
for column in range(2):
    for row in range(width):
        # print(pixels[row, column])
        red, green, blue = pixels[row, column]
        least_significant_bits += str(red & 1)

lsb = least_significant_bits
message = ''.join(chr(int(lsb[index:index+8], 2)) for index in range(0, len(lsb), 8))

# print("Decoded Message:\n{}".format(message))

image.close()

ciphertext = 57137914577367293228565062563368577615696665388608381580873561507292947653861927469728508713813257411185075565545254074
private_key_exponent = 72761679205516841695522601578696797363729760559784196552815142907219620114581442879614630977718023137750190028914578865
modulus = 227010481295437363334259960947493668895875336466084780038173258247009162675779735389791151574049166747880487470296548479

plaintext = pow(ciphertext, private_key_exponent, modulus)

hp = hex(plaintext)[2:]
flag = ''.join(chr(int(hp[index:index+2], 16)) for index in range(0, len(hp), 2))

print("Flag: {}".format(flag))