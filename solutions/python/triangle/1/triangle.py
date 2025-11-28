def _is_triangle(sides):
    cond1 = sides[0] + sides[1] >= sides[2]
    cond2 = sides[0] + sides[2] >= sides[1]
    cond3 = sides[1] + sides[2] >= sides[0]
    if (cond1 and cond2 and cond3) and all(sides) != 0:
        return True
    return False


def equilateral(sides):
    if not _is_triangle(sides):
        return False
    if sides[0] == sides[1] and \
            sides[1] == sides[2] and \
            sides[0] == sides[2]:
        return True
    return False


def isosceles(sides):
    if not _is_triangle(sides):
        return False

    from itertools import combinations

    sides_combinations = list(combinations(sides, 2))
    is_isosceles = [
        combination[0] == combination[1] for combination in sides_combinations
    ]
    if sum(is_isosceles) >= 1:
        return True
    return False


def scalene(sides):
    if not _is_triangle(sides):
        return False
    if sides[0] != sides[1] and \
            sides[1] != sides[2] and \
            sides[0] != sides[2]:
        return True
    return False
