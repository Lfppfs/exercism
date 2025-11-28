def commands(binary_str):
    actions = [
        'wink',
        'double blink',
        'close your eyes',
        'jump',
        'reverse',
    ]

    handshake = []
    for index, i in enumerate(binary_str[::-1]):
        if i == str(1):
            handshake.append(actions[index])

    if 'reverse' in handshake:
        handshake = handshake[:-1]
        handshake.reverse()

    return handshake
