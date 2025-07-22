class Student:
    def __init__(self, Name, Roll_Num):
        self.Name = Name
        self.Roll_Num = Roll_Num

    def set_marks(self, m1, m2, m3):
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def get_average(self):
        return (self.__m1 + self.__m2 + self.__m3) / 3 

    def display_info(self):
        print(f"Name: {self.Name}")
        print(f"Roll No: {self.Roll_Num}")
        print(f"Average Marks: {self.get_average():.2f}")

s1 = Student("Anshul", 42)
s1.set_marks(85,90,95)
s1.display_info()        