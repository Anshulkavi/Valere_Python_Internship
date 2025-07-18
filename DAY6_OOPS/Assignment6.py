# Employee Management System
class Employee:
    def __init__(self,name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.__base_salary = base_salary

    def set_salary(self, amount):
        self.__base_salary = amount

    def get_salary(self):
        return self.__base_salary

    def display_info(self):
        print(f"Name: {self.name}") 
        print(f"Employee ID: {self.emp_id}")  
        print(f"Salary: ${self.__base_salary}")
        
class Manager(Employee):
    def __init__(self,name, emp_id,base_salary,team_size):
        super().__init__(name, emp_id,base_salary)
        self.team_size = team_size

    def display_info(self):
        print(f"Name: {self.name}") 
        print(f"Employee ID: {self.emp_id}")  
        print(f"Salary: ${self.get_salary()}")
        print(f"Team Size: {self.team_size}")


e1 = Employee("virat",1,25000)
e1.display_info()
e2 = Employee("rahul",2,23000)
e2.display_info()
e3 = Manager("Prakash",3,50000,3)
e3.display_info()

             
