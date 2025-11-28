def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    divisors_list = []
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors_list.append(divisor)

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if number < sum(divisors_list):
        return "abundant"
    if number > sum(divisors_list):
        return "deficient"

    return "perfect"
