# Multiple Inheritance

class Father:
    def gardening(self):
        print("I love gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother):
    def sports(self):
        print("I love football")

c = Child()
c.gardening() # from father
c.cooking() # from mother
c.sports() # own method             
