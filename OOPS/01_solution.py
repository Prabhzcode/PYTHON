#basic class and object
# Q1. Create a car class with attributes and model , then create an instance of thid class

class Car:
    def __init__(self, brand, model):
        self.__brand = brand#__brand made the attribute private (encapsulated)
        self.model = model
    def get_brand(self):#it gives access to the encapsulated __brand attribute
        return self.__brand + "!"
    def fullcar(self):
        return f"{self.__brand} , {self.model}"
    def fuel_type(self):# polumorphism
        return "petrol or diesel"


class Electric_car(Car):
    def __init__(self,brand,model,battery):
        super(). __init__(brand,model)
        self.battery = battery
    def fuel_type(self):# polumorphism
        return "electric battery"

my_car = Car("Toyota","Hilux")
fortuner = Car("Toyota","Fortuner")
mytesla = Electric_car("tesla","s","80kmah")
print(my_car.fullcar())
print(mytesla.get_brand())
print(mytesla.battery)
print(mytesla.fuel_type())
print(fortuner.fuel_type())
print(fortuner.get_brand())