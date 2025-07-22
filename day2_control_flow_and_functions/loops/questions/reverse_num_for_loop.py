num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10 #Gets the last digit
    rev = rev * 10 + digit #Append it to the reversed number
    num = num // 10 #Remove the last digit from original number

print("Reversed number:", rev)

    