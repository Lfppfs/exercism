def transform(legacy_data):
    keys = legacy_data.keys()
    my_dict = {}
    for i in list(keys):
        for j in legacy_data.get(i):
            my_dict[j.lower()] = i
    return my_dict
