def latest(scores):
    import numpy as np
    scores = np.array(scores)
    return(scores[len(scores) - 1])


def personal_best(scores):
    import numpy as np
    return(np.max(scores))


def personal_top_three(scores):
    if len(scores) < 3:
        scores.sort(reverse=True)
        return(scores)
        # print(scores)
    import numpy as np
    scores_copy = np.array(scores)
    top_three = []
    while len(top_three) < 3:
        num_max_elements = np.size(
            scores_copy[scores_copy == np.max(scores_copy)])
        if num_max_elements > 1:
            for i in range(1, num_max_elements):
                top_three.append(np.max(scores_copy))
                if len(top_three) == 3:
                    return(top_three)
        top_three.append(np.max(scores_copy))
        scores_copy = scores_copy[scores_copy != np.max(scores_copy)]
    return(top_three)
