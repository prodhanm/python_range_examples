# The first example of the range function (range()) is to work 
# with one parameter. 

def range_1():
    ex1 = list(range(10))
    return ex1

print(range_1())

# result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# The range() with two parameters.

def range_2():
    ex2 = list(range(1,11))
    return ex2

print(range_2())

# result: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# The range() with three parameters.

def range_3():
    ex3 = list(range(1,10,3))
    return ex3

print(range_3())

# result: [1, 4, 7]

