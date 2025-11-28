import re


def response(question):
    question = question.strip()
    if len(question) == 0:
        return "Fine. Be that way!"

    pattern = re.compile(r'[A-Z\s\W\d]+(?![a-z])!$')
    if pattern.search(question):
        return "Whoa, chill out!"

    pattern = re.compile(r'[A-Z]*', flags=re.IGNORECASE)
    if pattern.search(question).span() == (0,0):
        pattern = re.compile(r'\?$')
        if pattern.search(question):
            return "Sure."
        return 'Whatever.'

    pattern = re.compile(r'^[0-9,A-Z\s\t\n\'\!]+\?*$')
    if pattern.search(question):
        pattern = re.compile(r'\?$')
        if pattern.search(question):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    pattern = re.compile(r'[:\)\(]*\?$')
    if pattern.search(question):
        return "Sure."
    return "Whatever."

