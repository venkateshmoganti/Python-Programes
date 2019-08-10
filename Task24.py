# Substitution Cipher
def sub_cipher():
    text = input("Enter a text to convert to Cipher Text: ")
    result = ""
    for letters in text:
        if letters.isupper():
            if ord(letters) > ((ord("Z") + ord("A"))/2):
                x = ord(letters) - 13
                result = result + chr(x)
            else:
                x = ord(letters) + 13
                result = result + chr(x)
        elif letters.islower():
            if ord(letters) > ((ord("z") + ord("a"))/2):
                x = ord(letters) - 13
                result = result + chr(x)
            else:
                x = ord(letters) + 13
                result = result + chr(x)
        else:
            result = result + letters

    print(result)


sub_cipher()
