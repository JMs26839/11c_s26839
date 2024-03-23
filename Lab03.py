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

# #task_5 exception handling
# try:
#     sq2= SquareGenerator()
#     sq2.square_gen_method(10,1)
#     print(sq2.square_gen_method())
#
# except Exception as e:
#     print("EndSmallerThanStartEXC",e)


#task_6
from square_generator import SquareGenerator
sq3= SquareGenerator()

# #task7
# from Package_task_7.square_generator_packaged import SquareGenerator
# sq4= SquareGenerator(1,5)

#task8
class CubicGenerator(SquareGenerator):

    def cubed_gen_method(self, start, end):
        list_of_cubes = [x ** 3 for x in range(start, end)]
        return list_of_cubes

cg= CubicGenerator()

print(cg.cubed_gen_method(1,10))

#task9
class task9(CubicGenerator):
    def cubed_gen_method(self, start, end):
        if start >= end:
            raise ValueError("start must be less than end")
        generate_list_of_squares=[x ** 2 for x in range(start, end)]


        return generate_list_of_squares

ts9= task9()
print(ts9.cubed_gen_method(1,10))

#task10
from abc import ABC, abstractmethod
class SquareGenerator(ABC):
    @abstractmethod
    def square_gen_method(self, start, end):
        abst_squares=[x ** 2 for x in range(start, end)]
        return abst_squares

class CubicGenerator(SquareGenerator):
    def square_gen_method(self, start, end):
        abs_cubes=[x ** 2 for x in range(start, end)]
        return abs_cubes
        

ts10= CubicGenerator()
print(ts10.square_gen_method(1,100))
