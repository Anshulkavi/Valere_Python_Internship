# Multi-Level Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")    

d = Dog()
d.eat() # from Animal
d.walk() # from Mammal
d.bark() # own method