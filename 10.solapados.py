def solapados(lista1,lista2):
    '''
    >>> solapados(['a','b'],['l','z'])
    False
    >>> solapados(['a','b'],['a','z'])
    True
    >>> solapados(['a','b'],['k','b'])
    True

    '''
    
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False
