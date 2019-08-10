# Caesar Cipher
def ccd():
    original_text = input("Enter the text: ")
    text = original_text.replace(" ", "")
    key = input("Enter the key: ")
    a = int(input("Press 1 for Encryption, 2 for Decryption : "))
    z = []
    result = ""
    for i in range(0, len(text), len(key)):
        temp = text[i:i + len(key)]
        z.append(temp)
    if a == 1:
        for row in range(0, len(z)):
            for col in range(0, len(z[row])):
                if z[row][col].islower():
                    f = ord(z[row][col]) + int(key[col]) + 3
                    if f > ord("z"):
                        f = f - 26
                        result = result + chr(f)
                    else:
                        result = result + chr(f)
                elif z[row][col].isupper():
                    f = ord(z[row][col]) + int(key[col]) + 3
                    if f > ord("Z"):
                        f = f - 26
                        result = result + chr(f)
                    else:
                        result = result + chr(f)

                else:
                    result = result + z[row][col]
    elif a == 2:
        for row in range(0, len(z)):
            for col in range(0, len(z[row])):
                if z[row][col].islower():
                    f = ord(z[row][col]) - int(key[col]) - 3
                    if f < ord("a"):
                        f = f + 26
                        result = result + chr(f)
                    else:
                        result = result + chr(f)
                elif z[row][col].isupper():
                    f = ord(z[row][col]) - int(key[col]) - 3
                    if f < ord("A"):
                        f = f + 26
                        result = result + chr(f)
                    else:
                        result = result + chr(f)

                else:
                    result = result + z[row][col]
    else:
        print("You have not entered correct input")

    for letters in range(0, len(original_text)):
        if ord(original_text[letters]) == 32:
            result = result[:letters] + " " + result[letters:]

    print(result)


ccd()
