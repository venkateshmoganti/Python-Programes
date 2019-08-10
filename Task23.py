# Program for translation
var1 = input("Enter a string or word: ")
final = ""
for i in var1:
    if i.upper() in "AEIOU":
        if i.isupper():
            final += "Z"
        else:
            final += "z"
    else:
        final += "L"
print(final)
print(ord("J"))
