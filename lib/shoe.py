#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condidtion = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError('Brand must be a string.')
        else:
            self._brand = brand.title()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, int): #should be float?
            print(f'size must be an integer')
        else:
            self._size = size

    def cobble(self):
        self.condition = "New"
        print(f'Your shoe is as good as new!')
