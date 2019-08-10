# Vernam Cipher
def vc():
    text = input("Enter the text to encrypt:")
    number = []
    result = ""
    for i in range(0, len(text)):
        z = input("Enter the number:")
        number.append(int(z))
    for letters in range(0, len(text)):
        if text[letters].islower():
            test = "a"
        else:
            test = "A"
        temp = ord(text[letters]) + int(number[letters]) - ord(test)
        mod = temp % 26
        result = result + chr(mod + ord(test))

    print(result)


vc()
