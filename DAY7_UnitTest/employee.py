class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.__base_salary = base_salary
        self.bonus = 0

    def get_salary(self):
        return self.__base_salary + self.bonus

    def set_bonus(self, amount):
        if amount < 0:
            raise ValueError("Bonus cannot be negative")
        self.bonus = amount

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id}) - Salary: {self.get_salary()}"
