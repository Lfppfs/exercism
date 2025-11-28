def flatten(iterable):

    def flatten_recursion(iterable, n, iterable_aux):
        if n == 0:
            return iterable_aux
        for i in iterable:
            if type(i) is int:
                iterable_aux.append(i)
            elif type(i) is list:
                flatten_recursion(i, n, iterable_aux)

        return iterable_aux

    iterable_aux = []
    n = len(iterable) - 1
    flattened_array = flatten_recursion(iterable, n, iterable_aux)
    return flattened_array
