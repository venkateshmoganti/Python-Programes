grid_numbers = [
    "Jim",
    "Hello",
    [1, 2, 3],
    [7, 8, 9],
    [4, 5, 6],
    [0]
]
for i in grid_numbers:
    print(i)

for i in grid_numbers:
    for j in i:
        if j in range(5, 8):
            print(j)
