def palabras_numero(lista):
    '''
    list -> int
    
    convierte una lista de palabras en otra lista
    con números que representen la longitud de las
    palabras correspondientes.

    >>> palabras_numero(['aa','bbb','cccc'])
    [2, 3, 4]
    >>> palabras_numero(['españa','moliere','uruguay'])
    [6, 7, 7]
    
    '''
    lista_numero = []
    for palabra in lista:
        lista_numero.append(len(palabra))
    print(lista_numero)
