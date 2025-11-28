def label(colors):
    band_dict = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9,
    }

    if colors == ['black', 'black', 'black']:
        return '0 ohms'
    value = str(band_dict[colors[0]]) + str(band_dict[colors[1]])
    # line below removes trailing zeros
    value = str(int(value))
    n_zeros = '0' * band_dict[colors[2]]
    value += n_zeros
    value = int(value)
    divisor = 1

    prefix = ''
    if value > 10 ** 3:
        prefix = 'kilo'
        divisor = 10 ** 3
    if value > 10 ** 6:
        prefix = 'mega'
        divisor = 10 ** 6
    if value > 10 ** 9:
        prefix = 'giga'
        divisor = 10 ** 9

    value = int(value / divisor)
    return str(value) + f' {prefix}ohms'
