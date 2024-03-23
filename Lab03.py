import math
# task_1
squares_list=[x**2 for x in range(1,10)]
print(squares_list)

#task_2
def square_list_from_range(start, end):
    list=[x**2 for x in range(start,end)]
    return list
#task2 test
print(square_list_from_range(1,10))
