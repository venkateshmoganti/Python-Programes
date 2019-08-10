# Function to append something at certain position in a string
original = "My Name Is Tom"
text = "MyNameIsTom"
for letters in range(0, len(original)):
    if ord(original[letters]) == 32:
        text = text[:letters] + " " + text[letters:]

print(text)
