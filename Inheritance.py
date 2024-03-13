# Single Inheritance
'''
class Person: # parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):  # child class
    def info(self, id):
        self.id = id
        print(f"Id: {self.id} Name: {self.firstname} {self.lastname}")

s1 = Student("Ram", "Kumar")
# s1.printname()
s1.info(1)
'''

# Mutliple Inheritance - 2 or more than parent classes and a single child class
'''
class Father:
    fathername = ""
    def father(self, fathername):
        self.fathername = fathername

class Mother:
    mothername = ""
    def mother(self, mothername):
        self.mothername = mothername

class Son(Father, Mother):
    def printnames(self):
        print("Fathername: ", self.fathername)
        print("Mothername: ", self.mothername)

son = Son()
son.fathername = "Romeo"
son.mothername = "Juliet"
son.printnames()
'''

# Multi-level Inheritance
'''
class A:
    def method_A(self):
        print("Method A is called")

class B(A):
    def method_B(self):
        print("Method B is called")

class C(B):
    def method_C(self):
        print("Method C is called")

obj1 = C()
obj1.method_B()
obj1.method_A()
'''

# Hierarchical Inheritance
class Father:
    def __init__(self, name):
        self.name = name

class Son(Father):
    def sonName(self, sonname):
        self.sonname = sonname
        print(f"{self.sonname} {self.name}")

class Daughter(Father):
    def daughtername(self, daughterName):
        self.daughterName = daughterName
        print(f"{self.daughterName} {self.name}")

son = Son("Ram")
daughter = Daughter("Ram")
son.sonName("Son1")
daughter.daughtername("Daughter1")














