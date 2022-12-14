with open('./a.out', 'rb') as file:
    contents = file.read()
binary = ''.join([format(x, 'b') for x in contents])
print(binary)