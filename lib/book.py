#!/usr/bin/env python3

class Book:
    # Initialization of a Book object
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # Ensuring the page_count is an integer using property
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if type(value) is int:
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Turning a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
# Creating a Book instance
book1 = Book("Words from wises", 133)

print(book1.title)
print(book1.page_count)