# class classname:
# class Animal:
#
#     def eat(self): # method
#         print("Eating")
#     color = "red"  # property
#
# Dog = Animal() # object
# Dog.eat()
# print(Dog.color)

# class Employee:
#     def info(self, id, name):
#         self.id = id
#         self.name = name
#         print(self.id, self.name)
#
# emp1 = Employee()
# emp1.info(100, "John")

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"{self.id}: {self.name}")

emp1 = Employee(100, "John")
emp1.display()













