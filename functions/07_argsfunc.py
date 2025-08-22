# wap a fucntion that takes multiple args and return their sum

def sum_all(*args):
    print(args)#tuple 
    print(*args)#passed argument's value 
    return(sum(args))

print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5,6,7,8))
