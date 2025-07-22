# Heirarchical Inheritance
# One parent class, multiple child classes.

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")        

d = Dog()
c = Cat()

d.sound() # Inherited from Animal
d.bark()

c.sound() # Inherited from Animal
c.meow()

# both Dog and Cat inherit from the same base class Animal