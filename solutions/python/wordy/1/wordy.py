import re


def answer(question):
    operations_words = r'(\s*plus\s*|\s*minus\s*|\s*multiplied\s*by\s*|\s*divided\s*by\s*)'
    numbers = r'-*\s*[0-9]+\s*'

    pattern_numbers = re.compile(numbers)
    pattern_1 = re.compile(rf'What\s*is\s*({numbers})\?', re.IGNORECASE)
    if pattern_1.fullmatch(question):
        return int(pattern_1.fullmatch(question).groups()[0])
    match = pattern_numbers.findall(question)
    pattern_operations = re.compile(operations_words)
    if not match or not pattern_operations.search(question):
        if not pattern_operations.search(question):
            raise ValueError("unknown operation")
        raise ValueError("syntax error")

    pattern_2 = re.compile(numbers + operations_words + numbers)
    if not pattern_2.search(question):
        raise ValueError("syntax error")

    if pattern_operations.search(question):
        dict_operations = {
            ' plus ': '+',
            ' minus ': '-',
            ' multiplied by ': '*',
            ' divided by ': '/',
        }
        operations_symbols = []
        for i in pattern_operations.findall(question):
            operations_symbols.append(dict_operations[i])

    string_operation = ''
    numbers_matches = pattern_numbers.findall(question)
    for index, number in enumerate(numbers_matches[:-1]):
        if index == 0:
            string_operation = numbers_matches[index]
        try:
            string_operation = str(eval(string_operation + operations_symbols[index] + numbers_matches[index+1]))
        except IndexError:
            raise ValueError("syntax error")

    return float(string_operation)

print(answer("What is?"))
