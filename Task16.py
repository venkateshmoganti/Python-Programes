# Calculator
def calc():
    num1 = float(input("Enter the first number"))
    op = input("Enter the operand")
    num2 = float(input("Enter the second number"))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        if num1 > num2:
            print(num1 - num2)
        else:
            print(num2 - num1)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1/num2)
    else:
        print("You have entered wrong operand")


calc()
