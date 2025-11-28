def is_isogram(string):
    unicode_list, unicode_word = [], []

    for c in 'abcdefghijklmnopqrstuvwxyz':
        unicode_list.append(ord(c))

    for i in string:
        if ord(i.lower()) in unicode_list:
            unicode_word.append(ord(i.lower()))

    rep = 0

    for i in unicode_word:
        for j in unicode_word:
            # print(j)
            if i == j:
                rep += 1
            if rep > 1:
                print('{} is not an isogram'.format(string))
                return False  # ('{} is not an isogram'.format(string))
                # return

        rep = 0
    print('{} is an isogram'.format(string))
    return True


is_isogram('is')
