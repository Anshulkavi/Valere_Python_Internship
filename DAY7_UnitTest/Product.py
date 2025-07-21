class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)       # "40" → 40.0
        self.quantity = int(quantity)   # "10" → 10

    def update_stock(self, count):
        if count < 0:
            raise ValueError("Stock count cannot be negative")
        self.quantity += count

    def purchase(self, count):
        if count < 0:
            raise ValueError("Cannot purchase a negative nummber of times")
        if count > self.quantity:
            raise ValueError("Not enough stock available") 
        self.quantity -= count

    def get_total_value(self):
        return self.price * self.quantity

p = Product('apple', '40', '10')
p.update_stock(15)
p.purchase(10)
print(p.get_total_value())  # Output: 600.0
