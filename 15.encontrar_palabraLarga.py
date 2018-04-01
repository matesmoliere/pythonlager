def encontrar_palabra_larga(lista_de_palabras):
    '''
    >>> encontrar_palabra_larga(['pedo','tri','murcielago'])
    10
    >>> encontrar_palabra_larga(['pedo','trivvvvvvvvv','murcielago'])
    12

    '''
    longitudes=[]
    for i in lista_de_palabras:
        longitudes.extend([len(i)])
    return max(longitudes)
        
        
