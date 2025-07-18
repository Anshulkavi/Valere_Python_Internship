class Document:
    def __init__(self, title, author):
        self._title = title        # protected (encapsulation)
        self._author = author

    def info(self):               # polymorphic method
        print(f"Document: {self._title} by {self._author}")


class Book(Document):             # inheritance from Document
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def info(self):               # overriding (polymorphism)
        print(f"Book: {self._title} by {self._author} — {self.pages} pages")


class Magazine(Document):         # another subclass
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue

    def info(self):               # overriding again
        print(f"Magazine: {self._title} — Issue #{self.issue}")


# Function using polymorphism
def print_document_info(doc):
    doc.info()


# Create objects
b = Book("Atomic Habits", "James Clear", 320)
m = Magazine("National Geographic", "Editor Group", 125)

# Call function
print_document_info(b)
print_document_info(m)
