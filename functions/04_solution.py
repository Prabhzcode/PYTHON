#Returning multiple value 
#Wap that returns area well as circumference of the circle for a given radius
import math
def circle(radius):
    Area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return (Area,circumference)
result1 , result2 = circle(4)


#  TO ROUND OFF RESULT UPTO CERTAIN POINT 
print(f"{result1 :.2f}") #using f string
#  USING .FORMAT() method :  print("{result1:.2f}".format(result1))
# OR

print("Area is : %.2f" % result1 , "Circumference is : %.2f" % result2)





