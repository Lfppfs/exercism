def is_pangram(sentence):
    alphabet_lower = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    lower_in_sentence = [
        letter for letter in alphabet_lower if letter in sentence
    ]
    sum_all_lower = sum([letter in sentence for letter in lower_in_sentence])

    if sum_all_lower == 26:
        return True

    lower_not_in_sentence = set(alphabet_lower).\
        difference(set(lower_in_sentence))

    alphabet_upper = [
        letter.upper() for letter in lower_not_in_sentence
    ]

    upper_in_sentence = [
        letter for letter in alphabet_upper if letter in sentence
    ]

    sum_remaining_upper = sum([letter in sentence for letter in upper_in_sentence])

    if sum_all_lower + sum_remaining_upper == 26:
        return True

    return False

