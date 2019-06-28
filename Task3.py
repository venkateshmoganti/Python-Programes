# Add the numbers given in the list which are greater than 0
given_list = [1, 2, -3, 4, -5, 6]
total = 0
for element in given_list:
    if element > 0:
        total += element
    else:
        continue
print(total)
