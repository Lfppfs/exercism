import string


def rotate(text, key):
    lowercase_alphabet = string.ascii_lowercase
    uppercase_alphabet = string.ascii_uppercase

    lowercase_new_alphabet = {}
    for index, letter in enumerate(lowercase_alphabet):
        test = index + key
        if test > 25:
            test = test - 26
        lowercase_new_alphabet[letter] = lowercase_alphabet[test]
    uppercase_new_alphabet = {}
    for index, letter in enumerate(uppercase_alphabet):
        test = index + key
        if test > 25:
            test = test - 26
        uppercase_new_alphabet[letter] = uppercase_alphabet[test]

    new_text = []
    for index, letter in enumerate(text):
        if letter in lowercase_new_alphabet.keys():
            new_text.append(lowercase_new_alphabet[letter])
        elif letter in uppercase_new_alphabet.keys():
            new_text.append(uppercase_new_alphabet[letter])
        else:
            new_text.append(text[index])

    return "".join(new_text)
