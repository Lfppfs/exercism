import re


def is_valid(isbn):

    # x must only be last character
    if "X" in isbn and isbn[-1] != "X":
        return False
    # if isbn contains a letter that is not x, input is invalid
    pattern = re.compile(r"(?!X)[a-zA-Z]")
    list_invalid_letters = pattern.findall(isbn)
    if list_invalid_letters:
        return False

    pattern = re.compile(r"\d|X")
    list_digits = [
        int(digit.replace("X", "10"))
        for digit in pattern.findall(isbn)
    ]
    list_result = []
    for digit, i in zip(list_digits, range(1, 11)):
        list_result.append(int(digit) * i)

    if len(list_digits) != 10:
        return False

    return sum(list_result) % 11 == 0
