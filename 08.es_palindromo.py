def revertir(texto):
    '''
    (str)-> str

    Dada una cadena de texto (una sola palabra), invierte
    el orden de las letras

    >>> revertir('colegio moliere')
    ereilom oigeloc
    >>> revertir('hola mundo')
    odnum aloh
    '''
    return texto[::-1]

def es_palindromo():
    '''
    (str) -> bool
    
    la función reconoce palabras que son palíndromas,
    por ejemplo, radar se lee igual de izquierda a
    derecha que viceversa

    >>>es_palindromo()
    ¿Qué palabra quieres comprobar?: radar
    True
    >>>es_palindromo()
    ¿Qué palabra quieres comprobar?: amor
    False
    '''
    
    palabra = input('¿Qué palabra quieres comprobar?: ')
    #print(palabra)
    palabra_revertida = revertir(palabra)
    #print(palabra_revertida)
    return  palabra == palabra_revertida
