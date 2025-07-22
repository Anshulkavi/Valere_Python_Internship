num = int(input("Enter a number: "))

if num <= 1:
    print(f'{num} is not a Prime Number')
elif num == 2:
    print("2 is a Prime number")
elif num % 2 == 0:
    print(f'{num} is not a Prime number')
else:
    for i in range(3, int(num ** 0.5) + 1, 2): # check only odd numbers
       if num % i == 0:
           print(f'{num} is not a Prime Number')
           break
    else:
        print(f"{num} is a Prime number")    


        '''
❓Why start from 3 and use step 2?
Because:
We already check 2 separately (the only even prime)
Now we only want to check odd divisors (3, 5, 7, …)
So we skip even numbers using step = 2
'''