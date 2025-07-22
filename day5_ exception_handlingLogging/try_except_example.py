# try-except

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!") 
except ValueError:
    print("Invalid input! Please enter a number.")    


# try-except-else-finally

try:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    division = a / b
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print("Result:", division)
finally:
    print("Execution complete")            


# Custom Exceptions
class NegativeAgeError(Exception):
    '''Raised when age is negative'''
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age can't be negative")
    print(f"Age set to {age}")        


#Using it
try:
    set_age(-5)
except NegativeAgeError as e:
    print("Custom Error:", e)        