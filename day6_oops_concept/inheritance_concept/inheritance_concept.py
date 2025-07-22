#Parent class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def info(self):
        print(f"Brand: {self.brand}")
        print(f"Wheels: {self.wheels}") 


# super().__init__() calls the parent constructor.


#Child class
class Car(Vehicle): #Carinherits from Vehicle
    def __init__(self, brand, wheels, fuel):
        super().__init__(brand, wheels) # Call parent constructor
        self.fuel = fuel

    def car_info(self):
        self.info()  #call method from parent class
        print(f"Fuel Type: {self.fuel}")    


# Create object of child class
c = Car("Toyota", 4, "Petrol")
c.car_info()        