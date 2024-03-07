
print ('bienvenido a la ferreteria feliz')
ferreteria = 0.1
aseo =0.05
seguridad = 0.15
alimentos = 0.08
electrodomesticos =0.12
total = 0 
contador1,contador2,contador3,contador4,contador5=0,0,0,0,0
while True:
    tipo_producto = int(input('ingrese el tipo de producto para darle el descuento pertinente: 1) ferreteria 2)aseo 3)seguridad 4)alimentos 5) electrodomesticos 6)salir'))
    if tipo_producto>=1 and tipo_producto<=tipo_producto+1:
        if tipo_producto == 1:
            precio = int(input('precio del producto:'))
            decuento = precio*ferreteria
            precio -= decuento
            contador1 +=1
            total += precio
        if tipo_producto == 2:
            precio = int(input('precio del producto:'))
            decuento = precio*aseo
            precio -= decuento
            contador2 +=1
            total += precio
        if tipo_producto == 3:
            precio = int(input('precio del producto:'))
            decuento = precio*seguridad
            precio -= decuento
            contador3 +=1
            total += precio
        if tipo_producto == 4:
            precio = int(input('precio del producto:'))
            decuento = precio*alimentos
            precio -= decuento
            contador4 +=1
            total += precio
        if tipo_producto == 5:
            precio = int(input('precio del producto:'))
            decuento = precio*electrodomesticos
            precio -= decuento
            contador5 +=1
            total += precio
        if tipo_producto == 6:
            print(f'el total de productos comprados son:\n total de ferreteria: {contador1} \n total de aseo {contador2} \n total de seguridad {contador3} \n total de alimentos: {contador4} \n total de seguridad: {contador5} \n total a pagar: {total}')
            break
    
        