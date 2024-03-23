class SquareGenerator():
    def __init__(self, start,end):
        self.start = start
        self.end = end




    def square_gen_method(start, end):
        list_of_squares = [x ** 2 for x in range(start, end)]
        return list_of_squares