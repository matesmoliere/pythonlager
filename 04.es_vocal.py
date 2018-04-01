def es_vocal(caracter):
    '''
    (str -> bool)

    Lee una cadena alfanumérica
    y determina si es sólo una vocal

    >>> es_vocal('6')
    No es vocal
    >>> es_vocal('e')
    Es vocal
    >>> es_vocal(5)
    No es vocal
    >>> es_vocal('e9')
    No es vocal
    >>> es_vocal('ER')
    No es vocal
    >>> es_vocal('9f')
    No es vocal
    >>> es_vocal('oe')
    No es vocal
    
    '''
    caracter = str(caracter) # convertimos cualquier carácter en str
    caracter = caracter.lower() # convertimos en minúscula 
    
#------ una forma de hacerlo con if-elif-else ---------

##    if caracter == 'a':
##        print('Es vocal')
##    elif caracter == 'e':
##        print('Es vocal')
##    elif caracter == 'i':
##        print('Es vocal')
##    elif caracter == 'o':
##        print('Es vocal')
##    elif caracter == 'u':
##        print('Es vocal')
##    else:
##        print('No es vocal')

#------- otra forma usando boole -----------

##    if (caracter == 'a') or (caracter == 'e') or (caracter == 'i') or (caracter == 'o') or    (caracter == 'u'):
##        print('vocal')
##    else:
##        print('No es vocal')

#-------- más simple aún ----------------------

    if caracter not in 'aeiou':
        print('error')
    else:
        print('ok')
    
    
