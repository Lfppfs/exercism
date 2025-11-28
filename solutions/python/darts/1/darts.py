from math import sqrt, pi, fabs


def score(x, y):
    radius = sqrt(fabs(x) ** 2 + fabs(y) ** 2)
    area_dart_circle = pi * (radius ** 2)

    area_inner_circle = pi * (1 ** 2)
    area_middle_circle = (pi * (5 ** 2))
    area_outer_circle = (pi * (10 ** 2))

    if area_dart_circle > area_outer_circle:
        return 0
    if area_dart_circle > area_middle_circle:
        return 1
    if area_dart_circle > area_inner_circle:
        return 5
    return 10
