# OOP Practice Problem: Vehicle Fleet Management
class Vehicle:
    def __init__(self, make, model, year, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer

    def drive(self, distance):
    if distance > 0:
        self.__odometer += distance    

    def get_info(self):
        print(f"Info: {self.make} {self.model} ({self.year}) for {self.odometer} km driven")

    def get_odometer(self):
    return self.__odometer #(__ makes it private - Encapsulate)




class Car(Vehicle):
    def __init__(self,make,model,year,odometer,num_seats):
        super().__init__(make,model,year,odometer)
        self.num_seats = num_seats

    def get_info(self):
        print(f"Car: {self.make} {self.model} ({self.year}) - {self.num_seats} seats for {self.odometer:} km driven")   


class Truck(Vehicle):
    def __init__(self,make, model, year,odometer,cargo_capacity):
        super().__init__(make,model,year,odometer)
        self.cargo_capacity = cargo_capacity

    def get_info(self):
        print(f"Truck: {self.make} {self.model} ({self.year}) - {self.cargo_capacity:} kg - {self.odometer:} km driven")   



c = Car("Toyota", "Camry", 2023,100 ,5)
c.drive(50)
c.get_info()

t = Truck("Ford", "F-150", 2022, 250, 1000)
t.drive(120)
t.get_info()