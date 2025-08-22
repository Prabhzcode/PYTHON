# Create a function that accepts any number of keyword arguments and prints them in the format  ( key:value )

def print_kwargs(**kwargs):
    for x,y in kwargs.items():
        print(f"{x} : {y}")
        print(kwargs)

print_kwargs(name = "shaktimaaaaan" , power = "Flying" , enemy = "chor")
print_kwargs(name = "superman" , power = "Lazer")
print_kwargs(name = "flying jatt" , power = "Jatt")
