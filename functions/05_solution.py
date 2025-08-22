# Wap a funtion that greets a user . if no name is provided , it should greet with a default name 


def greet(name = "anonymous user"): #parameter can act as variables if no value is passed 
    return "Hello, " + name + " !"

print(greet("chai")) # prints anonymous user if no args is passed in the greet() function
