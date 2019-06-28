# Exponent
def find_exponent(base, exp):
    i = 1
    result = 1
    while i <= exp:
        result *= base
        i += 1

    print(result)


find_exponent(23, 2)
