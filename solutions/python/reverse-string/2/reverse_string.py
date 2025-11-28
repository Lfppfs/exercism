def reverse(text):

    reversed_string = [
        text[letter_index]
        for letter_index in range(len(text) - 1, -1, -1)
    ]

    return ''.join(reversed_string)
