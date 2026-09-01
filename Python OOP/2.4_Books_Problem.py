class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages
    
    def read(self, pages_read):
        self.__pages = self.__pages - pages_read
        print("Pages remaining: ", self.__pages)
    
    def show(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Total Pages: ", self.__pages)

b = Book("Python", "John", 200)
b.show()
b.read(50)