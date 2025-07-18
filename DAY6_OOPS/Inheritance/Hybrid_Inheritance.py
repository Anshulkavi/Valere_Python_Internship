# Hybrid  Inheritance
# Combination of more than one type of inheritance (e.g., multiple + multilevel + hierarchical)

class Person:
    def show(self):
        print("I am a Person")

class Employee(Person):
    def work(self):
        print("I work as a employee")

class Student(Person):
    def study(self):
        print("I study")

class WorkingStudent(Employee, Student): # Hybrid: Multiple + Multilevel
    def multitask(self):
        print("I manage both work and study")

ws = WorkingStudent()
ws.show() # From Person (base of both)
ws.work() # From Employee
ws.study() # From Student
ws.multitask() # Own method

# WorkingStudent inherits from both Employee and Student, both of which indirectly relate to Person. So it's a hybrid structure.