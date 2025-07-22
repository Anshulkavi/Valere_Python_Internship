'''
What is Encapsulation?
Encapsulation means:

Wrapping data (variables) and methods that operate on the data into a single unit (class), while hiding the internal details from outside interference.

In simple terms:

You protect your data.

You provide controlled access via methods.

✅ Levels of Access in Python
Access       Level	    Syntax	Description
Public	    self.var	Accessible everywhere
Protected	self._var	Suggests "use only inside class or subclass"
Private	    self.__var	Name mangled, not directly accessible

'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner #public
        self.__balance = balance # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Anshul", 1000)

#Accessing public
print(acc.owner) 

#cant access private 

print(acc.get_balance()) #only accessed through method
acc.deposit(500) # +500 
acc.withdraw(2000)
print(acc.get_balance()) # 1500