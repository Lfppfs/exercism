def convert(number):
    raindrop = ''
    pls = ['Pling','Plang','Plong']
    for i, f in enumerate([3,5,7]):
        if number % f == 0:
            raindrop = raindrop + pls[i]
    # raindrop = [pl_string + pls[i] for i,j in enumerate([3,5,7]) if number % j == 0]
    if raindrop == '':
        print(str(number))
    else:
        print(raindrop)
convert(1)