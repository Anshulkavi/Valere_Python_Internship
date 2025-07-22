# Both class students contains __init__

class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, lang):
        super().__init__(name)
        self.language = lang


dev = Developer("Anshul", "Django")
print(dev.name)
print(dev.language)