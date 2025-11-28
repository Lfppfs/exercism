def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise Exception('Strands should have the same length')
    distance = 0
    for i,j in zip(strand_a, strand_b):
        if i != j:
            distance += 1
    # print(hamm_dist)
    return distance
# distance('GAGCCTACTGACGGGAT','CATCGTAATGACTTTTT')
