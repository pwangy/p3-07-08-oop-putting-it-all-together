#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError('Title must be a string.')
        else:
            self._title = title.title()

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if not isinstance(page_count, int):
            print(f'page_count must be an integer')
        else:
            self._page_count = page_count

    def turn_page(self):
        print(f"Flipping the page...wow, you read fast!")
