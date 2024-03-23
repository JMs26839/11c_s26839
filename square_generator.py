class SquareGenerator():

    @staticmethod
    def square_gen_method(start, end):
        list_of_squares = [x ** 2 for x in range(start, end)]
        return list_of_squares