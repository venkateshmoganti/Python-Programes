# For Loop Examples
friends = ["Ram", "Ravi", "Sai", "Summer"]
for i in range(len(friends)):
    print(friends[i])
j = 0
while j < len(friends):
    for letter in friends[j]:
        print(letter)
        j += 1
