from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    @abstractmethod
    def color(self):
        pass

class Tesla(Car):
   def mileage(self):
        print("The mileage is 30kmph")

   def color(self):
        print("Red")

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")
    def color(self):
        print("Red")


t = Tesla()
t.mileage()

s = Suzuki()
s.mileage()
