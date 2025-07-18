'''
What is Method Resolution Order (MRO) in Python?
MRO is the order in which Python looks for a method
or attribute in a hierarchy of classes during inheritance.

It becomes important especially when:

A class inherits from multiple parent classes 
(Multiple/Hybrid Inheritance).
There are shared base classes (diamond problem).


When you call a method on an object, 
Python follows MRO to decide which method to execute — 
starting from the class itself, then parent(s), then 
grandparents, etc., following a defined linear order.


How is MRO calculated?
Python uses the C3 Linearization Algorithm,
which ensures a consistent and predictable method 
resolution path,especially in diamond-shaped inheritance.
'''

# Diamond Problem Example
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

d = D()
d.show()    # Because MRO is: D → B → C → A
