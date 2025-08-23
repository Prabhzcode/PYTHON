#Create a decorator to print a fucntion name and the values of its arguments every time the function is called


def decorator(func):
    def wrapper(*args,**kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}:{v}" for k,v in kwargs.items())
        print (f"Funciton name is {func.__name__} with args = {args_value} and kwargs = {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper

@decorator
def greet(name , greeting = "hello"):
    print(f"{greeting} , {name}")

greet ("prabh", greeting = "welcome")