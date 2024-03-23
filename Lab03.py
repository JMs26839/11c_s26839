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


#task_3

class SquareGenerator():

    @staticmethod
    def square_gen_method(start, end):
        list_of_squares = [x ** 2 for x in range(start, end)]
        return list_of_squares
#testing
sq= SquareGenerator()

print(sq.square_gen_method(1,10))



#task_4
list_math_lib=[math.sqrt(x)for x in squares_list]
print(list_math_lib)

#task_5 exception handling
try:
    sq2= SquareGenerator()
    sq2.square_gen_method(10,1)
    print(sq2.square_gen_method())

except Exception as e:
    print("EndSmallerThanStartEXC",e)


