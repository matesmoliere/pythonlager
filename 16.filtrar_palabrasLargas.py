def filtrar_palabra_larga(numero,lista_de_palabras):
    '''
    (num.list) -> list

    Se pasan como parámetros un número y una lista de palabras. Basándonos
    en ese número, creamos una nueva lista con las palabras que tengan un
    número de caracteres mayor al número introducido

    >>> filtrar_palabra_larga(3,['hi','hier','hierro','hierros'])
    ['hier', 'hierro', 'hierros']
    >>> filtrar_palabra_larga(4,['hi','hier','hierro','hierros'])
    ['hierro', 'hierros']

    '''
    
    l=[]
    for i in lista_de_palabras:
        if len(i) > numero:
            l.extend([i])
    return l
    
