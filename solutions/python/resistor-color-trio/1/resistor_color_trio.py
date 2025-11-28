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

    value = str(band_dict[colors[0]]) + str(band_dict[colors[1]])
    n_zeros = '0' * band_dict[colors[2]]
    value += n_zeros
    if colors == ['black', 'black', 'black']:
        return '0 ohms'

    prefix = ''
    if n_zeros >= '3':
        prefix = 'kilo'
    if n_zeros >= '6':
        prefix = 'mega'
    if n_zeros >= '9':
        prefix = 'giga'
    return value + f' {prefix}ohms'
