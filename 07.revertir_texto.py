##def revertir(texto):
##    '''
##    (str)-> str
##
##    Dada una cadena de texto, invierte el orden de las letras
##    >>> revertir('colegio moliere')
##    ereilom oigeloc
##    >>> revertir('hola mundo')
##    odnum aloh
##    '''
##    print(texto[::-1])
#--------------------------------------------------------------
def revertir(palabra):
    '''
    (str)-> str

    Dada una cadena de texto, invierte el orden de las letras

    >>> revertir('colegio moliere')
    ereilom oigeloc
    >>> revertir('hola mundo')
    odnum aloh
    '''
    
    for i in range(len(palabra)):
        print(palabra[-i-1],end ='')
    
