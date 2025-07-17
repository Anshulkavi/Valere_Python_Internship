fruits = ['apple', 'banana', 'cherry']

#without enumerate
# index = 0
# for fruit in fruits:
#     print(f"{index}: {fruit}")
#     index += 1

for index, fruit in enumerate(fruits): # 0-indexing
    print(f"{index}: {fruit}")


for index, fruit in enumerate(fruits, start=1): # 0-indexing
    print(f"{index}: {fruit}")
