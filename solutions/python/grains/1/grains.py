def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    global grains_list
    grains_list = [1]
    for square in range(1, number):
        grains_list.append(grains_list[-1] * 2)
    return grains_list[-1]


def total():
    return sum(grains_list)
