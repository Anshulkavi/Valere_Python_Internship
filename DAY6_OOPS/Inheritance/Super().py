class Person:
    def __init__(self, name):
        self.name = name
        print("Person initialized")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name) #calls base constructor
        self.roll = roll
        print("Student initialized")


s = Student("Ravi", 101)
print(s.name, s.roll)