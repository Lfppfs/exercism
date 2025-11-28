def square_of_sum(number):
    list_numbers = [i for i in range(1, number + 1)]
    return sum(list_numbers) ** 2


def sum_of_squares(number):
    list_numbers = [i for i in range(1, number + 1)]
    return sum([i ** 2 for i in list_numbers])


def difference_of_squares(number):
    square_of_sum_result = square_of_sum(number)
    sum_of_squares_result = sum_of_squares(number)

    return square_of_sum_result - sum_of_squares_result

# it's faster with numpy
# import numpy as np
#
#
# def square_of_sum(number):
#     return (np.arange(1, number + 1, 1, dtype='float64').sum()) ** 2
#
# def sum_of_squares(number):
#     return np.square(np.arange(1, number + 1, 1, dtype='float64')).sum()
#
#
# def difference_of_squares(number):
#     square_of_sum_result = square_of_sum(number)
#     sum_of_squares_result = sum_of_squares(number)
#
#     return square_of_sum_result - sum_of_squares_result
#
