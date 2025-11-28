def count_words(sentence):
    import numpy as np
    import re
    # this will not match contracted words
    # such as don't and can't
    prog = re.compile(r"([\W^']|_)")
    result = prog.split(sentence)
    prog = re.compile(r"[\W_ ]?")
    # this removes non-word characters using the patten above
    items_to_keep = [i.lower() for i in result if prog.fullmatch(i) is None]
    for i in range(len(items_to_keep)):
        prog = re.compile(r"'[a-zA-Z]+'")
        new_result = prog.fullmatch(items_to_keep[i])
        print(items_to_keep[i])
        if new_result is not None:
            one_more_word = re.sub(r"'|\W", "", items_to_keep[i])
            print(one_more_word)
            items_to_keep[i] = one_more_word
    unique, counts = np.unique(np.array(items_to_keep), return_counts=True)
    final_result = dict(zip(unique, counts))

    return(final_result)
