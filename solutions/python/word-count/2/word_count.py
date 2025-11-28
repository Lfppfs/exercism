import re
from collections import Counter


def count_words(sentence):
    pattern = re.compile(r"[a-zA-Z0-9]+'[a-zA-Z0-9]+|[a-zA-Z0-9]+")
    return Counter([x.lower().strip() for x in pattern.findall(sentence)])

