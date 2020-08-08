'''
with open('tiger_transformeds.jpg', 'rb') as files:
    line=files.read()
    print(type(line))
'''
import binascii

def read(images):
    try:
        image_file = images
        fin = open(image_file, "rb")
        data = fin.read()
        fin.close()
    except IOError:
        print("Image file %s not found" % image_file)
        raise SystemExit
    hex_str = str(binascii.hexlify(data))
    bin_list = []
    for ix in range(2, len(hex_str)-1, 2):
        hex = hex_str[ix]+hex_str[ix+1]
        bin_list.append(bin(int(hex, 16))[2:])
    bin_str = "".join(bin_list)
    return bin_str

print(3%2)