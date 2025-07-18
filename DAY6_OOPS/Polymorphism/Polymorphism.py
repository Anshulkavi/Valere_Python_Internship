'''
🔁 What is Polymorphism?
Polymorphism means "many forms".
It allows the same method or function name to behave differently based on the object it is acting on.

✅ Real-Life Analogy:
A smartphone behaves differently when used by:

A child (for games)

A photographer (for camera)

A developer (for coding)

🟰 One device, many uses → polymorphism

✨ Types of Polymorphism in Python
Type	Meaning
Duck     Typing	If it walks like a duck and quacks like a duck, it's a duck.
Method   Overriding	Same method name in child class overrides parent class.
Function   Polymorphism	Same function works for different data types.
'''
# 1. Duck Typing Example
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!" 


def animal_sound(animal):
    print(animal.speak())

d = Dog()
c = Cat()

animal_sound(d) # Woof!
'''
#Method Overriding (OOP-style Polymorphism)
class Vehicle:
    def fuel(self):
        print("Petrol or Diesel")

class ElectricCar(Vehicle):
    def fuel(self):         # Overriding
        print("Electric Charge")

v.fuel() #Petrol or diesel
e.fuel() #Electric charge        
'''
#Same method name fuel(), but different behavior depending on the object — this is runtime polymorphism via method overriding.

# 3. Function Polymorphism(Built-in functions)
print(len("Anshul"))
print(len([1, 2, 3]))
print(len({'a': 1}))
# Same len() function works on different data types — this is also polymorphism.