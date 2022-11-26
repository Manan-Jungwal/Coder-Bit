def cake(N):
    if 360 % N == 0:
        a = 'y'
    else:'n'

    if N > 360:
        b='n'
    else:
        b='y'

    if N > 26:
        c='n'
    else:
        c='y'

    return f'{a} {b} {c} '

x = int(input())

print(cake(x))