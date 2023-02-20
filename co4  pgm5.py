class Publisher:
    def __init__(self,publisher):
        self.publisher=publisher
    def show(self):
        print("The publisher:",self.publisher)
class Book(Publisher):
    def __init__(self,title,author_name):
        self.title=title
        self.author_name=author_name
    def show(self):
        super().show()
        print("Title:",self.title)
        print("Author:",self.author_name)

class Python(Book):
    def __init__(self,publisher,title,author,price,page):
        self.price=price
        self.page=page
        Book.__init__(self,title,author)
        Publisher.__init__(self,publisher)
    def show(self):
        super().show()
        print("Price:",self.price)
        print("NO OF PAGES = ",self.page)

python_book=Python("Shakespear","Core Python Applications Programming","Wesley J. Chun","786 Rs/-",750)
python_book.show()
