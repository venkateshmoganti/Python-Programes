# Add numbers which can be divided by 3 & 5 from 1 to 100
def task():
    total = 0
    b = []
    for a in range(1, 100):
        if a % 3 == 0 and a % 5 == 0:
            b.append(a)
            total = total + a
    print(b)
    print("total =", total)


task()
