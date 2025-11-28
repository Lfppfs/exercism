def sum_of_multiples(limit, multiples):
    list_sets = []
    for index, item in enumerate(multiples):
        list_multiples = []
        counter = 1
        multiple_iter = counter * multiples[index]
        while multiple_iter < limit:
            if multiple_iter == 0:
                break
            list_multiples.append(counter * multiples[index])
            counter += 1
            multiple_iter = counter * multiples[index]
        list_sets.append(set(list_multiples))

    set_result = set()
    for i in list_sets:
        for j in i:
            set_result.add(j)
    counter = 0
    for i in set_result:
        counter += i
    return counter
