def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_lists = []
    for list in lists:
        new_lists = new_lists + list
    return new_lists


def filter(function, list):
    new_list = []
    for i in list:
        if function(i):
            new_list = new_list + [i]
    return new_list

# filter(lambda x: x % 2 == 0, [1,2, 3, 4])

def length(list):
    counter = 0
    for i in list:
        counter += 1
    return counter


def map(function, list):
    new_list = []
    for i in list:
        new_list = new_list + [function(i)]
    return new_list

# print(map(lambda x: x ** 2, [1,2, 3, 4]))


def foldl(function, list, initial):
    if type(initial) is str:
        result = ''
    else:
        result = 0
    for i in list:
        result = function(result, i)
    result = function(result, initial)
    return result

def foldr(function, list, initial):
    if type(initial) is str:
        result = ''
    else:
        result = 0
    result = function(result, initial)
    for i in list[::-1]:
        result = function(result, i)
    return result


def reverse(list):
    new_list = []
    for i in range(len(list) - 1, -1, -1):
        new_list = new_list + [list[i]]
    return new_list

