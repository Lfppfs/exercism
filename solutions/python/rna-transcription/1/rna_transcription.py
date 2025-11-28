def to_rna(dna_strand):
    # if c is not replaced with something
    # different than g (eg x), replacing all
    # Cs with Gs makes all Cs in the dna strand
    # turn to Cs in the rna strand
    return dna_strand.\
        replace("A", "U").\
        replace("T", "A").\
        replace("C", "X").\
        replace("G", "C").\
        replace("X", "G")
