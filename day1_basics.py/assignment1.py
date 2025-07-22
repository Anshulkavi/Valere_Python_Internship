operand1 = int(input("Enter the first number: "))
operand2 = int(input("Enter the second number: "))
operator = input("Enter the operator(+, -, *, /): ")

if operator == '+':
    print("Result:", operand1 + operand2)
elif operator == '-':
    print("Result:", operand1 - operand2)
elif operator == '*':
    print("Result:", operand1 * operand2)
elif operator == '/':
    if(operand2 == 0):
        print("Cannot Divide by Zero")
    else:
        print("Result:", operand1 / operand2)
else:
    print("Choose default operators given")                    