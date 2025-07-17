n = 1 #global variables

def fn():
    # global n
    n = 5 # local variable
    print('in',n)

fn()

print('out', n)