# wap a generator function that yields even number upto a specified limit
def even_generator(limit):
    for i in range (0, limit+1 , 5):
        yield i
for num in even_generator(100):
    print(num)