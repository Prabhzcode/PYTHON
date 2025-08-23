#functions as first class objects
#write a decorator function tt measures the time taken by a fucntion to execute
import time

def timer (func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f" {func.__name__} ran in{end - start : .6f} time ")
        return result
    return wrapper 
@timer
def example_func(n):
    time.sleep(n)
example_func(2)
