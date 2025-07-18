#Duck typing
# class PDFDocument:
#     def print_info(self):
#         print("This is a PDF file.")


# class WordDocument:
#     def print_info(self):
#         print("This is a Word file.")

# def print_doc_info(doc):
#     doc.print_info()

# p = PDFDocument()
# w = WordDocument()

# print_doc_info(p)
# print_doc_info(w)

#Overriding

class Employee:
    def __init__(self,name):
        self.name = name

    def work(self):
        print(f"{self.name} is doing general office work.")

#Subclass - Developer
class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")

#Subclass - Manager
class Manager(Employee):
    def work(self):
        print(f"{self.name} is organizing meetings.")

#Subclass - Designer
class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing user interfaces.")

#Polymorphic function
def assign_work(employee):
    employee.work()

# Creating different employee types
e1 = Developer("Alice")
e2 = Manager("Bob")
e3 = Designer("Charlie")

#Polymorphic behavior
assign_work(e1)
assign_work(e2)
assign_work(e3)