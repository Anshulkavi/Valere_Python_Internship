num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))
num3 = int(input("Enter the third Number: "))

if num1 > num2 and num2 > num3:
    print(num1)
elif num2 > num3 and num3 > num1:
    print(num2)
elif num3 > num2 and num2 > num1:
    print(num3)        