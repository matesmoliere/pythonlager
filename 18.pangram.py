def pangram(frase):

    '''
    Le pasamos una frase a la funcion, y esta nos devuelve
    las letras que no estan en esa frase

    >>> pangram('hola')
    bcdefgijkmnpqrstuvwxyz
    >>> pangram('supercalifragilistico')
    bdhjkmnqvwxyz
    >>> pangram('abcdefghijklmno')
    pqrstuvwxyz
    '''
    
    frase = frase.lower() # Si hubieran mayusculas, las convierte a minusculas
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in frase:
            print(i, end = ' ')
