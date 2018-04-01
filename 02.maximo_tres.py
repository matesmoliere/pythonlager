def maximo_de_tres(a,b,c):
    '''
    (int,int,int -> int)

    Toma tres números y devuelve el mayor de ellos

    >>> maximo_de_tres(6,9,12)
    12 es el mayor
    >>> maximo_de_tres(12,56,34)
    56 es el mayor
    >>> maximo_de_tres(122,56,34)
    122 es el mayor
    '''

    if (a > b) and (a > c):
        print(a, 'es el mayor')
    elif (b > c):
        print(b, 'es el mayor')
    else:
        print(c, 'es el mayor')
