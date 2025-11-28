def square_root(number):
    counter = 1
    while number > 0:
        if counter ** 2 == number:
            return counter
        counter += 1
