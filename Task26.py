# Program to slice string into given number of chunks and store in z and print each alphabet in chunks
text = "hii "
key = "123"
z = []
for i in range(0, len(text), 3):
    Temp = text[i:i+3]
    z.append(Temp)
print(z)
for row in range(0, len(z)):
    for col in range(0, len(z[row])):
        print((z[row][col]))

