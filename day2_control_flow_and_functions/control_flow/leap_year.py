year = int(input("Enter a year: "))

if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f'{year} is a leap year')
        else:
            print(f'{year} is NOT a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is NOT a leap year')                    


   '''
A year is a leap year if:

    It's divisible by 4, and

    Not divisible by 100, unless it's also divisible by 400.
''' 