
def encriptar(palabra):
    '''
    (str) -> str

    Escribe una función 'encriptar()' que convierta un texto cualquiera
    en "rövarspråket" (En sueco, "el lenguaje de los ladrones"). Esto es,
    duplica cada consonante, colocando entre ellas una "o". Por ejemplo,
    encriptar("this is fun") debería devolver "tothohisos isos fofunon".

    >>>encriptar("this is fun")
    tothohisos isos fofunon
    >>>encriptar('informatica')
    inonfoforormomatoticoca
    '''
    
    
    vocal = "aeiouAEIOU"
    encriptado=""
    
    for letra in palabra:
        if (letra not in vocal) and (letra != " "):             # Comprobamos que la letra no sea
                                                                # vocal ni espacio, es decir, que sea consonante                                                            #

              encriptado = encriptado + (letra + "o" + letra)   
                                                                
        else:
            encriptado = encriptado + letra                     #En caso sea vocal, avanza a la siguiente letra
        
    print(encriptado)
