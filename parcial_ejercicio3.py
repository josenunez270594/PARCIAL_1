print ('este prigrama te permitira cambiar de grados a fahrenheit y viceversa')
temperatura = float(input('ingrse la temperatua:'))
tipo_de_medida = input('ingrese el tipo de medida al que desea pasar: \n1) grados \n2) fahrenheit\n')

if tipo_de_medida == '1':
    formula = (temperatura-32)*(5/9)
    print (f'la formula paso de fahrenheit a grados y el resultado fue: {formula}')
elif tipo_de_medida == '2':
    formula = (temperatura*(9/5)) + 32
    print (f'la formula paso de grados a fahrenheit y el resultado fue: {formula}')
    