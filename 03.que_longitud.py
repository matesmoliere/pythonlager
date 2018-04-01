def que_longitud(texto):
    '''
    (str -> int)

    Toma una cadena de texto y cuenta cuántos
    elementos posee

    >>>que_longitud('hola')
    4
    >>> que_longitud('murciélago')
    10
    
    '''
    cuenta = 0
    for i in texto:
        cuenta +=1
    print(cuenta)

    
