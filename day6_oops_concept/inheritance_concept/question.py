# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# class Pet(Dog, Cat): # or change inheritance order 
#     def speak(self):  # class Pet(Cat,Dog) pass
#         Cat.speak(self)

# p = Pet()
# p.speak()
# # print(Pet.__mro__)

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Puppy(Dog, Cat):
    pass

p = Puppy()
p.speak()
print(Puppy.__mro__)
