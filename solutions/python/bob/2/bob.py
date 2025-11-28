import re


def response(question):
    question = question.strip()
    if len(question) == 0:
        return "Fine. Be that way!"
    pattern = re.compile(r'^[A-Z\s]+\?*$')
    if pattern.search(question):
        pattern = re.compile(r'^\s+$')
        if pattern.search(question):
            return "Fine. Be that way!"
        pattern = re.compile(r'\?$')
        if pattern.search(question):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    pattern = re.compile(r'\?$')
    if pattern.search(question):
        return "Sure."
    return "Whatever."

