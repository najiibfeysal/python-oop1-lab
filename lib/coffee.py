#!/usr/bin/env python3

class Coffee:
    # Initialization of Coffee instance
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # Ensuring the size of the coffee as property
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value == "Small" or value == "Medium" or value == "Large":
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Adding 1 to the price as a tip
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1

# Creating new instance
coffee1 = Coffee("Large", 6)

print(coffee1.size)
print(coffee1.price)

coffee1.tip()
print(coffee1.price)