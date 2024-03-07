
vocales = ['a', 'e', 'i', 'o', 'u']
total=0
while True:
    empezar = int(input('deseas empezar con el juego: 1. empezar 2. salir: '))
    if empezar>=1 and empezar<=2:
        if empezar ==1:
            valor = input('ingrese un valor unico tipo (a,b,c,d):')
            if valor in vocales:
                total+=1
        if empezar == 2:
            print("total de vocales son",total)
            break
    else:
        print('syntaxis error repetir')

    
    

