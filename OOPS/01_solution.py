#basic class and object
# Q1. Create a car class with attributes and model , then create an instance of thid class

class Car:
    total_car = 0 # to track the amount of objects being created under car class
    def __init__(self, brand, model):
        self.__brand = brand#__brand made the attribute private (encapsulated)
        self.__model = model
        Car.total_car += 1# increment every time when an object is created
                             #Car.total_car (not) self.total_car , since the 1st one refers to the class    variable , shared across all the instances , while self.total_car is refers to the instance variable called total_car that means each object would have its own copy of total_car, and the shared counter would break.

    def get_brand(self):# it gives access to the encapsulated  (__brand) attribute
        return self.__brand + "!"

    def fullcar(self):

        return f"{self.__brand} , {self.__model}"

    def fuel_type(self):# polymorphism
        return "petrol or diesel"

    def get_model(self):
        return self.__model + "!"

    @staticmethod
    def genral_description():
        return  "cars area means of transport"

    @property
    def model(self):
        return self.__model

class Electric_car(Car):
    def __init__(self,brand,model,battery):
        super(). __init__(brand,model)
        self.battery = battery
    def fuel_type(self):# polumorphism
        return "electric battery"

class battery():
    def battery_info(self):
        return "this is battery"

class engine():
    def engine_info(self):
        return "this is engine"
  
class Electric_car2(battery,engine,Car):
    pass

mytesla2 = Electric_car2("90kmah" , "electric" )
print(mytesla2.engine_info())
# my_car = Car("Toyota","Hilux")
# fortuner = Car("Toyota","Fortuner")
# safari = Car("Toyota","safari")
mytesla = Electric_car("tesla","s","80kmah")
# print(my_car.fullcar())
# print(fortuner.fuel_type())
# print(fortuner.get_brand())
# print(safari.genral_description())
# print(Car.genral_description())

# STATIC method = a method that belong to the class rather an instance of a class (@staticmethod) for creating static method
# Add a static method to the car class which deliver a general description ofthe car 



#property decorator in the class make the model read only
# my_car.model = "nexon"
# print(my_car.model)

#use (isinstance) (to check is mytesla is an instance of car and Electric_car)
# print(isinstance (mytesla,Car))
# print(isinstance (mytesla,Electric_car))



#multiple inheritence 
# create two class battery and engine amd let the electric car to inherit from both, demonstrating multpiple inheritence
