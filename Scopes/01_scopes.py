x = 99
def func():
    x = 88
    print(x) # x acts as local variable

print(x) # x acts as global variable
func()




def func2():
    x = 77
    def func3():
        print(x)
    func3()
func2()





def func4():
    x = 66
    def func5():
        print(x)
    return func5 # returns function defination instead of returning funciton value
myresult = func4()
myresult()





def chaicode(num):
    def actual(x):
        return x ** num
    return actual
sq = chaicode(2)
cube = chaicode(3)
print("Square is : ",sq(2))
print("Cube is   : ",cube(2))