# Magic Methods = Dunder methods (double underscores) __init__, __str__, __eq__
#                 They are automatically called by many of python's built-in operations
#                 They allow developers to define or customize object behavior


class Book:

    def __init__(self, title, author, num_pages):
        self.title =title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __eq__(self, other): #eq represents equal to
        return self.title == other.title and  self.author == other.author
    
    def __lt__(self, other): # lt represents less than
        return self.num_pages < other.num_pages
    

    def __gt__(self, other): # gt represents greater than
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        if key == "author":
            return self.author
    
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry potter", "J.K Rowling", 223)
book3 = Book("The Lion, The witch and the wardrobe", "C.S Lewis", 172)
book4 = Book("The Lion, The witch and the wardrobe", "C.S Lewis", 172)

print(book1)
print(book2)
print(book3)

print(book3 == book4) # the __eq__ makes this equal to True
print(book2 < book3) # __lt__ makes this equal to False
print(book2 > book3) # __gt__ makes this equal to True

print(book2 + book3) #__add__ gives us the total pages betwen the two


print("Lion" in book3) #__contains__ makes this check give us True


print(book1['title']) #__get_item__ returns the title of the book
print(book1['author']) #__get_item__