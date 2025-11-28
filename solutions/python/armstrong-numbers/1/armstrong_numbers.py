def is_armstrong_number(number):
    if sum([int(digit) ** len(str(number)) for digit in str(number)]) == number:
        return True
    return False
