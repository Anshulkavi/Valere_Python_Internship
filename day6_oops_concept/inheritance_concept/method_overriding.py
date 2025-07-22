class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def start(self):
        print("Car engine started") #Overrides parent method

c = Car()
c.start() # "Car engine started"        