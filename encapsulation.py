# access modifier -> public, private

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     def __str__(self):
#         return self.__name
#
# p1 = Person("Tom")
# p1.__name = "Ram"
# print(p1)

class House:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if not new_price < 0:
            self._price = new_price
        else:
            print("Please enter a valid price")

h1 = House(4000)
h1.price = 3000
print(h1.price)



















