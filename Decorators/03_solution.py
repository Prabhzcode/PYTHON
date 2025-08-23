# Implement a decorator funtion that caches the return value of a fucntion so that when its called with the same  arguments, the cached value is returned instead of re-existing in the function.

import time
def cache(func):
    cached_value = {}
    print(cached_value)
    def wrapper(*args):
        if args in cached_value:
            return cached_value[args]
        result = func(*args)
        cached_value[args] = result
        return result
    return wrapper

@cache  
def test1(a,b ):
    time.sleep(4)
    return a+b


print(test1(2,3))
print(test1(2,3))
