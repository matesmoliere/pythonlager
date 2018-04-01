def noventainueve_cervezas():

    '''
    Es un canción anglosajona que va cantando el número de cervezas que se van 
    bebiendo, y las que van quedando. Así, hasta llegar a cero cervezas:
    '99 bottles on the wall, 99 bottles of beer.
    Take one down, pass it around, 98 bottles on the wall'
    (99 botellas en la pared, 99 botellas de cerveza.
    Coge una y pásala, 98 botellas en la pared )
    '''
    x= 99
    while x != 0:
        print(x, 'botellas de cerveza en la pared,')
        x -= 1
        print('coge una y pásala, quedan', x, 'botellas')
        print()

##    x = 1
##    while x != 101:
##        print(x,'elefantes se columpiaban,\n como vieron que resistían\n fueron a llamar a otro elefante')
##        x += 1
##        print()
##        if x == 100:
##            print('Ya no!,Ploff!')
##            break


##
##    i = 99
##    while i > 0:
##        print(i,'bottles on the wall, ',i,' bottles of beer')
##        i = i-1
##        print('Take one down, pass it around, ',i,' bottles on the wall')
