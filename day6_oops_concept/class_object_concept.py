# Class - A class is a blueprint for creating objects.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")    


#Object - An object is an instance of a class.
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()

=======================================
#Constructor (__init__) - The constructor method initializes the object’s state.
def __init__(self, name, age):
    self.name = name
    self.age = age


# example
class Person: #Class
    def __init__(self, name, age): #constructor
        self.name = name #instance variable
        self.age = age

    def Introduction(self):
        print(f"Hi!,I am {self.name} and I am {self.age} old")

person1 = Person("Anshul", 21) #object
person2 = Person("Virat", 22)
person1.Introduction() #call
person2.Introduction() 


# Instance vs Class Variables
class Student:
    school = "ABC School" #Class variable

    def __init__(self,name):
        self.name = name #Instance variable

s1 = Student("Ravi")
s2 = Student("Anita")

print(s1.school) #ABC School
Student.school = "XYZ School"
print(s2.school) #XYZ School

=================================================


# Magic Methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book title: {self.title}"

    def __repr__(self):
        return f"Book(title='{self.title}', pages={self.pages})"

    def __len__(self):
        return self.pages

book = Book("Harry Potter", 400)

print(book) 
print(repr(book))
print(len(book)) 