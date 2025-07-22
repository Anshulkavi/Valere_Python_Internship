class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def info(self):
        print(f"{self.title} by {self.author}")

class Magazine:
    pass

book = Book("Wings of Fire", "A.P.J.Abdul Kalam")
book.info()                