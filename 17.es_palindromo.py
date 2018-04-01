def es_palindromo(texto):

    '''
    El texto no debe tener otros signos de puntuación que el
    apostrofe (') y los espacios entre palabras. En cualquier
    otro caso no funcionará 

    
    >>> es_palindromo("Go hang a salami I'm a lasagna hog")
    True
    >>> es_palindromo("I roamed under it as a tired nude Maori")
    True
    >>> es_palindromo("Was it a rat I saw?")
    False

    '''

    texto_sin_espacios = texto.replace(' ','')
    texto_sin_apostrofes = texto_sin_espacios.replace("'",'')
    texto_final = texto_sin_apostrofes.lower()
    return texto_final == texto_final[::-1]
